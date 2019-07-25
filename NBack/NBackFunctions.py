import numpy as np
# Create stimuli
# Limit = 10000
# 
# LoadLevel = 1
# TrialPerBlock = 48
# NumCorrectPerBlock = 20
# Out = np.zeros((100,100))
# for i in range(10,100):
#     for j in range(2,90):
#         CorrectLocations = CreateStim(LoadLevel,i,j)
#         if len(CorrectLocations) > 1:
#             Out[i,j] = 1
#             
#             
# 
# AssignStimuliv2(CorrectLocations,TrialPerBlock,Stimuli,LoadLevel)

def CreateStimFixed18_6(LoadLevel):
    # This was created so that a fixed order could be used for all participants.
    # It also
    if LoadLevel == 0:
        test = np.array([4,6,10,13,15,17]) # These are natural number locations starting at ONE
    if LoadLevel == 1:
        test = np.array([4,6,10,13,16,18])
    if LoadLevel == 2:
        test = np.array([3,6,9,11,14,18])
    return test

def MakeAllListsOfStimuli(LoadLevel, TrialPerBlock, StimList):
    NBlocks = len(LoadLevel)
    # Make a list of stimuli, one for each block
    AllLists = []
    AllCorrectLocations = []
    for BlockNumber in range(0,NBlocks,1):
        CurrentLoadLevel = int(LoadLevel[BlockNumber])
    
        CorrectLocations = CreateStimFixed18_6(CurrentLoadLevel)
    
        List = AssignStimuliv2(CorrectLocations,TrialPerBlock,StimList,CurrentLoadLevel)
    
        AllLists.append(List)
        AllCorrectLocations.append(CorrectLocations)
    return AllLists, AllCorrectLocations

