import os
import fnmatch
import shutil
import csv
import pandas as pd
import numpy as np
import glob

def FindResults(TaskList, VisitFolder, PartID):
    for j in TaskList:
        TempFile = glob.glob(os.path.join(VisitFolder,(PartID+'_'+j+'*.csv')))
         # Ideally the file names shoudl be checked to pick the latest one   
        if len(TempFile) > 0:
            TaskList[j]['DataFile'] = TempFile[-1]
            TaskList[j]['Completed'] = True
    return TaskList

def ListOfExpectedResults():
    # This list could be a structure
    # This list is the list of names in the structure
    # Then each would have a flag as to whether it was found
    # It can each have the results
    TaskList = {}
    TaskList['Stroop_Color'] = {}
    TaskList['Stroop_Color']['Completed'] = False
    
    TaskList['Stroop_Word'] = {}
    TaskList['Stroop_Word']['Completed'] = False  
    TaskList['Stroop_ColorWord'] = {}
    TaskList['Stroop_ColorWord']['Completed'] = False  
    TaskList['WCST'] = {}
    TaskList['WCST']['Completed'] = False  
    TaskList['DigitSpan_Forward'] = {}
    TaskList['DigitSpan_Forward']['Completed'] = False              
    TaskList['DigitSpan_Backward'] = {}
    TaskList['DigitSpan_Backward']['Completed'] = False  
    TaskList['Matrices_Main'] = {}
    TaskList['Matrices_Main']['Completed'] = False  
    TaskList['DMS_Stair'] = {}
    TaskList['DMS_Stair']['Completed'] = False  
    TaskList['DMS_Block'] = {}
    TaskList['DMS_Block']['Completed'] = False  
    TaskList['VSTM_Stair'] = {}
    TaskList['VSTM_Stair']['Completed'] = False                  
    TaskList['VSTM_Block'] = {}
    TaskList['VSTM_Block']['Completed'] = False  
    TaskList['Speed_PatternComp'] = {}
    TaskList['Speed_PatternComp']['Completed'] = False  
    TaskList['Vocab_Antonyms'] = {}
    TaskList['Vocab_Antonyms']['Completed'] = False  
    return TaskList
                                                                                     
def ReadFile(VisitFolder, subid, TaskTag):
    # Find the file that matches the TaskTag
    # If multiple CSV files are found then the user is prompted to pick one.
    # Un selected files are renamed with XXX at their beginning.
    # The next time this program is run on this folder there will now only be one file 
    # available and the user will not be prompted again
    Data = []
    # List all files in the visit folder
    ll = os.listdir(VisitFolder)
    # create the string you are looking for which is a combo of the subid and the task name
    SearchString = subid + '_' + TaskTag
    matching = fnmatch.filter(ll,SearchString+'*.csv')
    # It is possible that there are multipel files with similar names.
    # The following asks the user for the correct one and then renames the others
    count = 1
    if len(matching) > 1:
        # There are more than one file!
        print('There are multiple files found for %s'%(SearchString))
        for i in matching:
            # print the name and size of files
            SizeOfFile = np.round(os.stat(os.path.join(VisitFolder,matching[0])).st_size/1048)
            print('\t%d) %s, size = %0.0f kB'%(count, i,SizeOfFile))
            count += 1
        sel = input('Which one should be kept?  (Press return to skip)')
        if len(sel) > 0:
            SelectedFile = matching[int(sel)-1]
            # Rename the unselected files so they will hopefully not be selected the next time!
            count = 1
            for i in matching:
                if not count == int(sel):
                    OutName = 'XXX_' + i
                    print(OutName)
                    shutil.move(os.path.join(VisitFolder,i), os.path.join(VisitFolder, OutName))
                count += 1    
        else:
            SelectedFile = False
    elif len(matching) == 1:
        SelectedFile= matching[0]
    else:
        SelectedFile = False
        print('Did not find any files!!!')
    if SelectedFile != False:
        # Now open the file
        InputFile = os.path.join(VisitFolder, SelectedFile)
        # Read whole file into a dataframe
        # Note, in order for the data to be read as a dataframe all columns need to have headings.
        # If not an error is thrown
        Data = pd.read_csv(InputFile)
        # If the data is to be read into a big list use this:
        #    fid = open(InputFile, 'r')
        #    Data = csv.reader(fid)
        #    Data = list(Data)
    return Data
    
