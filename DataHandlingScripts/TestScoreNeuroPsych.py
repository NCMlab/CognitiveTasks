import os 
import importlib
import sys
import datetime


BaseDir = '/home/jsteffen'
BaseDir = '/Users/jasonsteffener'
sys.path.append(os.path.join(BaseDir,'Documents','GitHub','CognitiveTasks','DataHandlingScripts'))


import ScoreNeuroPsych
importlib.reload(ScoreNeuroPsych)

ScoreNeuroPsych.ScoreAll()

#
import ProcessNeuroPsychResults

VisitFolder = '/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/99012345/2018_Dec_12_1044_V001'
subid = '99012345'
Data = ScoreNeuroPsych.ReadFile(VisitFolder, subid, 'SRT_Delayed')

