#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Tue Mar 13 16:21:54 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'

from numpy.random import random, randint, normal, shuffle
import array
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'LexicalDecision'  # from the Builder filename that created this script
expInfo = {u'ParticipantID': u'99999999'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['ParticipantID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
#win = visual.Window(
#    size=(1440, 900), fullscr=True, screen=0,
#    allowGUI=False, allowStencil=False,
#    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
#    blendMode='avg', useFBO=True)
win = visual.Window(
    size=(800, 600), fullscr=False, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess


Instruct = visual.TextStim(win=win, name='Instruct',
    text='Press the left arrow for animate objects.\nPress the down arrow for inanimate objects.\n\nPress 5 to start.\nPress Escape at any time to interupt and stop the experiment.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
WhiteCrossHair1 = visual.TextStim(win=win, name='WhiteCrossHair1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
textWord = visual.TextStim(win=win, name='textWord',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
textTrialEndCross = visual.TextStim(win=win, name='textTrialEndCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
ITICrossHair = visual.TextStim(win=win, name='ITICrossHair',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
textThankYou = visual.TextStim(win=win, name='textThankYou',
    text='Thank You',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Wait"
WaitClock = core.Clock()

# Initialize components for Routine "WhiteCrossHair"
WhiteCrossHairClock = core.Clock()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()

# Initialize components for Routine "WhiteCrossHair"
WhiteCrossHairClock = core.Clock()

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Wait"-------
t = 0
WaitClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
WaitComponents = [Instruct, key_resp_2]
for thisComponent in WaitComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Wait"-------
while continueRoutine:
    # get current time
    t = WaitClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct* updates
    if t >= 0.0 and Instruct.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instruct.tStart = t
        Instruct.frameNStart = frameN  # exact frame index
        Instruct.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Wait"-------
for thisComponent in WaitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Wait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WhiteCrossHair"-------
t = 0
WhiteCrossHairClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
WhiteCrossHairComponents = [WhiteCrossHair1]
for thisComponent in WhiteCrossHairComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WhiteCrossHair"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WhiteCrossHairClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WhiteCrossHair1* updates
    if t >= 0.0 and WhiteCrossHair1.status == NOT_STARTED:
        # keep track of start time/frame for later
        WhiteCrossHair1.tStart = t
        WhiteCrossHair1.frameNStart = frameN  # exact frame index
        WhiteCrossHair1.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if WhiteCrossHair1.status == STARTED and t >= frameRemains:
        WhiteCrossHair1.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WhiteCrossHairComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WhiteCrossHair"-------
for thisComponent in WhiteCrossHairComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc

trials00 = data.TrialHandler(nReps=1, method='random',
    trialList=data.importConditions('WORDStaircaseFiles/WordLoad00.csv'),
     seed=None, name='trials00')
trials05 = data.TrialHandler(nReps=1, method='random',
    trialList=data.importConditions('WORDStaircaseFiles/WordLoad05.csv'),
     seed=None, name='trials05')
trials10 = data.TrialHandler(nReps=1, method='random',
    trialList=data.importConditions('WORDStaircaseFiles/WordLoad10.csv'),
     seed=None, name='trials10')     
trials15 = data.TrialHandler(nReps=1, method='random',
    trialList=data.importConditions('WORDStaircaseFiles/WordLoad15.csv'),
     seed=None, name='trials15')
trials20 = data.TrialHandler(nReps=1, method='random',
    trialList=data.importConditions('WORDStaircaseFiles/WordLoad20.csv'),
     seed=None, name='trials20')     
trials25 = data.TrialHandler(nReps=1, method='random',
    trialList=data.importConditions('WORDStaircaseFiles/WordLoad25.csv'),
     seed=None, name='trials25')
trials30 = data.TrialHandler(nReps=1, method='random',
    trialList=data.importConditions('WORDStaircaseFiles/WordLoad30.csv'),
     seed=None, name='trials30')     

ITI = 0.5     
# Put all trials together

AllTrials = [trials00, trials05, trials10, trials15, trials20, trials25, trials30]
# How many trials per load
NTrials = []
for i in AllTrials:
    NTrials.append(len(i.trialList))
Nloads = np.size(AllTrials)
LoadCount = np.zeros(int(Nloads))
LoadCount = array.array('i',(0 for i in range(0,Nloads)))

# How to shuffle the lists?
# I can make a list of random numbers. Then whenever I pick a stim set I just cycle 
# down this list of random numbers.
NumberOfReversals = 2
#create the staircase handler
staircase = data.StairHandler(startVal = 3,
                          stepType = 'lin', stepSizes=[0.5],
                          nUp=1, nDown=3,  # will home in on the 80% threshold
                          nReversals = NumberOfReversals, minVal = 0,maxVal = 3)
                          
                                    
     
#thisExp.addLoop(trials)  # add the loop to the experiment
#thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
#if thisTrial != None:
#    for paramName in thisTrial.keys():
#        exec(paramName + '= thisTrial.' + paramName)

for thisStep in staircase:

    CurrentLoadStr = ('%02d'%((int(thisStep*10))))
    CurrentLoadIndex = int(thisStep*2)
    #Extract the word for this trial from the appropriate trial list
    
    CurrentWord = AllTrials[CurrentLoadIndex].trialList[LoadCount[CurrentLoadIndex]]['Word']
    CurrentCorr = AllTrials[CurrentLoadIndex].trialList[LoadCount[CurrentLoadIndex]]['corr']
    LoadCount[CurrentLoadIndex] += 1
    print(LoadCount)
    print("Expected response is: %s"%(CurrentCorr))
    # Check to see if any lists have been exhausted
    if (np.array(NTrials) == LoadCount).any():
        # If any lists are exhausted reset the list
        ind = np.where(np.array(NTrials) == LoadCount)
        LoadCount[ind[0][0]] = 0

#    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
#    if thisTrial != None:
#        for paramName in thisTrial.keys():
#            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.750000)
    # update component parameters for each repeat
    textWord.setText(CurrentWord) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    key_resp_3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    TrialComponents = [textWord, key_resp_3, textTrialEndCross]
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and textWord.status == NOT_STARTED:
            # keep track of start time/frame for later
            textWord.tStart = t
            textWord.frameNStart = frameN  # exact frame index
            textWord.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textWord.status == STARTED and t >= frameRemains:
            textWord.setAutoDraw(False)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 1.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_3.status == STARTED and t >= frameRemains:
            key_resp_3.status = STOPPED
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'down', '1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                print("Actual response is: %s"%(key_resp_3.keys))
                print("---------")
                # was this 'correct'?
                
                if (key_resp_3.keys == str(CurrentCorr)) or (key_resp_3.keys == CurrentCorr):
                    thisResp = 1 
                    print("Correct")                   
                    key_resp_3.corr = 1
                else:
                    thisResp = -1
                    print("Incorrect")
                    key_resp_3.corr = 0
                staircase.addData(thisResp) 
        # *text_2* updates
        if t >= 1.5 and textTrialEndCross.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTrialEndCross.tStart = t
            textTrialEndCross.frameNStart = frameN  # exact frame index
            textTrialEndCross.setAutoDraw(True)
        frameRemains = 1.5 + 0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTrialEndCross.status == STARTED and t >= frameRemains:
            textTrialEndCross.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys=None
        # was no response the correct answer?!
        if str(CurrentCorr).lower() == 'none':
           key_resp_3.corr = 1  # correct non-response
        else:
           key_resp_3.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
#    trials.addData('key_resp_3.keys',key_resp_3.keys)
#    trials.addData('key_resp_3.corr', key_resp_3.corr)
#    if key_resp_3.keys != None:  # we had a response
#        trials.addData('key_resp_3.rt', key_resp_3.rt)
    
    # ------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [ITICrossHair]
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITICrossHair* updates
        if t >= 0.0 and ITICrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            ITICrossHair.tStart = t
            ITICrossHair.frameNStart = frameN  # exact frame index
            ITICrossHair.setAutoDraw(True)
        frameRemains = 0.0 + ITI-0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ITICrossHair.status == STARTED and t >= frameRemains:
            ITICrossHair.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

    
            
# completed 1 repeats of 'trials'

# get names of stimulus parameters
#if trials.trialList in ([], [None], None):
#    params = []
#else:
#    params = trials.trialList[0].keys()
# save data for this loop
#trials.saveAsText(filename + 'trials.csv', delim=',',
#    stimOut=params,
#    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "WhiteCrossHair"-------
t = 0
WhiteCrossHairClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
WhiteCrossHairComponents = [WhiteCrossHair1]
for thisComponent in WhiteCrossHairComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WhiteCrossHair"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WhiteCrossHairClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WhiteCrossHair1* updates
    if t >= 0.0 and WhiteCrossHair1.status == NOT_STARTED:
        # keep track of start time/frame for later
        WhiteCrossHair1.tStart = t
        WhiteCrossHair1.frameNStart = frameN  # exact frame index
        WhiteCrossHair1.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if WhiteCrossHair1.status == STARTED and t >= frameRemains:
        WhiteCrossHair1.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WhiteCrossHairComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WhiteCrossHair"-------
for thisComponent in WhiteCrossHairComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ThankYou"-------
t = 0
ThankYouClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThankYouComponents = [textThankYou]
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ThankYou"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThankYouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textThankYou* updates
    if t >= 0.0 and textThankYou.status == NOT_STARTED:
        # keep track of start time/frame for later
        textThankYou.tStart = t
        textThankYou.frameNStart = frameN  # exact frame index
        textThankYou.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textThankYou.status == STARTED and t >= frameRemains:
        textThankYou.setAutoDraw(False)
    
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
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
