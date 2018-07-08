#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Thu Jul 27 10:26:08 2017
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
expName = 'DMSDemo1'  # from the Builder filename that created this script
expInfo = {u'session': u'2', u'Participant ID': u''}
PartDataFolder = 'unorganized'
if len(sys.argv) > 1:
    expInfo['Participant ID'] = sys.argv[1]
    PartDataFolder = sys.argv[1]
    FontSize= int(sys.argv[2])
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    FontSize = 60
    if dlg.OK == False:
        core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp

ProbeColor = 'blue'

SpacingOfLettersRelativeToCenter = 80

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s_%s' % (expName, expInfo['Participant ID'], expInfo['date'])
OutDir = '..' + os.sep + '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
filename = OutDir + '%s_%s_%s' % (expName, expInfo['Participant ID'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/jasonsteffener/Dropbox/NeuralCognitiveMapping/DMSPsychopyFiles/DMSDemo.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "practInstruct1"
practInstruct1Clock = core.Clock()
textInstr1 = visual.TextStim(win=win, name='textInstr1',
    text='In this experiment you will be presented with a set of letters. A set may contain anywhere from 1 to 9 letters for you to memorize.\n\nFollowing a short delay you will then be presented with a single letter and you will have to decide whether this new letter was a member of the set.\n\nWhen you are ready to proceed press any key.',
    font='Times New Roman',
    units='pix', pos=[0, 0], height=FontSize, wrapWidth=2, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "practInstruct2"
practInstruct2Clock = core.Clock()
textInstr2 = visual.TextStim(win=win, name='textInstr2',
    #text='Respond with the keys;\n[LEFT] if the letter WAS in the set\n[DOWN] if the letter was NOT in the set\n\nThere will be a number of practice trials in which you will be given feedback.  Try to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    text='Press [LEFT] if the letter WAS in the set.\nPress [DOWN] if the letter WAS NOT in the set.\n\nTry to respond as quickly and as accurately as possible.',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=FontSize, wrapWidth=1200, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "countdown"
countdownClock = core.Clock()
text3 = visual.TextStim(win=win, name='text3',
    text='3',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text2 = visual.TextStim(win=win, name='text2',
    text='2',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text1 = visual.TextStim(win=win, name='text1',
    text='1',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
textITI = visual.TextStim(win=win, name='textITI',
    text='+',
    font='Times New Roman',
    units='pix', pos=[0, 0], height=FontSize, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=0.0);
textTL = visual.TextStim(win=win, name='textTL',
    text='default text',
    font='Times New Roman',
    units='pix', pos=[-SpacingOfLettersRelativeToCenter, SpacingOfLettersRelativeToCenter], height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
textTM = visual.TextStim(win=win, name='textTM',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
textTR = visual.TextStim(win=win, name='textTR',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(SpacingOfLettersRelativeToCenter, SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
textCL = visual.TextStim(win=win, name='textCL',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(-SpacingOfLettersRelativeToCenter, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
textCM = visual.TextStim(win=win, name='textCM',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
textCR = visual.TextStim(win=win, name='textCR',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(SpacingOfLettersRelativeToCenter, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
textBL = visual.TextStim(win=win, name='textBL',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(-SpacingOfLettersRelativeToCenter, -SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
textBM = visual.TextStim(win=win, name='textBM',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, -SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
textBR = visual.TextStim(win=win, name='textBR',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(SpacingOfLettersRelativeToCenter, -SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
textDelay = visual.TextStim(win=win, name='textDelay',
    text='+',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1,
    depth=-10.0);
textProbe = visual.TextStim(win=win, name='textProbe',
    text='default text',
    font='Times New Roman',
    units='pix', pos=[0, 0], height=FontSize, wrapWidth=None, ori=0, 
    color=ProbeColor, colorSpace='rgb', opacity=1,
    depth=-11.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
textFeedback = visual.TextStim(win=win, name='textFeedback',
    text='default text',
    font='Times New Roman',
    units='pix', pos=[0, 0], height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "mainInstruct"
mainInstructClock = core.Clock()
textInstr3 = visual.TextStim(win=win, name='textInstr3',
    text='OK, ready to start the main experiment?\n\nRemember:\nPress [LEFT] for IN the set\nPress [DOWN] for NOT in the set\n\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font='Times New Roman',
    units='pix', pos=[0, 0], height=FontSize, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "practInstruct1"-------
t = 0
practInstruct1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK1 = event.BuilderKeyResponse()
# keep track of which components have finished
#practInstruct1Components = [textInstr1, OK1]
#for thisComponent in practInstruct1Components:
#    if hasattr(thisComponent, 'status'):
#        thisComponent.status = NOT_STARTED
#
# -------Start Routine "practInstruct1"-------
#while continueRoutine:
#    # get current time
#    t = practInstruct1Clock.getTime()
#    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#    # update/draw components on each frame
#    
#    # *textInstr1* updates
#    if t >= 0.0 and textInstr1.status == NOT_STARTED:
#        # keep track of start time/frame for later
#        textInstr1.tStart = t
#        textInstr1.frameNStart = frameN  # exact frame index
#        textInstr1.setAutoDraw(True)
#    
#    # *OK1* updates
#    if t >= 0.0 and OK1.status == NOT_STARTED:
#        # keep track of start time/frame for later
#        OK1.tStart = t
#        OK1.frameNStart = frameN  # exact frame index
#        OK1.status = STARTED
#        # keyboard checking is just starting
#        event.clearEvents(eventType='keyboard')
#    if OK1.status == STARTED:
#        theseKeys = event.getKeys()
#        
#        # check for quit:
#        if "escape" in theseKeys:
#            endExpNow = True
#        if len(theseKeys) > 0:  # at least one key was pressed
#            # a response ends the routine
#            continueRoutine = False
#    
#    # check if all components have finished
#    if not continueRoutine:  # a component has requested a forced-end of Routine
#        break
#    continueRoutine = False  # will revert to True if at least one component still running
#    for thisComponent in practInstruct1Components:
#        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#            continueRoutine = True
#            break  # at least one component has not yet finished
#    
#    # check for quit (the Esc key)
#    if endExpNow or event.getKeys(keyList=["escape"]):
#        core.quit()
#    
#    # refresh the screen
#    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#        win.flip()
#
# -------Ending Routine "practInstruct1"-------
#for thisComponent in practInstruct1Components:
#    if hasattr(thisComponent, "setAutoDraw"):
#        thisComponent.setAutoDraw(False)
# the Routine "practInstruct1" was not non-slip safe, so reset the non-slip timer
#routineTimer.reset()

# ------Prepare to start Routine "practInstruct2"-------
t = 0
practInstruct2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK2 = event.BuilderKeyResponse()
# keep track of which components have finished
practInstruct2Components = [textInstr2, OK2]
for thisComponent in practInstruct2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practInstruct2"-------
while continueRoutine:
    # get current time
    t = practInstruct2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInstr2* updates
    if t >= 0.0 and textInstr2.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInstr2.tStart = t
        textInstr2.frameNStart = frameN  # exact frame index
        textInstr2.setAutoDraw(True)
    
    # *OK2* updates
    if t >= 0.0 and OK2.status == NOT_STARTED:
        # keep track of start time/frame for later
        OK2.tStart = t
        OK2.frameNStart = frameN  # exact frame index
        OK2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if OK2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practInstruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practInstruct2"-------
for thisComponent in practInstruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practInstruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "countdown"-------
t = 0
countdownClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
countdownComponents = [text3, text2, text1]
for thisComponent in countdownComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "countdown"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = countdownClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text3* updates
    if t >= 0.0 and text3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text3.tStart = t
        text3.frameNStart = frameN  # exact frame index
        text3.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text3.status == STARTED and t >= frameRemains:
        text3.setAutoDraw(False)
    
    # *text2* updates
    if t >= 1.0 and text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2.tStart = t
        text2.frameNStart = frameN  # exact frame index
        text2.setAutoDraw(True)
    frameRemains = 1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text2.status == STARTED and t >= frameRemains:
        text2.setAutoDraw(False)
    
    # *text1* updates
    if t >= 2.0 and text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1.tStart = t
        text1.frameNStart = frameN  # exact frame index
        text1.setAutoDraw(True)
    frameRemains = 2.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text1.status == STARTED and t >= frameRemains:
        text1.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "countdown"-------
for thisComponent in countdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
pracTrials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('DMSFileDemo.xlsx'),
    seed=None, name='pracTrials')
thisExp.addLoop(pracTrials)  # add the loop to the experiment
thisPracTrial = pracTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
if thisPracTrial != None:
    for paramName in thisPracTrial.keys():
        exec(paramName + '= thisPracTrial.' + paramName)

for thisPracTrial in pracTrials:
    currentLoop = pracTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
    if thisPracTrial != None:
        for paramName in thisPracTrial.keys():
            exec(paramName + '= thisPracTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    textTL.setText(TL)
    textTM.setText(TM)
    textTR.setText(TR)
    textCL.setText(CL)
    textCM.setText(CM)
    textCR.setText(CR)
    textBL.setText(BL)
    textBM.setText(BM)
    textBR.setText(BR)
    textProbe.setText(probe)
    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [textITI, textTL, textTM, textTR, textCL, textCM, textCR, textBL, textBM, textBR, textDelay, textProbe, resp]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textITI* updates
        if t >= 0.0 and textITI.status == NOT_STARTED:
            # keep track of start time/frame for later
            textITI.tStart = t
            textITI.frameNStart = frameN  # exact frame index
            textITI.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textITI.status == STARTED and t >= frameRemains:
            textITI.setAutoDraw(False)
        
        # *textTL* updates
        if t >= 0.5 and textTL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTL.tStart = t
            textTL.frameNStart = frameN  # exact frame index
            textTL.setAutoDraw(True)
        frameRemains = 0.5 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTL.status == STARTED and t >= frameRemains:
            textTL.setAutoDraw(False)
        
        # *textTM* updates
        if t >= 0.5 and textTM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTM.tStart = t
            textTM.frameNStart = frameN  # exact frame index
            textTM.setAutoDraw(True)
        frameRemains = 0.5 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTM.status == STARTED and t >= frameRemains:
            textTM.setAutoDraw(False)
        
        # *textTR* updates
        if t >= 0.5 and textTR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTR.tStart = t
            textTR.frameNStart = frameN  # exact frame index
            textTR.setAutoDraw(True)
        frameRemains = 0.5 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTR.status == STARTED and t >= frameRemains:
            textTR.setAutoDraw(False)
        
        # *textCL* updates
        if t >= 0.5 and textCL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCL.tStart = t
            textCL.frameNStart = frameN  # exact frame index
            textCL.setAutoDraw(True)
        frameRemains = 0.5 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCL.status == STARTED and t >= frameRemains:
            textCL.setAutoDraw(False)
        
        # *textCM* updates
        if t >= 0.5 and textCM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCM.tStart = t
            textCM.frameNStart = frameN  # exact frame index
            textCM.setAutoDraw(True)
        frameRemains = 0.5 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCM.status == STARTED and t >= frameRemains:
            textCM.setAutoDraw(False)
        
        # *textCR* updates
        if t >= 0.5 and textCR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCR.tStart = t
            textCR.frameNStart = frameN  # exact frame index
            textCR.setAutoDraw(True)
        frameRemains = 0.5 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCR.status == STARTED and t >= frameRemains:
            textCR.setAutoDraw(False)
        
        # *textBL* updates
        if t >= 0.5 and textBL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBL.tStart = t
            textBL.frameNStart = frameN  # exact frame index
            textBL.setAutoDraw(True)
        frameRemains = 0.5 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBL.status == STARTED and t >= frameRemains:
            textBL.setAutoDraw(False)
        
        # *textBM* updates
        if t >= 0.5 and textBM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBM.tStart = t
            textBM.frameNStart = frameN  # exact frame index
            textBM.setAutoDraw(True)
        frameRemains = 0.5 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBM.status == STARTED and t >= frameRemains:
            textBM.setAutoDraw(False)
        
        # *textBR* updates
        if t >= 0.5 and textBR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBR.tStart = t
            textBR.frameNStart = frameN  # exact frame index
            textBR.setAutoDraw(True)
        frameRemains = 0.5 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBR.status == STARTED and t >= frameRemains:
            textBR.setAutoDraw(False)
        
        # *textDelay* updates
        if t >= 2.5 and textDelay.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDelay.tStart = t
            textDelay.frameNStart = frameN  # exact frame index
            textDelay.setAutoDraw(True)
        frameRemains = 2.5 + 2.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textDelay.status == STARTED and t >= frameRemains:
            textDelay.setAutoDraw(False)
        
        # *textProbe* updates
        if t >= 5.0 and textProbe.status == NOT_STARTED:
            # keep track of start time/frame for later
            textProbe.tStart = t
            textProbe.frameNStart = frameN  # exact frame index
            textProbe.setAutoDraw(True)
        
        # *resp* updates
        if t >= 5.0 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'down'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(corr)) or (resp.keys == corr):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys=None
        # was no response the correct answer?!
        if str(corr).lower() == 'none':
           resp.corr = 1  # correct non-response
        else:
           resp.corr = 0  # failed to respond (incorrectly)
    # store data for pracTrials (TrialHandler)
    pracTrials.addData('resp.keys',resp.keys)
    pracTrials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        pracTrials.addData('resp.rt', resp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if resp.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp.rt)
    else:
      msg="Oops! That was wrong"
    textFeedback.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [textFeedback]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *textFeedback* updates
        if t >= 0.0 and textFeedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            textFeedback.tStart = t
            textFeedback.frameNStart = frameN  # exact frame index
            textFeedback.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textFeedback.status == STARTED and t >= frameRemains:
            textFeedback.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'pracTrials'

# get names of stimulus parameters
if pracTrials.trialList in ([], [None], None):
    params = []
else:
    params = pracTrials.trialList[0].keys()
# save data for this loop
pracTrials.saveAsExcel(filename + '.xlsx', sheetName='pracTrials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "mainInstruct"-------
#t = 0
#mainInstructClock.reset()  # clock
#frameN = -1
#continueRoutine = True
# update component parameters for each repeat
#OK3 = event.BuilderKeyResponse()
# keep track of which components have finished
#mainInstructComponents = [textInstr3, OK3]
#for thisComponent in mainInstructComponents:
#    if hasattr(thisComponent, 'status'):
#        thisComponent.status = NOT_STARTED
#
# -------Start Routine "mainInstruct"-------
#while continueRoutine:
#    # get current time
#    t = mainInstructClock.getTime()
#    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#    # update/draw components on each frame
#    
#    # *textInstr3* updates
#    if t >= 0.0 and textInstr3.status == NOT_STARTED:
#        # keep track of start time/frame for later
#        textInstr3.tStart = t
#        textInstr3.frameNStart = frameN  # exact frame index
#        textInstr3.setAutoDraw(True)
#    
#    # *OK3* updates
#    if t >= 0.0 and OK3.status == NOT_STARTED:
#        # keep track of start time/frame for later
#        OK3.tStart = t
#        OK3.frameNStart = frameN  # exact frame index
#        OK3.status = STARTED
#        # keyboard checking is just starting
#        event.clearEvents(eventType='keyboard')
#    if OK3.status == STARTED:
#        theseKeys = event.getKeys()
#        
#        # check for quit:
#        if "escape" in theseKeys:
#            endExpNow = True
#        if len(theseKeys) > 0:  # at least one key was pressed
#            # a response ends the routine
#            continueRoutine = False
#    
#    # check if all components have finished
#    if not continueRoutine:  # a component has requested a forced-end of Routine
#        break
#    continueRoutine = False  # will revert to True if at least one component still running
#    for thisComponent in mainInstructComponents:
#        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#            continueRoutine = True
#            break  # at least one component has not yet finished
#    
#    # check for quit (the Esc key)
#    if endExpNow or event.getKeys(keyList=["escape"]):
#        core.quit()
#    
#    # refresh the screen
#    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#        win.flip()
#
# -------Ending Routine "mainInstruct"-------
#for thisComponent in mainInstructComponents:
#    if hasattr(thisComponent, "setAutoDraw"):
#        thisComponent.setAutoDraw(False)
# the Routine "mainInstruct" was not non-slip safe, so reset the non-slip timer
#routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
