import numpy as np
# List1 = ['9', '7', '5', '9', '7', '5', '3', '1', 'b', 'b']
# List2 = ['1','2','4','5','6','7','a','x']
# List3 = ['1','2','3','4','5','6','9','c','a','3']
# List4 = ['1','2','3','5','x','6','7','9','c','3','b','8']
# List5 = ['1','2','3','5','6','7','9','c','a','b','4']
# List6 = ['1','2','x','x','3','5','6','7','c','a','b','4','8']
# 
# # Make an array that reflects the response table
# 
# cList1 = CleanSRTResponses(List1)
# cList2 = CleanSRTResponses(List2)
# cList3 = CleanSRTResponses(List3)
# cList4 = CleanSRTResponses(List4)
# cList5 = CleanSRTResponses(List5)
# cList6 = CleanSRTResponses(List6)
# 
# ResponseArray = np.zeros((12,6))
# ResponseArray = FillResponseArray(ResponseArray, cList1, 0)
# print(CheckForTwoCorrectTrials(ResponseArray))
# ResponseArray = FillResponseArray(ResponseArray, cList2, 1)
# print(CheckForTwoCorrectTrials(ResponseArray))
# ResponseArray = FillResponseArray(ResponseArray, cList3, 2)
# print(CheckForTwoCorrectTrials(ResponseArray))
# ResponseArray = FillResponseArray(ResponseArray, cList4, 3)
# print(CheckForTwoCorrectTrials(ResponseArray))
# ResponseArray = FillResponseArray(ResponseArray, cList5, 4)
# print(CheckForTwoCorrectTrials(ResponseArray))
# ResponseArray = FillResponseArray(ResponseArray, cList6, 5)
# print(CheckForTwoCorrectTrials(ResponseArray))
# # 
# NIntrusionArray = np.zeros(6)
# NIntrusionArray[0] = 1
# NIntrusionArray[4] = 2
# 
# # ResponseArray
# TotalRecall, TRarray = CalcTotalRecall(ResponseArray)
# LTS, LTSarray = CalcLongTermStorage(ResponseArray)
# LTR, LTRarray = CalcLongTermRecall(ResponseArray, LTSarray)
# 
# WordList = [u'THROW', u'LILY', u'FILM', u'DISCREET', u'LOFT', u'BEEF', u'STREET', u'HELMET', u'SNAKE', u'DUG', u'PACK', u'TIN']
# uniqueResp = ['a', 'c', 'b', '1', '3', '5', '7', '9', 'x']
# uniqueRespNoX = uniqueResp
# NIntrusions = np.count_nonzero(np.array(uniqueResp) == 'x')
# for i in range(0, len(uniqueResp)):
#     if uniqueResp[i] == 'x':
#         del uniqueRespNoX[i]
#         
#         
# 
# OutFile = open('testOutput.csv','w')
# WriteOutResults(OutFile, ResponseArray, NIntrusionArray, WordList)


def WriteOutResults(OutFile, ResponseArray, NIntrusionArray, WordList):
    # Writ eout the header
    WriteHeader(OutFile)
    # Write out the word list and the responses
    for i in range(0,12):
        OutFile.write('%s,'%(WordList[i]))
        for j in range(0,6):
            OutFile.write('%d,'%(ResponseArray[i,j]))
        OutFile.write('%s\n'%(WordList[i]))
    # Write out the intrusions
    OutFile.write('\n')
    # Make the table of scores
    WriteOutScores(OutFile, ResponseArray, NIntrusionArray)
    #OutFile.close()
      
    
def WriteHeader(OutFile):
    OutFile.write('Index,')
    for i in range(0,6):
        OutFile.write('%s%02d,'%('Trial',i+1))
    OutFile.write('Totals,\n')
    
def WriteOutScores(OutFile, ResponseArray, NIntrusionArray):
    # header row
    OutFile.write('\n\n,')
    for i in range(0,6):
        OutFile.write(',')
    OutFile.write('Total\n')

    # total recall
    # Calculate total recall
    TotalRecall, TRarray = CalcTotalRecall(ResponseArray)
    # write out results
    OutFile.write('Total Recall,')
    for i in range(0,6):
        OutFile.write('%d,'%(TRarray[i]))
    OutFile.write('%d\n'%(TotalRecall))

    # Write out long term storage
    LTS, LTSarray = CalcLongTermStorage(ResponseArray)    
    # write out results
    OutFile.write('LTS,')
    for i in range(0,6):
        OutFile.write('%d,'%(LTSarray[:,i].sum()))
    OutFile.write('%d\n'%(LTS))
    
    # Write out long term recall
    SRT_LTR, LTRarray = CalcLongTermRecall(ResponseArray, LTSarray) 
    # write out results
    OutFile.write('LTR,')
    for i in range(0,6):
        OutFile.write('%d,'%(LTRarray[:,i].sum()))    
    OutFile.write('%d\n'%(SRT_LTR))   # LTR
    
    # write out consistent long term retrieval
    # As of right now I need to figure out how to calculate CLTR for each trial
    # and not for each word
    CLTR, CLTRarray = CalcConsistentLongTermRetrieval(ResponseArray, LTRarray)
    # write out results
    OutFile.write('CLTR,')
    for i in range(0,6):
        OutFile.write('%d,'%(sum(CLTRarray[:,i])))
    OutFile.write('%d\n'%(CLTR))      
    
    # Write out intrusions
    OutFile.write('NIntrusions,')
    for j in range(0,6):
        OutFile.write('%d,'%(NIntrusionArray[j]))
    OutFile.write('%d\n'%(int(np.sum(NIntrusionArray))))  

