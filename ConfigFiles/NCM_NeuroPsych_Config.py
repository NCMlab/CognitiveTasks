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
SRT_WordOnTime = 2.0 # seconds
# The first word in a block is a little too quck so this helps
SRT_FudgeTime = 0.9
SRTPath = os.path.join('CompanionFolderForCognitiveTasks','SRT')
SoundPath = os.path.join('CompanionFolderForCognitiveTasks','SRT','SoundFiles')