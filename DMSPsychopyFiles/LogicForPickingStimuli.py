LetterList = 'BCDFGHJKLMNPQRSTVXYZ'
NLet = len(LetterList)
CurrentLoad = 5
LastStim = 'BCDF'
LastProbe = 'F'
LastTrial = LastStim + LastProbe
# Remove duplicates 
LettersToRemove = list(set(LastTrial))

tempLetterList = list(LetterList)


for i in LastTrial:
    tempLetterList[tempLetterList.index(i)] = ''
tempLetterList = [x for x in tempLetterList if x]
# Now select the new set of letters for the current trial 
# from this list

LastTrial = ''
CurrentLoad = 1
for i in range(0,9,1):
    LettersToRemove = list(set(LastTrial))
    tempLetterList = list(LetterList)
    for j in LettersToRemove:
        tempLetterList[tempLetterList.index(j)] = ''
    # remove empty locations from the list
    tempLetterList = [x for x in tempLetterList if x] 
    # Create the lost of curent stimulus letters
    CurrentStim = ''
    CurrentStimIndex = np.random.permutation(len(tempLetterList))[0:CurrentLoad]
    for j in CurrentStimIndex:
        CurrentStim += tempLetterList[j]
    # Is the probe in teh set?
    Probe = np.round(np.random.uniform())
    if bool(Probe):
        # Yes, the probe is in the set
        CurrentProbe = CurrentStim[np.random.permutation(len(CurrentStim))[0]]
        CurrentProbe = CurrentProbe.lower()
        corr = 'left'
    else:
        # Remove the current stim letters from the available letter set
        for j in CurrentStim:
            tempLetterList[tempLetterList.index(j)] = ''
        # remove empty locations from the list
        tempLetterList = [x for x in tempLetterList if x] 
        CurrentProbe = tempLetterList[np.random.permutation(len(tempLetterList))[0]]
        corr = 'down'
    LastTrial = CurrentStim + CurrentProbe
    InStim = MapLettersToScreen(CurrentStim)
    
    print(InStim+'   '+CurrentProbe)
    CurrentLoad += 1
    
def MapLettersToScreen(Stim):
    NLet = len(Stim)
    if NLet == 1:
        Output = '****'+Stim+'****'
    elif NLet == 2:
        Output = '***'+Stim[0]+'*'+Stim[1]+'***'
    elif NLet == 3:
        Output = '***'+Stim+'***'
    elif NLet == 4:
        Output = Stim[0]+'*'+Stim[1]+'***'+Stim[2]+'*'+Stim[3]
    elif NLet == 5:
        Output = Stim[0]+'*'+Stim[1]+'*'+Stim[2]+'*'+Stim[3]+'*'+Stim[4]
    elif NLet == 6:
        Output = Stim[0:3]+'***'+Stim[3:6]
    elif NLet == 7:
        Output = Stim[0:3]+'*'+Stim[3]+'*'+Stim[4:7]
    elif NLet == 8:
        Output = Stim[0:4]+'*'+Stim[4:8]
    else:
        Output = Stim
    return(Output)
        
        