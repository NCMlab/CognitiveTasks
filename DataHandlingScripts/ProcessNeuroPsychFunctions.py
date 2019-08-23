import pandas as pd
import collections
import numpy as np
# This script only contains the processing functions for each different 
# neuropsych test.
# This keeps the fiunctions from the separate functions for handling the file readings
# and checking whether the data has been scored yet.
#
def ProcessMultipleBlocksDMS(ListData):
    pass
    
def ProcessMultipleBlocksVSTM(ListData):
    pass

def ProcessMultipleBlocksNBack(ListData):
    pass

def ProcessVSTMBlockv2(Data, CapacityData):
    # This needs work to ignore time outs
    Out = collections.OrderedDict()
    # Read the capacity data
    Capacity = ReadCapacity(CapacityData)
    # Add this to the dictionary
    Out['VSTM_Cap'] = Capacity
    
    if len(Data) > 0:
        #cycle over load levels and save as relative load and absolute load
        UniqueLoad = Data['Load'].unique()
        UniqueLoad = UniqueLoad[~np.isnan(UniqueLoad)]
        UniqueLoad.sort()
        count = 1
        for i in UniqueLoad:
            temp = Data[Data['Load']==i]
            # find acc
            Acc = (temp['Corr'].mean())
            RT = (temp['RT'].mean())
            NResp = (temp['Corr'].count())
            Tag1 = 'RelLoad%02d'%(count)
#            Tag2 = 'AbsLoad%02d'%(i)
            Out[Tag1+'_Acc'] = Acc
#            Out[Tag2+'_Acc'] = Acc
            Out[Tag1+'_RT'] = RT
#            Out[Tag2+'_RT'] = RT
            Out[Tag1+'_NResp'] = NResp
#            Out[Tag2+'_NResp'] = NResp
            count += 1
    else:
        Out['VSTM_Cap'] = -9999
        for i in range(1,6):
            Tag1 = 'RelLoad%02d'%(i)
#            Tag2 = 'AbsLoad%02d'%(i)
            Out[Tag1+'_Acc'] = -9999
#            Out[Tag2+'_Acc'] = -9999
            Out[Tag1+'_RT'] = -9999
#            Out[Tag2+'_RT'] = -9999
            Out[Tag1+'_NResp'] = -9999
#            Out[Tag2+'_NResp'] = -9999
    return Out
    
def ProcessDMSBlockv2(Data, CapacityData):
    Out = collections.OrderedDict()
    # Read the capacity data
    Capacity = ReadCapacity(CapacityData)
    # Add this to the dictionary
    Out['DMS_Cap'] = Capacity
    if len(Data) > 0:
        #cycle over load levels and save as relative load and absolute load
        UniqueLoad = Data['Load'].unique()
        UniqueLoad = UniqueLoad[~np.isnan(UniqueLoad)]
        UniqueLoad.sort()
        count = 1
        
        for i in UniqueLoad:
            temp = Data[Data['Load']==i]
            # find acc
            Acc = (temp['resp.corr'].mean())
            RT = (temp['resp.rt'].mean())
            NResp = (temp['resp.corr'].count())
            Tag1 = 'RelLoad%02d'%(count)
#            Tag2 = 'AbsLoad%02d'%(i)
            Out[Tag1+'_Acc'] = Acc
#            Out[Tag2+'_Acc'] = Acc
            Out[Tag1+'_RT'] = RT
#            Out[Tag2+'_RT'] = RT
            Out[Tag1+'_NResp'] = NResp
#            Out[Tag2+'_NResp'] = NResp
            count += 1                    
    else:
        Out['DMS_Cap'] = -9999
        for i in range(1,6):
            Tag1 = 'RelLoad%02d'%(i)
#            Tag2 = 'AbsLoad%02d'%(i)
            Out[Tag1+'_Acc'] = -9999
#            Out[Tag2+'_Acc'] = -9999
            Out[Tag1+'_RT'] = -9999
#            Out[Tag2+'_RT'] = -9999
            Out[Tag1+'_NResp'] = -9999
#            Out[Tag2+'_NResp'] = -9999
    return Out
    

def ReadCapacity(Data):
    # The capacity file contains a single number
    # And when loaded in as a dataframe this number gets used 
    # as a column name
    Capacity = float(Data.columns[0])
    return Capacity
        
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
    if len(Data) > 0:
        # some versions of the DMS files do not have a column of load values
        if not 'Load' in Data.index:
            Load = []
            for index, row in Data.iterrows():
                Load.append(CalculateDMSLoad(row))
            Data['Load'] = Load
    return Data
    
