#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on Fri Feb  1 13:40:41 2019
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
import csv
import pandas as pd
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)


# #################
# Store info about the experiment session
expName = u'SRT'  # from the Builder filename that created this script
task = 'Recog'
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
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
dataFile = open(filename+'.csv', 'w')#a simple text file with 'comma-separated-values'
dataFile.write('NRecognized, Word01, Word02, Word03, Word04, Word05, Word06, Word07, Word08, Word09, Word10, Word11, Word12, Word13, Word14, Word15, Word16, Word17, Word18, Word19, Word20\n')

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
#logFile = logging.LogFile(filename+'.log', level=logging.EXP)
#logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1900, 1200], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

GridWidth = 1240
GridHeight = 500
NVer = 6
NHor = 4
VerSpace = (GridHeight/2)/(NHor/2)
HorSpace = (GridWidth/2)/(NVer/2)
# plus to right
# neg is up
Row1 = VerSpace/2 + 2*VerSpace
Row2 = VerSpace/2 + VerSpace
Row3 = VerSpace/2
Row4 = -VerSpace/2
Row5 = -VerSpace/2 - VerSpace
Row6 = -VerSpace/2 - 2*VerSpace
Col1 = -HorSpace/2 - HorSpace
Col2 = -HorSpace/2
Col3 = HorSpace/2
Col4 = HorSpace/2 + HorSpace
FontSize = 30
WordColor = 'white'
SelectedColor = 'blue'
inputFile = '../SelectiveReminding/RecogWordList.csv'
trials = pd.read_csv(inputFile)
# Initialize components for Routine "trial"
trialClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
# Initialize components for Routine "thanks"
thanksClock = core.Clock()
InstrClock = core.Clock()
InstrTest = visual.TextStim(win=win, name='text',
    text=u'Select all of the words from the list with your mouse.\nOrder is not important.\n\nPress [return] to start and when you are done.',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=1000, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=0.0);

text = visual.TextStim(win=win, name='text',
    text=u'Thank You',
    font=u'Arial',
    units='pix', pos=(0, 0), height=45, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=0.0);

text1 = visual.TextStim(win=win, name='text1',
    text=trials['Word'][0],
    font=u'Arial',
    units='pix', pos=(Col1, Row1), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-1.0);

