import os 
import importlib
import sys
import datetime


BaseDir = '/home/jsteffen'
BaseDir = '/Users/jasonsteffener'
sys.path.append(os.path.join(BaseDir,'Documents','GitHub','CognitiveTasks','DataHandlingScripts'))


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