def ProcessVSTMBlock(Data):
    if len(Data) > 0:
        Out = {}
        # If there is an entry that is -99 it is a missing value and needs to be changed to NaN
        Data = Data.replace(-99, nan)
        TabNResp = pd.pivot_table(Data, values = 'Corr', index = 'Load', aggfunc = 'count')
        TabRT = pd.pivot_table(Data, values = 'RT', index = 'Load', aggfunc = np.mean)    
        TabAcc = pd.pivot_table(Data, values = 'Corr', index = 'Load', aggfunc = np.mean)    
        Out['NResp'] = TabNResp
        Out['RT'] = TabRT
        Out['Acc'] = TabAcc
    else:
        Out = {}
        Out['NResp'] = -9999
        Out['Acc'] = -9999
        Out['RT'] = -9999
    return Out
    
def ProcessDMSBlock(Data):
    if len(Data) > 0:
        Out = {}
        # This finds the number of trials for which a response was made
        TabNResp = pd.pivot_table(Data, values = 'resp.corr', index = 'Load', aggfunc = 'count')
        # What is the average RT broken by load
        TabRT = pd.pivot_table(Data, values = 'resp.rt', index = 'Load', aggfunc = np.mean)    
        # What is the average accuracy
        TabAcc = pd.pivot_table(Data, values = 'resp.corr', index = 'Load', aggfunc = np.mean)    
        Out['NResp'] = TabNResp
        Out['RT'] = TabRT
        Out['Acc'] = TabAcc
    else:
        Out = {}
        Out['NResp'] = -9999
        Out['Acc'] = -9999
        Out['RT'] = -9999
    return Out  
    
def ProcessDMSBlockv2(Data):
    #cycle over load levels and save as relative load and absolute load
    UniqueLoad = Data['Load'].unique()
    UniqueLoad = UniqueLoad[~np.isnan(UniqueLoad)]
    UniqueLoad.sort()
    
    Out = {}
    count = 1
    for i in UniqueLoad:
        temp = Data[Data['Load']==i]
        # find acc
        Acc = (temp['resp.corr'].mean())
        RT = (temp['resp.rt'].mean())
        NResp = (temp['resp.corr'].count())
        Tag1 = 'RelLoad%02d'%(count)
        Tag2 = 'AbsLoad%02d'%(i)
        Out[Tag1+'_Acc'] = Acc
        Out[Tag2+'_Acc'] = Acc
        Out[Tag1+'_RT'] = RT
        Out[Tag2+'_RT'] = RT
        Out[Tag1+'_NResp'] = NResp
        Out[Tag2+'_NResp'] = NResp
        count += 1
    return Out
    
def CalculateDMSLoad(OneLineOfData):
    # calculate load from CSV results file
    Stim = OneLineOfData['TL']+OneLineOfData['TM']+OneLineOfData['TR']
    Stim = Stim + OneLineOfData['CL']+OneLineOfData['CM']+OneLineOfData['CR']
    Stim = Stim + OneLineOfData['BL']+OneLineOfData['BM']+OneLineOfData['BR']
    if  not OneLineOfData.isnull()['TL']:
        Load = 9 - Stim.count('*')
    else:
        Load = np.nan
    #OneLineOfData['Load'] = Load
    return Load

def CheckDMSDataFrameForLoad(Data):
    # some versions of the DMS files do not have a column of load values
    if not 'Load' in Data.index:
        Load = []
        for index, row in Data.iterrows():
            Load.append(CalculateDMSLoad(row))
        Data['Load'] = Load
    return Data
    
def ProcessPattComp(Data):
    if len(Data) > 0:
        # First remove the practice rows from the data file
        Data_Run = Data[Data['Run.thisN'].notnull()]
        Out = {}
        LevelsOfDiff = Data_Run['Difficulty'].unique()
        LevelsOfDiff.sort()
        for i in LevelsOfDiff:
            temp = Data_Run[Data_Run['Difficulty'] == i]
            Tag = 'Load%02d'%(i)
            Out[Tag + '_Acc'] = temp['resp.corr'].mean()
            Out[Tag + '_RT'] = temp['resp.rt'].mean()
            Out[Tag + '_NResp'] = temp['resp.corr'].count()            
    else:
        Out = {}
        for i in arange(1,4):
            Tag = 'Load%02d'%(i)
            Out[Tag + '_Acc'] = -9999
            Out[Tag + '_RT'] = -9999
            Out[Tag + '_NResp'] = -9999  

    return Out
    
