BaseDir = '/home/jsteffen'
VisitFolder = os.path.join(BaseDir, 'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/99012345/2018_Dec_12_1044_V001')
subid = '99012345'

Results = {}
# Wisconsin
Data = ReadFile(VisitFolder, subid, 'WCST')
Results['WCST'] = ProcessWCST(Data)
# Pattern Comparison
Data = ReadFile(VisitFolder, subid, 'Speed_PatternComp')
Results['PatternComp'] = ProcessPattComp(Data)
# DMS Tasks
Data = ReadFile(VisitFolder, subid, 'DMS_Block_MRIRun1')
Results['DMSMRI1'] = ProcessDMSBlock(Data)
#DataDMSR2 = ReadFile(VisitFolder, subid, 'DMS_Block_MRIRun4')
#Results['DMSMRI1'] = ProcessDMSBlock(DataDMSR2)
# VSTM Tasks
Data = ReadFile(VisitFolder, subid, 'VSTM_Block')
Results['VSTM1'] = ProcessVSTMBlock(Data)
# Antonyms
Data = ReadFile(VisitFolder, subid, 'Vocab_Antonyms')
Results['Ant'] = ProcessAntonym(Data)
# Matrics
Data = ReadFile(VisitFolder, subid, 'Matrices_Main')
Results['Matrices'] = ProcessMatrices(Data)
Results