def HardCodedLists_18sym_6Targets_Loads012012(RunNumber = 0):

    # Fix this so that all zero back blocks have the same letter positions
    ZeroBackBlock1Run1 = ['HKFXPXJTLXPRXZXJXM'] # 
    # These are written in 1,2,3 counting
    CorrLocZeroBlock1Run1 = np.array([4,6,10,13,15,17])    
    ZeroBackBlock2Run1 = ['GXLKMSXZXDSXRMXVXP']
    CorrLocZeroBlock2Run1 = np.array([2,7,9,12,15,17])
    
    ZeroBackBlock1Run2 = ['MVDXMXFKJXTYXRXBXM'] # 
    CorrLocZeroBlock1Run2 = np.array([4,6,10,13,15,17])    
    ZeroBackBlock2Run2 = ['LXDNPGXHXMYXLKXVXY']
    CorrLocZeroBlock2Run2 = np.array([3,5,10,12,14,18])


    ZeroBackBlock1Run3 = ['TYVXKXSPYXVHXMXTXF']
    CorrLocZeroBlock1Run3 = np.array([4,6,10,13,15,17])
    ZeroBackBlock2Run3 = ['DXLJYHXKXJTXHNXJXK']
    CorrLocZeroBlock2Run3 = np.array([3,5,9,12,14,18])
    
    ZeroBackBlock1Run4 = ['RNSXMXPRKXSGXVXCXM']
    CorrLocZeroBlock1Run4 = np.array([4,6,10,13,15,17])
    ZeroBackBlock2Run4 = ['FXLHSYXZXMLXCMXNXG']
    CorrLocZeroBlock2Run4 = np.array([3,5,9,12,14,18])
    
    
    
    OneBackBlock1Run1 = ['RDDVPPRRMPFFJJYCCT'] # 
    CorrLocOneBlock1Run1 = np.array([3,6,8,12,14,17])
    OneBackBlock2Run1 = ['PHFFRRTBBPDDZZTGGF'] # 
    CorrLocOneBlock2Run1 = np.array([4,6,9,12,14,17])
    
    OneBackBlock1Run2 = ['YPPNGGDDSCMMYYHSSM']
    CorrLocOneBlock1Run2 = np.array([3,6,8,12,14,17])
    OneBackBlock2Run2 = ['MRTTSSDJJYHHFFDVVT']
    CorrLocOneBlock2Run2 = np.array([4,6,9,12,14,17])
    
    OneBackBlock1Run3 = ['RGGNYYCCLJZZLLRJJH']
    CorrLocOneBlock1Run3 = np.array([3,6,8,12,14,17])
    OneBackBlock2Run3 = ['JHKKSSGHHZFFVVKJJF']
    CorrLocOneBlock2Run3 = np.array([4,6,9,12,14,17])
    
    OneBackBlock1Run4 = ['JPPRKKHHCLRRGGVJJC']
    CorrLocOneBlock1Run4 = np.array([3,6,8,12,14,17])
    OneBackBlock2Run4 = ['YTFFDDMVVTMMYYDSSC']
    CorrLocOneBlock2Run4 = np.array([4,6,9,12,14,17])  

    TwoBackBlock1Run1 = ['BMJMRDRHJHTNTVTSBS'] 
    CorrLocTwoBlock1Run1 = np.array([4,7,10,13,15,18])
    TwoBackBlock2Run1 = ['TMDMYLDLGLPHPKRKJK'] 
    CorrLocTwoBlock2Run1 = np.array([4,8,10,13,16,18])
    
    TwoBackBlock1Run2 = ['MCFCTSTRZRSNSFSYVY']
    CorrLocTwoBlock1Run2 = np.array([4,7,10,13,15,18])
    TwoBackBlock2Run2 = ['HCGCLTRTYTPCPLDLJL']
    CorrLocTwoBlock2Run2 = np.array([4,8,10,13,16,18])
    
    TwoBackBlock1Run3 = ['NMPMDKDKRKCGCJCRSR']
    CorrLocTwoBlock1Run3 = np.array([4,7,10,13,15,18])
    TwoBackBlock2Run3 = ['STKTRYLYHYRMRDCDZD']
    CorrLocTwoBlock2Run3 = np.array([4,8,10,13,16,18])
    
    TwoBackBlock1Run4 = ['TDSDKTKHNHGBGFGLCL']
    CorrLocTwoBlock1Run4 = np.array([4,7,10,13,15,18])
    TwoBackBlock2Run4 = ['GYLYSTLTNTJKJMVMKM']
    CorrLocTwoBlock2Run4 = np.array([4,8,10,13,16,18])  
    
    Run1 = np.array([ZeroBackBlock1Run1, OneBackBlock1Run1, TwoBackBlock1Run1, ZeroBackBlock2Run1, OneBackBlock2Run1, TwoBackBlock2Run1])
    Run2 = np.array([ZeroBackBlock1Run2, OneBackBlock1Run2, TwoBackBlock1Run2, ZeroBackBlock2Run2, OneBackBlock2Run2, TwoBackBlock2Run2])
    Run3 = np.array([ZeroBackBlock1Run3, OneBackBlock1Run3, TwoBackBlock1Run3, ZeroBackBlock2Run3, OneBackBlock2Run3, TwoBackBlock2Run3])
    Run4 = np.array([ZeroBackBlock1Run4, OneBackBlock1Run4, TwoBackBlock1Run4, ZeroBackBlock2Run4, OneBackBlock2Run4, TwoBackBlock2Run4]) 
    CorLocRun1 = np.array([CorrLocZeroBlock1Run1, CorrLocOneBlock1Run1, CorrLocTwoBlock1Run1, CorrLocZeroBlock2Run1, CorrLocOneBlock2Run1, CorrLocTwoBlock2Run1])
    CorLocRun2 = np.array([CorrLocZeroBlock1Run2, CorrLocOneBlock1Run2, CorrLocTwoBlock1Run2, CorrLocZeroBlock2Run2, CorrLocOneBlock2Run2, CorrLocTwoBlock2Run2])
    CorLocRun3 = np.array([CorrLocZeroBlock1Run3, CorrLocOneBlock1Run3, CorrLocTwoBlock1Run3, CorrLocZeroBlock2Run3, CorrLocOneBlock2Run3, CorrLocTwoBlock2Run3])
    CorLocRun4 = np.array([CorrLocZeroBlock1Run4, CorrLocOneBlock1Run4, CorrLocTwoBlock1Run4, CorrLocZeroBlock2Run4, CorrLocOneBlock2Run4, CorrLocTwoBlock2Run4])
                
    
    AllListsRun1 = ConvertNBackLists(Run1)
    AllListsRun2 = ConvertNBackLists(Run2)
    AllListsRun3 = ConvertNBackLists(Run3)
    AllListsRun4 = ConvertNBackLists(Run4)
    # This just makes it easier to call the list needed
    All = np.array([AllListsRun1, AllListsRun2, AllListsRun3, AllListsRun4])
    AllCorLoc = np.array([CorLocRun1, CorLocRun2, CorLocRun3, CorLocRun4])
    
    return All[RunNumber], AllCorLoc[RunNumber]
    
