

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
import ScoreFMRIBehavior
import ScoreNeuroPsych

dir_path = '/home/jsteffen/GitHub/CognitiveTasks/DataHandlingScripts'

# This will load the config file containing the location of the data folder
# If there is an error it means that the GUI program has not been run.
# The GUI checks to see if thie config file exists. If it does not then it is created.
print(dir_path)
sys.path.append(os.path.join(dir_path,'..','ConfigFiles'))
import NeuropsychDataFolder


# VisitFolder = '/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/990123454/2019_May_13_0930_V001'
subid = '1002004'
Visit = '2019_Jun_18_1245_V001'
VisitFolder = os.path.join(NeuropsychDataFolder.NeuropsychDataFolder, subid, Visit)

Results = {}

Data = ReadFile(VisitFolder, subid, 'DMS_CAP')



Data = ScoreNeuroPsych.ReadFile(VisitFolder, subid, 'DMS_Block_BehRun1')


Data = ProcessNeuroPsychFunctions.CheckDMSDataFrameForLoad(Data)
tempResults = ProcessNeuroPsychFunctions.ProcessDMSBlockv2(Data)
Results['DMS1'] = ScoreNeuroPsych.ReorderDMSResults(tempResults)
FlatResults = MakeFlattenDict(Results)
FlatResults['AAsubid'] = subid
FlatResults['AAVisid'] = Visit
FlatResults['AAChecked'] = 0
ListOfFlat = []
ListOfFlat.append(FlatResults)
df = pd.DataFrame(ListOfFlat)

df.to_csv('testout.csv', index = False)

Data1 = ScoreFMRIBehavior.ReadFile(VisitFolder, subid, 'NBack_012012_MRIRun01')

Data = ScoreNeuroPsych.ReadFile(VisitFolder, subid, 'VSTM_Block_MRIRun2')

ProcessNeuroPsychFunctions.ProcessVSTMBlockv2(Data)


AllResults = ProcessNeuroPsychFunctions.ProcessNBack(AllData)



def MakeFlattenDict(Results):
    # The process functions all return a dictionary of their results. 
    # In order to write these results to a CSV fuile the dictionaries need to be flattened first
    #
    # cycle over tasks
    FlatResults = collections.OrderedDict()
    for i in Results.keys():
        for j in Results[i].keys():
            FlatResults['%s_%s'%(i,j)] = Results[i][j]
    return FlatResults    

