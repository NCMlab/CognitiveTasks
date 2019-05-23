"""
Use this scoring program in other programs as:
    
    import ScoreNeuroPsych
    ScoreNeuroPsych.ScoreAll()
    
    This could be added to the end of the GUI program, so that when the GUI is closed
    the data os scored and updated.

"""
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
# What folder is this file in?
dir_path = os.path.dirname(os.path.realpath(__file__))
# This will load the config file containing the location of the data folder
# If there is an error it means that the GUI program has not been run.
# The GUI checks to see if thie config file exists. If it does not then it is created.
print(dir_path)
sys.path.append(os.path.join(dir_path,'..','ConfigFiles'))
import NeuropsychDataFolder
# Load up the data location as a global variable
AllOutDataFolder = NeuropsychDataFolder.NeuropsychDataFolder

def ScoreAll():
    # Cycle over all data folders and load them up
    NewData = CycleOverDataFolders()
    # find the name of the existing results file
    ExistingDataFileName = LocateOutDataFile()
    # Load the existing results file
    if os.path.exists(ExistingDataFileName):
        # Found the existing data file
        OldData = LoadOutDataFile(ExistingDataFileName)
    else:
        # There is no old data file
        OldData = []
    # created an updated results datafram, respectivein the "locked down" 
    # data rows
    UpdatedData = CreateUpdatedDataFrameOfResults(NewData, OldData)
    # Create an updated output file name
    UpdatedDataFileName = CreateOutFileName()
    # write out the updated data and move the old data file
    WriteOutNewdataMoveOldData(UpdatedData, UpdatedDataFileName, ExistingDataFileName)

def CycleOverDataFolders():
    # Take as input the folder that contains folders of data
    #cycle over folders
    # Enter each folder and identify the visit folders in them. 
    # These start with the letter V
    df = pd.DataFrame()
    ListOfDict = []
    # get all sub dirs
    subdirs = glob.glob(os.path.join(AllOutDataFolder,'*/'))
    for subdir in subdirs:
        # check subdir based on some criteria
        CurDir = os.path.split(subdir)[0]
        CurDir = os.path.split(CurDir)[-1]
        if CurDir.isdigit():
            #enter the directory and find visit folders

            VisitFolders = glob.glob(os.path.join(subdir,'*/'))
            # What if there are no visit folders?
            # Then define teh visit as V001 and use a filename to idetify the visitid
            # Check to see if there is a visiti folder in the subject folder and if there is 
            # no visit folder, check to see if there are data files
            if (len(VisitFolders) > 0): 
                for visFold in VisitFolders:
                    CurVis = os.path.split(visFold)[0]
                    CurVis = os.path.split(CurVis)[-1]
                    if CurVis[-4:-2] == 'V0':
                        # From the directory structre extract the subject ID and the visit ID
                        subid = CurDir
                        Visid = CurVis
                        print('%s, %s'%(subid, Visid))
                        # Load up the raw data from the files in the visit folder
                        Results = LoadRawData(os.path.join(AllOutDataFolder, subid, Visid),subid)
                        FlatResults = FlattenDict(Results)
                        # add subid and visitid
                        FlatResults['AAsubid'] = subid
                        FlatResults['AAVisid'] = Visid
                        FlatResults['AAChecked'] = 0
                        ListOfDict.append(FlatResults)
            elif len(os.listdir(subdir)) > 0:
                # This seems to be data in a subject folder with no visit folder
                # Create the visit ID
                subid = CurDir
                Visid = FindVisitIDFromFileNames(subdir)
                
                # Load up the raw data from the files in the visit folder
                Results = LoadRawData(os.path.join(AllOutDataFolder, subid),subid)
                FlatResults = FlattenDict(Results)
                # add subid and visitid
                FlatResults['AAsubid'] = subid
                FlatResults['AAVisid'] = Visid
                FlatResults['AAChecked'] = 0
                ListOfDict.append(FlatResults)
                
    df = pd.DataFrame(ListOfDict)
    return df

def FindVisitIDFromFileNames(subdir):
    # Make a list of the files in the folder
    ListOfFiles = glob.glob(os.path.join(subdir,'*.csv'))
    # Find the date and time stamps encoded in teh file names
    for filePath in ListOfFiles:
        Visid = ProcessBehavioralFunctions.ParseFileNamesForDateTime(filePath)
        break
    return Visid

    

