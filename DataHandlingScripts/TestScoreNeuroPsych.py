import os 
import importlib
import sys
import datetime


BaseDir = '/home/jsteffen'
BaseDir = '/Users/jasonsteffener'
sys.path.append(os.path.join(BaseDir,'Documents','GitHub','CognitiveTasks','DataHandlingScripts'))


import ScoreNeuroPsych

importlib.reload(ScoreNeuroPsych)

AllOutDataFolder = os.path.join(BaseDir, 'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/')

NewData = ScoreNeuroPsych.CycleOverDataFolders(AllOutDataFolder)

# Now that the data has been loaded up from the raw data files,
# load up the existing data and see if any of it has been "Locked down"

ExistingDataFile = ScoreNeuroPsych.LocateOutDataFile()
OldData = ScoreNeuroPsych.LoadOutDataFile(ExistingDataFile)
UpdataFile = ScoreNeuroPsych.CreateOutFileName(AllOutDataFolder)

# Create a dataframe to hold teh updated data
OutDataFrame = pd.DataFrame()
# Now cycle over each row and compare
for index, NewRow in NewData.iterrows():
    # Add the new data

    NewDataSubId = NewRow['AAsubid']
    NewDataVisitId = NewRow['AAVisid']
    print(NewDataSubId)
    print(NewDataVisitId)
    # for each subid and visit found in the new data look for it in the old data
    # If the same subid/visitid is found in both check the Old data column 
    # labeled AAChecked to see if it is 1. If so then skip this data line in the new data 
    # and go onto the next one.
    
    # If the value is 0 in the old data file, then the data line has NOT been checked 
    # by a human and it is OK for this program to overwrite it.
    # Data is written out as follows:
    OldRow = OldData.loc[(OldData['AAsubid'] == int(NewDataSubId)) & (OldData['AAVisid'] == NewDataVisitId)] 
    
    if len(OldRow) > 0:
        # found this data in the exisiting data file
        # Check to see if the data has been checked by a human
        if int(OldRow['AAChecked']) == 1:
            # It has been checked
            # write temp to the out data file
            OutDataRow = OldRow
        else:
            # Data is in the out file but it has not been checked
            OutDataRow = NewRow
    else:
        # Did not find the new data in the old data file
        OutDataRow = NewRow
    # Add OutDataRow to the updated out dataframe
    OutDataFrame = OutDataFrame.append(OutDataRow)
    
    
    


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
