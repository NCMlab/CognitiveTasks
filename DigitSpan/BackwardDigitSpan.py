
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
""" 
I need to add instructions and a pause at the beginning of this task along with some practive trials



This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Thu Oct  4 11:53:30 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import sound
from psychopy import locale_setup, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import re
FontSize = 30
FontSizeUnits = 'pix'

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# #################
# Store info about the experiment session
expName = u'DigitSpan'  # from the Builder filename that created this script
task = 'Backward'
expInfo = {u'session': u'01', u'Participant ID': u'9999999'}

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
if len(sys.argv) > 1:
    #tempFile.write("Entered if clause\n")
    #tempFile.write('%s\n'%(sys.argv[2]))
    expInfo['Participant ID'] = sys.argv[1]
    #tempFile.write('%s\n'%(sys.argv[1]))
    #tempFile.write('%s\n'%(sys.argv[2]))

    PartDataFolder = sys.argv[2]
    Tag = '1'
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    DataFolder = "../../data"
    PartDataFolder = 'unorganized'
    OutDir = os.path.join(DataFolder, PartDataFolder)
    if not os.path.exists(OutDir):
        os.mkdir(OutDir)
    Tag = '1'
    PartDataFolder = OutDir
 
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = os.path.join(PartDataFolder, '%s_%s_%s_%s_%s' % (expInfo['Participant ID'],expName, task, Tag, expInfo['date']))
CounterBalFlag = 'False'
NumberOfTrials = 14
# #################
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

TrialDuration = 1.0
RespDuration = 6
ITI = 1
corr = 1
resp = event.BuilderKeyResponse()
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# Setup the Window
win = visual.Window(
    size=[1200, 800], fullscr=False, screen=0,
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
sound_1 = sound.Sound('NumberSounds2/1b.wav', secs=-1,sampleRate=44100, bits=16)
sound_1.setVolume(0.8)
SoundFileList.append(sound_1)
sound_2 = sound.Sound('NumberSounds2/2b.wav', secs=-1,sampleRate=44100, bits=16)
sound_2.setVolume(0.8)
SoundFileList.append(sound_2)
sound_3 = sound.Sound('NumberSounds2/3b.wav', secs=-1,sampleRate=44100, bits=16)
sound_3.setVolume(0.8)
SoundFileList.append(sound_3)
sound_4 = sound.Sound('NumberSounds2/4b.wav', secs=-1,sampleRate=44100, bits=16)
sound_4.setVolume(0.8)
SoundFileList.append(sound_4)
sound_5 = sound.Sound('NumberSounds2/5b.wav', secs=-1,sampleRate=44100, bits=16)
sound_5.setVolume(0.8)
SoundFileList.append(sound_5)
sound_6 = sound.Sound('NumberSounds2/6b.wav', secs=-1,sampleRate=44100, bits=16)
sound_6.setVolume(0.8)
SoundFileList.append(sound_6)
sound_7 = sound.Sound('NumberSounds2/7b.wav', secs=-1,sampleRate=44100, bits=16)
sound_7.setVolume(0.8)
SoundFileList.append(sound_7)
sound_8 = sound.Sound('NumberSounds2/8b.wav', secs=-1,sampleRate=44100, bits=16)
sound_8.setVolume(0.8)
SoundFileList.append(sound_8)
sound_9 = sound.Sound('NumberSounds2/9b.wav', secs=-1,sampleRate=44100, bits=16)
sound_9.setVolume(0.8)
SoundFileList.append(sound_9)
CorrectSound = sound.Sound('NumberSounds/correct.wav', secs = -1)
CorrectSound.setVolume(0.8)
IncorrectSound = sound.Sound('NumberSounds/incorrect.wav', secs = -1)
IncorrectSound.setVolume(0.8)

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
ThankYouText = visual.TextStim(win=win, name='ThankYouText',
    text='Thank You',
    font='Arial',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-9.0, units=FontSizeUnits);

Instruct1text = 'Tell the person:\n'"You are going to hear some numbers, when the list ends, I want you to say them to me BACKWARDS from how you heard them."'\n\nPress any key to play the practice numbers.'

Instruct1 = visual.TextStim(win=win, name='Instruct1',
    text=Instruct1text,
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-9.0);
Answer = visual.TextStim(win=win, name='Answer',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-9.0);
Instruct1.setAutoDraw(True)
win.flip()

WaitingForResponseFlag = True
while WaitingForResponseFlag:
    theseKeys = event.getKeys()
            
        # check for quit:
    if "escape" in theseKeys:
        #thisExp.abort()  # or data files will save again on exit
        win.close()
        core.quit()
    if len(theseKeys) > 0:  # at least one key was pressed
        WaitingForResponseFlag = False
        break
    else:
        pass
Instruct1.setAutoDraw(False)        
win.flip()

# START OF PRACTICE TRIAL
CorrectPracticeFlag = False
# Create a list of three numbers drawn from the numbers 1 to 9
R = np.random.permutation(9) + 1
R = R[0:3]
Answer.text = 'Ask the person to repeat the three digits BACKWARDS from how they heard them.\nThe person should repeat: %s\n\nType in what the person said and press "return." If you make a mistake typing in the numbers press x and then retype in what the person said.\n\nPress any key to start the actual experiment.'%(R[::-1])
# cycle over the numbers and play them
for i in range(3):
    countDown.reset()    
    countDown.add(TrialDuration)
    #print('index: %d, Number: %d'%(i,R[i]))
    Index = R[i]-1
    SoundFileList[Index].play()
    #sound_1.play()  # start the sound (it finishes automatically)
    # store data for Stairs (StairHandler)
    while countDown.getTime() > 0:
        pass        
    
    event.clearEvents(eventType='keyboard')
# -------Start Routine "trial"-------
Answer.setAutoDraw(True)
win.flip()

WaitingForResponseFlag = True
while WaitingForResponseFlag:
    theseKeys = event.getKeys()
        
    # check for quit:
    if "escape" in theseKeys:
        #thisExp.abort()  # or data files will save again on exit
        win.close()
        core.quit()
    if len(theseKeys) > 0:  # at least one key was pressed
        resp.keys.extend(theseKeys)  # storing all keys
        resp.rt.append(resp.clock.getTime())

    if 'return' in theseKeys:
        # remove the return before continuing
        resp.keys = resp.keys[:-1]
        WaitingForResponseFlag = False
        break
    else:
        pass
    
if 'x' in resp.keys:
    print('Found a mistake')
    # A mistake as made entering the digits
    # take all values after the LAST x   
    resp.keys = resp.keys[''.join(resp.keys).rindex('x')+1:]

print('Responses: %s'%(resp.keys))
Answer.setAutoDraw(False)
win.flip()
# Convert responses to an array
RespList = []
for i in resp.keys:
    RespList.append(int(i))
RespList = np.array(RespList)
print(RespList)
# This is the BACKWARD Span Task
if np.array_equiv(R[::-1],RespList):
    print('Correct')
    CorrectSound.play()
    thisResp = 1
    resp.corr = 1
else:
    print('Incorrect')
    IncorrectSound.play()
    thisResp = -1
    resp.corr = 0

# END OF PRACTICE TRIAL

#WaitingForResponseFlag = True
#while WaitingForResponseFlag:
#    theseKeys = event.getKeys()
#            
#        # check for quit:
#    if "escape" in theseKeys:
#        thisExp.abort()  # or data files will save again on exit
#        win.close()
#        core.quit()
#    if len(theseKeys) > 0:  # at least one key was pressed
#        WaitingForResponseFlag = False
#        break
#    else:
#        pass
#Answer.setAutoDraw(False)        
#win.flip()

Instruct1.text = 'Tell the person to "Get Ready" for the real task.\n\nPress any key to begin.'


Instruct1.setAutoDraw(True)
win.flip()

WaitingForResponseFlag = True
while WaitingForResponseFlag:
    theseKeys = event.getKeys()
            
        # check for quit:
    if "escape" in theseKeys:
        thisExp.abort()  # or data files will save again on exit
        win.close()
        core.quit()
    if len(theseKeys) > 0:  # at least one key was pressed
        WaitingForResponseFlag = False
        break
    else:
        pass
Instruct1.setAutoDraw(False)        
win.flip()


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# --------Prepare to start Staircase "Stairs" --------
# set up handler to look after next chosen value etc
# This is the BACKWARD Span Task
Stairs = data.StairHandler(startVal=2, extraInfo=expInfo,
    stepSizes=1, stepType='lin',
    nReversals=0, nTrials=NumberOfTrials, 
    nUp=2, nDown=1,
    minVal=2, maxVal=20,
    originPath=-1, name='Stairs')
  
thisExp.addLoop(Stairs)  # add the loop to the experiment
level = thisStair = 3  # initialise some vals

count = 0
for thisStair in Stairs:
    resp.keys = []
    currentLoop = Stairs
    level = thisStair
    print("Trial Number: %d"%(count))
    count += 1
    # Generate the number list
    # Generate random numbers and make sure no consecutive numbers are the same
    Flag = True
    # Change the random numbers to all be different
    
    R = np.random.permutation(9) + 1
    
    # what if someone has a span more than 9!
    if level > 9:
        R1 = np.random.permutation(9) + 1
        R2 = np.random.permutation(9) + 1
        R = np.concatenate((R1,R2))
    
    R = R[0:level]
    #while Flag:
    #    R = np.random.randint(1,10,level)
    #    Flag = any(np.diff(R) == 0)
    print(R)    
    Answer.text = 'Backward: %s\n\n\nTrial Number %d of %d\n\nIf you make a mistake entering the person\'s response, press [x]. This will clear what you entered so you can restart.'%(R[::-1],count+1, NumberOfTrials)
    # cycle over the numbers and play them
    for i in range(level):
        countDown.reset()    
        countDown.add(TrialDuration)
        #print('index: %d, Number: %d'%(i,R[i]))
        Index = R[i]-1
        SoundFileList[Index].play()
        #sound_1.play()  # start the sound (it finishes automatically)
        # store data for Stairs (StairHandler)
        while countDown.getTime() > 0:
            pass        
        
        event.clearEvents(eventType='keyboard')
    # -------Start Routine "trial"-------
    Answer.setAutoDraw(True)
    win.flip()

    WaitingForResponseFlag = True
    while WaitingForResponseFlag:
        theseKeys = event.getKeys()
            
        # check for quit:
        if "escape" in theseKeys:
            #thisExp.abort()  # or data files will save again on exit
            win.close()
            core.quit()
        if len(theseKeys) > 0:  # at least one key was pressed
            resp.keys.extend(theseKeys)  # storing all keys
            resp.rt.append(resp.clock.getTime())

        if 'return' in theseKeys:
            # remove the return before continuing
            resp.keys = resp.keys[:-1]
            WaitingForResponseFlag = False
            break
        else:
            pass
        
    if 'x' in resp.keys:
        print('Found a mistake')
        # A mistake as made entering the digits
        # take all values after the LAST x   
        resp.keys = resp.keys[''.join(resp.keys).rindex('x')+1:]
        
    print('Responses: %s'%(resp.keys))
    Answer.setAutoDraw(False)
    win.flip()
    # Convert responses to an array
    RespList = []
    for i in resp.keys:
        RespList.append(int(i))
    RespList = np.array(RespList)
    print(RespList)
    # This is the BACKWARD Span Task
    if np.array_equiv(R[::-1],RespList):
        print('Correct')
        CorrectSound.play()
        thisResp = -1
        resp.corr = 1
    else:
        print('Incorrect')
        IncorrectSound.play()
        thisResp = 1
        resp.corr = 0
        
    thisExp.addData('Digits',R)
    thisExp.addData('resp.keys',resp.keys)
    if resp.keys != None:  # we had a response
        thisExp.addData('resp.rt', resp.rt)
    thisExp.nextEntry()
    # these shouldn't be strictly necessary (should auto-save)
    
    #thisExp.saveAsPickle(filename)  
    Stairs.addResponse(thisResp)
    Answer.setAutoDraw(False)
    win.flip()
    # Add a between trial wait time
    countDown.reset()
    countDown.add(ITI)
    while countDown.getTime() > 0:
            pass     
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # Make sure only the right number of trials are presented.
    # Sometimes the loop does too many!
    if count == NumberOfTrials:
        break
    
    # staircase completed
t = 0
ThankYouClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThankYouComponents = [ThankYouText]
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ThankYou"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThankYouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankYouText* updates
    if t >= 0.0 and ThankYouText.status == NOT_STARTED:
        # keep track of start time/frame for later
        ThankYouText.tStart = t
        ThankYouText.frameNStart = frameN  # exact frame index
        ThankYouText.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ThankYouText.status == STARTED and t >= frameRemains:
        ThankYouText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ThankYou"-------
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
#thisExp.saveAsPickle(filename)
thisExp.saveAsWideText(filename+'.csv')
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
