#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Thu Jul 27 10:18:04 2017
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
expName = 'FRTDemo1'  # from the Builder filename that created this script
expInfo = {u'session': u'2', u'Participant ID': u''}
PartDataFolder = 'unorganized'
if len(sys.argv) > 1:
    expInfo['Participant ID'] = sys.argv[1]
    PartDataFolder = sys.argv[1]
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp


# import parameters from a config file
sys.path.append(os.path.join(_thisDir, '..','ConfigFiles'))
from BehavioralDataFolder import *

FontSizeUnits = 'pix'
FontSize = 40


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s_%s' % (expName, expInfo['Participant ID'], expInfo['date'])
#OutDir = '..' + os.sep + '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
DropBoxFolder = BehavioralDataFolder
#os.path.join('/Users','jasonsteffener','Dropbox','steffenercolumbia','Projects','MyProjects','NeuralCognitiveMapping')
# OutDir = '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
OutDir = os.path.join(DropBoxFolder, 'data',PartDataFolder)

filename = OutDir + os.sep+'%s_%s_%s' % (expName, expInfo['Participant ID'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=os.path.join(_thisDir, 'FRTDemo.psyexp'),
    savePickle=False, saveWideText=True,
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
    text='In this experiment you will be presented with a pair of faces. \n\nYou will have to decide whether these faces are from the same person or different people. \n\nWhen you are ready to proceed press any key.',
    font='Times New Roman',
    units='pix', pos=[0, 0], height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "practInstruct2"
practInstruct2Clock = core.Clock()
textInstr2 = visual.TextStim(win=win, name='textInstr2',
    text='For example;\nThese two faces are from the SAME PERSON',
    font='Times New Roman',
    units='pix', pos=(-256, 192), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
textInstr3 = visual.TextStim(win=win, name='textInstr3',
    text='These next two faces are from DIFFERENT PEOPLE',
    font='Times New Roman',
    units='pix', pos=(-256, -140), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
textInstr4 = visual.TextStim(win=win, name='textInstr4',
    text='When you are ready to proceed press any key.',
    font='Times New Roman',
    units='pix', pos=(-256, -350), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
image1 = visual.ImageStim(
    win=win, name='image1',units='pix', 
    image='FRTFaces/cropAF31NEHR.JPG', mask=None,
    ori=0, pos=(128, 192), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image2 = visual.ImageStim(
    win=win, name='image2',units='pix', 
    image='FRTFaces/cropAF31NEHL.JPG', mask=None,
    ori=0, pos=(384, 192), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image3 = visual.ImageStim(
    win=win, name='image3',units='pix', 
    image='FRTFaces/cropAF31NEHR.JPG', mask=None,
    ori=0, pos=(128, -140), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image4 = visual.ImageStim(
    win=win, name='image4',units='pix', 
    image='FRTFaces/cropAF35NEHL.JPG', mask=None,
    ori=0, pos=(384, -140), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "practInstruct3"
practInstruct3Clock = core.Clock()
textInstr5 = visual.TextStim(win=win, name='textInstr5',
    text='Faces will be degraded to varying levels. \n\nDo not worry if you cannot distinguish certain faces, just try your best!\n\nWhen you are ready to proceed press any key.',
    font='Times New Roman',
    units='pix', pos=(-256, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
image1A = visual.ImageStim(
    win=win, name='image1A',units='pix', 
    image='FRTFaces/cropAF35NEHL.JPG', mask=None,
    ori=0, pos=(128, 192), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=0.9,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image1An = visual.ImageStim(
    win=win, name='image1An',units='pix', 
    image='FRTFaces/noisecropAF35NEHL.JPG', mask=None,
    ori=0, pos=(128, 192), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=0.1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image2A = visual.ImageStim(
    win=win, name='image2A',units='pix', 
    image='FRTFaces/cropAF35NEHL.JPG', mask=None,
    ori=0, pos=(384, 192), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=0.7,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image2An = visual.ImageStim(
    win=win, name='image2An',units='pix', 
    image='FRTFaces/noisecropAF35NEHL.JPG', mask=None,
    ori=0, pos=(384, 192), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=0.3,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image3A = visual.ImageStim(
    win=win, name='image3A',units='pix', 
    image='FRTFaces/cropAF35NEHL.JPG', mask=None,
    ori=0, pos=(128, -140), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=0.6,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image3An = visual.ImageStim(
    win=win, name='image3An',units='pix', 
    image='FRTFaces/noisecropAF35NEHL.JPG', mask=None,
    ori=0, pos=(128, -140), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=0.4,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
image4A = visual.ImageStim(
    win=win, name='image4A',units='pix', 
    image='FRTFaces/cropAF35NEHL.JPG', mask=None,
    ori=0, pos=(384, -140), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
image4An = visual.ImageStim(
    win=win, name='image4An',units='pix', 
    image='FRTFaces/noisecropAF35NEHL.JPG', mask=None,
    ori=0, pos=(384, -140), size=(230, 268),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "practInstruct4"
practInstruct4Clock = core.Clock()
textInstr6 = visual.TextStim(win=win, name='textInstr6',
    text='Respond with the keys:\n[LEFT] if the two faces are from the SAME PERSON\n[RIGHT] if the two faces are from DIFFERENT PEOPLE\n\nThere will be a number of practice trials in which you will be given feedback.  Try to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.\n',
    font='Times New Roman',
    units='pix', pos=(0, 0), height=40, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
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
    units='pix', pos=[0, 0], height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
imageLEFT = visual.ImageStim(
    win=win, name='imageLEFT',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-175, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
imageRIGHT = visual.ImageStim(
    win=win, name='imageRIGHT',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(175, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
imageLEFTnoise = visual.ImageStim(
    win=win, name='imageLEFTnoise',
    image='sin', mask=None,
    ori=0, pos=(-175, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
imageRIGHTnoise = visual.ImageStim(
    win=win, name='imageRIGHTnoise',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(175, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
textFeedback = visual.TextStim(win=win, name='textFeedback',
    text='default text',
    font='Times New Roman',
    units='pix', pos=[0, 0], height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "mainInstruct1"
mainInstruct1Clock = core.Clock()
textInstr7 = visual.TextStim(win=win, name='textInstr7',
    text='OK, ready to start the main experiment?\n\nRemember:\nPress [LEFT] for the SAME person\nPress [RIGHT] for DIFFERENT people\n\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font='Times New Roman',
    units='pix', pos=[0, 0], height=40, wrapWidth=1000, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "mainInstruct2"
mainInstruct2Clock = core.Clock()
textInstr8 = visual.TextStim(win=win, name='textInstr8',
    text='Remember;\nFaces will be degraded to varying levels.',
    font='Times New Roman',
    units='pix', pos=(-256, -300), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
image1B = visual.ImageStim(
    win=win, name='image1B',units='pix', 
    image='FRTFaces/cropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.9,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image1Bn = visual.ImageStim(
    win=win, name='image1Bn',units='pix', 
    image='FRTFaces/noisecropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image2B = visual.ImageStim(
    win=win, name='image2B',units='pix', 
    image='FRTFaces/cropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.8,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image2Bn = visual.ImageStim(
    win=win, name='image2Bn',units='pix', 
    image='FRTFaces/noisecropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.2,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image3B = visual.ImageStim(
    win=win, name='image3B',units='pix', 
    image='FRTFaces/cropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.7,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image3Bn = visual.ImageStim(
    win=win, name='image3Bn',units='pix', 
    image='FRTFaces/noisecropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.3,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
image4B = visual.ImageStim(
    win=win, name='image4B',units='pix', 
    image='FRTFaces/cropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.6,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
image4Bn = visual.ImageStim(
    win=win, name='image4Bn',units='pix', 
    image='FRTFaces/noisecropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.4,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
image5B = visual.ImageStim(
    win=win, name='image5B',units='pix', 
    image='FRTFaces/cropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
image5Bn = visual.ImageStim(
    win=win, name='image5Bn',units='pix', 
    image='FRTFaces/noisecropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
image6B = visual.ImageStim(
    win=win, name='image6B',units='pix', 
    image='FRTFaces/cropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.4,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
image6Bn = visual.ImageStim(
    win=win, name='image6Bn',units='pix', 
    image='FRTFaces/noisecropAF31NEHL.JPG', mask=None,
    ori=0, pos=(0, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=0.6,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
textInstr9 = visual.TextStim(win=win, name='textInstr9',
    text='When you are ready to proceed press any key.',
    font='Times New Roman',
    units='pix', pos=(256, -300), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);

textThankyou = visual.TextStim(win=win, name='textThankyou',
    text='Thank you for participating!',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
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
practInstruct1Components = [textInstr1, OK1]
for thisComponent in practInstruct1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practInstruct1"-------
while continueRoutine:
    # get current time
    t = practInstruct1Clock.getTime()
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
    for thisComponent in practInstruct1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practInstruct1"-------
for thisComponent in practInstruct1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practInstruct1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practInstruct2"-------
t = 0
practInstruct2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK2 = event.BuilderKeyResponse()
# keep track of which components have finished
practInstruct2Components = [textInstr2, textInstr3, textInstr4, image1, image2, image3, image4, OK2]
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
    
    # *textInstr3* updates
    if t >= 0.0 and textInstr3.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInstr3.tStart = t
        textInstr3.frameNStart = frameN  # exact frame index
        textInstr3.setAutoDraw(True)
    
    # *textInstr4* updates
    if t >= 0.0 and textInstr4.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInstr4.tStart = t
        textInstr4.frameNStart = frameN  # exact frame index
        textInstr4.setAutoDraw(True)
    
    # *image1* updates
    if t >= 0.0 and image1.status == NOT_STARTED:
        # keep track of start time/frame for later
        image1.tStart = t
        image1.frameNStart = frameN  # exact frame index
        image1.setAutoDraw(True)
    
    # *image2* updates
    if t >= 0.0 and image2.status == NOT_STARTED:
        # keep track of start time/frame for later
        image2.tStart = t
        image2.frameNStart = frameN  # exact frame index
        image2.setAutoDraw(True)
    
    # *image3* updates
    if t >= 0.0 and image3.status == NOT_STARTED:
        # keep track of start time/frame for later
        image3.tStart = t
        image3.frameNStart = frameN  # exact frame index
        image3.setAutoDraw(True)
    
    # *image4* updates
    if t >= 0.0 and image4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image4.tStart = t
        image4.frameNStart = frameN  # exact frame index
        image4.setAutoDraw(True)
    
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

# ------Prepare to start Routine "practInstruct3"-------
t = 0
practInstruct3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK3 = event.BuilderKeyResponse()
# keep track of which components have finished
practInstruct3Components = [textInstr5, image1A, image1An, image2A, image2An, image3A, image3An, image4A, image4An, OK3]
for thisComponent in practInstruct3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practInstruct3"-------
while continueRoutine:
    # get current time
    t = practInstruct3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInstr5* updates
    if t >= 0.0 and textInstr5.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInstr5.tStart = t
        textInstr5.frameNStart = frameN  # exact frame index
        textInstr5.setAutoDraw(True)
    
    # *image1A* updates
    if t >= 0.0 and image1A.status == NOT_STARTED:
        # keep track of start time/frame for later
        image1A.tStart = t
        image1A.frameNStart = frameN  # exact frame index
        image1A.setAutoDraw(True)
    
    # *image1An* updates
    if t >= 0.0 and image1An.status == NOT_STARTED:
        # keep track of start time/frame for later
        image1An.tStart = t
        image1An.frameNStart = frameN  # exact frame index
        image1An.setAutoDraw(True)
    
    # *image2A* updates
    if t >= 0.0 and image2A.status == NOT_STARTED:
        # keep track of start time/frame for later
        image2A.tStart = t
        image2A.frameNStart = frameN  # exact frame index
        image2A.setAutoDraw(True)
    
    # *image2An* updates
    if t >= 0.0 and image2An.status == NOT_STARTED:
        # keep track of start time/frame for later
        image2An.tStart = t
        image2An.frameNStart = frameN  # exact frame index
        image2An.setAutoDraw(True)
    
    # *image3A* updates
    if t >= 0.0 and image3A.status == NOT_STARTED:
        # keep track of start time/frame for later
        image3A.tStart = t
        image3A.frameNStart = frameN  # exact frame index
        image3A.setAutoDraw(True)
    
    # *image3An* updates
    if t >= 0.0 and image3An.status == NOT_STARTED:
        # keep track of start time/frame for later
        image3An.tStart = t
        image3An.frameNStart = frameN  # exact frame index
        image3An.setAutoDraw(True)
    
    # *image4A* updates
    if t >= 0.0 and image4A.status == NOT_STARTED:
        # keep track of start time/frame for later
        image4A.tStart = t
        image4A.frameNStart = frameN  # exact frame index
        image4A.setAutoDraw(True)
    
    # *image4An* updates
    if t >= 0.0 and image4An.status == NOT_STARTED:
        # keep track of start time/frame for later
        image4An.tStart = t
        image4An.frameNStart = frameN  # exact frame index
        image4An.setAutoDraw(True)
    
    # *OK3* updates
    if t >= 0.0 and OK3.status == NOT_STARTED:
        # keep track of start time/frame for later
        OK3.tStart = t
        OK3.frameNStart = frameN  # exact frame index
        OK3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if OK3.status == STARTED:
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
    for thisComponent in practInstruct3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practInstruct3"-------
for thisComponent in practInstruct3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practInstruct3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practInstruct4"-------
t = 0
practInstruct4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK4 = event.BuilderKeyResponse()
# keep track of which components have finished
practInstruct4Components = [textInstr6, OK4]
for thisComponent in practInstruct4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practInstruct4"-------
while continueRoutine:
    # get current time
    t = practInstruct4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInstr6* updates
    if t >= 0.0 and textInstr6.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInstr6.tStart = t
        textInstr6.frameNStart = frameN  # exact frame index
        textInstr6.setAutoDraw(True)
    
    # *OK4* updates
    if t >= 0.0 and OK4.status == NOT_STARTED:
        # keep track of start time/frame for later
        OK4.tStart = t
        OK4.frameNStart = frameN  # exact frame index
        OK4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if OK4.status == STARTED:
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
    for thisComponent in practInstruct4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practInstruct4"-------
for thisComponent in practInstruct4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practInstruct4" was not non-slip safe, so reset the non-slip timer
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
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('FRTFileDemo.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec('{} = thisTrial[paramName]'.format(paramName))
        
for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            #exec(paramName + '= thisTrial.' + paramName)
            exec('{} = thisTrial[paramName]'.format(paramName))
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    imageLEFT.setOpacity(imageLop)
    imageLEFT.setImage(imageL)
    imageRIGHT.setOpacity(imageRop)
    imageRIGHT.setImage(imageR)
    imageLEFTnoise.setOpacity(imageLnop)
    imageLEFTnoise.setImage(imageLn)
    imageRIGHTnoise.setOpacity(imageRnop)
    imageRIGHTnoise.setImage(imageRn)
    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [textITI, imageLEFT, imageRIGHT, imageLEFTnoise, imageRIGHTnoise, resp]
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
        
        # *imageLEFT* updates
        if t >= 0.5 and imageLEFT.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageLEFT.tStart = t
            imageLEFT.frameNStart = frameN  # exact frame index
            imageLEFT.setAutoDraw(True)
        
        # *imageRIGHT* updates
        if t >= 0.5 and imageRIGHT.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageRIGHT.tStart = t
            imageRIGHT.frameNStart = frameN  # exact frame index
            imageRIGHT.setAutoDraw(True)
        
        # *imageLEFTnoise* updates
        if t >= 0.5 and imageLEFTnoise.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageLEFTnoise.tStart = t
            imageLEFTnoise.frameNStart = frameN  # exact frame index
            imageLEFTnoise.setAutoDraw(True)
        
        # *imageRIGHTnoise* updates
        if t >= 0.5 and imageRIGHTnoise.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageRIGHTnoise.tStart = t
            imageRIGHTnoise.frameNStart = frameN  # exact frame index
            imageRIGHTnoise.setAutoDraw(True)
        
        # *resp* updates
        if t >= 0.5 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
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
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
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
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
#trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
#    stimOut=params,
#    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "mainInstruct1"-------
t = 0
mainInstruct1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK5 = event.BuilderKeyResponse()
# keep track of which components have finished
mainInstruct1Components = [textInstr7, OK5]
for thisComponent in mainInstruct1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mainInstruct1"-------
while continueRoutine:
    # get current time
    t = mainInstruct1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInstr7* updates
    if t >= 0.0 and textInstr7.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInstr7.tStart = t
        textInstr7.frameNStart = frameN  # exact frame index
        textInstr7.setAutoDraw(True)
    
    # *OK5* updates
    if t >= 0.0 and OK5.status == NOT_STARTED:
        # keep track of start time/frame for later
        OK5.tStart = t
        OK5.frameNStart = frameN  # exact frame index
        OK5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if OK5.status == STARTED:
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
    for thisComponent in mainInstruct1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mainInstruct1"-------
for thisComponent in mainInstruct1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "mainInstruct1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mainInstruct2"-------
t = 0
mainInstruct2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
OK6 = event.BuilderKeyResponse()
# keep track of which components have finished
mainInstruct2Components = [textInstr8, image1B, image1Bn, image2B, image2Bn, image3B, image3Bn, image4B, image4Bn, image5B, image5Bn, image6B, image6Bn, textInstr9, OK6]
for thisComponent in mainInstruct2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mainInstruct2"-------
while continueRoutine:
    # get current time
    t = mainInstruct2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInstr8* updates
    if t >= 0 and textInstr8.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInstr8.tStart = t
        textInstr8.frameNStart = frameN  # exact frame index
        textInstr8.setAutoDraw(True)
    
    # *image1B* updates
    if t >= 0.0 and image1B.status == NOT_STARTED:
        # keep track of start time/frame for later
        image1B.tStart = t
        image1B.frameNStart = frameN  # exact frame index
        image1B.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image1B.status == STARTED and t >= frameRemains:
        image1B.setAutoDraw(False)
    
    # *image1Bn* updates
    if t >= 0.0 and image1Bn.status == NOT_STARTED:
        # keep track of start time/frame for later
        image1Bn.tStart = t
        image1Bn.frameNStart = frameN  # exact frame index
        image1Bn.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image1Bn.status == STARTED and t >= frameRemains:
        image1Bn.setAutoDraw(False)
    
    # *image2B* updates
    if t >= 0.5 and image2B.status == NOT_STARTED:
        # keep track of start time/frame for later
        image2B.tStart = t
        image2B.frameNStart = frameN  # exact frame index
        image2B.setAutoDraw(True)
    frameRemains = 0.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image2B.status == STARTED and t >= frameRemains:
        image2B.setAutoDraw(False)
    
    # *image2Bn* updates
    if t >= 0.5 and image2Bn.status == NOT_STARTED:
        # keep track of start time/frame for later
        image2Bn.tStart = t
        image2Bn.frameNStart = frameN  # exact frame index
        image2Bn.setAutoDraw(True)
    frameRemains = 0.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image2Bn.status == STARTED and t >= frameRemains:
        image2Bn.setAutoDraw(False)
    
    # *image3B* updates
    if t >= 1.0 and image3B.status == NOT_STARTED:
        # keep track of start time/frame for later
        image3B.tStart = t
        image3B.frameNStart = frameN  # exact frame index
        image3B.setAutoDraw(True)
    frameRemains = 1.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image3B.status == STARTED and t >= frameRemains:
        image3B.setAutoDraw(False)
    
    # *image3Bn* updates
    if t >= 1.0 and image3Bn.status == NOT_STARTED:
        # keep track of start time/frame for later
        image3Bn.tStart = t
        image3Bn.frameNStart = frameN  # exact frame index
        image3Bn.setAutoDraw(True)
    frameRemains = 1.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image3Bn.status == STARTED and t >= frameRemains:
        image3Bn.setAutoDraw(False)
    
    # *image4B* updates
    if t >= 1.5 and image4B.status == NOT_STARTED:
        # keep track of start time/frame for later
        image4B.tStart = t
        image4B.frameNStart = frameN  # exact frame index
        image4B.setAutoDraw(True)
    frameRemains = 1.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image4B.status == STARTED and t >= frameRemains:
        image4B.setAutoDraw(False)
    
    # *image4Bn* updates
    if t >= 1.5 and image4Bn.status == NOT_STARTED:
        # keep track of start time/frame for later
        image4Bn.tStart = t
        image4Bn.frameNStart = frameN  # exact frame index
        image4Bn.setAutoDraw(True)
    frameRemains = 1.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image4Bn.status == STARTED and t >= frameRemains:
        image4Bn.setAutoDraw(False)
    
    # *image5B* updates
    if t >= 2.0 and image5B.status == NOT_STARTED:
        # keep track of start time/frame for later
        image5B.tStart = t
        image5B.frameNStart = frameN  # exact frame index
        image5B.setAutoDraw(True)
    frameRemains = 2.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image5B.status == STARTED and t >= frameRemains:
        image5B.setAutoDraw(False)
    
    # *image5Bn* updates
    if t >= 2.0 and image5Bn.status == NOT_STARTED:
        # keep track of start time/frame for later
        image5Bn.tStart = t
        image5Bn.frameNStart = frameN  # exact frame index
        image5Bn.setAutoDraw(True)
    frameRemains = 2.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image5Bn.status == STARTED and t >= frameRemains:
        image5Bn.setAutoDraw(False)
    
    # *image6B* updates
    if t >= 2.5 and image6B.status == NOT_STARTED:
        # keep track of start time/frame for later
        image6B.tStart = t
        image6B.frameNStart = frameN  # exact frame index
        image6B.setAutoDraw(True)
    
    # *image6Bn* updates
    if t >= 2.5 and image6Bn.status == NOT_STARTED:
        # keep track of start time/frame for later
        image6Bn.tStart = t
        image6Bn.frameNStart = frameN  # exact frame index
        image6Bn.setAutoDraw(True)
    
    # *textInstr9* updates
    if t >= 2.5 and textInstr9.status == NOT_STARTED:
        # keep track of start time/frame for later
        textInstr9.tStart = t
        textInstr9.frameNStart = frameN  # exact frame index
        textInstr9.setAutoDraw(True)
    
    # *OK6* updates
    if t >= 2.5 and OK6.status == NOT_STARTED:
        # keep track of start time/frame for later
        OK6.tStart = t
        OK6.frameNStart = frameN  # exact frame index
        OK6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if OK6.status == STARTED:
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
    for thisComponent in mainInstruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mainInstruct2"-------
for thisComponent in mainInstruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "mainInstruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# Thank you
textThankyou.setAutoDraw(True)
countDown.add(5)
win.flip()
while countDown.getTime() > 0:
    pass   
win.flip()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
#thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
