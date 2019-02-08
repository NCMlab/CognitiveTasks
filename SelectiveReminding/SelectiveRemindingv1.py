#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on Thu Jan 31 21:07:32 2019
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
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)


# #################
# Store info about the experiment session
expName = u'SRT'  # from the Builder filename that created this script
task = 'ImmRecall'
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
BGColor = 'grey'
FontColor = 'white'
FontSize = 60
InstrFontSize = 35

# #################
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
dataFile = open(filename+'.csv', 'w')#a simple text file with 'comma-separated-values'
dataFile.write('Trial, NRecall, Word01, Word2, Word3, Word4, Word5, Word6, Word7, Word8, Word9, Word10, Word11, Word12\n')

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

WordOnTime = 2.0

countDown = core.CountdownTimer()
# Setup the Window
win = visual.Window(
    size=[800, 600], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
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
instr = visual.TextStim(win=win, name='instr',
    text=u'You will see a list of 12 words, presented one by one. \n\nAfter you see the list you will have to recall as many words as you can\nby speaking them out loud.\n\nFor those items that were not recalled during the current trial, the words will be repeated and you  \nare to again recall as many of the original list words as they can. \nThis procedure is repeated for 5 trials.\n \nPress [return] to begin',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=1000, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "EnterResponses"
EnterResponsesClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=u'Please repeat the word list',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Wait"
WaitClock = core.Clock()
WaitText = visual.TextStim(win=win, name='WaitText',
    text=u'+',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
textThankyou = visual.TextStim(win=win, name='Thanks',
    text=u'Thank You',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
    
# on screen timer
Clock = visual.TextStim(win=win, name='Clock',
    text='default text',
    font='Arial',
    pos=(400, -400), height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-19.0);
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [instr, key_resp_4]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if t >= 0.0 and instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr.tStart = t
        instr.frameNStart = frameN  # exact frame index
        instr.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
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
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Blocks = data.TrialHandler(nReps=6, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Blocks')
thisExp.addLoop(Blocks)  # add the loop to the experiment
thisBlock = Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

# create a selection list for the words
# use tjis to decide which word to present
SelectionList = list(range(0,12,1))
ThisBlockSelList = ",".join(str(i) for i in SelectionList)
    # set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../SelectiveReminding/WordList.csv', selection=ThisBlockSelList),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# create word list
WordList = []
CorrList = []
for i in trials.trialList:
    #print(i['Word'])
    WordList.append(i['Word'])
    CorrList.append(i['corr'])


BlockCount = 0
for thisBlock in Blocks:
    BlockCount += 1
    currentLoop = Blocks
    #print(BlockCount)
 
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
        # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential',    
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('../SelectiveReminding/WordList.csv', selection=ThisBlockSelList),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

        
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
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
        routineTimer.add(WordOnTime)
        # update component parameters for each repeat
        text.setText(Word)
        # keep track of which components have finished
        trialComponents = [text]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            frameRemains = 0.0 + WordOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)
            
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
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "EnterResponses"-------
    t = 0
    EnterResponsesClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()
    key_resp_3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    EnterResponsesComponents = [text_2, key_resp_2, key_resp_3]
    for thisComponent in EnterResponsesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "EnterResponses"-------
    while continueRoutine:
        # get current time
        t = EnterResponsesClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6','7','8','9','a','b','c'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys.extend(theseKeys)  # storing all keys
                key_resp_2.rt.append(key_resp_2.clock.getTime())
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
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
        for thisComponent in EnterResponsesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "EnterResponses"-------
    for thisComponent in EnterResponsesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    Blocks.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        Blocks.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "EnterResponses" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Wait"-------
    t = 0
    WaitClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    WaitComponents = [WaitText]
    for thisComponent in WaitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Wait"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = WaitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *WaitText* updates
        if t >= 0.0 and WaitText.status == NOT_STARTED:
            # keep track of start time/frame for later
            WaitText.tStart = t
            WaitText.frameNStart = frameN  # exact frame index
            WaitText.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if WaitText.status == STARTED and t >= frameRemains:
            WaitText.setAutoDraw(False)
        
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
            
            
            
    # Identify the recalled words and create the new list of words
    #print(key_resp_2.keys)
    if key_resp_2.keys != None:
        uniqueResp = list(set(key_resp_2.keys))
        uniqueResp.sort()
        UpdatedWordList = list(WordList)
        # find words to remove    
        WordsToRemove = []
        for i in uniqueResp:
            #print(i)
            index = CorrList.index(i)
            WordsToRemove.append(index)
        # remove the words    
        for i in sorted(WordsToRemove, reverse=True): 
            del UpdatedWordList[i]
            
        # Create selection list
        ThisBlockSelList = []
        count = 0
        for i in WordList:
            for j in UpdatedWordList:
                if i == j:
                    ThisBlockSelList.append(count)
            count += 1
        # if all words were recalled pesent jus a blank
        if len(ThisBlockSelList) == 0:
            ThisBlockSelList.append(12)
        #print(ThisBlockSelList)
    else:
        ThisBlockSelList = ",".join(str(i) for i in SelectionList)
    # Write the words to the file
    dataFile.write('%d,%d,'%(BlockCount, len(uniqueResp)))
    for i in WordsToRemove:
        dataFile.write('%s,'%(WordList[i]))
    dataFile.write('\n') 
    # completed 5 repeats of 'Blocks'

Blocks.addData('key_resp_2.keys',key_resp_2.keys)

# Thank you
textThankyou.setAutoDraw(True)
countDown.add(3)
win.flip()
while countDown.getTime() > 0:
    pass   
win.flip()
# these shouldn't be strictly necessary (should auto-save)
#thisExp.saveAsWideText(filename+'.csv')
dataFile.close()
#thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
