#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Fri 28 Jul 2017 03:09:05 PM EDT
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

#from __future__ import absolute_import, division
import os  # handy system and path functions
#tempFile = open('tempFileDMS.txt', 'w')

from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import sys  # to get file system encoding

#tempFile.write("Loaded libraries\n")


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)
# tempFile.write("Set directory\n")
# Store info about the experiment session


expName = u'DMS_Block'  # from the Builder filename that created this script
expInfo = {'Participant ID':'', 'Session':'001'}
#tempFile.write("Number of input arguments: %d\n"%(len(sys.argv)))
PartDataFolder = 'unorganized'
if len(sys.argv) > 2:
    #tempFile.write("Entered if clause\n")
    #tempFile.write('%s\n'%(sys.argv[2]))
    expInfo['Participant ID'] = sys.argv[1]
    #tempFile.write('%s\n'%(sys.argv[1]))
    #tempFile.write('%s\n'%(sys.argv[2]))
    LoadList = sys.argv[2].split(' ')
    LoadList = np.array(LoadList)
    LoadList = LoadList.astype(np.int)
    PartDataFolder = sys.argv[1]
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    LoadList = np.array(range(1,7,1))
    LoadList = LoadList.astype(np.int)
#tempFile.write("Loaded inputs\n")
expInfo['date'] = data.getDateStr()  # add a simple timestamp
#for e in LoadList:
#    tempFile.write('%d\n'%(e))
#tempFile.write('%s\n'%(sys.argv[2]))

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc

