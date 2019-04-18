import os
# Config Parameters

# General 
BGColor = 'grey'
FontColor = 'white'
FontSize = 60
InstrFontSize = 35

ThankYouOnTime = 3

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
NBack_MRI1_LoadLevel = '012012' # each number refers to the load level for a block
# Timing parameters
NBack_MRI1_TimePerTrial = 0.5
NBack_MRI1_InterStimulusDelay = 2
NBack_MRI1_TrialPerBlock = 24
NBack_MRI1_NumCorrectPerBlock = 8
NBack_MRI1_StimList = 'BCDFGHJKLMNPRSTVYZ'
NBack_MRI1_ResponseKeys = ['left','right']
NBack_MRI1_IntroOffDuration = 20
NBack_MRI1_InterBlockTime = 15
NBack_MRI1_InstructionTime = 15 
NBack_MRI1_TextSize = 60 # This is in pixels
NBack_MRI1_InstructionFigureSize = 800 # in pixels
NBack_MRI1_Instructions = 'Press the [left] key if the current letter is a match.\n\nPress [return] key to continue.'
NBack_MRI1_InstructFontSize = 45 # in pixels
NBack_MRI1_ThankYouOnTime = 3

# Practice With Feedback
NBack_Prac1_LoadLevel = '012' # each number refers to the load level for a block
# Timing parameters
NBack_Prac1_TimePerTrial = 0.5
NBack_Prac1_InterStimulusDelay = 2
NBack_Prac1_TrialPerBlock = 12
NBack_Prac1_NumCorrectPerBlock = 4
NBack_Prac1_StimList = 'BCDFGHJKLMNPRSTVYZ'
NBack_Prac1_ResponseKeys = ['left','right']
NBack_Prac1_IntroOffDuration = 4 #14
NBack_Prac1_InterBlockTime = 4 #14
NBack_Prac1_InstructionTime = 6 #
NBack_Prac1_TextSize = 60 # This is in pixels
NBack_Prac1_InstructionFigureSize = 800 # in pixels
NBack_Prac1_Instructions = 'Press the [left] key if the current letter is a match.\n\nPress [return] key to continue.'
NBack_Prac1_InstructFontSize = 45 # in pixels
NBack_Prac1_ThankYouOnTime = 3