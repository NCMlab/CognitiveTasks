import os 
import importlib
import sys

import glob
import pandas as pd
import fnmatch
import numpy as np

BaseDir = '/home/jsteffen'
BaseDir = '/Users/jasonsteffener'
sys.path.append(os.path.join(BaseDir,'Documents','GitHub','CognitiveTasks','DataHandlingScripts'))


import DataHandlingScriptsPart1
importlib.reload(DataHandlingScriptsPart1)


AllOutDataFolder = os.path.join(BaseDir, 'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/')

df = DataHandlingScriptsPart1.CycleOverDataFolders(AllOutDataFolder)

def CycleOverBehDataFolders(AllOutDataFolder):
    #cycle over folders
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
           # Results = LoadRawBehData(subdir,subid)
            
            # #enter the directory and find visit folders
            # VisitFolders = glob.glob(os.path.join(subdir,'*/'))
            # for visFold in VisitFolders:
            #     CurVis = os.path.split(visFold)[0]
            #     CurVis = os.path.split(CurVis)[-1]
            #     if CurVis[-4:-2] == 'V0':
            #         subid = CurDir
            #         Visid = CurVis
            #         print('%s, %s'%(subid, Visid))
            #         Results = LoadRawBehData(os.path.join(AllOutDataFolder, subid, Visid),subid)
    #                 FlatResults = FlattenDict(Results)
    #                 # add subid and visitid
    #                 FlatResults['AAsubid'] = subid
    #                 FlatResults['AAVisid'] = Visid
    #                 FlatResults['AAChecked'] = 0
    #                 ListOfDict.append(FlatResults)
    # df = pd.DataFrame(ListOfDict)
    # return df



VisitFolder='/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/11101035/'
subid = '11101035'
TaskTag = 'DMS_Block'
DataHandlingScriptsPart1.ReadFile(subdir, subid, 'DMS_Block')

def LoadRawBehData(VisitFolder, subid):
    print('working on %s'%(subid))
    Results = {}
    # DMS
    pass

def ReadBehFile(VisitFolder, subid, TaskTag):
    ll = os.listdir(VisitFolder)
    SearchFor = TaskTag + '_' + subid
    matching = fnmatch.filter(ll,SearchFor+'*.csv')
    matchingBlock = fnmatch.filter(ll,SearchString+'*Blocks.csv')
    matchingTrial = fnmatch.filter(ll,SearchString+'*trials.csv')
    if len(matchingBlock) > 0:
        NewDMSFlag = True
            
    matching = set(matching) - set(matchingBlock)
    matching = list(set(matching) - set(matchingTrial))             
    matching = matching[-1]
    InputFile = os.path.join(VisitFolder, matching)
    Data = pd.read_csv(InputFile)

    return Data

def ReadCapacity(SubDir, SearchString):
    ll = os.listdir(SubDir)
    matching = fnmatch.filter(ll,'*'+SearchString+'*')
    if len(matching) > 0:
        InFile = os.path.join(SubDir,matching[0])
        fid = open(InFile,'r')
        Capacity = float(fid.readline())
        fid.close()
    else:
        Capacity = -9999
    return Capacity
       
def CreateFRTList(FRTCapacity):
    Limit = np.float(FRTCapacity)*1.25
    #FRTList = range(0,6,1)Limit,Limit/(6-1))
    FRTList = np.array(range(0,6,1))/(6.0-1)*Limit
    # Convert this array to a string so it can be passed as an argument
    FRTList = ' '.join(str(e) for e in FRTList)
    return FRTList 
         
         
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
            Tag2 = 'AbsLoad%02f'%(ActLoad)
            Out[Tag1+'_Acc'] = Acc
            Out[Tag2+'_Acc'] = Acc
            Out[Tag1+'_RT'] = RT
            Out[Tag2+'_RT'] = RT
            Out[Tag1+'_NResp'] = NResp
            Out[Tag2+'_NResp'] = NResp
            count += 1
    else:
        for i in range(1,6):
            Tag1 = 'RelLoad%02d'%(i)
            Tag2 = 'AbsLoad%02d'%(i)
            Out[Tag1+'_Acc'] = -9999
            Out[Tag2+'_Acc'] = -9999
            Out[Tag1+'_RT'] = -9999
            Out[Tag2+'_RT'] = -9999
            Out[Tag1+'_NResp'] = -9999
            Out[Tag2+'_NResp'] = -9999
    return Out


Results = {} 
Data = ReadBehFile(VisitFolder, subid, 'DMS_Block')
Data = DataHandlingScriptsPart1.CheckDMSDataFrameForLoad(Data)
Results['DMSBeh1'] = DataHandlingScriptsPart1.ProcessDMSBlockv2(Data)

Data = ReadBehFile(VisitFolder, subid, 'FRT_Block')
CAP = ReadCapacity(VisitFolder, 'CAPACITY_FRTstair')
Results['FRTBeh1'] = ProcessFRTBlock(Data, CAP)