def LoadRawData(VisitFolder, subid):
    # Given a visit folder, check for the existance of specific files
    # read the file and process teh results
    # This function looks for very specific files
    
    print('working on %s'%(subid))
    Results = {}
    # Stroop
    Data = ReadFile(VisitFolder, subid, 'Stroop_Color_')
    Results['StrpC'] = ProcessNeuroPsychFunctions.ProcessStroopColor(Data)
    
    Data = ReadFile(VisitFolder, subid, 'Stroop_Word_')
    Results['StrpW'] = ProcessNeuroPsychFunctions.ProcessStroopWord(Data)
    
    Data = ReadFile(VisitFolder, subid, 'Stroop_ColorWord')
    Results['StrpCW'] = ProcessNeuroPsychFunctions.ProcessStroopColorWord(Data)
    
    # Wisconsin Card Sort
    Data = ReadFile(VisitFolder, subid, 'WCST')
    Results['WCST'] = ProcessNeuroPsychFunctions.ProcessWCST(Data)
    
    # Antonyms
    Data = ReadFile(VisitFolder, subid, 'Vocab_Antonyms')
    Results['Ant'] = ProcessNeuroPsychFunctions.ProcessAntonym(Data)
    
    # Digit Span
    # Forward
    Data = ReadFile(VisitFolder, subid, 'DigitSpan_Forward')
    Dir = 'Forward'
    Results['DSFor'] = ProcessNeuroPsychFunctions.ProcessDigitSpan(Data, Dir)
    
    # Backward
    Data = ReadFile(VisitFolder, subid, 'DigitSpan_Backward')
    Dir = 'Backward'
    Results['DSBack'] = ProcessNeuroPsychFunctions.ProcessDigitSpan(Data, Dir)
    
    # Pattern Comparison
    Data = ReadFile(VisitFolder, subid, 'Speed_PatternComp')
    Results['PComp'] = ProcessNeuroPsychFunctions.ProcessPattComp(Data)
    
    # Matrics
    Data = ReadFile(VisitFolder, subid, 'Matrices_Main')
    Results['Matr'] = ProcessNeuroPsychFunctions.ProcessMatrices(Data)
    # DMS
    Data = ReadFile(VisitFolder, subid, 'DMS_Block_BehRun1')
    Data = ProcessNeuroPsychFunctions.CheckDMSDataFrameForLoad(Data)
    Results['DMSBeh1'] = ProcessNeuroPsychFunctions.ProcessDMSBlockv2(Data)
    # VSTM
    Data = ReadFile(VisitFolder, subid, 'VSTM_Block_BehRun1')
    Results['VSTMBeh1'] = ProcessNeuroPsychFunctions.ProcessVSTMBlock(Data)
    # SRT
    Data = ReadFile(VisitFolder, subid, 'SRT_ImmRecall')
    Results['SRT'] = ProcessNeuroPsychFunctions.ProcessSRTImm(Data)
    Data = ReadFile(VisitFolder, subid, 'SRT_Recog')
    Results['SRT'] = ProcessNeuroPsychFunctions.ProcessSRTRecog(Data)   

    # N-Back
    Data = ReadFile(VisitFolder, subid, 'NBack')
    Results['NBack'] = ProcessNeuroPsychFunctions.ProcessNBack(Data)          
    
#     Data = ReadFile(VisitFolder, subid, 'DMS_Block_MRIRun1')
#     Data = CheckDMSDataFrameForLoad(Data)
#     Results['DMSMRI1'] = ProcessDMSBlockv2(Data)
# 
#     Data = ReadFile(VisitFolder, subid, 'DMS_Block_MRIRun2')
#     Data = CheckDMSDataFrameForLoad(Data)
#     Results['DMSMRI2'] = ProcessDMSBlockv2(Data)
# 
#     Data = ReadFile(VisitFolder, subid, 'DMS_Block_BehRun1')
#     Data = CheckDMSDataFrameForLoad(Data)
#     Results['DMSBeh1'] = ProcessDMSBlockv2(Data)
#     
    return Results

def ReadFile(VisitFolder, subid, TaskTag):
    # Find the file that matches the TaskTag
    # If multiple CSV files are found then the user is prompted to pick one.
    # Un selected files are renamed with XXX at their beginning.
    # The next time this program is run on this folder there will now only be one file 
    # available and the user will not be prompted again
    Data = []
    # List all files in the visit folder
    ll = os.listdir(VisitFolder)
    # create the string you are looking for which is a combo of the subid and the task name
    SearchString = subid + '_' + TaskTag
    matching = fnmatch.filter(ll,SearchString+'*.csv')
    # It is possible that there are multipel files with similar names.
    # The following asks the user for the correct one and then renames the others
    count = 1
    if len(matching) > 1:
        # There are more than one file!
        print('There are multiple files found for %s in folder: %s'%(SearchString, VisitFolder))
        for i in matching:
            # print the name and size of files
            SizeOfFile = np.round(os.stat(os.path.join(VisitFolder,matching[0])).st_size/1048)
            print('\t%d) %s, size = %0.0f kB'%(count, i,SizeOfFile))
            count += 1
        sel = input('Which one should be kept?  (Press return to skip)')
        if len(sel) > 0:
            SelectedFile = matching[int(sel)-1]
            # Rename the unselected files so they will hopefully not be selected the next time!
            count = 1
            for i in matching:
                if not count == int(sel):
                    OutName = 'XXX_' + i
                    print(OutName)
                    shutil.move(os.path.join(VisitFolder,i), os.path.join(VisitFolder, OutName))
                count += 1    
        else:
            SelectedFile = False
    elif len(matching) == 1:
        SelectedFile= matching[0]
    else:
        SelectedFile = False
        print('Did not find any files!!!')
    if SelectedFile != False:
        # Now open the file
        InputFile = os.path.join(VisitFolder, SelectedFile)
        # Read whole file into a dataframe
        # Note, in order for the data to be read as a dataframe all columns need to have headings.
        # If not an error is thrown
        Data = pd.read_csv(InputFile)
        # If the data is to be read into a big list use this:
        #    fid = open(InputFile, 'r')
        #    Data = csv.reader(fid)
        #    Data = list(Data)
    return Data

