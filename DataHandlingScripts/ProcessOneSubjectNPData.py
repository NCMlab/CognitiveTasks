import os 
import importlib
import sys

BaseDir = '/home/jsteffen'
BaseDir = '/Users/jasonsteffener'
sys.path.append(os.path.join(BaseDir,'Documents','GitHub','CognitiveTasks','DataHandlingScripts'))
import DataHandlingScriptsPart1 as DH

importlib.reload(DataHandlingScriptsPart1)


#BaseDir = '~'
VisitFolder = os.path.join(BaseDir, 'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/99012345/2018_Dec_12_1044_V001')
subid = '99012345'




Results = {}
# Stroop
Data = DH.ReadFile(VisitFolder, subid, 'Stroop_Color_')
Results['StroopColor'] = DH.ProcessStroopColor(Data)

Data = DH.ReadFile(VisitFolder, subid, 'Stroop_Word_')
Results['StroopWord'] = DH.ProcessStroopWord(Data)

Data = DataHandlingScriptsPart1.ReadFile(VisitFolder, subid, 'Stroop_ColorWord')
Results['StroopColorWord'] = DataHandlingScriptsPart1.ProcessStroopColorWord(Data)

# Wisconsin Card Sort
Data = DH.ReadFile(VisitFolder, subid, 'WCST')
Results['WCST'] = DH.ProcessWCST(Data)

# Antonyms
Data = ReadFile(VisitFolder, subid, 'Vocab_Antonyms')
Results['Ant'] = ProcessAntonym(Data)

# Digit Span
# Forward
Data = DH.ReadFile(VisitFolder, subid, 'DigitSpan_Forward')
Dir = 'Forward'
Results['DigitSpanForward'] = ProcessDigitSpan(Data, Dir)

# Backward
Data = DH.ReadFile(VisitFolder, subid, 'DigitSpan_Backward')
Dir = 'Backward'
Results['DigitSpanBackward'] = ProcessDigitSpan(Data, Dir)


# Pattern Comparison
Data = DH.ReadFile(VisitFolder, subid, 'Speed_PatternComp')
Results['PatternComp'] = DH.ProcessPattComp(Data)

# Matrics
Data = ReadFile(VisitFolder, subid, 'Matrices_Main')
Results['Matrices'] = ProcessMatrices(Data)

# DMS Tasks
# Read capacity also

Data = DH.ReadFile(VisitFolder, subid, 'DMS_Block_MRIRun1')
Results['DMSMRI1'] = DH.ProcessDMSBlock(Data)
#DataDMSR2 = ReadFile(VisitFolder, subid, 'DMS_Block_MRIRun4')
#Results['DMSMRI1'] = ProcessDMSBlock(DataDMSR2)
# VSTM Tasks
Data = ReadFile(VisitFolder, subid, 'VSTM_Block')
Results['VSTM1'] = ProcessVSTMBlock(Data)
Results


Results['StroopColorWord']