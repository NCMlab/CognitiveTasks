''' Score all'''
import os
import sys
import datetime
import glob
import ScoreNeuroPsych
import ScoreFMRIBehavior
import ScoreSurveyMonkey_NCM002
# What folder is this file in?
dir_path = os.path.dirname(os.path.realpath(__file__))
# This will load the config file containing the location of the data folder
# If there is an error it means that the GUI program has not been run.
# The GUI checks to see if thie config file exists. If it does not then it is created.
print(dir_path)
sys.path.append(os.path.join(dir_path,'..','ConfigFiles'))
import NeuropsychDataFolder
# Load up the data location as a global variable
AllInDataFolder = NeuropsychDataFolder.NeuropsychDataFolder
# Where to put the summary data
AllOutDataFolder = os.path.join(os.path.split(AllInDataFolder)[0], 'SummaryData')

BaseFileName = 'NCM_Master_Demog_NP'
# What files exist with this name?
Files = glob.glob(os.path.join(AllOutDataFolder, BaseFileName + '*.csv'))
now = datetime.datetime.now()
NowString = now.strftime("_updated_%b-%d-%Y_%H-%M.csv")
NewOutFileName = BaseFileName + NowString
if len(Files) == 0:
    FileName = os.path.join(AllOutDataFolder, NewOutFileName)
else:
    # this will open an existing file
    FileName = Files[-1] 



NPData = ScoreNeuroPsych.main()
BUNPData = NPData
FMRIData = ScoreFMRIBehavior.main()
LifeData, DemogData = ScoreSurveyMonkey_NCM002.main()

# Merge the data files together
# Merge Demog, NP and Life
# Change name of index column for NP
column_names = NPData.columns.values
column_names[0] = 'PartID'
NPData.columns = column_names
# Set the index in NP
NPData = NPData.set_index('PartID')
# Change index type
NPData.index = NPData.index.astype(int64)
DemogAndNP = DemogData.AllParts.merge(NPData, left_on = 'PartID', right_on = 'PartID')
DemogAndNP.to_csv(FileName, index = True, float_format='%.3f') 

# Merge Demog and fMRI