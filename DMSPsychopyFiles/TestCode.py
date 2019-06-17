import numpy as np
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