text2 = visual.TextStim(win=win, name='text2',
    text=trials['Word'][1],
    font=u'Arial',
    units='pix', pos=(Col2, Row1), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
text3 = visual.TextStim(win=win, name='text3',
    text=trials['Word'][2],
    font=u'Arial',
    units='pix', pos=(Col3, Row1), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
   
text4 = visual.TextStim(win=win, name='text4',
    text=trials['Word'][3],
    font=u'Arial',
    units='pix', pos=(Col4, Row1), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text5 = visual.TextStim(win=win, name='text5',
    text=trials['Word'][4],
    font=u'Arial',
    units='pix', pos=(Col1, Row2), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text6 = visual.TextStim(win=win, name='text6',
    text=trials['Word'][5],
    font=u'Arial',
    units='pix', pos=(Col2, Row2), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text7 = visual.TextStim(win=win, name='text7',
    text=trials['Word'][6],
    font=u'Arial',
    units='pix', pos=(Col3, Row2), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text8 = visual.TextStim(win=win, name='text8',
    text=trials['Word'][7],
    font=u'Arial',
    units='pix', pos=(Col4, Row2), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text9 = visual.TextStim(win=win, name='text9',
    text=trials['Word'][8],
    font=u'Arial',
    units='pix', pos=(Col1, Row3), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text10 = visual.TextStim(win=win, name='text10',
    text=trials['Word'][9],
    font=u'Arial',
    units='pix', pos=(Col2, Row3), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text11 = visual.TextStim(win=win, name='text11',
    text=trials['Word'][10],
    font=u'Arial',
    units='pix', pos=(Col3, Row3), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text12 = visual.TextStim(win=win, name='text12',
    text=trials['Word'][11],
    font=u'Arial',
    units='pix', pos=(Col4, Row3), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text13 = visual.TextStim(win=win, name='text13',
    text=trials['Word'][12],
    font=u'Arial',
    units='pix', pos=(Col1,Row4), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text14 = visual.TextStim(win=win, name='text14',
    text=trials['Word'][13],
    font=u'Arial',
    units='pix', pos=(Col2, Row4), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text15 = visual.TextStim(win=win, name='text15',
    text=trials['Word'][14],
    font=u'Arial',
    units='pix', pos=(Col3,Row4), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text16 = visual.TextStim(win=win, name='text16',
    text=trials['Word'][15],
    font=u'Arial',
    units='pix', pos=(Col4,Row4), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text17 = visual.TextStim(win=win, name='text17',
    text=trials['Word'][16],
    font=u'Arial',
    units='pix', pos=(Col1,Row5), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text18 = visual.TextStim(win=win, name='text18',
    text=trials['Word'][17],
    font=u'Arial',
    units='pix', pos=(Col2, Row5), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text19 = visual.TextStim(win=win, name='text19',
    text=trials['Word'][18],
    font=u'Arial',
    units='pix', pos=(Col3, Row5), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text20 = visual.TextStim(win=win, name='text20',
    text=trials['Word'][19],
    font=u'Arial',
    units='pix', pos=(Col4, Row5), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text21 = visual.TextStim(win=win, name='text21',
    text=trials['Word'][20],
    font=u'Arial',
    units='pix', pos=(Col1,Row6), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text22 = visual.TextStim(win=win, name='text22',
    text=trials['Word'][21],
    font=u'Arial',
    units='pix', pos=(Col2, Row6), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text23 = visual.TextStim(win=win, name='text23',
    text=trials['Word'][22],
    font=u'Arial',
    units='pix', pos=(Col3, Row6), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);
    
text24 = visual.TextStim(win=win, name='text24',
    text=trials['Word'][23],
    font=u'Arial',
    units='pix', pos=(Col4, Row6), height=FontSize, wrapWidth=None, ori=0, 
    color=WordColor, colorSpace='rgb', opacity=1,
    depth=-3.0);       
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


# ------Prepare to start Routine "Instr"-------
t = 0
InstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
InstrResp = event.BuilderKeyResponse()
# keep track of which components have finished
InstrComponents = [InstrTest, InstrResp]
for thisComponent in InstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instr"-------
while continueRoutine:
    # get current time
    t = InstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrTest* updates
    if t >= 0.0 and InstrTest.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrTest.tStart = t
        InstrTest.frameNStart = frameN  # exact frame index
        InstrTest.setAutoDraw(True)
    
    # *InstrResp* updates
    if t >= 0.0 and InstrResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrResp.tStart = t
        InstrResp.frameNStart = frameN  # exact frame index
        InstrResp.status = STARTED
        # keyboard checking is just starting
    if InstrResp.status == STARTED:
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
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr"-------
for thisComponent in InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
mouse.clicked_text = []
gotValidClick = False  # until a click is received

key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
trialComponents = [mouse, text1, text2, key_resp_2]
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------

CorrectRecog = 0
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
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
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(trialClock.getTime())
                # check if the mouse was inside our 'clickable' objects
                for obj in [text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20]:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_text.append(obj.text)
                # HERE is where accuracy is assessed
                for obj in [text3,text5,text6,text7,text14, text15, text16, text17, text18, text22, text23, text24]:
                    if obj.contains(mouse):
                        CorrectRecog += 1
    # *text1* updates
    if t >= 0.0 and text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1.tStart = t
        text1.frameNStart = frameN  # exact frame index
        text1.setAutoDraw(True)
    # *text2* updates
    if t >= 0.0 and text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text2.tStart = t
        text2.frameNStart = frameN  # exact frame index
        text2.setAutoDraw(True)
     # *text2* updates
    if t >= 0.0 and text3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text3.tStart = t
        text3.frameNStart = frameN  # exact frame index
        text3.setAutoDraw(True)
    # *text2* updates
    if t >= 0.0 and text4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text4.tStart = t
        text4.frameNStart = frameN  # exact frame index
        text4.setAutoDraw(True)
    # *text2* updates
    if t >= 0.0 and text5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text5.tStart = t
        text5.frameNStart = frameN  # exact frame index
        text5.setAutoDraw(True)           # *text2* updates
    if t >= 0.0 and text6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text6.tStart = t
        text6.frameNStart = frameN  # exact frame index
        text6.setAutoDraw(True)  
            # *text2* updates
    if t >= 0.0 and text7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text7.tStart = t
        text7.frameNStart = frameN  # exact frame index
        text7.setAutoDraw(True)  
            # *text2* updates
    if t >= 0.0 and text8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text8.tStart = t
        text8.frameNStart = frameN  # exact frame index
        text8.setAutoDraw(True)  
            # *text2* updates
    if t >= 0.0 and text9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text9.tStart = t
        text9.frameNStart = frameN  # exact frame index
        text9.setAutoDraw(True)  
    if t >= 0.0 and text10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text10.tStart = t
        text10.frameNStart = frameN  # exact frame index
        text10.setAutoDraw(True)      
    if t >= 0.0 and text11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text11.tStart = t
        text11.frameNStart = frameN  # exact frame index
        text11.setAutoDraw(True)      
    if t >= 0.0 and text12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text12.tStart = t
        text12.frameNStart = frameN  # exact frame index
        text12.setAutoDraw(True)          
    if t >= 0.0 and text13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text13.tStart = t
        text13.frameNStart = frameN  # exact frame index
        text13.setAutoDraw(True)      
    if t >= 0.0 and text14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text14.tStart = t
        text14.frameNStart = frameN  # exact frame index
        text14.setAutoDraw(True)      
    if t >= 0.0 and text15.status == NOT_STARTED:
        # keep track of start time/frame for later
        text15.tStart = t
        text15.frameNStart = frameN  # exact frame index
        text15.setAutoDraw(True)           
    if t >= 0.0 and text16.status == NOT_STARTED:
        # keep track of start time/frame for later
        text16.tStart = t
        text16.frameNStart = frameN  # exact frame index
        text16.setAutoDraw(True)      
    if t >= 0.0 and text17.status == NOT_STARTED:
        # keep track of start time/frame for later
        text17.tStart = t
        text17.frameNStart = frameN  # exact frame index
        text17.setAutoDraw(True)          
    if t >= 0.0 and text18.status == NOT_STARTED:
        # keep track of start time/frame for later
        text18.tStart = t
        text18.frameNStart = frameN  # exact frame index
        text18.setAutoDraw(True)      
    if t >= 0.0 and text19.status == NOT_STARTED:
        # keep track of start time/frame for later
        text19.tStart = t
        text19.frameNStart = frameN  # exact frame index
        text19.setAutoDraw(True)      
    if t >= 0.0 and text20.status == NOT_STARTED:
        # keep track of start time/frame for later
        text20.tStart = t
        text20.frameNStart = frameN  # exact frame index
        text20.setAutoDraw(True)      
    if t >= 0.0 and text21.status == NOT_STARTED:
        # keep track of start time/frame for later
        text21.tStart = t
        text21.frameNStart = frameN  # exact frame index
        text21.setAutoDraw(True)          
    if t >= 0.0 and text22.status == NOT_STARTED:
        # keep track of start time/frame for later
        text22.tStart = t
        text22.frameNStart = frameN  # exact frame index
        text22.setAutoDraw(True)      
    if t >= 0.0 and text23.status == NOT_STARTED:
        # keep track of start time/frame for later
        text23.tStart = t
        text23.frameNStart = frameN  # exact frame index
        text23.setAutoDraw(True)      
    if t >= 0.0 and text24.status == NOT_STARTED:
        # keep track of start time/frame for later
        text24.tStart = t
        text24.frameNStart = frameN  # exact frame index
        text24.setAutoDraw(True)    
    
    
    if mouse.isPressedIn(text1):
        text1.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text2):
        text2.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text3):
        text3.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text4):
        text4.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text5):
        text5.setColor(SelectedColor, 'rgb255')        
    if mouse.isPressedIn(text6):
        text6.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text7):
        text7.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text8):
        text8.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text9):
        text9.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text10):
        text10.setColor(SelectedColor, 'rgb255')   
    if mouse.isPressedIn(text11):
        text11.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text12):
        text12.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text13):
        text13.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text14):
        text14.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text15):
        text15.setColor(SelectedColor, 'rgb255')     
    if mouse.isPressedIn(text16):
        text16.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text17):
        text17.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text18):
        text18.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text19):
        text19.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text20):
        text20.setColor(SelectedColor, 'rgb255')     
    if mouse.isPressedIn(text21):
        text21.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text22):
        text22.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text23):
        text23.setColor(SelectedColor, 'rgb255')
    if mouse.isPressedIn(text24):
        text24.setColor(SelectedColor, 'rgb255')  
# *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
    if key_resp_2.status == STARTED:
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
        
print(mouse.clicked_text)
print(CorrectRecog)
dataFile.write('%d,'%(CorrectRecog))
for i in mouse.clicked_text:
    dataFile.write('%s,'%(i))
dataFile.write('\n')
dataFile.close()
# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)

thisExp.nextEntry()

# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
text1.setAutoDraw(False) 
text2.setAutoDraw(False) 
text3.setAutoDraw(False) 
text4.setAutoDraw(False) 
text5.setAutoDraw(False) 
text6.setAutoDraw(False) 
text7.setAutoDraw(False) 
text8.setAutoDraw(False) 
text9.setAutoDraw(False) 
text10.setAutoDraw(False) 
text11.setAutoDraw(False) 
text12.setAutoDraw(False) 
text13.setAutoDraw(False) 
text14.setAutoDraw(False) 
text15.setAutoDraw(False) 
text16.setAutoDraw(False) 
text17.setAutoDraw(False) 
text18.setAutoDraw(False) 
text19.setAutoDraw(False) 
text20.setAutoDraw(False) 
text21.setAutoDraw(False) 
text22.setAutoDraw(False) 
text23.setAutoDraw(False) 
text24.setAutoDraw(False) 
# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
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
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# these shouldn't be strictly necessary (should auto-save)
#thisExp.saveAsWideText(filename+'.csv')
#thisExp.saveAsPickle(filename)
#logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
