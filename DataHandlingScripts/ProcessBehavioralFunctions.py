""" Process the behavioral data

"""
import os
import glob
import pandas as pd

def CycleOverBehDataFolders(AllOutDataFolder):
    #cycle over folders
    # Create a dataframe to hold results
    df = pd.DataFrame()
    ListOfDict = []
    # get all sub dirs
    subdirs = glob.glob(os.path.join(AllOutDataFolder,'*/'))
    for subdir in subdirs:
        # check subdir based on some criteria
        CurDir = os.path.split(subdir)[0]
        CurDir = os.path.split(CurDir)[-1]
        if CurDir.isdigit() and CurDir[0] == '1':
            subid = CurDir
            print(CurDir)
            Results = LoadRawBehData(subdir, subid)
            
            FlatResults = DataHandlingScriptsPart1.FlattenDict(Results)
                    # add subid and visitid
            FlatResults['AAsubid'] = subid
            ListOfDict.append(FlatResults)
    df = pd.DataFrame(ListOfDict)
    return df
    
def ParseFileNamesForDateTime(filePath):
    # Tale a file name and extract the date and time encoded in it
    # Extract the file name
    # Remove extension
    filePathNoExt = os.path.splitext(filePath)[0]
    # Extract just the file name
    fileName = os.path.basename(filePathNoExt)
    # Split the file name
    fileNameParts = fileName.split('_')
    # Extract the different parts
    TimeStamp = fileNameParts[-1]
    MonthStamp = fileNameParts[-3]
    DayStamp = fileNameParts[-2]
    YearStamp = fileNameParts[-4]
    # Make the visit ID like the new study
    VisId = YearStamp + '_' + MonthStamp + '_' + DayStamp + '_' + TimeStamp + '_V001'
    return VisId
    
def LoadRawBehData(VisitFolder, subid):
    Results = {} 
    Data = ReadBehFile(VisitFolder, subid, 'DMS_Block')
    Data = DataHandlingScriptsPart1.CheckDMSDataFrameForLoad(Data)
    Results['DMSBeh1'] = DataHandlingScriptsPart1.ProcessDMSBlockv2(Data)
    DMSCap = ReadCapacity(VisitFolder, 'CAPACITY_DMSstair')
    Results['DMSBeh1']['Cap'] = DMSCap
    Data = ReadBehFile(VisitFolder, subid, 'FRT_Block')
    FRTCap = ReadCapacity(VisitFolder, 'CAPACITY_FRTstair')
    Results['FRTBeh1'] = ProcessFRTBlock(Data, FRTCap)
    Results['FRTBeh1']['Cap'] = FRTCap
    return Results
    
def ReadBehFile(VisitFolder, subid, TaskTag):
    ll = os.listdir(VisitFolder)
    SearchFor = TaskTag + '_' + subid
    matching = fnmatch.filter(ll,SearchFor+'*.csv')
    matchingBlock = fnmatch.filter(ll,SearchFor+'*Blocks.csv')
    matchingTrial = fnmatch.filter(ll,SearchFor+'*trials.csv')
    if len(matchingBlock) > 0:
        NewDMSFlag = True
            
    matching = set(matching) - set(matchingBlock)
    matching = list(set(matching) - set(matchingTrial))             
    if len(matching) > 0:
        matching = matching[-1]
        InputFile = os.path.join(VisitFolder, matching)
        print(matching)
        Data = pd.read_csv(InputFile)
    else:
        Data = []
    return Data