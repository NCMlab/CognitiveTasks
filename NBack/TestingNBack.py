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

Correct1Locations1 = array([3, 6, 8, 12, 14, 17])
Correct1Locations2 = array([4, 6, 9, 12, 14, 17])

Correct2Locations1 = array([4, 7 ,10, 13, 15, 18])
Correct2Locations2 = array([4, 8, 10, 13, 16, 18])

CurrentLoadLevel = 1
BadFlag = True
AttemptCount = 0
while BadFlag == True:
    BadFlag = False
    CorrectLocations = NBackFunctions.CreateStim(CurrentLoadLevel,TrialPerBlock,NumCorrectPerBlock)
    
    CorrectLocations = Correct1Locations2
    
        # Create an empty list 
    List = ['-99']*TrialPerBlock
    # Place random stimuli in the correct locations
#    List = NBackFunctions.AddResponseLettersAndBackLetters(CorrectLocations, List, StimList, TrialPerBlock, CurrentLoadLevel) 
    
    List = NBackFunctions.AssignStimuliv2(CorrectLocations,TrialPerBlock,StimList,CurrentLoadLevel)
    Current = List[0]
    for j in range(3,TrialPerBlock):
        # Two consectutive are equal
        if List[j] == Current:
            BadFlag = True
        Current = List[j-2]
    AttemptCount += 1
#print(List)
print(AttemptCount)
            
Str = ''
for i in List:
    Str = Str + i
print(Str)