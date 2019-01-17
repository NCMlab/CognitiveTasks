import pandas as pd
import os
import DataHandlingScriptsPart1
import tkinter
# 
# filename = tkinter.filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)



def Run(BaseDir):
    FNData, FNScore, FNReg = SelectScoresFile(BaseDir)
    Data, Score, Reg = LoadAssessments(FNData, FNScore, FNReg)
    PartIDList = ExtractUniquePartIDs(Data['PIN'])
    
    ListOfDict = []
    for partID in PartIDList:
        print('Working on: %s'%(partID))
    # partID = PartIDList[4]
        dataOne, scoreOne, regOne = ExtractDataFromOnePart(Data, Score, Reg, partID)
        Results = ScoreAll(dataOne, scoreOne, regOne)
        FlatResults = DataHandlingScriptsPart1.FlattenDict(Results)
                    # add subid and visitid
        FlatResults['AAsubid'] = partID
        ListOfDict.append(FlatResults)
    df = pd.DataFrame(ListOfDict)
    return df

def SelectScoresFile(BaseDir):
    # filename = tkinter.filedialog.askopenfilename() 
    #BaseDir = '/Users/jasonsteffener'
    NIHPath = os.path.join(BaseDir, 'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/NIHToolboxExports')
    FileNameData = os.path.join(NIHPath, '2018-09-23 21.16.07 Assessment Data.csv')
    FileNameScore = os.path.join(NIHPath, '2018-09-23 21.16.07 Assessment Scores.csv')
    FileNameReg = os.path.join(NIHPath, '2018-09-23 21.16.07 Registration Data.csv')
    return FileNameData, FileNameScore, FileNameReg
    
def LoadAssessments(FileNameData, FileNameScore, FileNameReg):
    Data = pd.read_csv(FileNameData)
    Score = pd.read_csv(FileNameScore)
    Reg = pd.read_csv(FileNameReg)
    return Data, Score, Reg

def ExtractDataFromOnePart(Data, Score, Reg, partID):
    dataOne = Data[Data['PIN'] == partID]
    scoreOne = Score[Score['PIN'] == partID]
    regOne = Reg[Reg['PIN'] == partID]
    return dataOne, scoreOne, regOne  
    
def ExtractUniquePartIDs(DFcol):
    PartIDList = DFcol.unique()
    return PartIDList

def ExtractReg(regOne):
    Out= {}
    Out['Age'] = regOne['Age'].max()
    Out['Edu'] = regOne['Education'].max()
    return Out
    
def ScoreAll(dataOne, scoreOne, regOne):
    Results = {}
    LongName = 'NIH Toolbox Picture Vocabulary Test Age 3+ v2.0'
    TaskScore = scoreOne[scoreOne['Inst'] == LongName]
    Results['PictVocab'] = ScorePictVocab(TaskScore)
    
    LongName = 'NIH Toolbox Flanker Inhibitory Control and Attention Test Age 12+ v2.1'
    TaskScore = scoreOne[scoreOne['Inst'] == LongName]
    TaskData = dataOne[dataOne['Inst'] == LongName]
    Results['Flanker'] = ScoreFlanker(TaskScore, TaskData)
       
    LongName = 'NIH Toolbox List Sorting Working Memory Test Age 7+ v2.1'
    TaskScore = scoreOne[scoreOne['Inst'] == LongName]
    Results['ListSort'] = ScoreListSort(TaskScore)
    
    LongName = 'NIH Toolbox Dimensional Change Card Sort Test Age 12+ v2.1'
    TaskScore = scoreOne[scoreOne['Inst'] == LongName]
    TaskData = dataOne[dataOne['Inst'] == LongName]
    Results['CardSort'] = ScoreDimCardSort(TaskScore, TaskData)
    
    LongName = 'NIH Toolbox Pattern Comparison Processing Speed Test Age 7+ v2.1'
    TaskScore = scoreOne[scoreOne['Inst'] == LongName]
    Results['PattComp'] = ScorePattComp(TaskScore)
    
    LongName = 'NIH Toolbox Picture Sequence Memory Test Age 8+ Form A v2.1'
    TaskScore = scoreOne[scoreOne['Inst'] == LongName]
    Results['PictSeq'] = ScorePictSeq(TaskScore)
    
    LongName = 'NIH Toolbox Oral Reading Recognition Test Age 3+ v2.0'
    TaskScore = scoreOne[scoreOne['Inst'] == LongName]
    Results['OralRead'] = ScoreOralRead(TaskScore)  
    
    Results['NIH'] = ExtractReg(regOne)
    return Results
    
def ScorePictVocab(TaskScore):
    # VOCAB
    # use score data
    Out = {}
    if len(TaskScore) > 0: 
        Out['uncScore'] = TaskScore['Uncorrected Standard Score'].values[0]	
        Out['corScore'] = TaskScore['Age-Corrected Standard Score'].values[0]
        Out['Theta'] = TaskScore['Theta'].values[0]
    else:
        Out['uncScore'] = -9999
        Out['corScore'] = -9999
        Out['Theta'] = -9999
    return Out

def ScoreFlanker(TaskScore, TaskData):
    # attention and inhibitory control.
    # score
