#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Tue Nov  6 14:17:34 2018
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
# #################
# Store info about the experiment session
expName = u'Matrices'  # from the Builder filename that created this script
task = 'Practice'
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
 

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = os.path.join(PartDataFolder, '%s_%s_%s_%s_%s' % (expInfo['Participant ID'],expName, task, Tag, expInfo['date']))
BGColor = 'grey'
FontColor = 'white'
FontSize = 60

# #################
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/jasonsteffener/Documents/GitHub/CognitiveTasks/Matrices/MatricesPractice.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instruct = visual.TextStim(win=win, name='Instruct',
    text='Progressive Matrices\n\nThis is a test of observation and clear thinking.\nAt the top of the screen you will see a pattern with a bit cut out of it. You will look at the pattern, think what the piece must be that is needed to complete the pattern correctly both along and down. Then find the right piece out of the eight bits shown below.\nOnly one of these pieces is perfectly correct.\n\nPress any key to perform practice trials.',
    font='Arial',
    pos=(0, 0), height=40, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 200), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
CFig1 = visual.ImageStim(
    win=win, name='CFig1',
    image='sin', mask=None,
    ori=0, pos=(-225, -75), size=(120, 120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
CFig2 = visual.ImageStim(
    win=win, name='CFig2',
    image='sin', mask=None,
    ori=0, pos=(-75, -75), size=(120, 120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
CFig3 = visual.ImageStim(
    win=win, name='CFig3',
    image='sin', mask=None,
    ori=0, pos=(75, -75), size=(120, 120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
CFig4 = visual.ImageStim(
    win=win, name='CFig4',
    image='sin', mask=None,
    ori=0, pos=(225, -75), size=(120, 120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
CFig5 = visual.ImageStim(
    win=win, name='CFig5',
    image='sin', mask=None,
    ori=0, pos=(-225, -225), size=(120,120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
CFIg6 = visual.ImageStim(
    win=win, name='CFIg6',
    image='sin', mask=None,
    ori=0, pos=(-75, -225), size=(120, 120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
Opt1 = visual.TextStim(win=win, name='Opt1',
    text='1',
    font='Arial',
    pos=(-170, -30), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-7.0);
Opt2 = visual.TextStim(win=win, name='Opt2',
    text=u'2',
    font=u'Arial',
    pos=(-20, -30), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-8.0);
Opt3 = visual.TextStim(win=win, name='Opt3',
    text=u'3',
    font=u'Arial',
    pos=(130, -30), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-9.0);
Opt4 = visual.TextStim(win=win, name='Opt4',
    text='4',
    font='Arial',
    pos=(280, -30), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-10.0);
Opt5 = visual.TextStim(win=win, name='Opt5',
    text='5',
    font='Arial',
    pos=(-170, -180), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-11.0);
CFig7 = visual.ImageStim(
    win=win, name='CFig7',
    image='sin', mask=None,
    ori=0, pos=(75, -225), size=(120, 120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
CFig8 = visual.ImageStim(
    win=win, name='CFig8',
    image='sin', mask=None,
    ori=0, pos=(225, -225), size=(120, 120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
Opt6 = visual.TextStim(win=win, name='Opt6',
    text='6',
    font='Arial',
    pos=(-20, -180), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-15.0);
Opt7 = visual.TextStim(win=win, name='Opt7',
    text='7',
    font='Arial',
    pos=(130, -180), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-16.0);
Opt8 = visual.TextStim(win=win, name='Opt8',
    text='8',
    font='Arial',
    pos=(280, -180), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-17.0);

# Initialize components for Routine "Feedback1"
Feedback1Clock = core.Clock()
Prac1Feedback = visual.TextStim(win=win, name='Prac1Feedback',
    text='default text',
    font=u'Arial',
    pos=(-350, -160), height=30, wrapWidth=660, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
Prac1Matrix = visual.ImageStim(
    win=win, name='Prac1Matrix',
    image='sin', mask=None,
    ori=0, pos=(0, 200), size=(430, 380),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Prac1Choice = visual.ImageStim(
    win=win, name='Prac1Choice',
    image='sin', mask=None,
    ori=0, pos=(75, -75), size=(120,120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
CorrectAnswer = visual.TextStim(win=win, name='CorrectAnswer',
    text='default text',
    font=u'Arial',
    pos=(130, -30), height=40, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "crosshair"
crosshairClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Thank You',
    font='Arial',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
StartPractice = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [Instruct, StartPractice]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruct* updates
    if t >= 0.0 and Instruct.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instruct.tStart = t
        Instruct.frameNStart = frameN  # exact frame index
        Instruct.setAutoDraw(True)
    
    # *StartPractice* updates
    if t >= 0.0 and StartPractice.status == NOT_STARTED:
        # keep track of start time/frame for later
        StartPractice.tStart = t
        StartPractice.frameNStart = frameN  # exact frame index
        StartPractice.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(StartPractice.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if StartPractice.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            StartPractice.keys = theseKeys[-1]  # just the last key pressed
            StartPractice.rt = StartPractice.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if StartPractice.keys in ['', [], None]:  # No response was made
    StartPractice.keys=None
thisExp.addData('StartPractice.keys',StartPractice.keys)
if StartPractice.keys != None:  # we had a response
    thisExp.addData('StartPractice.rt', StartPractice.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'MatricesPractice.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(Stimulus)
    image.setSize((430,380))
    CFig1.setImage(Choice1)
    CFig2.setImage(Choice2)
    CFig3.setImage(Choice3)
    CFig4.setImage(Choice4)
    CFIg6.setImage(Choice6)
    key_resp_2 = event.BuilderKeyResponse()
    CFig7.setImage(Choice7)
    CFig8.setImage(Choice8)
    # keep track of which components have finished
    trialComponents = [image, CFig1, CFig2, CFig3, CFig4, CFig5, CFIg6, Opt1, Opt2, Opt3, Opt4, Opt5, key_resp_2, CFig7, CFig8, Opt6, Opt7, Opt8]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *CFig1* updates
        if t >= 0.0 and CFig1.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig1.tStart = t
            CFig1.frameNStart = frameN  # exact frame index
            CFig1.setAutoDraw(True)
        
        # *CFig2* updates
        if t >= 0.0 and CFig2.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig2.tStart = t
            CFig2.frameNStart = frameN  # exact frame index
            CFig2.setAutoDraw(True)
        
        # *CFig3* updates
        if t >= 0.0 and CFig3.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig3.tStart = t
            CFig3.frameNStart = frameN  # exact frame index
            CFig3.setAutoDraw(True)
        
        # *CFig4* updates
        if t >= 0.0 and CFig4.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig4.tStart = t
            CFig4.frameNStart = frameN  # exact frame index
            CFig4.setAutoDraw(True)
        
        # *CFig5* updates
        if t >= 0.0 and CFig5.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig5.tStart = t
            CFig5.frameNStart = frameN  # exact frame index
            CFig5.setAutoDraw(True)
        if CFig5.status == STARTED:  # only update if drawing
            CFig5.setImage(Choice5, log=False)
        
        # *CFIg6* updates
        if t >= 0.0 and CFIg6.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFIg6.tStart = t
            CFIg6.frameNStart = frameN  # exact frame index
            CFIg6.setAutoDraw(True)
        
        # *Opt1* updates
        if t >= 0.0 and Opt1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt1.tStart = t
            Opt1.frameNStart = frameN  # exact frame index
            Opt1.setAutoDraw(True)
        
        # *Opt2* updates
        if t >= 0.0 and Opt2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt2.tStart = t
            Opt2.frameNStart = frameN  # exact frame index
            Opt2.setAutoDraw(True)
        
        # *Opt3* updates
        if t >= 0.0 and Opt3.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt3.tStart = t
            Opt3.frameNStart = frameN  # exact frame index
            Opt3.setAutoDraw(True)
        
        # *Opt4* updates
        if t >= 0.0 and Opt4.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt4.tStart = t
            Opt4.frameNStart = frameN  # exact frame index
            Opt4.setAutoDraw(True)
        
        # *Opt5* updates
        if t >= 0.0 and Opt5.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt5.tStart = t
            Opt5.frameNStart = frameN  # exact frame index
            Opt5.setAutoDraw(True)
        
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
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # was this 'correct'?
                if (key_resp_2.keys == str(Corr)) or (key_resp_2.keys == Corr):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *CFig7* updates
        if t >= 0.0 and CFig7.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig7.tStart = t
            CFig7.frameNStart = frameN  # exact frame index
            CFig7.setAutoDraw(True)
        
        # *CFig8* updates
        if t >= 0.0 and CFig8.status == NOT_STARTED:
            # keep track of start time/frame for later
            CFig8.tStart = t
            CFig8.frameNStart = frameN  # exact frame index
            CFig8.setAutoDraw(True)
        
        # *Opt6* updates
        if t >= 0.0 and Opt6.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt6.tStart = t
            Opt6.frameNStart = frameN  # exact frame index
            Opt6.setAutoDraw(True)
        
        # *Opt7* updates
        if t >= 0.0 and Opt7.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt7.tStart = t
            Opt7.frameNStart = frameN  # exact frame index
            Opt7.setAutoDraw(True)
        
        # *Opt8* updates
        if t >= 0.0 and Opt8.status == NOT_STARTED:
            # keep track of start time/frame for later
            Opt8.tStart = t
            Opt8.frameNStart = frameN  # exact frame index
            Opt8.setAutoDraw(True)
        
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
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
        # was no response the correct answer?!
        if str(Corr).lower() == 'none':
           key_resp_2.corr = 1  # correct non-response
        else:
           key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback1"-------
    t = 0
    Feedback1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Prac1Feedback.setText(Feedback)
    Prac1Matrix.setImage(Stimulus)
    Prac1Choice.setImage(CorrectImage)
    Prac1End = event.BuilderKeyResponse()
    CorrectAnswer.setText(Corr)
    # keep track of which components have finished
    Feedback1Components = [Prac1Feedback, Prac1Matrix, Prac1Choice, Prac1End, CorrectAnswer]
    for thisComponent in Feedback1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback1"-------
    while continueRoutine:
        # get current time
        t = Feedback1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Prac1Feedback* updates
        if t >= 0.0 and Prac1Feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac1Feedback.tStart = t
            Prac1Feedback.frameNStart = frameN  # exact frame index
            Prac1Feedback.setAutoDraw(True)
        
        # *Prac1Matrix* updates
        if t >= 0.0 and Prac1Matrix.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac1Matrix.tStart = t
            Prac1Matrix.frameNStart = frameN  # exact frame index
            Prac1Matrix.setAutoDraw(True)
        
        # *Prac1Choice* updates
        if t >= 0.0 and Prac1Choice.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac1Choice.tStart = t
            Prac1Choice.frameNStart = frameN  # exact frame index
            Prac1Choice.setAutoDraw(True)
        
        # *Prac1End* updates
        if t >= 0.0 and Prac1End.status == NOT_STARTED:
            # keep track of start time/frame for later
            Prac1End.tStart = t
            Prac1End.frameNStart = frameN  # exact frame index
            Prac1End.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Prac1End.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if Prac1End.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Prac1End.keys = theseKeys[-1]  # just the last key pressed
                Prac1End.rt = Prac1End.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *CorrectAnswer* updates
        if t >= 0.0 and CorrectAnswer.status == NOT_STARTED:
            # keep track of start time/frame for later
            CorrectAnswer.tStart = t
            CorrectAnswer.frameNStart = frameN  # exact frame index
            CorrectAnswer.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback1"-------
    for thisComponent in Feedback1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Prac1End.keys in ['', [], None]:  # No response was made
        Prac1End.keys=None
    trials.addData('Prac1End.keys',Prac1End.keys)
    if Prac1End.keys != None:  # we had a response
        trials.addData('Prac1End.rt', Prac1End.rt)
    # the Routine "Feedback1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "crosshair"-------
    t = 0
    crosshairClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    crosshairComponents = [text]
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "crosshair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = crosshairClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crosshairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "crosshair"-------
    for thisComponent in crosshairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "ThankYou"-------
t = 0
ThankYouClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThankYouComponents = [text_2]
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ThankYou"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThankYouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
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
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
