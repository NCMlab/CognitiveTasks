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


CurrentLoadLevel = 2
TrialPerBlock = 18
NumCorrectPerBlock = 6
CorrectLocations = NBackFunctions.CreateStim(CurrentLoadLevel,TrialPerBlock,NumCorrectPerBlock)
BadFlag = True
AttemptCount = 0
while BadFlag == True:
    BadFlag = False
    CorrectLocations = NBackFunctions.CreateStim(CurrentLoadLevel,TrialPerBlock,NumCorrectPerBlock)
    List = NBackFunctions.AssignStimuliv2(CorrectLocations,TrialPerBlock,StimList,CurrentLoadLevel)
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