#    Computed Score	has range of 0 to 10 and combines SAcc and RT
    Out = {}
    if len(TaskScore) > 0 and len(TaskData) > 0:
        Out['uncScore'] = TaskScore['Uncorrected Standard Score'].values[0]	
        Out['corScore'] = TaskScore['Age-Corrected Standard Score'].values[0]
        Out['RawScore'] = TaskScore['RawScore'].values[0]
        Out['CompScore'] = TaskScore['Computed Score'].values[0]
        # extract trial rows
        TaskDataTrialsAll = TaskData[TaskData['ItemID'].str.contains("CONGRUENT")]
        TaskDataTrialsCon = TaskData[TaskData['ItemID'].str.contains("_CONGRUENT")]
        TaskDataTrialsInc = TaskData[TaskData['ItemID'].str.contains("_INCONGRUENT")]
        Out['AllAcc'] = TaskDataTrialsAll['Score'].mean()
        Out['ConAcc'] = TaskDataTrialsCon['Score'].mean()
        Out['IncAcc'] = TaskDataTrialsInc['Score'].mean()
        Out['AllRT'] = TaskDataTrialsAll['ResponseTime'].mean()
        Out['ConRT'] = TaskDataTrialsCon['ResponseTime'].mean()
        Out['IncRT'] = TaskDataTrialsInc['ResponseTime'].mean()
    else:
        Out['uncScore'] = -9999
        Out['corScore'] = -9999
        Out['RawScore'] = -9999
        Out['CompScore'] = -9999
        Out['AllAcc'] = -9999
        Out['ConAcc'] = -9999
        Out['IncAcc'] = -9999
        Out['AllRT'] = -9999
        Out['ConRT'] = -9999
        Out['IncRT'] = -9999
    return Out
        
def ScoreListSort(TaskScore):
    # working memory
            # use score data
    Out = {}
    if len(TaskScore) > 0: 
        Out['uncScore'] = TaskScore['Uncorrected Standard Score'].values[0]	
        Out['corScore'] = TaskScore['Age-Corrected Standard Score'].values[0]
        Out['RawScore'] = TaskScore['RawScore'].values[0]
    else:
        Out['uncScore'] = -9999
        Out['corScore'] = -9999
        Out['RawScore'] = -9999        
    return Out
    
def ScoreDimCardSort(TaskScore, TaskData):
    # cognitive flexibility.
        # score
    Out = {}
    if len(TaskScore) > 0: 
        Out['uncScore'] = TaskScore['Uncorrected Standard Score'].values[0]	
        Out['corScore'] = TaskScore['Age-Corrected Standard Score'].values[0]
        Out['RawScore'] = TaskScore['RawScore'].values[0]
        Out['CompScore'] = TaskScore['Computed Score'].values[0]
        
        # extract trial rows
        TaskDataTrialsAll = TaskData[TaskData['ItemID'].str.contains("DCCSMIXED")]
        TaskDataTrialsRep = TaskData[TaskData['ItemID'].str.contains("_REPEAT")]
        TaskDataTrialsSwi = TaskData[TaskData['ItemID'].str.contains("_SWITCH")]
        
        Out['AllAcc'] = TaskDataTrialsAll['Score'].mean()
        Out['RepAcc'] = TaskDataTrialsRep['Score'].mean()
        Out['SwiAcc'] = TaskDataTrialsSwi['Score'].mean()
        Out['AllRT'] = TaskDataTrialsAll['ResponseTime'].mean()
        Out['RepRT'] = TaskDataTrialsRep['ResponseTime'].mean()
        Out['SwiRT'] = TaskDataTrialsSwi['ResponseTime'].mean()
    else:
        Out['uncScore'] = -9999
        Out['corScore'] = -9999
        Out['RawScore'] = -9999
        Out['CompScore'] = -9999
        Out['AllAcc'] = -9999
        Out['RepAcc'] = -9999
        Out['SwiAcc'] = -9999
        Out['AllRT'] = -9999
        Out['RepRT'] = -9999
        Out['SwiRT'] = -9999        
    return Out    
    
def ScorePattComp(TaskScore):
    # processing speed
    # raw score ... number corret in 85 sec
    Out = {}
    if len(TaskScore) > 0: 
        Out['uncScore'] = TaskScore['Uncorrected Standard Score'].values[0]	
        Out['corScore'] = TaskScore['Age-Corrected Standard Score'].values[0]
        Out['RawScore'] = TaskScore['RawScore'].values[0]
    else:
        Out['uncScore'] = -9999
        Out['corScore'] = -9999
        Out['RawScore'] = -9999 
    return Out
    
def ScorePictSeq(TaskScore):
    # the assessment of episodic memory and fluid ability
            # use score data
    Out = {}
    if len(TaskScore) > 0: 
        Out['uncScore'] = TaskScore['Uncorrected Standard Score'].values[0]	
        Out['corScore'] = TaskScore['Age-Corrected Standard Score'].values[0]
        Out['RawScore'] = TaskScore['RawScore'].values[0]
        Out['Theta'] = TaskScore['Theta'].values[0]
    else:
        Out['uncScore'] = -9999
        Out['corScore'] = -9999
        Out['RawScore'] = -9999
        Out['Theta'] = -9999
    return Out
    
    
def ScoreOralRead(TaskScore):
    # VOCAB
        # use score data
    Out = {}
    if len(TaskScore) > 0: 
        Out['uncScore'] = TaskScore['Uncorrected Standard Score'].values[0]	
        Out['corScore'] = TaskScore['Age-Corrected Standard Score'].values[0]
        Out['Theta'] = TaskScore['Theta'].values[0]
    else:
        Out['uncScore'] = -9999
        Out['corScore'] = -9999
        Out['Theta'] = -9999
    return Out
    


