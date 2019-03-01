from NBackFunctions import *
ExpParameters = {
    'LoadLevel': '01230123',
    'TimePerTrial': 1.5, # seconds
    'TrialPerBlock': 14,
    'StimList': 'ABCDEFGHJKLMNPRSTVWYZ',
    'ResponseKeys':['1','2','3','4','5','6','7','8','9','0'],
    'NumCorrectPerBlock': 4,
    'IntroOffDuration': 36,
    'OffDuration' : 28,
    'InstrTime': 6,
    'TextSize': 0.2,
    'InterStimulusDelay': 0.5
}
NBlocks = 8
AllLists = []
for BlockNumber in range(0,NBlocks,1):
    CurrentLoadLevel = int(ExpParameters['LoadLevel'][BlockNumber])
    CorrectLocations = CreateStim(CurrentLoadLevel,ExpParameters['TrialPerBlock'],ExpParameters['NumCorrectPerBlock'])
    # Try to assign letters to the list of correct locations
    # If it is not possible then -99 is returned
    List = AssignStimuli(CorrectLocations,ExpParameters['TrialPerBlock'],ExpParameters['StimList'],CurrentLoadLevel)
    while not isinstance(List,(list,tuple,np.ndarray)):
        CorrectLocations = CreateStim(CurrentLoadLevel,ExpParameters['TrialPerBlock'],ExpParameters['NumCorrectPerBlock'])
        List = AssignStimuli(CorrectLocations,ExpParameters['TrialPerBlock'],ExpParameters['StimList'],CurrentLoadLevel)
    AllLists.append(List)



NStim = 14
RandomPick = int(np.round(np.random.uniform(1*NStim)))
RandomPick
    
    
    List = AssignStimuli(CorrectLocations,ExpParameters['TrialPerBlock'],ExpParameters['StimList'],CurrentLoadLevel)
    AllLists.append(List)
AllLists

