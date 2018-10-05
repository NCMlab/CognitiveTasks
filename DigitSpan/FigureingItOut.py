from __future__ import absolute_import, division
from psychopy import sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
print("Hello World")
sound_1 = sound.Sound('NumberSounds/1.wav', secs=-1)
sound_1.play()

sound_1.play()
sound_1.play()

trials = data.StairHandler(startVal=3, extraInfo=expInfo,
    stepSizes=-1, stepType='lin',
    nReversals=0, nTrials=14.0, 
    nUp=2, nDown=1,
    minVal=1.0, maxVal=20.0,
    originPath=-1, name='trials')
    