OutDir = '..' + os.sep + '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
filename = OutDir + '%s_%s_%s' % (expName, expInfo['Participant ID'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/jsteffe/Dropbox/SteffenerColumbia/Projects/MyProjects/NeuralCognitiveMapping/DMSPsychopyFiles/DMS_Adaptive.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')

StimOnTime = 2.5
RetOnTime = 3.5
ProbeOnTime= 2.5
ITITime = 1.0

'''win = visual.Window(
    size=(800, 600), fullscr=False, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
StimOnTime = .25
RetOnTime = .25
ProbeOnTime= 0.25
ITITime = .25'''
TotalTrialTime = StimOnTime + RetOnTime + ProbeOnTime + ITITime
InterBlockTime = 2.0

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
textInstr1 = visual.TextStim(win=win, name='textInstr1',
#    text='Ready to start the main experiment?\n\nRemember:\nPress [LEFT] if the letter WAS in the set.\nPress [DOWN] if the letter was NOT in the set.\n\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    text='Remember:\nPress [LEFT] for IN the set.\nPress [DOWN] for NOT in the set.\nThis time, the next trial will not appear automatically after your answer (there may be a delay).\n\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed, press any key.',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Countdown"
CountdownClock = core.Clock()
text3 = visual.TextStim(win=win, name='text3',
    text='3',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text2 = visual.TextStim(win=win, name='text2',
    text='2',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text1 = visual.TextStim(win=win, name='text1',
    text='1',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
textITI = visual.TextStim(win=win, name='textITI',
    text='+',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
textTL = visual.TextStim(win=win, name='textTL',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(-50, 50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
textTM = visual.TextStim(win=win, name='textTM',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, 50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
textTR = visual.TextStim(win=win, name='textTR',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(50, 50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
textCL = visual.TextStim(win=win, name='textCL',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(-50, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
textCM = visual.TextStim(win=win, name='textCM',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
textCR = visual.TextStim(win=win, name='textCR',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(50, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
textBL = visual.TextStim(win=win, name='textBL',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(-50, -50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
textBM = visual.TextStim(win=win, name='textBM',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, -50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
textBR = visual.TextStim(win=win, name='textBR',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(50, -50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
textDelay = visual.TextStim(win=win, name='textDelay',
    text='+',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1,
    depth=-10.0);
textProbe = visual.TextStim(win=win, name='textProbe',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0);

# Initialize components for Routine "Interblock"
InterblockClock = core.Clock()
textInterblock = visual.TextStim(win=win, name='textInterblock',
    text='+',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=0.0);
text3A = visual.TextStim(win=win, name='text3A',
    text='3',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text2A = visual.TextStim(win=win, name='text2A',
    text='2',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text1A = visual.TextStim(win=win, name='text1A',
    text='1',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Interblock"
InterblockClock = core.Clock()





# Initialize components for Routine "trial"
trialClock = core.Clock()
textITI = visual.TextStim(win=win, name='textITI',
    text='+',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
textTL = visual.TextStim(win=win, name='textTL',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(-50, 50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
textTM = visual.TextStim(win=win, name='textTM',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, 50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
textTR = visual.TextStim(win=win, name='textTR',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(50, 50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
textCL = visual.TextStim(win=win, name='textCL',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(-50, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
textCM = visual.TextStim(win=win, name='textCM',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
textCR = visual.TextStim(win=win, name='textCR',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(50, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
textBL = visual.TextStim(win=win, name='textBL',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(-50, -50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
textBM = visual.TextStim(win=win, name='textBM',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, -50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
textBR = visual.TextStim(win=win, name='textBR',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(50, -50), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
textDelay = visual.TextStim(win=win, name='textDelay',
    text='+',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1,
    depth=-10.0);
textProbe = visual.TextStim(win=win, name='textProbe',
    text='default text',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-11.0);

# Initialize components for Routine "EndDelay"
EndDelayClock = core.Clock()
textEndDelay = visual.TextStim(win=win, name='textEndDelay',
    text='+',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Thankyou"
ThankyouClock = core.Clock()
textThankyou = visual.TextStim(win=win, name='textThankyou',
    text='Thank you for participating!\n\nWhen you are ready to proceed press any key.',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
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
OK1 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [textInstr1, OK1]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInstr1* updates
    if t >= 0.0 and textInstr1.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInstr1.tStart = t
        textInstr1.frameNStart = frameN  # exact frame index
        textInstr1.setAutoDraw(True)
    
    # *OK1* updates
    if t >= 0.0 and OK1.status == NOT_STARTED:
        # keep track of start time/frame for later
        OK1.tStart = t
        OK1.frameNStart = frameN  # exact frame index
        OK1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if OK1.status == STARTED:
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

# ------Prepare to start Routine "Countdown"-------
t = 0
CountdownClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
CountdownComponents = [text3, text2, text1]
for thisComponent in CountdownComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Countdown"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = CountdownClock.getTime()
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
    for thisComponent in CountdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Countdown"-------
for thisComponent in CountdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
# ========================================================
## BLOCK 1
Block = 1
print "Block = %d"%(Block)
print LoadList
CurrentLoad = LoadList[Block-1]
print "CurrentLoad = %d"%(CurrentLoad)
SelectionList = np.array(range(0,6,1)) + (CurrentLoad - 1)*6
print SelectionList

trials1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../DMSPsychopyFiles/DMSBlockListv2.csv', selection=SelectionList),
    seed=None, name='trials1')
    
thisExp.addLoop(trials1)  # add the loop to the experiment
thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
if thisTrials1 != None:
    for paramName in thisTrials1.keys():
        exec(paramName + '= thisTrials1.' + paramName)

for thisTrials1 in trials1:
    currentLoop = trials1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1.keys():
            exec(paramName + '= thisTrials1.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(TotalTrialTime)#############################################
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + ITITime- win.monitorFramePeriod * 0.75  # most of one frame period left #############################################
        if textITI.status == STARTED and t >= frameRemains:
            textITI.setAutoDraw(False)
        
        # *textTL* updates
        if t >= ITITime and textTL.status == NOT_STARTED: #############################################
            # keep track of start time/frame for later 
            textTL.tStart = t
            textTL.frameNStart = frameN  # exact frame index
            textTL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left #############################################
        if textTL.status == STARTED and t >= frameRemains:
            textTL.setAutoDraw(False)
        
        # *textTM* updates
        if t >= ITITime and textTM.status == NOT_STARTED: #############################################
            # keep track of start time/frame for later
            textTM.tStart = t
            textTM.frameNStart = frameN  # exact frame index
            textTM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left #############################################
        if textTM.status == STARTED and t >= frameRemains:
            textTM.setAutoDraw(False)
        
        # *textTR* updates
        if t >= ITITime and textTR.status == NOT_STARTED: #############################################
            # keep track of start time/frame for later
            textTR.tStart = t
            textTR.frameNStart = frameN  # exact frame index
            textTR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left #############################################
        if textTR.status == STARTED and t >= frameRemains:
            textTR.setAutoDraw(False)
        
        # *textCL* updates
        if t >= ITITime and textCL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCL.tStart = t
            textCL.frameNStart = frameN  # exact frame index
            textCL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCL.status == STARTED and t >= frameRemains:
            textCL.setAutoDraw(False)
        
        # *textCM* updates
        if t >= ITITime and textCM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCM.tStart = t
            textCM.frameNStart = frameN  # exact frame index
            textCM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCM.status == STARTED and t >= frameRemains:
            textCM.setAutoDraw(False)
        
        # *textCR* updates
        if t >= ITITime and textCR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCR.tStart = t
            textCR.frameNStart = frameN  # exact frame index
            textCR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCR.status == STARTED and t >= frameRemains:
            textCR.setAutoDraw(False)
        
        # *textBL* updates
        if t >= ITITime and textBL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBL.tStart = t
            textBL.frameNStart = frameN  # exact frame index
            textBL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBL.status == STARTED and t >= frameRemains:
            textBL.setAutoDraw(False)
        
        # *textBM* updates
        if t >= ITITime and textBM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBM.tStart = t
            textBM.frameNStart = frameN  # exact frame index
            textBM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBM.status == STARTED and t >= frameRemains:
            textBM.setAutoDraw(False)
        
        # *textBR* updates
        if t >= ITITime and textBR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBR.tStart = t
            textBR.frameNStart = frameN  # exact frame index
            textBR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime - win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBR.status == STARTED and t >= frameRemains:
            textBR.setAutoDraw(False)
        
        # *textDelay* updates
        if t >=(ITITime+StimOnTime) and textDelay.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDelay.tStart = t
            textDelay.frameNStart = frameN  # exact frame index
            textDelay.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime) + RetOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textDelay.status == STARTED and t >= frameRemains:
            textDelay.setAutoDraw(False)
        
        # *textProbe* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and textProbe.status == NOT_STARTED:
            # keep track of start time/frame for later
            textProbe.tStart = t
            textProbe.frameNStart = frameN  # exact frame index
            textProbe.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textProbe.status == STARTED and t >= frameRemains:
            textProbe.setAutoDraw(False)
        
        # *resp* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
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
                # continueRoutine = False
        
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
    # store data for trials1 (TrialHandler)
    trials1.addData('resp.keys',resp.keys)
    trials1.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials1.addData('resp.rt', resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials1'


# ------Prepare to start Routine "Interblock"-------
t = 0
InterblockClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(InterBlockTime+3.0)
# update component parameters for each repeat
# keep track of which components have finished
InterblockComponents = [textInterblock, text3A, text2A, text1A]
for thisComponent in InterblockComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Interblock"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InterblockClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterblock* updates
    if t >= 0.0 and textInterblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInterblock.tStart = t
        textInterblock.frameNStart = frameN  # exact frame index
        textInterblock.setAutoDraw(True)
    frameRemains = 0.0 + InterBlockTime- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textInterblock.status == STARTED and t >= frameRemains:
        textInterblock.setAutoDraw(False)
    
    # *text3A* updates
    if t >= InterBlockTime and text3A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text3A.tStart = t
        text3A.frameNStart = frameN  # exact frame index
        text3A.setAutoDraw(True)
    frameRemains = InterBlockTime + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text3A.status == STARTED and t >= frameRemains:
        text3A.setAutoDraw(False)
    
    # *text2A* updates
    if t >= InterBlockTime+1.0 and text2A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2A.tStart = t
        text2A.frameNStart = frameN  # exact frame index
        text2A.setAutoDraw(True)
    frameRemains = InterBlockTime+1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text2A.status == STARTED and t >= frameRemains:
        text2A.setAutoDraw(False)
    
    # *text1A* updates
    if t >= InterBlockTime+2.0 and text1A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1A.tStart = t
        text1A.frameNStart = frameN  # exact frame index
        text1A.setAutoDraw(True)
    frameRemains = InterBlockTime+2.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text1A.status == STARTED and t >= frameRemains:
        text1A.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InterblockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Interblock"-------
for thisComponent in InterblockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# set up handler to look after randomisation of conditions etc
# ========================================================
## BLOCK 2
# Check the Load list for the second entry. Use this to create a selection list.
Block = 2
print "Block = %d"%(Block)
print LoadList
CurrentLoad = LoadList[Block-1]
print "CurrentLoad = %d"%(CurrentLoad)
SelectionList = np.array(range(0,6,1)) + (CurrentLoad - 1)*6
print SelectionList

trials2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../DMSPsychopyFiles/DMSBlockListv2.csv', selection=SelectionList),
    seed=None, name='trials2')

thisExp.addLoop(trials2)  # add the loop to the experiment
thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
if thisTrials2 != None:
    for paramName in thisTrials2.keys():
        exec(paramName + '= thisTrials2.' + paramName)

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2.keys():
            exec(paramName + '= thisTrials2.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(TotalTrialTime)
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + ITITime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textITI.status == STARTED and t >= frameRemains:
            textITI.setAutoDraw(False)
        
        # *textTL* updates
        if t >= ITITime and textTL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTL.tStart = t
            textTL.frameNStart = frameN  # exact frame index
            textTL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTL.status == STARTED and t >= frameRemains:
            textTL.setAutoDraw(False)
        
        # *textTM* updates
        if t >= ITITime and textTM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTM.tStart = t
            textTM.frameNStart = frameN  # exact frame index
            textTM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTM.status == STARTED and t >= frameRemains:
            textTM.setAutoDraw(False)
        
        # *textTR* updates
        if t >= ITITime and textTR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTR.tStart = t
            textTR.frameNStart = frameN  # exact frame index
            textTR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTR.status == STARTED and t >= frameRemains:
            textTR.setAutoDraw(False)
        
        # *textCL* updates
        if t >= ITITime and textCL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCL.tStart = t
            textCL.frameNStart = frameN  # exact frame index
            textCL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCL.status == STARTED and t >= frameRemains:
            textCL.setAutoDraw(False)
        
        # *textCM* updates
        if t >= ITITime and textCM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCM.tStart = t
            textCM.frameNStart = frameN  # exact frame index
            textCM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCM.status == STARTED and t >= frameRemains:
            textCM.setAutoDraw(False)
        
        # *textCR* updates
        if t >= ITITime and textCR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCR.tStart = t
            textCR.frameNStart = frameN  # exact frame index
            textCR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCR.status == STARTED and t >= frameRemains:
            textCR.setAutoDraw(False)
        
        # *textBL* updates
        if t >= ITITime and textBL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBL.tStart = t
            textBL.frameNStart = frameN  # exact frame index
            textBL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBL.status == STARTED and t >= frameRemains:
            textBL.setAutoDraw(False)
        
        # *textBM* updates
        if t >= ITITime and textBM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBM.tStart = t
            textBM.frameNStart = frameN  # exact frame index
            textBM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBM.status == STARTED and t >= frameRemains:
            textBM.setAutoDraw(False)
        
        # *textBR* updates
        if t >= ITITime and textBR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBR.tStart = t
            textBR.frameNStart = frameN  # exact frame index
            textBR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBR.status == STARTED and t >= frameRemains:
            textBR.setAutoDraw(False)
        
        # *textDelay* updates
        if t >=(ITITime+StimOnTime) and textDelay.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDelay.tStart = t
            textDelay.frameNStart = frameN  # exact frame index
            textDelay.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime) + RetOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textDelay.status == STARTED and t >= frameRemains:
            textDelay.setAutoDraw(False)
        
        # *textProbe* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and textProbe.status == NOT_STARTED:
            # keep track of start time/frame for later
            textProbe.tStart = t
            textProbe.frameNStart = frameN  # exact frame index
            textProbe.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textProbe.status == STARTED and t >= frameRemains:
            textProbe.setAutoDraw(False)
        
        # *resp* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
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
                # continueRoutine = False
        
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
    # store data for trials2 (TrialHandler)
    trials2.addData('resp.keys',resp.keys)
    trials2.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials2.addData('resp.rt', resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials2'


# ------Prepare to start Routine "Interblock"-------
t = 0
InterblockClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(InterBlockTime+3.0)
# update component parameters for each repeat
# keep track of which components have finished
InterblockComponents = [textInterblock, text3A, text2A, text1A]
for thisComponent in InterblockComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Interblock"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InterblockClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterblock* updates
    if t >= 0.0 and textInterblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInterblock.tStart = t
        textInterblock.frameNStart = frameN  # exact frame index
        textInterblock.setAutoDraw(True)
    frameRemains = 0.0 + InterBlockTime- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textInterblock.status == STARTED and t >= frameRemains:
        textInterblock.setAutoDraw(False)
    
    # *text3A* updates
    if t >= InterBlockTime and text3A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text3A.tStart = t
        text3A.frameNStart = frameN  # exact frame index
        text3A.setAutoDraw(True)
    frameRemains = InterBlockTime + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text3A.status == STARTED and t >= frameRemains:
        text3A.setAutoDraw(False)
    
    # *text2A* updates
    if t >= InterBlockTime+1.0 and text2A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2A.tStart = t
        text2A.frameNStart = frameN  # exact frame index
        text2A.setAutoDraw(True)
    frameRemains = InterBlockTime+1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text2A.status == STARTED and t >= frameRemains:
        text2A.setAutoDraw(False)
    
    # *text1A* updates
    if t >= InterBlockTime+2.0 and text1A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1A.tStart = t
        text1A.frameNStart = frameN  # exact frame index
        text1A.setAutoDraw(True)
    frameRemains = InterBlockTime+2.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text1A.status == STARTED and t >= frameRemains:
        text1A.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InterblockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Interblock"-------
for thisComponent in InterblockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# ========================================================
## BLOCK 3
# set up handler to look after randomisation of conditions etc
Block = 3
print "Block = %d"%(Block)
print LoadList
CurrentLoad = LoadList[Block-1]
print "CurrentLoad = %d"%(CurrentLoad)
SelectionList = np.array(range(0,6,1)) + (CurrentLoad - 1)*6
print SelectionList

trials3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../DMSPsychopyFiles/DMSBlockListv2.csv', selection=SelectionList),
    seed=None, name='trials3')
    
thisExp.addLoop(trials3)  # add the loop to the experiment
thisTrials3 = trials3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
if thisTrials3 != None:
    for paramName in thisTrials3.keys():
        exec(paramName + '= thisTrials3.' + paramName)

for thisTrials3 in trials3:
    currentLoop = trials3
    # abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
    if thisTrials3 != None:
        for paramName in thisTrials3.keys():
            exec(paramName + '= thisTrials3.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(TotalTrialTime)
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + ITITime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textITI.status == STARTED and t >= frameRemains:
            textITI.setAutoDraw(False)
        
        # *textTL* updates
        if t >= ITITime and textTL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTL.tStart = t
            textTL.frameNStart = frameN  # exact frame index
            textTL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTL.status == STARTED and t >= frameRemains:
            textTL.setAutoDraw(False)
        
        # *textTM* updates
        if t >= ITITime and textTM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTM.tStart = t
            textTM.frameNStart = frameN  # exact frame index
            textTM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTM.status == STARTED and t >= frameRemains:
            textTM.setAutoDraw(False)
        
        # *textTR* updates
        if t >= ITITime and textTR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTR.tStart = t
            textTR.frameNStart = frameN  # exact frame index
            textTR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTR.status == STARTED and t >= frameRemains:
            textTR.setAutoDraw(False)
        
        # *textCL* updates
        if t >= ITITime and textCL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCL.tStart = t
            textCL.frameNStart = frameN  # exact frame index
            textCL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCL.status == STARTED and t >= frameRemains:
            textCL.setAutoDraw(False)
        
        # *textCM* updates
        if t >= ITITime and textCM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCM.tStart = t
            textCM.frameNStart = frameN  # exact frame index
            textCM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCM.status == STARTED and t >= frameRemains:
            textCM.setAutoDraw(False)
        
        # *textCR* updates
        if t >= ITITime and textCR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCR.tStart = t
            textCR.frameNStart = frameN  # exact frame index
            textCR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCR.status == STARTED and t >= frameRemains:
            textCR.setAutoDraw(False)
        
        # *textBL* updates
        if t >= ITITime and textBL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBL.tStart = t
            textBL.frameNStart = frameN  # exact frame index
            textBL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBL.status == STARTED and t >= frameRemains:
            textBL.setAutoDraw(False)
        
        # *textBM* updates
        if t >= ITITime and textBM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBM.tStart = t
            textBM.frameNStart = frameN  # exact frame index
            textBM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBM.status == STARTED and t >= frameRemains:
            textBM.setAutoDraw(False)
        
        # *textBR* updates
        if t >= ITITime and textBR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBR.tStart = t
            textBR.frameNStart = frameN  # exact frame index
            textBR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBR.status == STARTED and t >= frameRemains:
            textBR.setAutoDraw(False)
        
        # *textDelay* updates
        if t >=(ITITime+StimOnTime) and textDelay.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDelay.tStart = t
            textDelay.frameNStart = frameN  # exact frame index
            textDelay.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime) + RetOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textDelay.status == STARTED and t >= frameRemains:
            textDelay.setAutoDraw(False)
        
        # *textProbe* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and textProbe.status == NOT_STARTED:
            # keep track of start time/frame for later
            textProbe.tStart = t
            textProbe.frameNStart = frameN  # exact frame index
            textProbe.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textProbe.status == STARTED and t >= frameRemains:
            textProbe.setAutoDraw(False)
        
        # *resp* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
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
                # continueRoutine = False
        
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
    # store data for trials3 (TrialHandler)
    trials3.addData('resp.keys',resp.keys)
    trials3.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials3.addData('resp.rt', resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials3'


# ------Prepare to start Routine "Interblock"-------
t = 0
InterblockClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(InterBlockTime+3.0)
# update component parameters for each repeat
# keep track of which components have finished
InterblockComponents = [textInterblock, text3A, text2A, text1A]
for thisComponent in InterblockComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Interblock"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InterblockClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterblock* updates
    if t >= 0.0 and textInterblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInterblock.tStart = t
        textInterblock.frameNStart = frameN  # exact frame index
        textInterblock.setAutoDraw(True)
    frameRemains = 0.0 + InterBlockTime- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textInterblock.status == STARTED and t >= frameRemains:
        textInterblock.setAutoDraw(False)
    
    # *text3A* updates
    if t >= InterBlockTime and text3A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text3A.tStart = t
        text3A.frameNStart = frameN  # exact frame index
        text3A.setAutoDraw(True)
    frameRemains = InterBlockTime + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text3A.status == STARTED and t >= frameRemains:
        text3A.setAutoDraw(False)
    
    # *text2A* updates
    if t >= InterBlockTime+1.0 and text2A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2A.tStart = t
        text2A.frameNStart = frameN  # exact frame index
        text2A.setAutoDraw(True)
    frameRemains = InterBlockTime+1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text2A.status == STARTED and t >= frameRemains:
        text2A.setAutoDraw(False)
    
    # *text1A* updates
    if t >= InterBlockTime+2.0 and text1A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1A.tStart = t
        text1A.frameNStart = frameN  # exact frame index
        text1A.setAutoDraw(True)
    frameRemains = InterBlockTime+2.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text1A.status == STARTED and t >= frameRemains:
        text1A.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InterblockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Interblock"-------
for thisComponent in InterblockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# ========================================================
## BLOCK 4
# set up handler to look after randomisation of conditions etc
Block = 4
print "Block = %d"%(Block)
print LoadList
CurrentLoad = LoadList[Block-1]
print "CurrentLoad = %d"%(CurrentLoad)
SelectionList = np.array(range(0,6,1)) + (CurrentLoad - 1)*6
print SelectionList

trials4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../DMSPsychopyFiles/DMSBlockListv2.csv', selection=SelectionList),
    seed=None, name='trials4')
    
thisExp.addLoop(trials4)  # add the loop to the experiment
thisTrials4 = trials4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials4.rgb)
if thisTrials4 != None:
    for paramName in thisTrials4.keys():
        exec(paramName + '= thisTrials4.' + paramName)

for thisTrials4 in trials4:
    currentLoop = trials4
    # abbreviate parameter names if possible (e.g. rgb = thisTrials4.rgb)
    if thisTrials4 != None:
        for paramName in thisTrials4.keys():
            exec(paramName + '= thisTrials4.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(TotalTrialTime)
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + ITITime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textITI.status == STARTED and t >= frameRemains:
            textITI.setAutoDraw(False)
        
        # *textTL* updates
        if t >= ITITime and textTL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTL.tStart = t
            textTL.frameNStart = frameN  # exact frame index
            textTL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTL.status == STARTED and t >= frameRemains:
            textTL.setAutoDraw(False)
        
        # *textTM* updates
        if t >= ITITime and textTM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTM.tStart = t
            textTM.frameNStart = frameN  # exact frame index
            textTM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTM.status == STARTED and t >= frameRemains:
            textTM.setAutoDraw(False)
        
        # *textTR* updates
        if t >= ITITime and textTR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTR.tStart = t
            textTR.frameNStart = frameN  # exact frame index
            textTR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTR.status == STARTED and t >= frameRemains:
            textTR.setAutoDraw(False)
        
        # *textCL* updates
        if t >= ITITime and textCL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCL.tStart = t
            textCL.frameNStart = frameN  # exact frame index
            textCL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCL.status == STARTED and t >= frameRemains:
            textCL.setAutoDraw(False)
        
        # *textCM* updates
        if t >= ITITime and textCM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCM.tStart = t
            textCM.frameNStart = frameN  # exact frame index
            textCM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCM.status == STARTED and t >= frameRemains:
            textCM.setAutoDraw(False)
        
        # *textCR* updates
        if t >= ITITime and textCR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCR.tStart = t
            textCR.frameNStart = frameN  # exact frame index
            textCR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCR.status == STARTED and t >= frameRemains:
            textCR.setAutoDraw(False)
        
        # *textBL* updates
        if t >= ITITime and textBL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBL.tStart = t
            textBL.frameNStart = frameN  # exact frame index
            textBL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBL.status == STARTED and t >= frameRemains:
            textBL.setAutoDraw(False)
        
        # *textBM* updates
        if t >= ITITime and textBM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBM.tStart = t
            textBM.frameNStart = frameN  # exact frame index
            textBM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBM.status == STARTED and t >= frameRemains:
            textBM.setAutoDraw(False)
        
        # *textBR* updates
        if t >= ITITime and textBR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBR.tStart = t
            textBR.frameNStart = frameN  # exact frame index
            textBR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBR.status == STARTED and t >= frameRemains:
            textBR.setAutoDraw(False)
        
        # *textDelay* updates
        if t >=(ITITime+StimOnTime) and textDelay.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDelay.tStart = t
            textDelay.frameNStart = frameN  # exact frame index
            textDelay.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime) + RetOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textDelay.status == STARTED and t >= frameRemains:
            textDelay.setAutoDraw(False)
        
        # *textProbe* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and textProbe.status == NOT_STARTED:
            # keep track of start time/frame for later
            textProbe.tStart = t
            textProbe.frameNStart = frameN  # exact frame index
            textProbe.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textProbe.status == STARTED and t >= frameRemains:
            textProbe.setAutoDraw(False)
        
        # *resp* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
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
                # continueRoutine = False
        
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
    # store data for trials4 (TrialHandler)
    trials4.addData('resp.keys',resp.keys)
    trials4.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials4.addData('resp.rt', resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials4'


# ------Prepare to start Routine "Interblock"-------
t = 0
InterblockClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(InterBlockTime+3.0)
# update component parameters for each repeat
# keep track of which components have finished
InterblockComponents = [textInterblock, text3A, text2A, text1A]
for thisComponent in InterblockComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Interblock"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InterblockClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterblock* updates
    if t >= 0.0 and textInterblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInterblock.tStart = t
        textInterblock.frameNStart = frameN  # exact frame index
        textInterblock.setAutoDraw(True)
    frameRemains = 0.0 + InterBlockTime- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textInterblock.status == STARTED and t >= frameRemains:
        textInterblock.setAutoDraw(False)
    
    # *text3A* updates
    if t >= InterBlockTime and text3A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text3A.tStart = t
        text3A.frameNStart = frameN  # exact frame index
        text3A.setAutoDraw(True)
    frameRemains = InterBlockTime + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text3A.status == STARTED and t >= frameRemains:
        text3A.setAutoDraw(False)
    
    # *text2A* updates
    if t >= InterBlockTime+1.0 and text2A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2A.tStart = t
        text2A.frameNStart = frameN  # exact frame index
        text2A.setAutoDraw(True)
    frameRemains = InterBlockTime+1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text2A.status == STARTED and t >= frameRemains:
        text2A.setAutoDraw(False)
    
    # *text1A* updates
    if t >= InterBlockTime+2.0 and text1A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1A.tStart = t
        text1A.frameNStart = frameN  # exact frame index
        text1A.setAutoDraw(True)
    frameRemains = InterBlockTime+2.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text1A.status == STARTED and t >= frameRemains:
        text1A.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InterblockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Interblock"-------
for thisComponent in InterblockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# ========================================================
## BLOCK 5
# set up handler to look after randomisation of conditions etc
Block = 5
print "Block = %d"%(Block)
print LoadList
CurrentLoad = LoadList[Block-1]
print "CurrentLoad = %d"%(CurrentLoad)
SelectionList = np.array(range(0,6,1)) + (CurrentLoad - 1)*6
print SelectionList

trials5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../DMSPsychopyFiles/DMSBlockListv2.csv', selection=SelectionList),
    seed=None, name='trials5')
    
thisExp.addLoop(trials5)  # add the loop to the experiment
thisTrials5 = trials5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials5.rgb)
if thisTrials5 != None:
    for paramName in thisTrials5.keys():
        exec(paramName + '= thisTrials5.' + paramName)

for thisTrials5 in trials5:
    currentLoop = trials5
    # abbreviate parameter names if possible (e.g. rgb = thisTrials5.rgb)
    if thisTrials5 != None:
        for paramName in thisTrials5.keys():
            exec(paramName + '= thisTrials5.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(TotalTrialTime)
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + ITITime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textITI.status == STARTED and t >= frameRemains:
            textITI.setAutoDraw(False)
        
        # *textTL* updates
        if t >= ITITime and textTL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTL.tStart = t
            textTL.frameNStart = frameN  # exact frame index
            textTL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTL.status == STARTED and t >= frameRemains:
            textTL.setAutoDraw(False)
        
        # *textTM* updates
        if t >= ITITime and textTM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTM.tStart = t
            textTM.frameNStart = frameN  # exact frame index
            textTM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTM.status == STARTED and t >= frameRemains:
            textTM.setAutoDraw(False)
        
        # *textTR* updates
        if t >= ITITime and textTR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTR.tStart = t
            textTR.frameNStart = frameN  # exact frame index
            textTR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTR.status == STARTED and t >= frameRemains:
            textTR.setAutoDraw(False)
        
        # *textCL* updates
        if t >= ITITime and textCL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCL.tStart = t
            textCL.frameNStart = frameN  # exact frame index
            textCL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCL.status == STARTED and t >= frameRemains:
            textCL.setAutoDraw(False)
        
        # *textCM* updates
        if t >= ITITime and textCM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCM.tStart = t
            textCM.frameNStart = frameN  # exact frame index
            textCM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCM.status == STARTED and t >= frameRemains:
            textCM.setAutoDraw(False)
        
        # *textCR* updates
        if t >= ITITime and textCR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCR.tStart = t
            textCR.frameNStart = frameN  # exact frame index
            textCR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCR.status == STARTED and t >= frameRemains:
            textCR.setAutoDraw(False)
        
        # *textBL* updates
        if t >= ITITime and textBL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBL.tStart = t
            textBL.frameNStart = frameN  # exact frame index
            textBL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBL.status == STARTED and t >= frameRemains:
            textBL.setAutoDraw(False)
        
        # *textBM* updates
        if t >= ITITime and textBM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBM.tStart = t
            textBM.frameNStart = frameN  # exact frame index
            textBM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBM.status == STARTED and t >= frameRemains:
            textBM.setAutoDraw(False)
        
        # *textBR* updates
        if t >= ITITime and textBR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBR.tStart = t
            textBR.frameNStart = frameN  # exact frame index
            textBR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBR.status == STARTED and t >= frameRemains:
            textBR.setAutoDraw(False)
        
        # *textDelay* updates
        if t >=(ITITime+StimOnTime) and textDelay.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDelay.tStart = t
            textDelay.frameNStart = frameN  # exact frame index
            textDelay.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime) + RetOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textDelay.status == STARTED and t >= frameRemains:
            textDelay.setAutoDraw(False)
        
        # *textProbe* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and textProbe.status == NOT_STARTED:
            # keep track of start time/frame for later
            textProbe.tStart = t
            textProbe.frameNStart = frameN  # exact frame index
            textProbe.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textProbe.status == STARTED and t >= frameRemains:
            textProbe.setAutoDraw(False)
        
        # *resp* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
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
                # continueRoutine = False
        
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
    # store data for trials5 (TrialHandler)
    trials5.addData('resp.keys',resp.keys)
    trials5.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials5.addData('resp.rt', resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials5'


# ------Prepare to start Routine "Interblock"-------
t = 0
InterblockClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(InterBlockTime+3.0)
# update component parameters for each repeat
# keep track of which components have finished
InterblockComponents = [textInterblock, text3A, text2A, text1A]
for thisComponent in InterblockComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Interblock"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = InterblockClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInterblock* updates
    if t >= 0.0 and textInterblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInterblock.tStart = t
        textInterblock.frameNStart = frameN  # exact frame index
        textInterblock.setAutoDraw(True)
    frameRemains = 0.0 + InterBlockTime- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textInterblock.status == STARTED and t >= frameRemains:
        textInterblock.setAutoDraw(False)
    
    # *text3A* updates
    if t >= InterBlockTime and text3A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text3A.tStart = t
        text3A.frameNStart = frameN  # exact frame index
        text3A.setAutoDraw(True)
    frameRemains = InterBlockTime + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text3A.status == STARTED and t >= frameRemains:
        text3A.setAutoDraw(False)
    
    # *text2A* updates
    if t >= InterBlockTime+1.0 and text2A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2A.tStart = t
        text2A.frameNStart = frameN  # exact frame index
        text2A.setAutoDraw(True)
    frameRemains = InterBlockTime+1.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text2A.status == STARTED and t >= frameRemains:
        text2A.setAutoDraw(False)
    
    # *text1A* updates
    if t >= InterBlockTime+2.0 and text1A.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1A.tStart = t
        text1A.frameNStart = frameN  # exact frame index
        text1A.setAutoDraw(True)
    frameRemains = InterBlockTime+2.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text1A.status == STARTED and t >= frameRemains:
        text1A.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InterblockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Interblock"-------
for thisComponent in InterblockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
        
# ========================================================
## BLOCK 6
# set up handler to look after randomisation of conditions etc
Block = 6
print "Block = %d"%(Block)
print LoadList
CurrentLoad = LoadList[Block-1]
print "CurrentLoad = %d"%(CurrentLoad)
SelectionList = np.array(range(0,6,1)) + (CurrentLoad - 1)*6
print SelectionList

trials6 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('../DMSPsychopyFiles/DMSBlockListv2.csv', selection=SelectionList),
    seed=None, name='trials6')
    
thisExp.addLoop(trials6)  # add the loop to the experiment
thisTrials6 = trials6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials6.rgb)
if thisTrials6 != None:
    for paramName in thisTrials6.keys():
        exec(paramName + '= thisTrials6.' + paramName)

for thisTrials6 in trials6:
    currentLoop = trials6
    # abbreviate parameter names if possible (e.g. rgb = thisTrials6.rgb)
    if thisTrials6 != None:
        for paramName in thisTrials6.keys():
            exec(paramName + '= thisTrials6.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(TotalTrialTime)
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        frameRemains = 0.0 + ITITime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textITI.status == STARTED and t >= frameRemains:
            textITI.setAutoDraw(False)
        
        # *textTL* updates
        if t >= ITITime and textTL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTL.tStart = t
            textTL.frameNStart = frameN  # exact frame index
            textTL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTL.status == STARTED and t >= frameRemains:
            textTL.setAutoDraw(False)
        
        # *textTM* updates
        if t >= ITITime and textTM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTM.tStart = t
            textTM.frameNStart = frameN  # exact frame index
            textTM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTM.status == STARTED and t >= frameRemains:
            textTM.setAutoDraw(False)
        
        # *textTR* updates
        if t >= ITITime and textTR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textTR.tStart = t
            textTR.frameNStart = frameN  # exact frame index
            textTR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textTR.status == STARTED and t >= frameRemains:
            textTR.setAutoDraw(False)
        
        # *textCL* updates
        if t >= ITITime and textCL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCL.tStart = t
            textCL.frameNStart = frameN  # exact frame index
            textCL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCL.status == STARTED and t >= frameRemains:
            textCL.setAutoDraw(False)
        
        # *textCM* updates
        if t >= ITITime and textCM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCM.tStart = t
            textCM.frameNStart = frameN  # exact frame index
            textCM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCM.status == STARTED and t >= frameRemains:
            textCM.setAutoDraw(False)
        
        # *textCR* updates
        if t >= ITITime and textCR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textCR.tStart = t
            textCR.frameNStart = frameN  # exact frame index
            textCR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textCR.status == STARTED and t >= frameRemains:
            textCR.setAutoDraw(False)
        
        # *textBL* updates
        if t >= ITITime and textBL.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBL.tStart = t
            textBL.frameNStart = frameN  # exact frame index
            textBL.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBL.status == STARTED and t >= frameRemains:
            textBL.setAutoDraw(False)
        
        # *textBM* updates
        if t >= ITITime and textBM.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBM.tStart = t
            textBM.frameNStart = frameN  # exact frame index
            textBM.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBM.status == STARTED and t >= frameRemains:
            textBM.setAutoDraw(False)
        
        # *textBR* updates
        if t >= ITITime and textBR.status == NOT_STARTED:
            # keep track of start time/frame for later
            textBR.tStart = t
            textBR.frameNStart = frameN  # exact frame index
            textBR.setAutoDraw(True)
        frameRemains = ITITime + StimOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textBR.status == STARTED and t >= frameRemains:
            textBR.setAutoDraw(False)
        
        # *textDelay* updates
        if t >=(ITITime+StimOnTime) and textDelay.status == NOT_STARTED:
            # keep track of start time/frame for later
            textDelay.tStart = t
            textDelay.frameNStart = frameN  # exact frame index
            textDelay.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime) + RetOnTime- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textDelay.status == STARTED and t >= frameRemains:
            textDelay.setAutoDraw(False)
        
        # *textProbe* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and textProbe.status == NOT_STARTED:
            # keep track of start time/frame for later
            textProbe.tStart = t
            textProbe.frameNStart = frameN  # exact frame index
            textProbe.setAutoDraw(True)
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if textProbe.status == STARTED and t >= frameRemains:
            textProbe.setAutoDraw(False)
        
        # *resp* updates
        if t >= (ITITime+StimOnTime+RetOnTime) and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
        frameRemains = (ITITime+StimOnTime+RetOnTime) + (ProbeOnTime)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
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
                # continueRoutine = False
        
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
    # store data for trials6 (TrialHandler)
    trials6.addData('resp.keys',resp.keys)
    trials6.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials6.addData('resp.rt', resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials6'


# ------Prepare to start Routine "EndDelay"-------
t = 0
EndDelayClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndDelayComponents = [textEndDelay]
for thisComponent in EndDelayComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EndDelay"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndDelayClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndDelay* updates
    if t >= 0.0 and textEndDelay.status == NOT_STARTED:
        # keep track of start time/frame for later
        textEndDelay.tStart = t
        textEndDelay.frameNStart = frameN  # exact frame index
        textEndDelay.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if textEndDelay.status == STARTED and t >= frameRemains:
        textEndDelay.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndDelayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndDelay"-------
for thisComponent in EndDelayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Thankyou"-------
t = 0
ThankyouClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK2 = event.BuilderKeyResponse()
# keep track of which components have finished
ThankyouComponents = [textThankyou, OK2]
for thisComponent in ThankyouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thankyou"-------
while continueRoutine:
    # get current time
    t = ThankyouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textThankyou* updates
    if t >= 0.0 and textThankyou.status == NOT_STARTED:
        # keep track of start time/frame for later
        textThankyou.tStart = t
        textThankyou.frameNStart = frameN  # exact frame index
        textThankyou.setAutoDraw(True)
    
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
    for thisComponent in ThankyouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thankyou"-------
for thisComponent in ThankyouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Thankyou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
