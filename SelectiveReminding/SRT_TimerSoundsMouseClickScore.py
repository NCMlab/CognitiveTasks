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

Preserve order of responses
"""

from __future__ import absolute_import, division
from psychopy import sound
from psychopy import locale_setup, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import pandas as pd
import SRT_Functions as SRT
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# #################
# import parameters from a config file
sys.path.append(os.path.join(_thisDir, '..','ConfigFiles'))
from NCM_NeuroPsych_Config import *
import SRT_Functions
SRT_WordOnTime = 1 # <<< Just for testing

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
print(filename)
# The number of trials, or repeats
NBlocks = 6
#BGColor = 'grey'
#FontColor = 'white'
#FontSize = 60
#InstrFontSize = 35

# #################
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
dataFile = open(filename+'.csv', 'w')#a simple text file with 'comma-separated-values'
#dataFile.write('Trial, NRecall, Word01, Word2, Word3, Word4, Word5, Word6, Word7, Word8, Word9, Word10, Word11, Word12\n')

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

countDown = core.CountdownTimer()
# Setup the Window
win = visual.Window(
    size=[1200, 800], fullscr=False, screen=0,
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
instr = visual.TextStim(win=win, name='instr',
    text=u'You will hear a list of 12 words, presented one by one. \n\nAfter you hear the list you will have to recall as many words as you can by speaking them out loud.\n\nFor the words that were not recalled during the trial, they will be repeated and you will be asked to recall the entire list of words again (including the original list of words and the words you may have forgot). This procedure is repeated for 5 trials.\n \nPress [return] to begin',
   # For those items that were not recalled during the current trial, the words will be repeated and you  \nare to again recall as many of the original list words as they can. \nThis procedure is repeated for 5 trials.\n \nPress [return] to begin',
    font=u'Arial',
    units='pix', pos=(0, 0), height=35, wrapWidth=1100, ori=0, 
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

ResponseText = visual.TextStim(win=win, name='text_2',
    text=u'Please repeat the entire word list',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
# Get the count down clock going
countDownStarted = False
ResponseTimer = visual.TextStim(win=win, name='ResponseTimer',
    text='default text',
    font=u'Arial',
    units='pix', pos=(40, -200), height=30, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
    
RemainingTime = visual.TextStim(win=win, name='RemainingTime',
    text=u'Remaining Time:',
    font=u'Arial',
    units='pix', pos=(-100, -200), height=30, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0);    
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
    
# ##############################
# Define how the words should appear on the screen
GridWidth = 600
GridHeight = 500
NRows = 6
NCols = 3
# Make lists of screen locations for the words
ColLocsList, RowLocsList = SRT.MakeGridOfSRTWords(GridWidth, GridHeight, NCols, NRows)



FontSize = 30
WordColor = 'white'
SelectedColor = 'blue'
inputFile = '../SelectiveReminding/WordListScoring.csv'
trials = pd.read_csv(inputFile)
# Initialize components for Routine "trial"
trialClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]

# For every word in the word list do the following
WordListObjects = []
count = 1
for word in trials['Word']:
    print(count)
    # Make a unique name
    WordCount = 'text%02d'%(count)
    # Create a text stim object for Psychopy
    textTemp = visual.TextStim(win=win, name = WordCount,
        text=word,
        font=u'Arial',
        units='pix', pos=(ColLocsList[count-1][0], RowLocsList[count-1][0]), height=FontSize, wrapWidth=None, ori=0, 
        color=WordColor, colorSpace='rgb', opacity=1,
        depth=-1.0);
    # Add this visual stim obkect to a list
    WordListObjects.append(textTemp) 
    count += 1

# ########
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

# create a selection list for the words
# use tjis to decide which word to present
SelectionList = list(range(0,12,1))
ThisBlockSelList = ",".join(str(i) for i in SelectionList)
ThisBlockSelList = SelectionList


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(os.path.join(_thisDir,'..','..',SRTPath,'WordList.csv'), selection=ThisBlockSelList),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# Make a listxvb of all of the sounds
SoundList = []
for i in trials.trialList:
    print(i['Word'])
    TempSound = sound.Sound(os.path.join(_thisDir,'..','..',SoundPath,'%s.wav'%(i['Word'])), secs=1.0)
    TempSound.setVolume(1)
    SoundList.append(TempSound)
print('Loaded sound files')
# Add the blank dummy to the end when someone recalls all WordsToRemove
TempSound = sound.Sound(os.path.join(_thisDir,'..','..',SoundPath,'%s.wav'%('BLANK')), secs=1.0)
TempSound.setVolume(1)
SoundList.append(TempSound)
    
# create word list
WordList = []
CorrList = []
for i in trials.trialList:
    #print(i['Word'])
    WordList.append(i['Word'])
    CorrList.append(i['corr'])

# Initialize the response array
ResponseArray = np.zeros((12,6))
NIntrusionArray = np.zeros(6)
#print(Blocks)
BlockCount = 0
for thisBlock in range(0,NBlocks):
    routineTimer.reset()
    BlockCount += 1
#    currentLoop = Blocks
    #print(BlockCount)
 
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
#    if thisBlock != None:
#        for paramName in thisBlock:
#            exec('{} = thisBlock[paramName]'.format(paramName))
    
        # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential',    
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(os.path.join(_thisDir,'..','..', SRTPath, 'WordList.csv'), selection=ThisBlockSelList),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

        
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    
    routineTimer.add(SRT_FudgeTime)
    TrialCount = 0
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
        routineTimer.add(SRT_WordOnTime)
        # update component parameters for each repeat
        
        text.setText(Word)
        print(ThisBlockSelList[TrialCount])
        sound_1 = SoundList[ThisBlockSelList[TrialCount]]
        
        
        # keep track of which components have finished
        trialComponents = [text, sound_1]
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
            frameRemains = 0.0 + SRT_WordOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)
            
            
            # start/stop sound_1
            if t >= 0.0 and sound_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_1.tStart = t
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.play()  # start the sound (it finishes automatically)
            
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
        TrialCount += 1
    # completed 1 repeats of 'trials'
    
    print("Finished presenting words")
    WordListObjects, mouse = SRT.PresentWordSelection(WordListObjects, trialClock, mouse, event, endExpNow, win, core)
    # Check to see if any intrusions were recalled
    # Have the tester type in the intrusion words
    SRT.CheckForIntrusions(mouse)      
#   Change the list for the next trial
    
                
    print("Mouse Clicked text:%s"%(mouse.clicked_text))
#    print("Correct Recog: %s"%(CorrectRecog))

#    # ------Prepare to start Routine "EnterResponses"-------
#    t = 0
#    EnterResponsesClock.reset()  # clock
#    frameN = -1
#    continueRoutine = True
#    # update component parameters for each repeat
#    key_resp_2 = event.BuilderKeyResponse()
#    key_resp_3 = event.BuilderKeyResponse()
#    if not countDownStarted:
#        countDownClock = core.CountdownTimer(SRT_ResponseTimeAllowed)
#        countDownStarted = True
#    # keep track of which components have finished
#    EnterResponsesComponents = [ResponseText, key_resp_2, key_resp_3, ResponseTimer, RemainingTime]
#    for thisComponent in EnterResponsesComponents:
#        if hasattr(thisComponent, 'status'):
#            thisComponent.status = NOT_STARTED
#    
#    # -------Start Routine "EnterResponses"-------
#    while continueRoutine:
#        # get current time
#        t = EnterResponsesClock.getTime()
#        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#        # update/draw components on each frame
#        
#        # *text_2* updates
#        if t >= 0.0 and ResponseText.status == NOT_STARTED:
#            # keep track of start time/frame for later
#            ResponseText.tStart = t
#            ResponseText.frameNStart = frameN  # exact frame index
#            ResponseText.setAutoDraw(True)
#        
#        # *key_resp_2* updates
#        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
#            # keep track of start time/frame for later
#            key_resp_2.tStart = t
#            key_resp_2.frameNStart = frameN  # exact frame index
#            key_resp_2.status = STARTED
#            # keyboard checking is just starting
#            key_resp_2.clock.reset()  # now t=0
#        if key_resp_2.status == STARTED:
#            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6','7','8','9','a','b','c','x'])
#            
#            # check for quit:
#            if "escape" in theseKeys:
#                endExpNow = True
#            if len(theseKeys) > 0:  # at least one key was pressed
#                key_resp_2.keys.extend(theseKeys)  # storing all keys
#                key_resp_2.rt.append(key_resp_2.clock.getTime())
#        
#        # *key_resp_3* updates
#        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
#            # keep track of start time/frame for later
#            key_resp_3.tStart = t
#            key_resp_3.frameNStart = frameN  # exact frame index
#            key_resp_3.status = STARTED
#            # keyboard checking is just starting
#            event.clearEvents(eventType='keyboard')
#        if key_resp_3.status == STARTED:
#            theseKeys = event.getKeys(keyList=['return'])
#            
#            # check for quit:
#            if "escape" in theseKeys:
#                endExpNow = True
#            if len(theseKeys) > 0:  # at least one key was pressed
#                # a response ends the routine
#                continueRoutine = False
#        # This is for the countdown timer
#        timeRemaining = countDownClock.getTime()
#        if timeRemaining <= 0.0:
#            continueRoutine = False
#            ResponseText.finished = True
#            countDownStarted = False
#        else:
#            seconds = int(timeRemaining)
#            timeText = "%02d"%(seconds)
#        
#        
#        # *ResponseTimer* updates
#        if t >= 0.0 and ResponseTimer.status == NOT_STARTED:
#            # keep track of start time/frame for later
#            ResponseTimer.tStart = t
#            ResponseTimer.frameNStart = frameN  # exact frame index
#            ResponseTimer.setAutoDraw(True)
#        if ResponseTimer.status == STARTED:  # only update if drawing
#            ResponseTimer.setText(timeText, log=False)
#        
#        # *RemainingTime* updates
#        if t >= 0.0 and RemainingTime.status == NOT_STARTED:
#            # keep track of start time/frame for later
#            RemainingTime.tStart = t
#            RemainingTime.frameNStart = frameN  # exact frame index
#            RemainingTime.setAutoDraw(True)
#            
#        # check if all components have finished
#        if not continueRoutine:  # a component has requested a forced-end of Routine
#            break
#        continueRoutine = False  # will revert to True if at least one component still running
#        for thisComponent in EnterResponsesComponents:
#            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#                continueRoutine = True
#                break  # at least one component has not yet finished
#        
#        # check for quit (the Esc key)
#        if endExpNow or event.getKeys(keyList=["escape"]):
#            core.quit()
#        
#        # refresh the screen
#        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#            win.flip()
#
#    # -------Ending Routine "EnterResponses"-------
#    for thisComponent in EnterResponsesComponents:
#        if hasattr(thisComponent, "setAutoDraw"):
#            thisComponent.setAutoDraw(False)
#    # check responses
#    if key_resp_2.keys in ['', [], None]:  # No response was made
#        key_resp_2.keys=None
##    Blocks.addData('key_resp_2.keys',key_resp_2.keys)
##    if key_resp_2.keys != None:  # we had a response
##        Blocks.addData('key_resp_2.rt', key_resp_2.rt)
#    # reset the timer for each recall attempt    
#    countDownStarted = False
#    # the Routine "EnterResponses" was not non-slip safe, so reset the non-slip timer
#    routineTimer.reset()
#    
#    # ------Prepare to start Routine "Wait"-------
#    t = 0
#    WaitClock.reset()  # clock
#    frameN = -1
#    continueRoutine = True
#    routineTimer.add(1.000000)
#    # update component parameters for each repeat
#    # keep track of which components have finished
#    WaitComponents = [WaitText]
#    for thisComponent in WaitComponents:
#        if hasattr(thisComponent, 'status'):
#            thisComponent.status = NOT_STARTED
#    
#    # -------Start Routine "Wait"-------
#    while continueRoutine and routineTimer.getTime() > 0:
#        # get current time
#        t = WaitClock.getTime()
#        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#        # update/draw components on each frame
#        
#        # *WaitText* updates
#        if t >= 0.0 and WaitText.status == NOT_STARTED:
#            # keep track of start time/frame for later
#            WaitText.tStart = t
#            WaitText.frameNStart = frameN  # exact frame index
#            WaitText.setAutoDraw(True)
#        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
#        if WaitText.status == STARTED and t >= frameRemains:
#            WaitText.setAutoDraw(False)
#        
#        # check if all components have finished
#        if not continueRoutine:  # a component has requested a forced-end of Routine
#            break
#        continueRoutine = False  # will revert to True if at least one component still running
#        for thisComponent in WaitComponents:
#            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#                continueRoutine = True
#                break  # at least one component has not yet finished
#        
#        # check for quit (the Esc key)
#        if endExpNow or event.getKeys(keyList=["escape"]):
#            core.quit()
#        
#        # refresh the screen
#        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#            win.flip()
#    
#    # -------Ending Routine "Wait"-------
#    for thisComponent in WaitComponents:
#        if hasattr(thisComponent, "setAutoDraw"):
#            thisComponent.setAutoDraw(False)
#            
#            
#
#    # Identify the recalled words and create the new list of words
#    #print(key_resp_2.keys)
#    if key_resp_2.keys != None:
#        
#        # Add these responses to the response array
#        cList = SRT.CleanSRTResponses(key_resp_2.keys)        
#        ResponseArray = SRT.FillResponseArray(ResponseArray, cList, BlockCount - 1)
#        
#        # Create the word list for the next trial
#        uniqueResp = list(set(key_resp_2.keys))
#        uniqueResp.sort()
#        # Remove the intrusions from the list
#        uniqueRespNoX = uniqueResp
#        NIntrusions = np.count_nonzero(np.array(key_resp_2.keys) == 'x')
#        NIntrusionArray[BlockCount -1] = NIntrusions
#        for i in range(0, len(uniqueResp)):
#            if uniqueResp[i] == 'x':
#                del uniqueRespNoX[i]
#        
#        UpdatedWordList = list(WordList)
#        # find words to remove    
#        WordsToRemove = []        
#        for i in uniqueRespNoX:
#            #print(i)
#            index = CorrList.index(i)
#            WordsToRemove.append(index)
#        # remove the words    
#        for i in sorted(WordsToRemove, reverse=True): 
#            del UpdatedWordList[i]
#            
#        # Create selection list
#        ThisBlockSelList = []
#        count = 0
#        for i in WordList:
#            for j in UpdatedWordList:
#                if i == j:
#                    ThisBlockSelList.append(count)
#            count += 1
#        # if all words were recalled, present just a blank
#        if len(ThisBlockSelList) == 0:
#            ThisBlockSelList.append(12)
#        #print(ThisBlockSelList)
#    else:
#        # no responses
#        uniqueResp = []
#        WordsToRemove = []
#        ThisBlockSelList = list(range(0,12,1))
        
#        ThisBlockSelList = ",".join(str(i) for i in SelectionList)
    # Write the words to the file
    # dataFile.write('%d,%d,'%(BlockCount, len(uniqueResp)))
#    for i in WordsToRemove:
#        dataFile.write('%s,'%(WordList[i]))
#    dataFile.write('\n') 
#    # completed 5 repeats of 'Blocks'

#Blocks.addData('key_resp_2.keys',key_resp_2.keys)

# Thank you
textThankyou.setAutoDraw(True)
countDown.add(ThankYouOnTime)
win.flip()
while countDown.getTime() > 0:
    pass   
win.flip()
# these shouldn't be strictly necessary (should auto-save)
#thisExp.saveAsWideText(filename+'.csv')

print(ResponseArray)
print(WordList)
print(NIntrusionArray)
print('Writing results')

SRT.WriteOutResults(dataFile, ResponseArray, NIntrusionArray, WordList)

dataFile.close()
#thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
