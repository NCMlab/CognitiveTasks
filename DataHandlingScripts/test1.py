import os
import importlib
import sys
BaseDir = '/home/jsteffen'
#BaseDir = '/Users/jasonsteffener'
sys.path.append(os.path.join(BaseDir,'Documents','GitHub','CognitiveTasks','DataHandlingScripts'))


import DataHandlingScriptsPart1
importlib.reload(DataHandlingScriptsPart1)
import DataHandlingBehavioral
importlib.reload(DataHandlingBehavioral)


AllOutDataFolder = os.path.join(BaseDir, 'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/')

df = DataHandlingScriptsPart1.CycleOverDataFolders(AllOutDataFolder)



df = DataHandlingBehavioral.CycleOverBehDataFolders(AllOutDataFolder)



VisitFolder='/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/11101035/'
subid = '11101035'
TaskTag = 'DMS_Block'
DataHandlingScriptsPart1.ReadFile(subdir, subid, 'DMS_Block')


Results = {}
Data = ReadBehFile(VisitFolder, subid, 'DMS_Block')
Data = DataHandlingScriptsPart1.CheckDMSDataFrameForLoad(Data)
Results['DMSBeh1'] = DataHandlingScriptsPart1.ProcessDMSBlockv2(Data)

Data = ReadBehFile(VisitFolder, subid, 'FRT_Block')
CAP = ReadCapacity(VisitFolder, 'CAPACITY_FRTstair')
Results['FRTBeh1'] = ProcessFRTBlock(Data, CAP)

inputFileName = [u'/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/SurveyMonkeyExports/Participant Questionnaire.csv']
# open the file
fid = open(inputFileName[0],'r', encoding="ISO-8859-1")

data = csv.reader(fid)
#data = pandas.read_csv(fid, sep=',', encoding='latin-1')

