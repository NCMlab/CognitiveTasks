#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Tue Apr  9 12:10:45 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))#.decode(sys.getfilesystemencoding())
os.chdir(_thisDir)
# #################
# Store info about the experiment session
expName = u'Vocab'  # from the Builder filename that created this script
task = 'Antonyms'
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
BGColor = 'grey'
FontColor = 'white'
FontSize = 60
# #################
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1000, 800], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=BGColor, colorSpace='rgb',
    blendMode='avg', useFBO=True, units='height')

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "LongInstr"
LongInstrClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Antonyms Vocabulary\n\nEach item in this test consists of a word in capital letters followed by four words. Select the word that is most nearly the OPPOSITE in meaning as the word in capital letters.\n\nSince some of the items require you to distinguish fine shades of meaning, consider all the choices before deciding which is the best. Please guess if you are unsure since there is no penalty for incorrect responses.\n\nPress any key to begin.',
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=1000, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "GetReady"
GetReadyClock = core.Clock()
GetRead = visual.TextStim(win=win, name='GetRead',
    text='Get Ready',
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',units='pix', 
    width=(500, 150)[0], height=(500, 150)[1],
    ori=0, pos=(0, 200),
    lineWidth=3, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
TestWord = visual.TextStim(win=win, name='TestWord',
    text='default text',
    font=u'Arial',
    units='pix', pos=(0, 200), height=60, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=-1.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
RespBoxWidth = 375
RespBoxHeight = 100
RespBoxX1 = -200
RespBoxY1 = -50
RespBoxX2 = 200
RespBoxY2 = -160

Resp1Box = visual.Rect(
    win=win, name='Resp1Box',
    width=(RespBoxWidth, RespBoxHeight)[0], height=(RespBoxWidth, RespBoxHeight)[1],
    ori=0, pos=(RespBoxX1, RespBoxY1),
    lineWidth=3, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',units='pix',
    opacity=1, depth=-4.0, interpolate=True)
Resp2Box = visual.Rect(
    win=win, name='Resp2Box',
    width=(RespBoxWidth, RespBoxHeight)[0], height=(RespBoxWidth, RespBoxHeight)[1],
    ori=0, pos=(RespBoxX2, RespBoxY1),
    lineWidth=3, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',units='pix',
    opacity=1, depth=-5.0, interpolate=True)
Resp3Box = visual.Rect(
    win=win, name='Resp3Box',
    width=(RespBoxWidth, RespBoxHeight)[0], height=(RespBoxWidth, RespBoxHeight)[1],
    ori=0, pos=(RespBoxX1, RespBoxY2),
    lineWidth=3, lineColor=[-1,-1,-1], lineColorSpace='rgb',units='pix',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
Resp4Box = visual.Rect(
    win=win, name='Resp4Box',
    width=(RespBoxWidth, RespBoxHeight)[0], height=(RespBoxWidth, RespBoxHeight)[1],
    ori=0, pos=(RespBoxX2, RespBoxY2),
    lineWidth=3, lineColor=[-1,-1,-1], lineColorSpace='rgb',units='pix',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
Resp1 = visual.TextStim(win=win, name='Resp1',
    text='default text',
    font=u'Arial',
    units='pix', pos=(RespBoxX1, RespBoxY1), height=50, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=-8.0);
Resp2 = visual.TextStim(win=win, name='Resp2',
    text='default text',
    font=u'Arial',
    units='pix', pos=(RespBoxX2, RespBoxY1), height=50, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=-9.0);
Resp3 = visual.TextStim(win=win, name='Resp3',
    text='default text',
    font=u'Arial',
    units='pix', pos=(RespBoxX1, RespBoxY2), height=50, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=-10.0);
Resp4 = visual.TextStim(win=win, name='Resp4',
    text='default text',
    font=u'Arial',
    units='pix', pos=(RespBoxX2, RespBoxY2), height=50, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=-11.0);

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
msg = ''
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=600, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    units='pix', pos=(0, 0), height=60, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ShortInstr"
ShortInstrClock = core.Clock()
Instruct = visual.TextStim(win=win, name='Instruct',
    text='Select the word that is most nearly the OPPOSITE in meaning as the word in capital letters.\n\nPress any key to begin.',
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=600, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "GetReady"
GetReadyClock = core.Clock()
GetRead = visual.TextStim(win=win, name='GetRead',
    text='Get Ready',
    font='Arial',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
polygon = visual.Rect(
    win=win, name='polygon',units='pix', 
    width=(500, 150)[0], height=(500, 150)[1],
    ori=0, pos=(0, 200),
    lineWidth=3, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
TestWord = visual.TextStim(win=win, name='TestWord',
    text='default text',
    font=u'Arial',
    units='pix', pos=(0, 200), height=60, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=-1.0);
mouse = event.Mouse(win=win)
x, y = [None, None]


# Initialize components for Routine "ITI"
ITIClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    units='pix', pos=(0, 0), height=60, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
Merci = visual.TextStim(win=win, name='Merci',
    text='Thank you',
    font='Arial',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "LongInstr"-------
t = 0
LongInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
LongInstrComponents = [text, key_resp_3]
for thisComponent in LongInstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "LongInstr"-------
while continueRoutine:
    # get current time
    t = LongInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LongInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LongInstr"-------
for thisComponent in LongInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "LongInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "GetReady"-------
t = 0
GetReadyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
GetReadyComponents = [GetRead]
for thisComponent in GetReadyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "GetReady"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = GetReadyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetRead* updates
    if t >= 0.0 and GetRead.status == NOT_STARTED:
        # keep track of start time/frame for later
        GetRead.tStart = t
        GetRead.frameNStart = frameN  # exact frame index
        GetRead.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if GetRead.status == STARTED and t >= frameRemains:
        GetRead.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GetReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GetReady"-------
for thisComponent in GetReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
Practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'../../CompanionFolderForCognitiveTasks/AntonymsTest - Sheet1.csv', selection=u'[0,1,2,3]'),
    seed=None, name='Practice')
thisExp.addLoop(Practice)  # add the loop to the experiment
thisPractice = Practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in Practice:
    ButtonPressFlag = False
    currentLoop = Practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    TestWord.setText(Word)
    resp = event.BuilderKeyResponse()
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    Resp1.setText(Choice1)
    Resp2.setText(Choice2)
    Resp3.setText(Choice3)
    Resp4.setText(Choice4)
    # keep track of which components have finished
    trialComponents = [polygon, TestWord, resp, mouse, Resp1Box, Resp2Box, Resp3Box, Resp4Box, Resp1, Resp2, Resp3, Resp4]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------

    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        
        # *TestWord* updates
        if t >= 0.0 and TestWord.status == NOT_STARTED:
            # keep track of start time/frame for later
            TestWord.tStart = t
            TestWord.frameNStart = frameN  # exact frame index
            TestWord.setAutoDraw(True)
        
        # *resp* updates
        if t >= 0.0 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # A button press has occured
                ButtonPressFlag = True
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(Corr)) or (resp.keys == Corr):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    for obj in [Resp1,Resp2,Resp3,Resp4]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                            CurrentResponse = obj.name
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *Resp1Box* updates
        if t >= 0.0 and Resp1Box.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp1Box.tStart = t
            Resp1Box.frameNStart = frameN  # exact frame index
            Resp1Box.setAutoDraw(True)
        
        # *Resp2Box* updates
        if t >= 0.0 and Resp2Box.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp2Box.tStart = t
            Resp2Box.frameNStart = frameN  # exact frame index
            Resp2Box.setAutoDraw(True)
        
        # *Resp3Box* updates
        if t >= 0.0 and Resp3Box.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp3Box.tStart = t
            Resp3Box.frameNStart = frameN  # exact frame index
            Resp3Box.setAutoDraw(True)
        
        # *Resp4Box* updates
        if t >= 0.0 and Resp4Box.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp4Box.tStart = t
            Resp4Box.frameNStart = frameN  # exact frame index
            Resp4Box.setAutoDraw(True)
        
        # *Resp1* updates
        if t >= 0.0 and Resp1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp1.tStart = t
            Resp1.frameNStart = frameN  # exact frame index
            Resp1.setAutoDraw(True)
        
        # *Resp2* updates
        if t >= 0.0 and Resp2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp2.tStart = t
            Resp2.frameNStart = frameN  # exact frame index
            Resp2.setAutoDraw(True)
        
        # *Resp3* updates
        if t >= 0.0 and Resp3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp3.tStart = t
            Resp3.frameNStart = frameN  # exact frame index
            Resp3.setAutoDraw(True)
        
        # *Resp4* updates
        if t >= 0.0 and Resp4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp4.tStart = t
            Resp4.frameNStart = frameN  # exact frame index
            Resp4.setAutoDraw(True)
        
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
        if str(Corr).lower() == 'none':
           resp.corr = 1  # correct non-response
        else:
           resp.corr = 0  # failed to respond (incorrectly)

    # store data for Practice (TrialHandler)
    if sum(buttons):
        resp.rt = resp.clock.getTime()
        # check if the mouse was inside our 'clickable' objects
        for obj in [Resp1,Resp2,Resp3,Resp4]:
            if obj.contains(mouse):
                gotValidClick = True
                mouse.clicked_name.append(obj.name)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    mouse.time = trialClock.getTime()
#    Practice.addData('mouse.x', x)
#    Practice.addData('mouse.y', y)
#    Practice.addData('mouse.leftButton', buttons[0])
#    Practice.addData('mouse.midButton', buttons[1])
#    Practice.addData('mouse.rightButton', buttons[2])
    Practice.addData('mouse.RT', mouse.time)
    if len(mouse.clicked_name):
        Practice.addData('mouse.clicked_name', mouse.clicked_name[0])
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    t = 0
    FeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # Check whether the mouse response is correct or not
    # No response has been recorded yet.
    # Then lets assume that a mouse click has been performed

    if not ButtonPressFlag: 
        if (CurrentResponse[-1] == str(Corr)) or (CurrentResponse[-1] == Corr):
            resp.corr = 1
        else:
            resp.corr = 0
    # store data for Practice (TrialHandler)
    Practice.addData('resp.keys',resp.keys)
    Practice.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        Practice.addData('resp.rt', resp.rt)
    
    if resp.corr:#stored on last run routine
      msg="Correct!"
    else:
      msg="Oops! That was wrong"
    text_3.setText(msg)
    # keep track of which components have finished
    FeedbackComponents = [text_3]
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [text_2]
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)
        
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
    thisExp.nextEntry()
    
# completed 1 repeats of 'Practice'


# ------Prepare to start Routine "ShortInstr"-------
t = 0
ShortInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
ShortInstrComponents = [Instruct, key_resp_2]
for thisComponent in ShortInstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ShortInstr"-------
while continueRoutine:
    # get current time
    t = ShortInstrClock.getTime()
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
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # A button press has occured
            ButtonPressFlag = True
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ShortInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ShortInstr"-------
for thisComponent in ShortInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "ShortInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "GetReady"-------
t = 0
GetReadyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
GetReadyComponents = [GetRead]
for thisComponent in GetReadyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "GetReady"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = GetReadyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetRead* updates
    if t >= 0.0 and GetRead.status == NOT_STARTED:
        # keep track of start time/frame for later
        GetRead.tStart = t
        GetRead.frameNStart = frameN  # exact frame index
        GetRead.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if GetRead.status == STARTED and t >= frameRemains:
        GetRead.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GetReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GetReady"-------
for thisComponent in GetReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../../CompanionFolderForCognitiveTasks/AntonymsTest - Sheet1.csv', selection='[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    ButtonPressFlag = False
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    TestWord.setText(Word)
    resp = event.BuilderKeyResponse()
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    Resp1.setText(Choice1)
    Resp2.setText(Choice2)
    Resp3.setText(Choice3)
    Resp4.setText(Choice4)
    # keep track of which components have finished
    trialComponents = [polygon, TestWord, resp, mouse, Resp1Box, Resp2Box, Resp3Box, Resp4Box, Resp1, Resp2, Resp3, Resp4]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        
        # *TestWord* updates
        if t >= 0.0 and TestWord.status == NOT_STARTED:
            # keep track of start time/frame for later
            TestWord.tStart = t
            TestWord.frameNStart = frameN  # exact frame index
            TestWord.setAutoDraw(True)
        
        # *resp* updates
        if t >= 0.0 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(Corr)) or (resp.keys == Corr):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    resp.rt = resp.clock.getTime()
                    # check if the mouse was inside our 'clickable' objects
                    for obj in [Resp1,Resp2,Resp3,Resp4]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *Resp1Box* updates
        if t >= 0.0 and Resp1Box.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp1Box.tStart = t
            Resp1Box.frameNStart = frameN  # exact frame index
            Resp1Box.setAutoDraw(True)
        
        # *Resp2Box* updates
        if t >= 0.0 and Resp2Box.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp2Box.tStart = t
            Resp2Box.frameNStart = frameN  # exact frame index
            Resp2Box.setAutoDraw(True)
        
        # *Resp3Box* updates
        if t >= 0.0 and Resp3Box.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp3Box.tStart = t
            Resp3Box.frameNStart = frameN  # exact frame index
            Resp3Box.setAutoDraw(True)
        
        # *Resp4Box* updates
        if t >= 0.0 and Resp4Box.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp4Box.tStart = t
            Resp4Box.frameNStart = frameN  # exact frame index
            Resp4Box.setAutoDraw(True)
        
        # *Resp1* updates
        if t >= 0.0 and Resp1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp1.tStart = t
            Resp1.frameNStart = frameN  # exact frame index
            Resp1.setAutoDraw(True)
        
        # *Resp2* updates
        if t >= 0.0 and Resp2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp2.tStart = t
            Resp2.frameNStart = frameN  # exact frame index
            Resp2.setAutoDraw(True)
        
        # *Resp3* updates
        if t >= 0.0 and Resp3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp3.tStart = t
            Resp3.frameNStart = frameN  # exact frame index
            Resp3.setAutoDraw(True)
        
        # *Resp4* updates
        if t >= 0.0 and Resp4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp4.tStart = t
            Resp4.frameNStart = frameN  # exact frame index
            Resp4.setAutoDraw(True)
        
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
#    # check responses
#    if resp.keys in ['', [], None]:  # No response was made
#        resp.keys=None
#        # was no response the correct answer?!
#        if str(Corr).lower() == 'none':
#           resp.corr = 1  # correct non-response
#        else:
#           resp.corr = 0  # failed to respond (incorrectly)



    # store data for trials (TrialHandler)
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        for obj in [Resp1,Resp2,Resp3,Resp4]:
            if obj.contains(mouse):
                gotValidClick = True
                mouse.clicked_name.append(obj.name)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    mouse.time = trialClock.getTime()
#    trials.addData('mouse.x', x)
#    trials.addData('mouse.y', y)
#    trials.addData('mouse.leftButton', buttons[0])
#    trials.addData('mouse.midButton', buttons[1])
#    trials.addData('mouse.rightButton', buttons[2])
    trials.addData('mouse.RT', mouse.time)
    if len(mouse.clicked_name):
        trials.addData('mouse.clicked_name', mouse.clicked_name[0])
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # If no keyboard response has been made, check the mouse for correct responses
    if not ButtonPressFlag: 
        if (CurrentResponse[-1] == str(Corr)) or (CurrentResponse[-1] == Corr):
            resp.corr = 1
        else:
            resp.corr = 0
            
  
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    
    
    # ------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [text_2]
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)
        
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
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "ThankYou"-------
t = 0
ThankYouClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThankYouComponents = [Merci]
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ThankYou"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThankYouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Merci* updates
    if t >= 0.0 and Merci.status == NOT_STARTED:
        # keep track of start time/frame for later
        Merci.tStart = t
        Merci.frameNStart = frameN  # exact frame index
        Merci.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Merci.status == STARTED and t >= frameRemains:
        Merci.setAutoDraw(False)
    
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
#thisExp.saveAsPickle(filename)
#logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
