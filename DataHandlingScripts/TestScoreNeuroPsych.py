

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
subid = '2002010'
Visit = '2019_Aug_23_1718_V001'
VisitFolder = os.path.join(NeuropsychDataFolder.NeuropsychDataFolder, subid, Visit)


Results = LoadRawData(os.path.join(AllOutDataFolder, subid, Visit),subid)
# Results = LoadRawDataSHORT(os.path.join(AllOutDataFolder, subid, Visid),subid)
FlatResults = FlattenDict(Results)


Data = ReadFile(VisitFolder, subid, 'Stroop_ColorWord')
Res = ProcessNeuroPsychFunctions.ProcessStroopColorWord(Data)

Data = ReadFile(VisitFolder, subid, 'DigitSpan_Backward')
Dir = 'Backward'
Res = ProcessNeuroPsychFunctions.ProcessDigitSpan(Data, Dir)


# R = ScoreNeuroPsych.CycleOverDataFolders(
AllOutDataFolder = NeuropsychDataFolder.NeuropsychDataFolder
ListOfDict = []
R = ScoreNeuroPsych.LoadRawData(os.path.join(AllOutDataFolder, subid, Visit),subid)
FlatResults = ScoreNeuroPsych.FlattenDict(R)

# add subid and visitid
FlatResults['AAsubid'] = subid
FlatResults['AAVisid'] = Visit
FlatResults['AAChecked'] = 0


ListOfDict.append(FlatResults)
df = pd.DataFrame(ListOfDict)

# Move the last three columns to the beginning of the data frame
# Make list of column names
ColNameList = []
for col in df:
    ColNameList.append(col)
# Now move the last three columns to the beginning
for j in range(0,3):
    ColNameList.insert(0,ColNameList.pop())
# Now apply these rearranged columns to the dataframe
df = df[ColNameList]


Results = collections.OrderedDict()
# Test DMS
Data = ScoreNeuroPsych.ReadFile(VisitFolder, subid, 'DMS_Block_BehRun1')
CapacityData = ScoreNeuroPsych.ReadFile(VisitFolder, subid, 'DMS_CAPACITY')    
Data = ProcessNeuroPsychFunctions.CheckDMSDataFrameForLoad(Data)
tempResults = ScoreNeuroPsych.ProcessNeuroPsychFunctions.ProcessDMSBlockv2(Data, CapacityData)
Results['DMSBeh1'] = ScoreNeuroPsych.Reorder_DMS_VSTM_Results(tempResults, 'DMS')


# Test VSTM
Data = ScoreNeuroPsych.ReadFile(VisitFolder, subid, 'VSTM_Block_BehRun1')
CapacityData = ScoreNeuroPsych.ReadFile(VisitFolder, subid, 'VSTM_CAPACITY')    
#Data = ProcessNeuroPsychFunctions.CheckDMSDataFrameForLoad(Data)
tempResults = ScoreNeuroPsych.ProcessNeuroPsychFunctions.ProcessVSTMBlockv2(Data, CapacityData)
Results['VSTMBeh1'] = ScoreNeuroPsych.Reorder_DMS_VSTM_Results(tempResults, 'VSTM')

# Test N-Back
Data1 = ScoreNeuroPsych.ReadFile(VisitFolder, subid, 'NBack_012012_BehRun*1_')
tempResults1 = ProcessNeuroPsychFunctions.ProcessNBack(Data1)   
Data2 = ScoreNeuroPsych.ReadFile(VisitFolder, subid, 'NBack_012012_BehRun*2_XX')
tempResults2 = ProcessNeuroPsychFunctions.ProcessNBack(Data2) 
    # Data2 = ReadFile(VisitFolder, subid, 'NBack*BehRun2')
    # tempResults2 = ProcessNeuroPsychFunctions.ProcessNBack(Data2)   
    # #Results['NBack'] = Reorder_NBack_Results(tempResults)
if len(tempResults1) > 0 and len(tempResults2) > 0: 
    AllData = Data1.append(Data2)
    if len(AllData) > 0:
        tempResultsAll = ProcessNeuroPsychFunctions.ProcessNBack(AllData)
        Results['NBack'] = ScoreNeuroPsych.Reorder_NBack_Results(tempResultsAll)
    print('\tBoth N-Back loaded')
elif len(tempResults1) > 0:
    Results['NBack'] = ScoreNeuroPsych.Reorder_NBack_Results(tempResults1)


FlatResults = ScoreNeuroPsych.FlattenDict(Results)
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