def ProcessAntonym(Data):
    if len(Data) > 0:
        # First remove the practice rows from the data file
        Data_Run = Data[Data['trials.thisN'].notnull()]
        Out = {}
        Out['NResp'] = Data_Run['resp.corr'].count()
        Out['Acc'] = Data_Run['resp.corr'].mean()    
        Out['RT'] = Data_Run['resp.rt'].mean()
    else:
        Out = {}
        Out['NResp'] = -9999
        Out['Acc'] = -9999
        Out['RT'] = -9999
    return Out

def CheckWCSTErrors(CurrentRow, CurrentRule, PreviousRule):
    RuleList = []
    RuleList.append('Color')
    RuleList.append('Shape')
    RuleList.append('Count')   
    # Make this so it gets passed one row at a time because passing the entire DF is too much
    Sel = CurrentRow['Card%02d%s'%(int(CurrentRow['Card']),RuleList[CurrentRule])]
    Probe = CurrentRow['Probe%s'%(RuleList[CurrentRule])]
    # Do they match?
    Match = Sel == Probe
    Error = True
    PersError = False
    if Match:
        Error = False
    elif not Match:
    # If an error is made does it match the previous rule?
        Error = True
        PreviousProbe = CurrentRow['Probe%s'%(RuleList[PreviousRule])]
        if Sel == PreviousProbe:
            PersError = True
    return Error, PersError, Sel, Probe

def ProcessWCST(Data):
    if len(Data) > 0:
        # Remove the practice trials
        FindTask = Data[Data['TrialNum'].str.match('TrialNum')].index[0]
        Data_Run = Data.iloc[FindTask+1:]
        PreviousRule = -1
        # Start counters for the number of errors
        NumTrials = 0
        NumErrors = 0
        NumPersErrors = 0
        # Cycle over each data row
        for i, CurrentRow in Data_Run.iterrows():
            NumTrials += 1
            # extrcat the current rule
            CurrentRule = int(CurrentRow['Rule'])
            if (PreviousRule != -1) and (CurrentRule != LastTrialRule):
                # If previous rule is -1 then leave it
                # if the current rule is different from the rule on the last trial, then change the previous rule
                # Then update the previous rule because the rules have changed
                PreviousRule = LastTrialRule
            # Check for errors on this row
            (Error, PersError, Sel, Probe) = CheckWCSTErrors(CurrentRow, CurrentRule, PreviousRule)
            # update error counters
            if Error: 
                NumErrors += 1
            if PersError:
                NumPersErrors += 1
            LastTrialRule = CurrentRule
            #print('%d, CurrentRule = %d, Probe = %d, Sel = %d, Error = %r, PerError = %r'%(i, CurrentRule, Probe, Sel, Error, PersError))    
        #print('Number of Trials: %d, Number of Errors: %d, Number Pers Errors: %d'%(NumTrials, NumErrors, NumPersErrors))
        Out = {}
        Out['NTrials'] = NumTrials
        Out['NErrors'] = NumErrors
        Out['NPersErrors'] = NumPersErrors
    else:
        Out = {}
        Out['NTrials'] = -9999
        Out['NErrors'] = -9999
        Out['NPersErrors'] = -9999
    return Out
    
def ProcessMatrices(Data):
    if len(Data) > 0:
        # How many trials were completed
        NTrials = Data['key_resp_2.corr'].count()
        # How many trials were answered correctly
        NCorr = Data['key_resp_2.corr'].sum()
        # What is the percent accuracy
        Acc = Data['key_resp_2.corr'].mean()
        Out = {}
        Out['Acc'] = Acc
        Out['NTrials'] = NTrials
        Out['NCorr'] = NCorr 
    else:
        Out = {}
        Out['Acc'] = -9999
        Out['NTrials'] = -9999
        Out['NCorr'] = -9999       
    return Out


