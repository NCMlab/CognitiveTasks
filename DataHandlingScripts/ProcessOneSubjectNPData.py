import os 
import importlib
import sys
import datetime

BaseDir = '/home/jsteffen'
#BaseDir = '/Users/jasonsteffener'
sys.path.append(os.path.join(BaseDir,'Documents','GitHub','CognitiveTasks','DataHandlingScripts'))


import DataHandlingScriptsPart1
importlib.reload(DataHandlingScriptsPart1)

AllOutDataFolder = os.path.join(BaseDir, 'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/')

df = DataHandlingScriptsPart1.CycleOverDataFolders(AllOutDataFolder)

FN = DataHandlingScriptsPart1.LocateOutDataFile()
df.to_csv(FN, index = False)


# 
# 
# subid = '99012345'
# Visid = '2018_Dec_12_1044_V001'
# FN = DataHandlingScriptsPart1.LocateOutDataFile()
# DD = DataHandlingScriptsPart1.LoadOutDataFile(FN)
# DataHandlingScriptsPart1.IsVisitInOutDataFile(DD, subid, Visid)
# 
# VisitFolder = os.path.join(AllOutDataFolder, subid, '2018_Oct_24_1022_V002')
# Data = DataHandlingScriptsPart1.ReadFile(VisitFolder, subid, 'DMS_Block_BehRun1')
# 
# Data = DataHandlingScriptsPart1.CheckDMSDataFrameForLoad(Data)
# 
# Results['DMSBeh1'] = DataHandlingScriptsPart1.ProcessDMSBlockv2(Data)
# 
# 
