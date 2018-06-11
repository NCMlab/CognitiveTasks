#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Mon Jun  4 11:48:18 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging
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
expName = u'Semantics_Block'  # from the Builder filename that created this script
expInfo = {'Participant ID':'', 'Session':'001'}
PartDataFolder = 'unorganized'
if len(sys.argv) > 2:
    #tempFile.write("Entered if clause\n")
    #tempFile.write('%s\n'%(sys.argv[2]))
    expInfo['Participant ID'] = sys.argv[1]
    #tempFile.write('%s\n'%(sys.argv[1]))
    #tempFile.write('%s\n'%(sys.argv[2]))
    PartDataFolder = sys.argv[1]
    CounterBalFlag = sys.argv[2]
    Tag = sys.argv[3]
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    CounterBalFlag = 'False'
    Tag = '2'
    
expInfo['date'] = data.getDateStr()  # add a simple timestamp
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
OutDir = '..' + os.sep + '..' + os.sep + '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
filename = OutDir + '%s%s_%s_%s' % (expName, Tag, expInfo['Participant ID'], expInfo['date'])
print(filename)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
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
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
if CounterBalFlag == 'False':
    Instructions = visual.TextStim(win=win, name='Instructions',
    text='Press [left] if the word is of a living thing.\nPress [down] if the word is of a non-living thing.\n\nPress [5] to start.',
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);
else:
    Instructions = visual.TextStim(win=win, name='Instructions',
    text='Press [down] if the word is of a living thing.\nPress [left] if the word is of a non-living thing.\n\nPress [5] to start.',
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "WhiteCrosshair"
WhiteCrosshairClock = core.Clock()
WhiteCrossHairStim = visual.TextStim(win=win, name='WhiteCrossHairStim',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "CountDown"
CountDownClock = core.Clock()
Three = visual.TextStim(win=win, name='Three',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
Two = visual.TextStim(win=win, name='Two',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
One = visual.TextStim(win=win, name='One',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "WordStimulus"
WordStimulusClock = core.Clock()
WordStim = visual.TextStim(win=win, name='WordStim',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "RedCrosshair"
RedCrosshairClock = core.Clock()
RedCrossHairStim = visual.TextStim(win=win, name='RedCrossHairStim',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "WhiteCrosshair"
WhiteCrosshairClock = core.Clock()
WhiteCrossHairStim = visual.TextStim(win=win, name='WhiteCrossHairStim',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ExtraTimeWhiteCH"
ExtraTimeWhiteCHClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
ThankYouText = visual.TextStim(win=win, name='ThankYouText',
    text='Thank you',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
IntroClock = core.Clock()
TrialClock = core.Clock()
# ------Prepare to start Routine "Intro"-------
t = 0
IntroClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
StartExperimentResponse = event.BuilderKeyResponse()
# keep track of which components have finished
IntroComponents = [Instructions, StartExperimentResponse]
for thisComponent in IntroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Intro"-------
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if t >= 0.0 and Instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions.tStart = t
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.setAutoDraw(True)
    
    # *StartExperimentResponse* updates
    if t >= 0.0 and StartExperimentResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        StartExperimentResponse.tStart = t
        StartExperimentResponse.frameNStart = frameN  # exact frame index
        StartExperimentResponse.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(StartExperimentResponse.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if StartExperimentResponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            StartExperimentResponse.keys = theseKeys[-1]  # just the last key pressed
            StartExperimentResponse.rt = StartExperimentResponse.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if StartExperimentResponse.keys in ['', [], None]:  # No response was made
    StartExperimentResponse.keys=None
thisExp.addData('StartExperimentResponse.keys',StartExperimentResponse.keys)
if StartExperimentResponse.keys != None:  # we had a response
    thisExp.addData('StartExperimentResponse.rt', StartExperimentResponse.rt)
thisExp.nextEntry()
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WhiteCrosshair"-------
t = 0
TrialClock.reset()
WhiteCrosshairClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(17.000000)
# update component parameters for each repeat
# keep track of which components have finished
WhiteCrosshairComponents = [WhiteCrossHairStim]
for thisComponent in WhiteCrosshairComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WhiteCrosshair"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WhiteCrosshairClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WhiteCrossHairStim* updates
    if t >= 0.0 and WhiteCrossHairStim.status == NOT_STARTED:
        # keep track of start time/frame for later
        WhiteCrossHairStim.tStart = t
        WhiteCrossHairStim.frameNStart = frameN  # exact frame index
        WhiteCrossHairStim.setAutoDraw(True)
    frameRemains = 0.0 + 17- win.monitorFramePeriod * 0.75  # most of one frame period left
    if WhiteCrossHairStim.status == STARTED and t >= frameRemains:
        WhiteCrossHairStim.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WhiteCrosshairComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WhiteCrosshair"-------
for thisComponent in WhiteCrosshairComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
Blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Run1Blocks.csv'),
    seed=None, name='Blocks')
thisExp.addLoop(Blocks)  # add the loop to the experiment
thisBlock = Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in Blocks:
    currentLoop = Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    # ------Prepare to start Routine "CountDown"-------
    t = 0
    CountDownClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CountDownComponents = [Three, Two, One]
    for thisComponent in CountDownComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "CountDown"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CountDownClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Three* updates
        if t >= 0.0 and Three.status == NOT_STARTED:
            # keep track of start time/frame for later
            Three.tStart = t
            Three.frameNStart = frameN  # exact frame index
            Three.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Three.status == STARTED and t >= frameRemains:
            Three.setAutoDraw(False)
        
        # *Two* updates
        if t >= 1 and Two.status == NOT_STARTED:
            # keep track of start time/frame for later
            Two.tStart = t
            Two.frameNStart = frameN  # exact frame index
            Two.setAutoDraw(True)
        frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Two.status == STARTED and t >= frameRemains:
            Two.setAutoDraw(False)
        
        # *One* updates
        if t >= 2 and One.status == NOT_STARTED:
            # keep track of start time/frame for later
            One.tStart = t
            One.frameNStart = frameN  # exact frame index
            One.setAutoDraw(True)
        frameRemains = 2 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if One.status == STARTED and t >= frameRemains:
            One.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CountDownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CountDown"-------
    for thisComponent in CountDownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    if Tag == '1':
        trials = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('../../../SemanticsListFiles/StimulusListRun1.csv', selection=rows),
            seed=None, name='trials')
    else:
        trials = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('../../../SemanticsListFiles/StimulusListRun2.csv', selection=rows),
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
        
        # ------Prepare to start Routine "WordStimulus"-------
        t = 0
        WordStimulusClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        WordStim.setText(Concept)
        Response = event.BuilderKeyResponse()
        # keep track of which components have finished
        WordStimulusComponents = [WordStim, Response]
        for thisComponent in WordStimulusComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "WordStimulus"-------
        CurrentTime = TrialClock.getTime()
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = WordStimulusClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *WordStim* updates
            if t >= 0.0 and WordStim.status == NOT_STARTED:
                # keep track of start time/frame for later
                WordStim.tStart = t
                WordStim.frameNStart = frameN  # exact frame index
                WordStim.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if WordStim.status == STARTED and t >= frameRemains:
                WordStim.setAutoDraw(False)
            
            # *Response* updates
            if t >= 0.0 and Response.status == NOT_STARTED:
                # keep track of start time/frame for later
                Response.tStart = t
                Response.frameNStart = frameN  # exact frame index
                Response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Response.status == STARTED and t >= frameRemains:
                Response.status = STOPPED
            if Response.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2', 'left', 'down'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    Response.keys = theseKeys[-1]  # just the last key pressed
                    Response.rt = Response.clock.getTime()

                if CounterBalFlag == 'False':
                    if Corr == 'left':
                        if ((Response.keys == Corr) or (Response.keys == str(Corr))):
                            Response.corr = 1
                        elif ((Response.keys == '1') or (Response.keys == '1')):
                            Response.corr = 1
                        else:
                            Response.corr = 0
                    if Corr == 1:
                        if ((Response.keys == Corr) or (Response.keys == str(Corr))):
                            Response.corr = 1
                        elif ((Response.keys == 'left') or (Response.keys == 'left')):
                            Response.corr = 1
                        else:
                            resp.corr = 0
                    if Corr == 'down':
                        if ((Response.keys == Corr) or (Response.keys == str(Corr))):
                            Response.corr = 1
                        elif ((Response.keys == '2') or (Response.keys == '2')):
                            Response.corr = 1
                        else:
                            Response.corr = 0    
                    if Corr == 2:
                        if ((Response.keys == Corr) or (Response.keys == str(Corr))):
                            Response.corr = 1
                        elif ((Response.keys == 'down') or (Response.keys == 'down')):
                            Response.corr = 1
                        else:
                            Response.corr = 0
                elif CounterBalFlag == 'True':
                    if Corr == 'left':
                        if ((Response.keys == Corr) or (Response.keys == str(Corr))):
                            Response.corr = 0
                        elif ((Response.keys == '1') or (Response.keys == '1')):
                            Response.corr = 0
                        else:
                            Response.corr = 1
                    if Corr == 1:
                        if ((Response.keys == Corr) or (Response.keys == str(Corr))):
                            Response.corr = 0
                        elif ((Response.keys == 'left') or (Response.keys == 'left')):
                            Response.corr = 0
                        else:
                            Response.corr = 1
                    if Corr == 'down':
                        if ((Response.keys == Corr) or (Response.keys == str(Corr))):
                            Response.corr = 0
                        elif ((Response.keys == '2') or (Response.keys == '2')):
                            Response.corr = 0
                        else:
                            Response.corr = 1    
                    if Corr == 2:
                        if ((Response.keys == Corr) or (Response.keys == str(Corr))):
                            Response.corr = 0
                        elif ((Response.keys == 'down') or (Response.keys == 'down')):
                            Response.corr = 0
                        else:
                            Response.corr = 1



                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in WordStimulusComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "WordStimulus"-------
        for thisComponent in WordStimulusComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Response.keys in ['', [], None]:  # No response was made
            Response.keys=None
            # was no response the correct answer?!
            if str(Corr).lower() == 'none':
               Response.corr = 1  # correct non-response
            else:
               Response.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('CurrentTime',CurrentTime)
        trials.addData('Response.keys',Response.keys)
        trials.addData('Response.corr', Response.corr)
        if Response.keys != None:  # we had a response
            trials.addData('Response.rt', Response.rt)
        
        # ------Prepare to start Routine "RedCrosshair"-------
        t = 0
        RedCrosshairClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        RedCrosshairComponents = [RedCrossHairStim]
        for thisComponent in RedCrosshairComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "RedCrosshair"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RedCrosshairClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *RedCrossHairStim* updates
            if t >= 0.0 and RedCrossHairStim.status == NOT_STARTED:
                # keep track of start time/frame for later
                RedCrossHairStim.tStart = t
                RedCrossHairStim.frameNStart = frameN  # exact frame index
                RedCrossHairStim.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if RedCrossHairStim.status == STARTED and t >= frameRemains:
                RedCrossHairStim.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RedCrosshairComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "RedCrosshair"-------
        for thisComponent in RedCrosshairComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "WhiteCrosshair"-------
    t = 0
    WhiteCrosshairClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    WhiteCrosshairComponents = [WhiteCrossHairStim]
    for thisComponent in WhiteCrosshairComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "WhiteCrosshair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = WhiteCrosshairClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *WhiteCrossHairStim* updates
        if t >= 0.0 and WhiteCrossHairStim.status == NOT_STARTED:
            # keep track of start time/frame for later
            WhiteCrossHairStim.tStart = t
            WhiteCrossHairStim.frameNStart = frameN  # exact frame index
            WhiteCrossHairStim.setAutoDraw(True)
        frameRemains = 0.0 + 17- win.monitorFramePeriod * 0.75  # most of one frame period left
        if WhiteCrossHairStim.status == STARTED and t >= frameRemains:
            WhiteCrossHairStim.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WhiteCrosshairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "WhiteCrosshair"-------
    for thisComponent in WhiteCrosshairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1 repeats of 'Blocks'


# ------Prepare to start Routine "ExtraTimeWhiteCH"-------
t = 0
ExtraTimeWhiteCHClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
ExtraTimeWhiteCHComponents = [text]
for thisComponent in ExtraTimeWhiteCHComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ExtraTimeWhiteCH"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ExtraTimeWhiteCHClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExtraTimeWhiteCHComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ExtraTimeWhiteCH"-------
for thisComponent in ExtraTimeWhiteCHComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "ThankYou"-------
t = 0
ThankYouClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
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
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
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
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
