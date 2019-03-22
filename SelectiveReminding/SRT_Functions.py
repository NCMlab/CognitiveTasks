import numpy as np
import wx



def MakeListOfRecalledWords(FullWordList, RecalledWordList):
    # How many words are in the list?
    NWords = int(FullWordList['Index'].max() + 1)
    # Make array to keep recalled words
    RecallList = np.arange(NWords)
    # If a word is recalled, remove it from the array
    # cycle over each recalled word
    for word in RecalledWordList:
        count = 0
        # cycle over each word in the full list
        for j in FullWordList['Word']:
            # If the word was recalled
            if word == j:
                # set the value to -99
                RecallList[count] = -99
            count += 1
    # remove all the -99
    MissedList = list(RecallList[RecallList > -1])
#    # Change teh array to a string
#    MissedList = ','.join(str(i) for i in MissedList)
    return MissedList
    
    

def MakeGridOfSRTWords(GridWidth, GridHeight, NCols, NRows):
    # Make grid of locations for where to put words on the screen
    # Create a list of column locations
    x = np.linspace(0, 1, NCols)*GridWidth - GridWidth/2
    # Create a list of row locations
    y = np.linspace(0, 1, NRows)*GridHeight - GridHeight/2
    # Make a grid of these locations
    ColLocs, RowLocs = np.meshgrid(x, y)
    # reshape the grid to a list and flip it 
    ColLocsList = (ColLocs.reshape(np.size(ColLocs),1))
    # reshape the grid to a list and flip it 
    RowLocsList = np.flipud(RowLocs.reshape(np.size(RowLocs),1))
    return ColLocsList, RowLocsList


def PresentWordSelection(WordListObjects, trialClock, mouse, event, endExpNow, win, core, NWords):
    
    from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
    
    # Output the words that are recalled for entry into the Response Array
    RecallList = np.zeros(NWords)
    
    SelectedColor = 'blue'                                
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_text = []
    gotValidClick = False  # until a click is received

    # Set word colors back to white
    for i in WordListObjects:
        i.setColor('white', 'rgb255')
        
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(mouse)
    for word in WordListObjects:
        trialComponents.append(word)
    trialComponents.append(key_resp_2)
    
#    trialComponents = [mouse, WordListObjects[0], WordListObjects[1], WordListObjects[2], WordListObjects[3], WordListObjects[4], WordListObjects[5],WordListObjects[6], WordListObjects[7], WordListObjects[8], WordListObjects[9], WordListObjects[10], WordListObjects[11],WordListObjects[12],WordListObjects[13],WordListObjects[14],WordListObjects[15],WordListObjects[16],WordListObjects[17],key_resp_2]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial"-------

    CorrectRecog = 0
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(trialClock.getTime())
                    # check if the mouse was inside our 'clickable' objects
                    for obj in WordListObjects:
                                        # text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_text.append(obj.text)
                    # HERE is where accuracy is assessed
                    for obj in WordListObjects:#[text3,text5,text6,text7,text14, text15, text16, text17, text18, text22, text23, text24]:
                        if obj.contains(mouse):
                            CorrectRecog += 1
        # *text1* updates
        for word in WordListObjects:
            if t >= 0.0 and word.status == NOT_STARTED:
                # keep track of start time/frame for later
                word.tStart = t
                word.frameNStart = frameN  # exact frame index
                word.setAutoDraw(True)
       # This cycls over the full list and checks to see which word is selected
        count = 0
        for word in WordListObjects:
            if mouse.isPressedIn(word):
                # Check only the words in teh list and not the intrusions
                if count < NWords:
                    RecallList[count] = 1
                word.setColor(SelectedColor, 'rgb255')
            count += 1
                
       
    # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    # Remove the words from the screen
    for word in WordListObjects:
        word.setAutoDraw(False)
    win.flip()
    return WordListObjects, mouse, RecallList

def CheckForIntrusions(mouse):
    # Go through the list of clicked words and see if any intrusions were said.
    ResponseList = mouse.clicked_text
    IntrusionCount = 1
    count = 0
    for word in ResponseList:
        if word == '[Intrusion]':      
            # Ask the tester to type in the intrusion word(s)
            IntrusionWord = TypeInWord(IntrusionCount)      
            IntrusionCount += 1
            ResponseList[count] = '[' + IntrusionWord + ']'
        count += 1
    return ResponseList
    # Change the [intrusion] in the word list to the typed in word
            
def TypeInWord(count): 
    app = wx.App()
    
    frame = wx.Frame(None, -1, 'win.py')
    frame.SetDimensions(0,0,200,50)
    
    # Create text input
    dlg = wx.TextEntryDialog(frame, 'Enter Intrusion %d'%(count),'Text Entry')
    # dlg.SetValue("Default")
    if dlg.ShowModal() == wx.ID_OK:
        print('You entered: %s\n' % dlg.GetValue())
    dlg.Destroy()
    return dlg.GetValue()

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
    print("Clean List:")
    print(CleanList)
    print(ResponseArray)
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
    

                