def ConvertNBackLists(Run):
    # Put all the lists into the same format that the "on the fly" programs use
    AllLists = []
    for i in Run:
        List = []
        for j in i[0]:
            List.append(j)
        AllLists.append(List)
    return AllLists
            
            
            
def CreateStimFixed12_4(LoadLevel):
    # This was created so that a fixed order ciuld be used for all participants.
    # It also
    if LoadLevel == 0:
        test = np.array([3,6,9,12]) # These are natural number locations starting at ONE
    if LoadLevel == 1:
        test = np.array([3,5,9,12])
    if LoadLevel == 2:
        test = np.array([4,7,10,12])
    return test

def CreateStim(LoadLevel,TrialPerBlock,NumCorrectPerBlock):
    print("Load level: %d, with %d correct in %d trials"%(LoadLevel,NumCorrectPerBlock,TrialPerBlock))
    # pick NumCorPerBlock unique numbers between 1 and TrialPerBlock
    # make sure that the numbers are seperated by at least the load level number of items 
    Limit = 10000
    if LoadLevel != -99: 
        AllTrue = False
        count = 0
        SuccessFlag = False
        while (AllTrue == False) and count < Limit:
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
            print("It took %d attempts to create this list"%(count))
            return test
        else:
            print("Could not find a solution in %d attempts"%(count))
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
    while (GoodFlag == False) & (count < Limit):
        # Place random stimuli in the correct locations
        for i in CorrectLocations:
            # Take a random letter from the list of stimuli
            RandomPick = int(np.round(np.random.uniform(1*NStim)))
            List[int(i)-1] = Stimuli[RandomPick-1]
        # go through and set the previous stimuli appropriately
        for i in range(0,TrialPerBlock,1):
            if List[i] != '-99':
                if List[i-LoadLevel] != '-99':
                    List[i] = List[i-LoadLevel]
                else:
                    List[i-LoadLevel] = List[i]
        # # Find the unused stimuli
        # UnusedStimuli = []
        # for i in Stimuli:
        #     if i not in List:
        #         UnusedStimuli.append(i)
        # fill in the empty trials
        for i in range(0,TrialPerBlock,1):
            if List[i] == '-99':
                RandomPick = int(np.round(np.random.uniform(1*len(Stimuli))))
                # remove the stimuli from the list
                List[i] = Stimuli[RandomPick-1]
                #UnusedStimuli.pop(RandomPick-1)
        if LoadLevel == 0:
            print("ZERO LOAD LEVEL")
            # load level zero is a specifal condition
            List = np.array(List)
            for i in CorrectLocations-1:
                List[int(i)] = 'X'
            # List[list(CorrectLocations-1)] = 'X'
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
        print("Assign letters count: %d"%(count))
    if GoodFlag == False:
        print("Could not assign letters")
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

