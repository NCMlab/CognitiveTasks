


Visid = '2019_Jun_18_1245_V001'


import ScoreNeuroPsych
# importlib.reload(ScoreNeuroPsych)
# 
# ScoreNeuroPsych.ScoreAll()

#
import ProcessNeuroPsychFunctions

VisitFolder = '/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/990123454/2019_May_13_0930_V001'

AllOutDataFolder = '/Volumes/GoogleDrive/Shared Drives/NCMLab/NCM002-MRIStudy/Data/NeuroPsych/'
VisitFolder = '/Volumes/GoogleDrive/Shared Drives/NCMLab/NCM002-MRIStudy/Data/NeuroPsych/1002004/2019_Jun_18_1245_V001'
subid = '1002004'
Visid = '2019_Jun_18_1245_V001'


Results = ScoreNeuroPsych.LoadRawData(os.path.join(AllOutDataFolder, subid, Visid),subid)
FlatResults = FlattenDict(Results)    



import os
import sys
import fnmatch
import shutil
import pandas as pd
import numpy as np
import glob
import datetime

import ProcessNeuroPsychFunctions
import ProcessBehavioralFunctions
import ScoreFMRIBehavior

# VisitFolder = '/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/990123454/2019_May_13_0930_V001'
VisitFolder = '/Volumes/GoogleDrive/Shared drives/NCMLab/NCM002-MRIStudy/Data/NeuroPsych/1002004/2019_Jun_18_1245_V001'
subid = '1002004'

Data1 = ScoreFMRIBehavior.ReadFile(VisitFolder, subid, 'NBack_012012_MRIRun01')
Data2 = ScoreFMRIBehavior.ReadFile(VisitFolder, subid, 'NBack_012012_MRIRun02')
AllData = Data1.append(Data2)
AllResults = ProcessNeuroPsychFunctions.ProcessNBack(AllData)
