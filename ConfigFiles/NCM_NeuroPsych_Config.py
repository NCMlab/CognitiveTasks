import os
# Config Parameters

# General 
BGColor = 'grey'
FontColor = 'white'
FontSize = 60
InstrFontSize = 35

ThankYouOnTime = 3

# SRT Task
SRT_ResponseTimeAllowed = 60 # seconds
SRT_WordOnTime = 1.0 # seconds
# The first word in a block is a little too quck so this helps
SRT_FudgeTime = 0.9
SRTPath = os.path.join('CompanionFolderForCognitiveTasks','SRT')
SoundPath = os.path.join('CompanionFolderForCognitiveTasks','SRT','SoundFiles')


# VSTM Tasks
StimOnTime = 2.5
RetOnTime = 3.2
ProbeOnTime= 2.5
MaskOnTime = 0.3
# This is the intertrial interval. This experimental component is part of the trial.
ITITime = 1.0 #1.0

GridCount = 6 # Number of circles to have on each row
GridSize = 52*GridCount + 1 # The size of the grid for which the circles on on

# N-Back task
# Behavioral Run 1
NBack_Beh1_LoadLevel = '012012' # each number refers to the load level for a block
# Timing parameters
NBack_Beh1_TimePerTrial = 0.5
NBack_Beh1_InterStimulusDelay = 1.5
NBack_Beh1_TrialPerBlock = 24
NBack_Beh1_NumCorrectPerBlock = 8
NBack_Beh1_StimList = 'ABCDEFGHJKLMNPRSTVYZ'
NBack_Beh1_ResponseKeys = ['left','right']
NBack_Beh1_IntroOffDuration = 4#14
NBack_Beh1_InterBlockTime = 4#14
NBack_Beh1_InstructionTime = 3#6 #
NBack_Beh1_TextSize = 60 # This is in pixels
NBack_Beh1_InstructionFigureSize = 800 # in pixels
NBack_Beh1_Instructions = 'Press the [left] key if the current letter is a match.\n\nPress [return] key to continue.'
NBack_Beh1_InstructFontSize = 45 # in pixels
NBack_Beh1_ThankYouOnTime = 3
# Practice With Feedback
NBack_Prac1_LoadLevel = '012' # each number refers to the load level for a block
# Timing parameters
NBack_Prac1_TimePerTrial = 0.5
NBack_Prac1_InterStimulusDelay = 1.5
NBack_Prac1_TrialPerBlock = 12
NBack_Prac1_NumCorrectPerBlock = 4
NBack_Prac1_StimList = 'ABCDEFGHJKLMNPRSTVYZ'
NBack_Prac1_ResponseKeys = ['left','right']
NBack_Prac1_IntroOffDuration = 4#14
NBack_Prac1_InterBlockTime = 4#14
NBack_Prac1_InstructionTime = 3#6 #
NBack_Prac1_TextSize = 60 # This is in pixels
NBack_Prac1_InstructionFigureSize = 800 # in pixels
NBack_Prac1_Instructions = 'Press the [left] key if the current letter is a match.\n\nPress [return] key to continue.'
NBack_Prac1_InstructFontSize = 45 # in pixels
NBack_Prac1_ThankYouOnTime = 3