def CheckForTwoCorrectTrials(ResponseArray):
    PrevColumn = ResponseArray[:,0]
    Flag = False
    for i in range(1,6):
        CurrentColumn = ResponseArray[:,i]
        if (np.sum(PrevColumn != 0) == 12) and (np.sum(CurrentColumn !=0 ) == 12):
            Flag = True
        PrevColumn = CurrentColumn
    return Flag

def CleanSRTResponses(InitialList):
    # Remove duplicates but preserve the order
    CleanList = []
    for i in InitialList:
        if i not in CleanList:
            CleanList.append(i)
    return CleanList
    
def FillResponseArray(ResponseArray, CleanList, TrialNumber):
    # For each response enter them in the Response array
    ResponseCount  = 1 # What order were responses made?
    for i in CleanList:
        # check whether it is a number or a letter
        if i.isdigit():
            ResponseValue = int(i) - 1 # To make the response a position in the array
        elif i == 'a':
            ResponseValue = 9
        elif i == 'b':
            ResponseValue = 10
        elif i == 'c':
            ResponseValue = 11
        ResponseArray[ResponseValue, TrialNumber] = ResponseCount
        ResponseCount += 1
    return ResponseArray

def CalcTotalRecall(ResponseArray):
    if CheckForTwoCorrectTrials(ResponseArray):
        TotalRecall = 72
    else:
        TotalRecall = np.sum(ResponseArray != 0)
    # Create total recall for each trial
    TRarray = np.zeros(6)
    for i in range(0,6):
        col = ResponseArray[:,i]
        TRarray[i] = np.sum(col != 0)
    return TotalRecall, TRarray
            
def CalcLongTermStorage(ResponseArray):
    # Calculate long term storage based on the when a word is recalled two trials in a row
    LTSList = np.zeros(12)
    # Make an array based on whether or not a word is in LTS
    LTSarray = np.zeros((12,6))
    for i in range(0,12):
        CurrentRow = ResponseArray[i,:]
        PrevTrial = CurrentRow[0]
        for j in range(1,6):
            CurrentTrial = CurrentRow[j]
            if (PrevTrial != 0) and (CurrentTrial != 0):
                # This word was recalled two trials in a row
                LTSList[i] = 6 - (j - 1)
                LTSarray[i,j-1:] = 1
                break
            PrevTrial = CurrentTrial
    LTS = sum(LTSList)
    return LTS, LTSarray
    
def CalcLongTermRecall(ResponseArray, LTSarray):
    # Point wise multiply the two arrays
    LTRarray = np.multiply(ResponseArray, LTSarray)
    # this will highight which words were in LTS and recalled
    LTRarray = 1*(LTRarray != 0) # This autoconverts the array to ints
    LTR = int(np.sum(LTRarray))
    # Convert the array to binary for use calculating the CLTR
    #LTRarray = LTRarray.astype(int)
    return LTR, LTRarray

def CalcConsistentLongTermRetrieval(ResponseArray, LTRarray):
    # find words consistenty recalled from long term storage
    CLTRarray = np.zeros((12,6))
    for i in range(12):
        # check the last two trials
        if (LTRarray[i,4] == 1) and (LTRarray[i,5] == 1):
            # If the last two trials were recalled then they are considered
            # consistent. 
            CLTRarray[i,4] = 1
            CLTRarray[i,5] = 1            
            # Now check previous trials            
            for j in range(4,0,-1):
                if LTRarray[i,j-1] == 1:
                    CLTRarray[i,j-1] = 1
    CLTR = int(np.sum(CLTRarray))
    return CLTR, CLTRarray

    for i in range(0,12):
        # take one row
        row = LTRarray[i,:]
        # flip it to read from the last trial first
        row = np.flip(row,0)
        count = 0
        # cycle over each row
        for j in row:
            # check to see if the word was recalled
            if j == 1:
                count += 1
            else:
                # stop when a word was not recalled for a trial
                break
        # if the count is less than 2
        if count < 2:
            count = 0
        CLTR += count
    return CLTR

def ReadDataFile(FileIn):
    # Read the file as a pandas data frame
    InData = pd.read_csv(InFileName)
    # set the index    
    InData = InData.set_index('Index')
    # extract the total values
    # convert the extracted dataframe values to single interger values
    TotRecall = int(InData.loc[['Total Recall']]['Totals'][0])
    LTR = int(InData.loc[['LTS']]['Totals'][0])
    LTS = int(InData.loc[['LTR']]['Totals'][0])
    CLTR = int(InData.loc[['CLTR']]['Totals'][0])
    Nintr = int(InData.loc[['NIntrusions']]['Totals'][0])
    return TotRecall, LTR, LTS, CLTR, Nintr

def CalculatePrimacy():
    """ Bruno D, Grothe MJ, Nierenberg J, Zetterberg H, Blennow K, Teipel SJ, Pomara N. 
    A study on the specificity of the association between hippocampal volume and delayed 
    primacy performance in cognitively intact elderly individuals. Neuropsychologia. 2015;69:1-8.
    """
    pass

def CalculateShortTermRecall():
    """ 
    Look at the original paper for all the measures
    """
    pass
    
        