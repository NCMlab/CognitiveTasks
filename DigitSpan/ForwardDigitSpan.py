#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Thu Oct  4 11:53:30 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'ForwardDigitSpan'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[800, 600], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

countDown = core.CountdownTimer()

# Initialize components for Routine "trial"
trialClock = core.Clock()
# Create a list of sound files
SoundFileList = []
sound_1 = sound.Sound('NumberSounds/1.wav', secs=-1)
sound_1.setVolume(1)
SoundFileList.append(sound_1)
sound_2 = sound.Sound('NumberSounds/2.wav', secs=-1)
sound_2.setVolume(1)
SoundFileList.append(sound_2)
sound_3 = sound.Sound('NumberSounds/3.wav', secs=-1)
sound_3.setVolume(1)
SoundFileList.append(sound_3)
sound_4 = sound.Sound('NumberSounds/4.wav', secs=-1)
sound_4.setVolume(1)
SoundFileList.append(sound_4)
sound_5 = sound.Sound('NumberSounds/5.wav', secs=-1)
sound_5.setVolume(1)
SoundFileList.append(sound_5)
sound_6 = sound.Sound('NumberSounds/6.wav', secs=-1)
sound_6.setVolume(1)
SoundFileList.append(sound_6)
sound_7 = sound.Sound('NumberSounds/7.wav', secs=-1)
sound_7.setVolume(1)
SoundFileList.append(sound_7)
sound_8 = sound.Sound('NumberSounds/8.wav', secs=-1)
sound_8.setVolume(1)
SoundFileList.append(sound_8)
sound_9 = sound.Sound('NumberSounds/9.wav', secs=-1)
sound_9.setVolume(1)
SoundFileList.append(sound_9)
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# --------Prepare to start Staircase "Stairs" --------
# set up handler to look after next chosen value etc
Stairs = data.StairHandler(startVal=3, extraInfo=expInfo,
    stepSizes=-1, stepType='lin',
    nReversals=10, nTrials=14, 
    nUp=2, nDown=1,
    minVal=3, maxVal=20,
    originPath=-1, name='Stairs')
thisExp.addLoop(Stairs)  # add the loop to the experiment
level = thisStair = 3  # initialise some vals

TrialDuration = 1.5
RespDuration = 6
corr = 1
resp = event.BuilderKeyResponse()
for thisStair in Stairs:

    
    currentLoop = Stairs
    level = thisStair
    print("Stair %d"%(thisStair))
    # Generate the number list
    # Generate random numbers and make sure no consecutive numbers are the same
    Flag = True
    while Flag:
        R = np.random.randint(1,10,level)
        Flag = any(np.diff(R) == 0)
    print(R)    
    for i in range(level):
        countDown.reset()    
        countDown.add(TrialDuration)
        print('index: %d, Number: %d'%(i,R[i]))
        Index = R[i]-1
        SoundFileList[Index].play()
        #sound_1.play()  # start the sound (it finishes automatically)
        # store data for Stairs (StairHandler)
        while countDown.getTime() > 0:
            pass        
        
        event.clearEvents(eventType='keyboard')
  #  print(countDown.getTime())
    countDown.add(RespDuration)
    thisResp = -1
    resp.keys = -99
    resp.rt = -99
    while countDown.getTime() > 0:
        theseKeys = event.getKeys(keyList=['escape','1', '0'])
        if 'escape' in theseKeys:
            win.close()
            core.quit()
        if len(theseKeys) > 0:  # at least one key was pressed
            resp.keys = theseKeys[-1]  # just the last key pressed
            resp.rt = resp.clock.getTime()
            # was this 'correct'?
            if (resp.keys == str(corr)) or (resp.keys == corr):
                print(resp.keys)
                print(corr)
                print('Correct')
                thisResp = 1
                resp.corr = 1
                break
            else:
                print(resp.keys)
                print(corr)                
                print('incorrect')
                thisResp = -1
                resp.corr = 0   
                break
        pass        
        
    Stairs.addResponse(thisResp)
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # staircase completed

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