def AssignStimuliv2(CorrectLocations,TrialPerBlock,Stimuli,LoadLevel):
    # Create an empty list 
    List = ['-99']*TrialPerBlock
    # Place random stimuli in the correct locations
    List = AddResponseLettersAndBackLetters(CorrectLocations, List, Stimuli, TrialPerBlock, LoadLevel)
    # Fill in the rest of the letters    
    List = FillinTheLettersWithNoResponsesv2(List, Stimuli)    
    return List
    
def FillinTheLettersWithNoResponsesv2(List, Stimuli):  
    NStim = len(Stimuli)
    count = 0
    for i in List:
        if i == '-99':
            MatchFlag = True
            while MatchFlag == True:
                RandomPick = int(np.round(np.random.uniform(1*NStim)))
                # Make sure this letter is NOT in the list already
                CurrentStim = Stimuli[RandomPick-1]
                MatchFlag = CheckLetterAlreadyInList(List, CurrentStim)
            print(CurrentStim)
            List[count] = CurrentStim
        count += 1
    return List
            
def FillinTheLettersWithNoResponses(List, Stimuli):
    NStim = len(Stimuli)
    # Start at the begining of the list
    Position = 0
    # This is a limit for how many random picks from the letter list will be used 
    # when trying to pick a letter.
    # 1000 is way too many
    Limit = 1000
    for i in List:
        count = 0        
        if i == '-99':
            # Letter is needed at this position

            while count < Limit:
                # Pick a random letter
                RandomPick = int(np.round(np.random.uniform(1*NStim)))
                NewLetter = Stimuli[RandomPick-1]                
                # Check to see if this new letter is not the same as, 1,2,3 back
                if CheckNewLetter(List, NewLetter, Position):
                    # If the letter is good, add it to the list
                    List[Position] = NewLetter
                    # then break out of the while loop
                    break
                else:
                    count += 1
        Position += 1
        #print(count)
    return List

def CheckLetterAlreadyInList(List, CurrentLetter):
    MatchFlag = False
    for i in List:
        if CurrentLetter == i:
            MatchFlag = True
    return MatchFlag
                
def AddResponseLettersAndBackLetters(CorrectLocations, List, Stimuli, TrialPerBlock, LoadLevel):
    # STart with an empty list and place the letters that will require a response
    # and the appropriate "Back" letters
    NStim = len(Stimuli)
    if LoadLevel > 0:
        for i in CorrectLocations:
        # Take a random letter from the list of stimuli and make sure it is not already in the list
            MatchFlag = True
            while MatchFlag == True:
                RandomPick = int(np.round(np.random.uniform(1*NStim)))
                # Make sure this letter is NOT in the list already
                CurrentStim = Stimuli[RandomPick-1]
                MatchFlag = CheckLetterAlreadyInList(List, CurrentStim)
            print(CurrentStim)
            List[int(i)-1] = CurrentStim
        # go through and set the previous stimuli appropriately
        for i in range(0,TrialPerBlock,1):
            if List[i] != '-99':
                if List[i-LoadLevel] != '-99':
                    List[i] = List[i-LoadLevel]
                else:
                    List[i-LoadLevel] = List[i]
    else:
        for i in CorrectLocations:
            List[int(i)-1] = 'X'
    return List
    
def CheckNewLetter(List, NewLetter, Position):
    # For each NON stim letter to be added to the list check to make sure that it is 
    # Not the same as the previous 0,1,2,3,4 letter
    Flag = True
    # Check previous letter
    # If we are not at the first letter
    if Position > 0:
        if (List[Position - 1] == NewLetter):
            Flag = False
    if Position > 1:
        if List[Position - 2] == NewLetter:
            Flag = False
    if Position > 2:
        if List[Position - 3] == NewLetter:
            Flag = False    
    return Flag     