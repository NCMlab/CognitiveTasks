""" Process the behavioral data

"""
import os
import glob
import pandas as pd
import fnmatch
import ProcessNeuroPsychFunctions
import numpy as np
from ScoreNeuroPsych import FlattenDict

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
        if CurDir.isdigit():# and CurDir[0] == '1':
            subid = CurDir
            print(CurDir)
            Results = LoadRawBehData(subdir, subid)
            
            FlatResults = FlattenDict(Results)
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
    # THere may be more than one run of the DMS task
    # Read each file and create a list of the dataframes containing the data
    Data = ReadBehFile(VisitFolder, subid, 'DMS_Block')
    RunNames = []
    if len(Data) > 0:
    
        print(">>>>>>>>>>>>> %d <<<<<<<<<<<<<<<"%(len(Data)))
        for i in range(0,len(Data)):
            Data[i] = ProcessNeuroPsychFunctions.CheckDMSDataFrameForLoad(Data[i])
            # For each run that was found make a name for it    
            RunNames.append("DMSRun%02d"%(i + 1))
            # Score eahc run and add it to the dictionary of results
            Results[RunNames[i]] = ProcessNeuroPsychFunctions.ProcessDMSBlockv2(Data[i])
    else:
        # Just in case there is a capacity file found
        RunNames.append('DMSRun01')
        Results[RunNames[0]] = {}
    # Read the capacity file    
    DMSCap = ReadCapacity(VisitFolder, 'CAPACITY_DMSstair')
    # Associate the Capacity with run 1, but it could be either run, if there are more than one
    Results[RunNames[0]]['Cap'] = DMSCap
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
    # Check to see if there are more than one data file.
    # If so extract the time stamps and create a list of dataframes       
    Data = []
    if len(matching) > 0:
        for i in matching:
            print(i)
            # for each file check to see how big it is. It should be at least 1kB
            statinfo = os.stat(os.path.join(VisitFolder, i))
            if statinfo.st_size > 1000:
                InputFile = os.path.join(VisitFolder, i)
        
                Data.append(pd.read_csv(InputFile))            
    else:
        Data = []
    return Data

def ReadCapacity(SubDir, SearchString):
    ll = os.listdir(SubDir)
    matching = fnmatch.filter(ll,SearchString+'*')
    if len(matching) > 0:
        InFile = os.path.join(SubDir,matching[0])
        print(InFile)
        fid = open(InFile,'r')
        Capacity = float(fid.readline())
        fid.close()
    else:
        Capacity = -9999
    return Capacity

def ProcessFRTBlock(Data, CAP):
    # big note on this. The load is not entered in the ouput file!!
    #CAP = ReadCapacity(VisitFolder, 'CAPACITY_FRTstair')
    FRTLoads = CreateFRTList(CAP)
    FRTLoads = [float(s) for s in FRTLoads.split()] 
    Out = {}
    if len(Data) > 0:
        #cycle over load levels and save as relative load and absolute load
        UniqueLoad = Data['imageLnop'].unique()
        UniqueLoad = UniqueLoad[~np.isnan(UniqueLoad)]
        UniqueLoad.sort()
        count = 1
        for i in UniqueLoad:
            # recalculate load and use
            ActLoad = FRTLoads[count-1]
            temp = Data[Data['imageLnop']==i]
            # find acc
            Acc = (temp['resp.corr'].mean())
            RT = (temp['resp.rt'].mean())
            NResp = (temp['resp.corr'].count())
            Tag1 = 'RelLoad%02d'%(count)
            #Tag2 = 'AbsLoad%02f'%(ActLoad)
            Out[Tag1+'_Acc'] = Acc
            #Out[Tag2+'_Acc'] = Acc
            Out[Tag1+'_RT'] = RT
            #Out[Tag2+'_RT'] = RT
            Out[Tag1+'_NResp'] = NResp
            #Out[Tag2+'_NResp'] = NResp
            count += 1

    else:
        for i in range(1,6):
            Tag1 = 'RelLoad%02d'%(i)
            Tag2 = 'AbsLoad%02d'%(i)
            Out[Tag1+'_Acc'] = -9999
            #Out[Tag2+'_Acc'] = -9999
            Out[Tag1+'_RT'] = -9999
            #Out[Tag2+'_RT'] = -9999
            Out[Tag1+'_NResp'] = -9999
            #Out[Tag2+'_NResp'] = -9999
    return Out
    
def CreateFRTList(FRTCapacity):
    Limit = np.float(FRTCapacity)*1.25
    #FRTList = range(0,6,1)Limit,Limit/(6-1))
    FRTList = np.array(range(0,6,1))/(6.0-1)*Limit
    # Convert this array to a string so it can be passed as an argument
    FRTList = ' '.join(str(e) for e in FRTList)
    return FRTList 
         