def FlattenDict(Results):
    # The process functions all return a dictionary of their results. 
    # In order to write these results to a CSV fuile the dictionaries need to be flattened first
    #
    # cycle over tasks
    FlatResults = {}
    for i in Results.keys():
        for j in Results[i].keys():
            FlatResults['%s_%s'%(i,j)] = Results[i][j]
    return FlatResults    
    
def PutDataIntoOutputFile():
    # There will be a single output resultsvfile
    # it will have these columns:
    #   partID
    #   visitID, which will often be 1,2,3
    #   data checked, this cannot be changed by the program but only by a human
    #   data completeness flag
    #
    # 
    # First, the part id and visit id are read from the folder names.
    # Then the output data is checked to find this person. If found the data checked flag is TRUE
    # if yes, check to see if data is complete in out file. 
    # if not, then load all data and see if the missing data is now available
    df2 = pd.DataFrame.from_dict(FlatResults, orient='index')
    pass
        
def LoadOutDataFile(OutDataFilePathName):
    # Make a data frame from CSV file
    OutDF = pd.read_csv(OutDataFilePathName)
    return OutDF   
    
def CreateOutFileName():
    # Create a file to hold processed data using the time and date
    # to indicate when it was made
    BaseFileName = 'NCM_Master_NP'
    now = datetime.datetime.now()
    NowString = now.strftime("_updated_%b-%d-%Y_%H-%M.csv")
    NewOutFileName = os.path.join(AllOutDataFolder, BaseFileName + NowString)
    return NewOutFileName
    
def LocateOutDataFile():
    # Locate an existing processed data file and if it does not exist, then make it.
    BaseFileName = 'NCM_Master_NP'
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
    return FileName

def CreateUpdatedDataFrameOfResults(NewData, OldData):    
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
    return OutDataFrame
   
def WriteOutNewdataMoveOldData(UpdatedData, UpdatedDataFileName, ExistingDataFileName):
    # Move the old file 
    OldDataFolder = os.path.join(AllOutDataFolder, 'OldResultFiles')
    # if the folder for old data does not exist, then make it
    if not os.path.exists(OldDataFolder):
        os.mkdir(OldDataFolder)
    # change the name of the results file so it is not confused with current data
    MovedDataFile = os.path.join(OldDataFolder, 'X_'+os.path.basename(ExistingDataFileName))
    shutil.move(ExistingDataFileName, MovedDataFile)
    # Now that the old data is moved, write out the updated data
    UpdatedData.to_csv(UpdatedDataFileName, index = False)    
      
# def ListOfExpectedResults():
#     # This list could be a structure
#     # This list is the list of names in the structure
#     # Then each would have a flag as to whether it was found
#     # It can each have the results
#     TaskList = {}
#     TaskList['Stroop_Color'] = {}
#     TaskList['Stroop_Color']['Completed'] = False
#     TaskList['Stroop_Word'] = {}
#     TaskList['Stroop_Word']['Completed'] = False  
#     TaskList['Stroop_ColorWord'] = {}
#     TaskList['Stroop_ColorWord']['Completed'] = False  
#     TaskList['WCST'] = {}
#     TaskList['WCST']['Completed'] = False  
#     TaskList['DigitSpan_Forward'] = {}
#     TaskList['DigitSpan_Forward']['Completed'] = False              
#     TaskList['DigitSpan_Backward'] = {}
#     TaskList['DigitSpan_Backward']['Completed'] = False  
#     TaskList['Matrices_Main'] = {}
#     TaskList['Matrices_Main']['Completed'] = False  
#     TaskList['DMS_Stair'] = {}
#     TaskList['DMS_Stair']['Completed'] = False  
#     TaskList['DMS_Block'] = {}
#     TaskList['DMS_Block']['Completed'] = False  
#     TaskList['VSTM_Stair'] = {}
#     TaskList['VSTM_Stair']['Completed'] = False                  
#     TaskList['VSTM_Block'] = {}
#     TaskList['VSTM_Block']['Completed'] = False  
#     TaskList['Speed_PatternComp'] = {}
#     TaskList['Speed_PatternComp']['Completed'] = False  
#     TaskList['Vocab_Antonyms'] = {}
#     TaskList['Vocab_Antonyms']['Completed'] = False  
#     return TaskList


# def FindResults(TaskList, VisitFolder, PartID):
#     for j in TaskList:
#         TempFile = glob.glob(os.path.join(VisitFolder,(PartID+'_'+j+'*.csv')))
#          # Ideally the file names should be checked to pick the latest one   
#         if len(TempFile) > 0:
#             TaskList[j]['DataFile'] = TempFile[-1]
#             TaskList[j]['Completed'] = True
#     return TaskList