

import os
import sys
import fnmatch
import shutil
import pandas as pd
import numpy as np
import glob
import datetime
import collections
import ProcessNeuroPsychFunctions
import ProcessBehavioralFunctions
import ScoreNeuroPsych

# VisitFolder = '/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/990123454/2019_May_13_0930_V001'

AllOutDataFolder = '/Volumes/GoogleDrive/Shared drives/NCMLab/NCM002-MRIStudy/Data/NeuroPsych'
VisitFolder = '/Volumes/GoogleDrive/Shared drives/NCMLab/NCM002-MRIStudy/Data/NeuroPsych/1002008/2019_Jul_10_1255_V001'
subid = '1002008'
Visid = '2019_Jul_10_1255_V001'

Data1 = ScoreFMRIBehavior.ReadFile(VisitFolder, subid, 'NBack_012012_MRIRun01')

Data = ScoreNeuroPsych.ReadFile(VisitFolder, subid, 'VSTM_Block_MRIRun2')

ProcessNeuroPsychFunctions.ProcessVSTMBlockv2(Data)


AllResults = ProcessNeuroPsychFunctions.ProcessNBack(AllData)

Results = ScoreNeuroPsych.LoadRawDataSHORT(os.path.join(AllOutDataFolder, subid, Visid),subid)
FlatResults = ScoreNeuroPsych.FlattenDict(Results)

ListOfDict = []
FlatResults['AAsubid'] = subid
FlatResults['AAVisid'] = Visid
FlatResults['AAChecked'] = 0
ListOfDict.append(FlatResults)

df = pd.DataFrame(ListOfDict)
