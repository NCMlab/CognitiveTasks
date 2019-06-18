import numpy as np

LetterList = 'BCDFGHJKLMNPQRSTVXYZ'
tempLetterList = LetterList
CurrentStim = ''
CurrentLoad = 2
NotOneL_StimFlag = True
while NotOneL_StimFlag:
    CurrentStimIndex = np.random.permutation(len(tempLetterList))[0:CurrentLoad]
    
    for j in CurrentStimIndex:
        CurrentStim += tempLetterList[j]
    if not CurrentStim == 'L':
        NotOneL_StimFlag = False
        
# CHeck for the L stim situation


CurrentStim = 'L'
Probe = np.round(np.random.uniform())
if bool(Probe):
    # Yes, the probe is in the set
    #CurrentProbe = CurrentStim[np.random.permutation(len(CurrentStim))[0]]
    LookingForProbe = True
    while LookingForProbe:
        #CurrentProbe = tempLetterList[np.random.permutation(len(CurrentStim))[0]]
        CurrentProbe = CurrentStim[np.random.permutation(len(CurrentStim))[0]]
        if CurrentProbe != 'L':
            LookingForProbe = False
    corr = 'left'
else:
    # Remove the current stim letters from the available letter set
    for j in CurrentStim:
        tempLetterList[tempLetterList.index(j)] = ''
    # remove empty locations from the list
    tempLetterList = [x for x in tempLetterList if x] 
    LookingForProbe = True
    while LookingForProbe:
        CurrentProbe = tempLetterList[np.random.permutation(len(tempLetterList))[0]]
        if CurrentProbe != 'L':
            LookingForProbe = False
    corr = 'right'
CurrentProbe = CurrentProbe.lower()    
