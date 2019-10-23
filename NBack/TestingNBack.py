import sys
import os
import NBackFunctions
_thisDir = os.getcwd()
sys.path.append(os.path.join(_thisDir, '..','ConfigFiles'))

ConfigFile = 'NBack_fMRI_Config'
# Load up the config file
print("Loading up the config file: %s"%(ConfigFile))
Str = 'from %s import *'%(ConfigFile)
exec(Str)



TrialPerBlock = 18
NumCorrectPerBlock = 6

Correct0Locations1 = array([4,6,10,13,15,17])
Correct0Locations2 = array([2,7,9,12,15,17])


CurrentLoadLevel = 0
BadFlag = True
AttemptCount = 0
while BadFlag == True:
    BadFlag = False
    CorrectLocations = NBackFunctions.CreateStim(CurrentLoadLevel,TrialPerBlock,NumCorrectPerBlock)
    
    CorrectLocations = Correct0Locations2
    
        # Create an empty list 
    List = ['-99']*TrialPerBlock
    # Place random stimuli in the correct locations
    List = NBackFunctions.AddResponseLettersAndBackLetters(CorrectLocations, List, StimList, TrialPerBlock, CurrentLoadLevel) 
    List = NBackFunctions.FillinTheLettersWithNoResponses(List, StimList) 
    # List = NBackFunctions.AssignStimuliv2(CorrectLocations,TrialPerBlock,StimList,CurrentLoadLevel)
    Current = List[0]
    for j in range(3,TrialPerBlock):
        # Two consectutive are equal
        if List[j] == Current:
            BadFlag = True
        Current = List[j-2]
    AttemptCount += 1
print(List)
print(AttemptCount)
            
Str = ''
for i in List:
    Str = Str + i
print(Str)




## ######
LoadLevel = '012012' #
NBlocks = len(LoadLevel)
AllLists = []
AllCorrectLocations = []
for BlockNumber in range(0,NBlocks,1):
    CurrentLoadLevel = int(LoadLevel[BlockNumber])
#    print(CurrentLoadLevel)
#    print(TrialPerBlock)
#    print(NumCorrectPerBlock)
    CorrectLocations = NBackFunctions.CreateStimFixed18_6(CurrentLoadLevel)
    #CorrectLocations = NBackFunctions.CreateStim(CurrentLoadLevel, TrialPerBlock, NumCorrectPerBlock)
#    print(CorrectLocations)
    # Try to assign letters to the list of correct locations
    # If it is not possible then -99 is returned
    print(TrialPerBlock)
    print(StimList)
    print(CurrentLoadLevel)
    List = NBackFunctions.AssignStimuliv2(CorrectLocations,TrialPerBlock,StimList,CurrentLoadLevel)
#    List = AssignStimuli(CorrectLocations, TrialPerBlock, StimList, CurrentLoadLevel)
#    while not isinstance(List,(list,tuple,np.ndarray)):
#        CorrectLocations = NBackFunctions.CreateStim(CurrentLoadLevel, TrialPerBlock, NumCorrectPerBlock)
#        List = NBackFunctions.AssignStimuliv2(CorrectLocations, TrialPerBlock, StimList, CurrentLoadLevel)
    AllLists.append(List)
    AllCorrectLocations.append(CorrectLocations)