def ProcessStroopColor(Data):
    # Stroop color uses the shape color to determine the test colors which is the 
    # same as the TEXT color
    # Mapping is
    # Red -- v
    # Green -- b
    # Yellow - n
    # Blue - m
    if len(Data) > 0:
        # First remove the practice rows from the data file
        Data_Run = Data[Data['trials.thisN'].notnull()]
        Out = {}
        Out['Acc'] =   Data_Run['resp.corr'].mean()
        Out['NTrials'] = Data_Run['resp.corr'].count()
        Out['NCorr'] = Data_Run['resp.corr'].sum()
        Out['RT'] = Data_Run['resp.rt'].mean()
    else:
        Out = {}
        Out['Acc'] = -9999
        Out['NTrials'] = -9999
        Out['NCorr'] = -9999   
        Out['RT'] = -9999
    return Out
    
def ProcessStroopWord(Data):
    # Stroop color uses the shape color to determine the test colors which is the 
    # same as the TEXT color
    # Mapping is
    # Red -- v
    # Green -- b
    # Yellow - n
    # Blue - m
    if len(Data) > 0:
        # First remove the practice rows from the data file
        Data_Run = Data[Data['trials.thisN'].notnull()]
        Out = {}
        Out['Acc'] =   Data_Run['resp.corr'].mean()
        Out['NTrials'] = Data_Run['resp.corr'].count()
        Out['NCorr'] = Data_Run['resp.corr'].sum()
        Out['RT'] = Data_Run['resp.rt'].mean()
    else:
        Out = {}
        Out['Acc'] = -9999
        Out['NTrials'] = -9999
        Out['NCorr'] = -9999   
        Out['RT'] = -9999         
    return Out    
    
def ProcessStroopColorWord(Data):
    # Stroop color uses the shape color to determine the test colors which is the 
    # same as the TEXT color
    # Mapping is
    # Red -- v
    # Green -- b
    # Yellow - n
    # Blue - m
    if len(Data) > 0:
        # First remove the practice rows from the data file
        Data_Run = Data[Data['trials.thisN'].notnull()]
        Data_Run_Con = Data[Data['Congruency']=='Con']
        Data_Run_Incon = Data[Data['Congruency']=='Incon']
        Out = {}
        Out['All_Acc'] = Data_Run['resp.corr'].mean()
        Out['All_NTrials'] = Data_Run['resp.corr'].count()
        Out['All_NCorr'] = Data_Run['resp.corr'].sum()
        Out['All_RT'] = Data_Run['resp.rt'].mean()
        Out['Con_Acc'] = Data_Run_Con['resp.corr'].mean()
        Out['Con_NTrials'] = Data_Run_Con['resp.corr'].count()
        Out['Con_NCorr'] = Data_Run_Con['resp.corr'].sum()
        Out['Con_RT'] = Data_Run_Con['resp.rt'].mean()  
        Out['Incon_Acc'] = Data_Run_Incon['resp.corr'].mean()
        Out['Incon_NTrials'] = Data_Run_Incon['resp.corr'].count()
        Out['Incon_NCorr'] = Data_Run_Incon['resp.corr'].sum()
        Out['Incon_RT'] = Data_Run_Incon['resp.rt'].mean()  
        #               
        # Out['Acc'] = pd.pivot_table(Data_Run, values = 'resp.corr', index = 'Congruency', aggfunc = np.mean)
        # Out['NCorr'] = pd.pivot_table(Data_Run, values = 'resp.corr', index = 'Congruency', aggfunc = np.sum)
        # Out['NTrials'] = pd.pivot_table(Data_Run, values = 'resp.corr', index = 'Congruency', aggfunc = 'count')
        # Out['RT'] = pd.pivot_table(Data_Run, values = 'resp.rt', index = 'Congruency', aggfunc = np.mean)
    else:
        Out = {}
        Out['Acc'] = -9999
        Out['NTrials'] = -9999
        Out['NCorr'] = -9999   
        Out['RT'] = -9999    
    return Out        

def ProcessDigitSpan(Data, Dir):
    StairLoad = []
    Correct = []
    if len(Data) > 0:
        # cycle over each row 
        for i, CurrentRow in Data.iterrows():
            match, Load = ProcessDigitSpanOneRow(CurrentRow, Dir)
            StairLoad.append(Load)
            print(match)
            if match:
                Correct.append(1)
            else:
                Correct.append(0)
        Capacity, NReversals = CalcuateCapacity(StairLoad)
        NTrials = len(Data)
        Out = {}
        Out['Capacity'] = Capacity
        Out['NReversals'] = NReversals
        Out['NTrials'] = NTrials
        Out['NCorrect'] = sum(Correct)
    else:
        Out = {}
        Out['Capacity'] = -9999
        Out['NReversals'] = -9999
        Out['NTrials'] = -9999
        Out['NCorrect'] = -9999
    print(Correct)
    return Out
            