def ProcessPattComp(Data):
    if len(Data) > 10:
        try:
            # First remove the practice rows from the data file
            Data_Run = Data[Data['Run.thisN'].notnull()]
            Out = collections.OrderedDict()
            LevelsOfDiff = Data_Run['Difficulty'].unique()
            LevelsOfDiff.sort()
            for i in LevelsOfDiff:
                temp = Data_Run[Data_Run['Difficulty'] == i]
                Tag = 'Load%02d'%(i)
                Out[Tag + '_Acc'] = temp['resp.corr'].mean()
                Out[Tag + '_RT'] = temp['resp.rt'].mean()
                Out[Tag + '_NResp'] = temp['resp.corr'].count()          
        except:
            Out = collections.OrderedDict()
            for i in range(1,4):
                Tag = 'Load%02d'%(i)
                Out[Tag + '_Acc'] = -9999
                Out[Tag + '_RT'] = -9999
                Out[Tag + '_NResp'] = -9999  
    else:
        Out = collections.OrderedDict()
        for i in range(1,4):
            Tag = 'Load%02d'%(i)
            Out[Tag + '_Acc'] = -9999
            Out[Tag + '_RT'] = -9999
            Out[Tag + '_NResp'] = -9999  

    return Out
    
def ProcessAntonym(Data):
    if len(Data) > 10:
        # First remove the practice rows from the data file
        Data_Run = Data[Data['trials.thisN'].notnull()]
        Out = collections.OrderedDict()
        Out['NResp'] = Data_Run['resp.corr'].count()
        Out['Acc'] = Data_Run['resp.corr'].mean()    
        Out['RT'] = Data_Run['mouse.RT'].mean()

    else:
        Out = collections.OrderedDict()
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
    if len(Data) > 10:
        # Remove the practice trials
        # The data file has two parts, one for practice and one for the actual task
        try:
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
            Out = collections.OrderedDict()
            Out['NTrials'] = NumTrials
            Out['NErrors'] = NumErrors
            Out['NPersErrors'] = NumPersErrors
        except:
            Out = collections.OrderedDict()
            Out['NTrials'] = NumTrials
            Out['NErrors'] = NumErrors
            Out['NPersErrors'] = NumPersErrors
    else:
        Out = collections.OrderedDict()
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
        Out = collections.OrderedDict()
        Out['Acc'] = Acc
        Out['NTrials'] = NTrials
        Out['NCorr'] = NCorr 
    else:
        Out = collections.OrderedDict()
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
        Out = collections.OrderedDict()
        Out['Acc'] =   Data_Run['resp.corr'].mean()
        Out['NTrials'] = Data_Run['resp.corr'].count()
        Out['NCorr'] = Data_Run['resp.corr'].sum()
        Out['RT'] = Data_Run['resp.rt'].mean()
    else:
        Out = collections.OrderedDict()
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
        Out = collections.OrderedDict()
        Out['Acc'] =   Data_Run['resp.corr'].mean()
        Out['NTrials'] = Data_Run['resp.corr'].count()
        Out['NCorr'] = Data_Run['resp.corr'].sum()
        Out['RT'] = Data_Run['resp.rt'].mean()
    else:
        Out = collections.OrderedDict()
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
        Out = collections.OrderedDict()
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
        Out = collections.OrderedDict()
        Out['Acc'] = -9999
        Out['NTrials'] = -9999
        Out['NCorr'] = -9999   
        Out['RT'] = -9999    
    return Out        

def ProcessDigitSpan(Data, Dir):
    try:
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
            Capacity, NReversals = CalculateCapacity(StairLoad)
            NTrials = len(Data)
            Out = collections.OrderedDict()
            Out['Capacity'] = Capacity
            Out['NReversals'] = NReversals
            Out['NTrials'] = NTrials
            Out['NCorrect'] = sum(Correct)
        else:
            Out = collections.OrderedDict()
            Out['Capacity'] = -9999
            Out['NReversals'] = -9999
            Out['NTrials'] = -9999
            Out['NCorrect'] = -9999
        print(Correct)
    except:
        print('\t%s, %s >> Error!!!'%('Digit Span',Dir))
        Out = collections.OrderedDict()
    return Out
    
            
def ProcessDigitSpanOneRow(Row, Dir):
    StrTest = Row['Digits']
    Test = [];
    for i in StrTest:
        if i.isdigit():
            Test.append(int(i))
    # This is stored as a string
    StrResp = str(Row['resp.keys'])
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

def CalculateCapacity(StairLoad):
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
    
def ProcessSRTImm(Data):
    # Prepare the results dictionary
    Out = collections.OrderedDict()
    if len(Data) > 0:
        # # set the index    
        InData = Data.set_index('Index')
        # extract the total values
        # convert the extracted dataframe values to single interger values
        Out['TotRecall'] = int(InData.loc[['Total Recall']]['Totals'][0])
        Out['LTR'] = int(InData.loc[['LTS']]['Totals'][0])
        Out['LTS'] = int(InData.loc[['LTR']]['Totals'][0])
        Out['CLTR'] = int(InData.loc[['CLTR']]['Totals'][0])
        Out['Nintr'] = int(InData.loc[['NIntrusions']]['Totals'][0])
    else:
        Out['TotRecall'] = -9999
        Out['LTR'] = -9999 
        Out['LTS'] = -9999 
        Out['CLTR'] = -9999 
        Out['Nintr'] = -9999 
    return Out
    
