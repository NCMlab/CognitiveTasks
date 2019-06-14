

AllOutDataFolder = '/media/jsteffen/Data001/NCMTeamDrive/NCMLab/NCM002/Data/NeuroPsych'
subid = '9999999'
Visid = '2019_May_10_0918_V001'
VisitFolder = os.path.join(AllOutDataFolder, subid, Visid)
Results = LoadRawData(os.path.join(AllOutDataFolder, subid, Visid),subid)


import ScoreNeuroPsych
# importlib.reload(ScoreNeuroPsych)
# 
# ScoreNeuroPsych.ScoreAll()

#
import ProcessNeuroPsychFunctions

VisitFolder = '/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/990123454/2019_May_13_0930_V001'
VisitFolder = '/Volumes/GoogleDrive/Team Drives/NCMLab/NCM002-MRIStudy/Data/NeuroPsych/990123454/2019_May_13_0930_V001'
subid = '990123454'

Data = ReadFile(VisitFolder, subid, 'NBack*BehRun')