def ProcessDigitSpanOneRow(Row, Dir):
    StrTest = Row['Digits']
    Test = [];
    for i in StrTest:
        if i.isdigit():
            Test.append(int(i))
    # This is stored as a string
    StrResp = Row['resp.keys']
    Resp = [];
    for i in StrResp:
        if i.isdigit():
            Resp.append(int(i))
    # If this is the backward span, flip the list
    if Dir == 'Backward':
        # Are the test sequence and the response the same?
        Test.reverse()
        match = Test == Resp
    else:
        match = Test == Resp
    # What is the load?
    Load = len(Test)
    return match, Load

def CalcuateCapacity(StairLoad):
    # Take as input the load levels
    Rev = []
    # find out when the load is increasing and when it is decreasing
    Up = False
    Down = False
    Previous = 0
    for i in StairLoad:
        if i > Previous:
            Up = True
            Rev.append(1)
        elif i < Previous:
            Down = True
            Rev.append(-1)
        else:
            Rev.append(Rev[-1])
        Previous = i
        # any changes in the direction are reversals
    Rev = np.diff(Rev)
    Rev = np.nonzero(Rev)[0]
    RevLoads = np.array(StairLoad)[Rev]
    NReversals = len(RevLoads)
    Capacity = RevLoads.mean()
    return Capacity, NReversals
    
def PutDataIntoOutputFile():
    # There will be a single output resultsvfile
    # it will have these columns:
    #   partID
    #   visitID, which will often be 1,2,3
    #   data checked, this cannot be changed by the program but only by a human
    #   data completeness flag
    #
    # 
    # First, the part id and visit id are read from the folder names.
    # Then the output data is checked to find this person. If found the data checked flag is TRUE
    # if yes, check to see if data is complete in out file. 
    # if not, then load all data and see if the missing data is now available
    pass
    
def CycleOverDataFolders():
    return VisitFolder, partID, VisID
    
def LoadOutDataFile(OutDataFilePathName):
    # Make a data frame from CSV file
    return OutDF   

def IsVisitInOutDataFile(OutDF, partID, VisID):
    return Flag
    
def IsDataComplete(OutDF, partID, VisID):
    return Flag
    
def WriteOneSubjToOutDataFile(OneSubData, OutFile):
    pass
    
def WriteHeaderToOutDataFile(OneSubData, OutFile):
    pass
    
def LoadRawData(VisitFolder, subid):
    Results = {}
    # Stroop
    Data = ReadFile(VisitFolder, subid, 'Stroop_Color_')
    Results['StrpC'] = ProcessStroopColor(Data)
    
    Data = ReadFile(VisitFolder, subid, 'Stroop_Word_')
    Results['StrpW'] = ProcessStroopWord(Data)
    
    Data = ReadFile(VisitFolder, subid, 'Stroop_ColorWord')
    Results['StrpCW'] = ProcessStroopColorWord(Data)
    
    # Wisconsin Card Sort
    Data = ReadFile(VisitFolder, subid, 'WCST')
    Results['WCST'] = ProcessWCST(Data)
    
    # Antonyms
    Data = ReadFile(VisitFolder, subid, 'Vocab_Antonyms')
    Results['Ant'] = ProcessAntonym(Data)
    
    # Digit Span
    # Forward
    Data = ReadFile(VisitFolder, subid, 'DigitSpan_Forward')
    Dir = 'Forward'
    Results['DSFor'] = ProcessDigitSpan(Data, Dir)
    
    # Backward
    Data = ReadFile(VisitFolder, subid, 'DigitSpan_Backward')
    Dir = 'Backward'
    Results['DSBack'] = ProcessDigitSpan(Data, Dir)
    
    
    # Pattern Comparison
    Data = ReadFile(VisitFolder, subid, 'Speed_PatternComp')
    Results['PComp'] = ProcessPattComp(Data)
    
    # Matrics
    Data = ReadFile(VisitFolder, subid, 'Matrices_Main')
    Results['Matr'] = ProcessMatrices(Data)

    Data = ReadFile(VisitFolder, subid, 'DMS_Block_BehRun2')
    Data = CheckDMSDataFrameForLoad(Data)
    Results['DMSBeh1'] = ProcessDMSBlockv2(Data)

    return Results
    