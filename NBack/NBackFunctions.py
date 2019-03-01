import numpy as np
# Create stimuli
def CreateStim(LoadLevel,TrialPerBlock,NumCorrectPerBlock):
    print "Load level: %d, with %d correct in %d trials"%(LoadLevel,NumCorrectPerBlock,TrialPerBlock)
    # pick NumCorPerBlock unique numbers between 1 and TrialPerBlock
    # make sure that the numbers are seperated by at least the load level number of items 
    if LoadLevel != 0: 
        AllTrue = False
        count = 0
        SuccessFlag = False
        while (AllTrue == False) and count < 1000:
            test = np.round(np.random.uniform(TrialPerBlock*np.ones(NumCorrectPerBlock)))
            test.sort()
            UniqueFlag = len(set(test)) == len(test)
            FirstEntryFlag = test[0] > LoadLevel
            SpacingFlag = True
            PreviousLoc = test[0]
            # Make sure that no more then two corrct responses are in a row
            if sum(np.diff(test) == LoadLevel) > 1:
                SpacingFlag = False 
#            for i in range(1,len(test)):
#                if test[i] < test[i-1] + LoadLevel:
#                    SpacingFlag = False
            # Make sure all conditions are true
            AllTrue = UniqueFlag == True & FirstEntryFlag == True & SpacingFlag == True
            count += 1
            #print "Count = %d"%(count)
            
        if AllTrue == True:
            print "It took %d attempts to create this list"%count
            return test
        else:
            print "Could not find a solution in %d attempts"%count
            return -99
    else:
        test = CreateListZero(TrialPerBlock,NumCorrectPerBlock)
        return test

def AssignStimuli(CorrectLocations,TrialPerBlock,Stimuli,LoadLevel):
    List = ['-99']*TrialPerBlock
    NCor = len(CorrectLocations)
    NStim = len(Stimuli)
    # Use a while loop to check to see if the created list os good or not
    GoodFlag = False
    # Add counter here
    count = 0
    while (GoodFlag == False) & (count < 100):
        # Place random stimuli in the correct locations
        for i in CorrectLocations:
            RandomPick = int(np.round(np.random.uniform(1*NStim)))
            List[int(i)-1] = Stimuli[RandomPick-1]
        # go through and set the previous stimuli appropriately
        for i in range(0,TrialPerBlock,1):
            if List[i] != '-99':
                if List[i-LoadLevel] != '-99':
                    List[i] = List[i-LoadLevel]
                else:
                    List[i-LoadLevel] = List[i]
        # Find the unused stimuli
        UnusedStimuli = []
        for i in Stimuli:
            if i not in List:
                UnusedStimuli.append(i)
        # fill in the empty trials
        for i in range(0,TrialPerBlock,1):
            if List[i] == '-99':
                RandomPick = int(np.round(np.random.uniform(1*len(UnusedStimuli))))
                # remove the stimuli from the list
                List[i] = UnusedStimuli[RandomPick-1]
                UnusedStimuli.pop(RandomPick-1)
        if LoadLevel == 0:
            print "ZERO LOAD LEVEL"
            # load level zero is a specifal condition
            List = np.array(List)
            List[list(CorrectLocations-1)] = 'X'
            List = list(List)
            GoodFlag = True
        # Double check to make sure the list is correct and no correct trials are made accidently.
        # First convert letters to ascii numbers
        NumList = [ord(i) for i in List]
        # Check to see how many correct entries their are 

        if (LoadLevel == 3):
            if (sum(np.diff(NumList[0::LoadLevel]) == 0) + sum(np.diff(NumList[1::LoadLevel]) == 0) + sum(np.diff(NumList[2::LoadLevel]) == 0)) == NCor:
                GoodFlag = True
        elif (LoadLevel == 2):
            if (sum(np.diff(NumList[0::LoadLevel]) == 0) + sum(np.diff(NumList[1::LoadLevel]) == 0)) == NCor:
                GoodFlag = True
        elif (LoadLevel == 1):
            if sum(np.diff(NumList[0::LoadLevel]) == 0) == NCor:
                GoodFlag = True
        count = count + 1
        print "Assign letters count: %d"%(count)
    if GoodFlag == False:
        print "Could not assign letters"
        List = -99
    return List
        
def CreateListZero(TrialPerBlock,NumCorrectPerBlock):
    UniqueFlag = False
    # check to see if this list is appropriate
    SuccessFlag = False
    count = 0
    while not((SuccessFlag == True) and (UniqueFlag)):
        SuccessFlag = False
        UniqueFlag = False
        List = np.round(np.random.uniform(TrialPerBlock*np.ones(NumCorrectPerBlock)))
        List.sort()
        # Are all entries unique?
        UniqueFlag = len(set(List)) == len(List)
        # check to see if any numbers are sequential
        if ~(np.diff(List) == 1).any():
            SuccessFlag = True
        count = count + 1
        if count > 5000:
            raise ValueError('Could not create trial list after 5000 attempts!')
    return List