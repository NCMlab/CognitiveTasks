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
_thisDir = os.path.dirname(os.path.abspath(__file__))#.decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# #################
# import parameters from a config file
sys.path.append(os.path.join(_thisDir, '..','ConfigFiles'))
from NCM_NeuroPsych_Config import *

SRT_WordOnTime = 2 # <<< Just for testing

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
# Define how the words should appear on the screen
GridWidth = 300
GridHeight = 300
NRows = 6
NCols = 3
FontSize = 30
WordColor = 'white'
SelectedColor = 'blue'


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

    size=[1440, 900], fullscr=False, screen=0,
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
    text=u'You will see and hear a list of 12 words, presented one by one. \n\nAfter you see and hear the list, you will have to recall as many of the words as you can in 1 minute by speaking them out loud.\n\nFor the words that were not recalled during the trial, they will be repeated and you will be asked to recall the entire list of words again (including the original list of words and the words you may have forgot). This procedure is repeated for 5 trials.\n \nPress [return] to begin',
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

CrossHair = visual.TextStim(win=win, name='CrossHair1',
    text='+',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

WaitText1 = visual.TextStim(win=win, name='text',
    text='Please turn the computer to your tester.\n\nPress [return] to start recall and scoring',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
    
WaitText2 = visual.TextStim(win=win, name='text',
    text='Please turn the computer to the participant.\n\nPress [return] to start the next trial.',
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
    units='pix', pos=(-40, -300), height=30, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
    
RemainingTime = visual.TextStim(win=win, name='RemainingTime',
    text=u'Remaining Time:',
    font=u'Arial',
    units='pix', pos=(-200, -300), height=30, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0);    
# Initialize components for Routine "Wait"
WaitClock = core.Clock()


# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
textThankyou = visual.TextStim(win=win, name='Thanks',
    text=u'Thank You',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

TrialCountText = visual.TextStim(win=win, name='TrialCount',
    text=u'Trial Count',
    font=u'Arial',
    units='pix', pos=(200, -300), height=30, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
# ##############################

# Make lists of screen locations for the words
ColLocsList, RowLocsList = SRT.MakeGridOfSRTWords(GridWidth, GridHeight, NCols, NRows)


# Load up the list of words used for scoring. The only difference is that this list has 
# a bunch of [intrusion] options in it.
inputFile = '../SelectiveReminding/WordListScoring.csv'
FullWordScoringList = pd.read_csv(inputFile)

# Load up the original word list
inputFile = '../SelectiveReminding/WordList.csv'
FullWordList = pd.read_csv(inputFile)

# Initialize components for Routine "trial"
trialClock = core.Clock()
mouse = event.Mouse(True, None, win=win)

x, y = [None, None]

# For every word in the word list do the following
WordListObjects = []
count = 1
for word in FullWordScoringList['Word']:
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

# For every word in the word list do the following
WordListBoxObjects = []
count = 1
for word in FullWordScoringList['Word']:
    print(count)
    # Make a unique name
    WordBoxCount = 'text%02d'%(count)
    # Create a text stim object for Psychopy

    polygon = visual.Rect(
        win=win, name=WordBoxCount,
        width=50, height=FontSize,
        ori=0, pos=(ColLocsList[count-1][0], RowLocsList[count-1][0]),
        lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
        fillColor=[1,1,1], fillColorSpace='rgb',
        opacity=0.1, depth=-2.0, interpolate=True)        
    # Add this visual stim obkect to a list
    WordListBoxObjects.append(polygon) 
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
#print("Original")
#print(ThisBlockSelList)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(os.path.join(_thisDir,'..','..',SRTPath,'WordList.csv'), selection=ThisBlockSelList),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values


# Make a list of all of the sounds
SoundList = []
for i in trials.trialList:
    print(i['Word'])
    TempSound = sound.Sound(os.path.join(_thisDir,'..','..',SoundPath,'%s.wav'%(i['Word'])), secs=1.0)
    TempSound.setVolume(1)
    SoundList.append(TempSound)
print('Loaded sound files')
# How many words in the test list?
NWords = len(trials.trialList)
print("There are %d words"%(NWords))
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
ResponseArray = np.zeros((12,NBlocks))
NIntrusionArray = np.zeros(NBlocks)
AllIntrusionList = []
#print(Blocks)
BlockCount = 0
for thisBlock in range(0,NBlocks):
    routineTimer.reset()
    BlockCount += 1

    
    # Check to see if all words were recalled. If so then skip the word presentation 
    # and go straight too recall
    if len(ThisBlockSelList) > 0:
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
    else:
        # IF all words were recalled during the last trialClock
        # present just a cross hair for one second to differentiate the two TURN screens
        CrossHair.setAutoDraw(True)
        win.flip()
        core.wait(1)
        CrossHair.setAutoDraw(False)
        win.flip()
    
    print("Finished presenting words")

    # Now wait until the screen is turned to the tester
    # Add the wait block
    # Put the wait text on the screen
    WaitText1.setAutoDraw(True)
    win.flip()
    WaitingFlag = True
    while WaitingFlag is True:
        theseKeys = event.getKeys(keyList=['escape','return'])
        if 'escape' in theseKeys:
            SRT.WriteOutResults(dataFile, ResponseArray, NIntrusionArray, WordList, AllIntrusionList)
            core.quit()
        elif 'return' in theseKeys:
            WaitingFlag = False
            WaitText1.setAutoDraw(False)
        else:
            pass       
    # Put all the words on the screen and have the tester click the recalled words and enter any intrusions
    TrialCountText.text = 'Trial count: %d'%(thisBlock+1)
    WordListObjects, mouse, RecallList, RecallOrder = SRT.PresentWordSelection(WordListObjects, trialClock, mouse, event, endExpNow, win, core, NWords, ResponseTimer, RemainingTime, TrialCountText, WordListBoxObjects)
    print("Recall List:")
    print(RecallList)
    ResponseArray[:,BlockCount - 1] = RecallList
    print(RecallOrder)
    print(mouse.clicked_text)
    #    print(ResponseArray)
    
    # Check to see if any intrusions were recalled
    # Have the tester type in the intrusion words
    ResponseList, IntrusionCount, IntrusionList = SRT.CheckForIntrusions(mouse) 
    NIntrusionArray[BlockCount - 1] = IntrusionCount
    AllIntrusionList.append(IntrusionList)
    
    
    
#   Change the list for the next trial
    ThisBlockSelList = SRT.MakeListOfRecalledWords(FullWordList, RecallList)
    print("This Block Sel List:")
    print(ThisBlockSelList)
    # Fill in the list of words recalled to be saved to the data file
    # ResponseArray = SRT.FillResponseArray(ResponseArray, mouse.clicked_text, BlockCount - 1)
    
#    print(ThisBlockSelList)            
#    print("Mouse Clicked text:%s"%(mouse.clicked_text))
#    print(IntrusionCount)
#    print(IntrusionList)
    print(NIntrusionArray)
    print(AllIntrusionList)
    # Now wait until the screen is turned to the PARTICIPANT
    # Add the wait block
    # Put the wait text on the screen
    WaitText2.setAutoDraw(True)
    win.flip()
    WaitingFlag = True
    while WaitingFlag is True:
        theseKeys = event.getKeys(keyList=['escape','return'])
        if 'escape' in theseKeys:
            SRT.WriteOutResults(dataFile, ResponseArray, NIntrusionArray, WordList, AllIntrusionList)
            core.quit()
        elif 'return' in theseKeys:
            WaitingFlag = False
            WaitText2.setAutoDraw(False)
        else:
            pass  
    # At the end of each trial write out results
    #SRT.WriteOutResults(dataFile, ResponseArray, NIntrusionArray, WordList, AllIntrusionList)
#    print("Correct Recog: %s"%(CorrectRecog))

# Thank you
textThankyou.setAutoDraw(True)
countDown.reset()
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

SRT.WriteOutResults(dataFile, ResponseArray, NIntrusionArray, WordList, AllIntrusionList)

#dataFile.close()
#thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