def ProcessSRTRecog(Data):
    # The saved results score hits and correct rejections as correct.
    # What scores should be kept?
    # Misses
    # Correct Rejection
    # False Alarms
    # Hits
    # dL
    # dPrime
    Out = collections.OrderedDict()
    if len(Data) > 0:
        Hits = 0
        FA = 0
        CR = 0
        Miss = 0
        for index, row in Data.iterrows():
            ExpectedResponse = row['Corr']
            Correct = row['key_resp_3.corr']
            if (ExpectedResponse == 'left') & (Correct == 1):
                Hits += 1
            elif (ExpectedResponse == 'left') & (Correct == 0):
                Miss += 1
            elif (ExpectedResponse == 'right') & (Correct == 1):
                CR += 1
            elif (ExpectedResponse == 'right') & (Correct == 0):
                FA += 1
        Out['Recog'] = Hits
    else:
        Out['Recog'] = -9999
    return Out

def ProcessNBack(Data):
    try:
        Out = collections.OrderedDict()
        if len(Data) > 0:
            # Use the presentation of instructions to differentiate the blocks
            InstrRows = Data[Data['Stimulus'].str.match('Instructions')]
            NBlocks = len(InstrRows)
            AllLoads = []
            # Find out how many rows per block
            if NBlocks > 1:
                NRows = InstrRows.index[1] - InstrRows.index[0] - 1
            # Create arrays for data
            Hit = np.zeros(NBlocks)
            FalseAlarm = np.zeros(NBlocks)        
            HitRT = np.zeros(NBlocks)
            FalseAlarmRT = np.zeros(NBlocks)  
            TargetCount = np.zeros(NBlocks)
            for i in range(NBlocks):
                CurrentBlock = Data[InstrRows.index[i]+1:InstrRows.index[i]+1+NRows]
                # What is the load of this block
                AllLoads.append(CurrentBlock.iloc[0]['LoadLevel'])
                # How many target trials
                NTarget = CurrentBlock['Expected'].sum()
                NNonTarget = len(CurrentBlock['Expected']) - NTarget
                TargetCount[i] += NTarget
                # WHen are there responses
                for index, row in CurrentBlock.iterrows():
                    # Was there a response
                    if not str(row.KeyPress) =='nan':
                        # Was a response expetced?
                        if row.Expected == 1:
                            # Hit
                            Hit[i] += 1
                            HitRT[i] += row.RT
                        else:
                            FalseAlarm[i] += 1
                            FalseAlarmRT[i] += row.RT                
            # Find repeat blocks
            UniqueLoads = set(AllLoads)
            NLoads = len(UniqueLoads)
            # Find average responses over blocks with repeat loads
            AverageHit = np.zeros(NLoads)
            AverageHitRT = np.zeros(NLoads)
            AverageFalseAlarm = np.zeros(NLoads)
            AverageFalseAlarmRT = np.zeros(NLoads)
            AllTargetCount = np.zeros(NLoads)
            count = 0
            for i in UniqueLoads:
                # Find the blocks that correspond to this load level
                CurrentLoad = [j for j, x in enumerate(AllLoads) if x == i]
                # Calculate the average responses for this load level
                AverageHit[count] = Hit[CurrentLoad].sum()/(NTarget*len(Hit[CurrentLoad]))
                AverageHitRT[count] = HitRT[CurrentLoad].sum()/(NTarget*len(Hit[CurrentLoad]))
                AverageFalseAlarm[count] = FalseAlarm[CurrentLoad].sum()/(NNonTarget*len(Hit[CurrentLoad]))
                AverageFalseAlarmRT[count] = FalseAlarmRT[CurrentLoad].sum()/(NNonTarget*len(Hit[CurrentLoad]))
                AllTargetCount[count] = TargetCount[CurrentLoad].sum()
                count += 1
            # Now prepare the results for output            
            count = 0
            for i in UniqueLoads:
                Tag = 'Load%02d'%(i)
                Out[Tag+"Hit"] = AverageHit[count]
                Out[Tag+"Hitrt"] = AverageHitRT[count]   
                Out[Tag+"FA"] = AverageFalseAlarm[count]                    
                Out[Tag+"FArt"] = AverageFalseAlarmRT[count]
                Out[Tag+"N"] = AllTargetCount[count]
                count += 1
        else:
            for i in UniqueLoads:
                Tag = 'Load%02d'%(i)
                Out[Tag+"Hit"] = -99
                Out[Tag+"Hitrt"] = -99
                Out[Tag+"FA"] = -99
                Out[Tag+"FArt"] = -99  
                Out[Tag+"N"] = -99
    except:
        print('\tN-back >>> Error!!')
    return Out                                
        
def ProcessSRTDelRecall(Data):
    
    pass