import os 
import importlib
import sys
import datetime

BaseDir = '/home/jsteffen'
BaseDir = '/Users/jasonsteffener'
sys.path.append(os.path.join(BaseDir,'Documents','GitHub','CognitiveTasks','DataHandlingScripts'))
from DataHandlingScriptsPart1 import *

import DataHandlingScriptsPart1
importlib.reload(DataHandlingScriptsPart1)


#BaseDir = '~'
VisitFolder = os.path.join(BaseDir, 'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/99012345/2018_Dec_12_1044_V001')
subid = '99012345'


TaskList = DataHandlingScriptsPart1.ListOfExpectedResults()
TaskList = DataHandlingScriptsPart1.FindResults(TaskList, VisitFolder, subid)
Results = DataHandlingScriptsPart1.LoadRawData(VisitFolder, subid)



Results = {}
# Stroop
Data = DataHandlingScriptsPart1.ReadFile(VisitFolder, subid, 'Stroop_Color_')
Results['StroopColor'] = DataHandlingScriptsPart1.ProcessStroopColor(Data)

Data = DataHandlingScriptsPart1.ReadFile(VisitFolder, subid, 'Stroop_Word_')
Results['StroopWord'] = DataHandlingScriptsPart1.ProcessStroopWord(Data)

Data = DataHandlingScriptsPart1.ReadFile(VisitFolder, subid, 'Stroop_ColorWord')
Results['StroopColorWord'] = DataHandlingScriptsPart1.ProcessStroopColorWord(Data)

# Wisconsin Card Sort
Data = DataHandlingScriptsPart1.ReadFile(VisitFolder, subid, 'WCST')
Results['WCST'] = DataHandlingScriptsPart1.ProcessWCST(Data)

# Antonyms
Data = DataHandlingScriptsPart1.ReadFile(VisitFolder, subid, 'Vocab_Antonyms')
Results['Ant'] = DataHandlingScriptsPart1.ProcessAntonym(Data)

# Digit Span
# Forward
Data = DataHandlingScriptsPart1.ReadFile(VisitFolder, subid, 'DigitSpan_Forward')
Dir = 'Forward'
Results['DigitSpanForward'] = DataHandlingScriptsPart1.ProcessDigitSpan(Data, Dir)

# Backward
Data = DataHandlingScriptsPart1.ReadFile(VisitFolder, subid, 'DigitSpan_Backward')
Dir = 'Backward'
Results['DigitSpanBackward'] = DataHandlingScriptsPart1.ProcessDigitSpan(Data, Dir)


# Pattern Comparison
Data = DH.ReadFile(VisitFolder, subid, 'Speed_PatternComp')
Results['PatternComp'] = DH.ProcessPattComp(Data)

# Matrics
Data = ReadFile(VisitFolder, subid, 'Matrices_Main')
Results['Matrices'] = ProcessMatrices(Data)

# DMS Tasks
# Read capacity also

Data = DataHandlingScriptsPart1.ReadFile(VisitFolder, subid, 'DMS_Block_MRIRun1')
Results['DMSMRI1'] = DataHandlingScriptsPart1.ProcessDMSBlock(Data)
#DataDMSR2 = ReadFile(VisitFolder, subid, 'DMS_Block_MRIRun4')
#Results['DMSMRI1'] = ProcessDMSBlock(DataDMSR2)
# VSTM Tasks
Data = ReadFile(VisitFolder, subid, 'VSTM_Block')
Results['VSTM1'] = ProcessVSTMBlock(Data)
Results


Results['StroopColorWord']


Data = ReadFile(VisitFolder, subid, 'DMS_Block_BehRun2')
Data = CheckDMSDataFrameForLoad(Data)
Res = ProcessDMSBlock(Data)




## List keys
for i in Results.keys():
    print(i)
    for j in Results[i].keys():
        print('%s: %0.3f'%(j,Results[i][j]))
