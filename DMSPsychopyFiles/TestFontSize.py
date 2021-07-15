
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

if len(sys.argv) > 1:
    FontSize= int(sys.argv[1])
else:
    FontSize = 100

FontSizeUnits = 'pix'
SpacingOfLettersRelativeToCenter = FontSize*1.33
# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=False, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units=FontSizeUnits)

textTL = visual.TextStim(win=win, name='textTL',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(-SpacingOfLettersRelativeToCenter, SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
textTM = visual.TextStim(win=win, name='textTM',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
textTR = visual.TextStim(win=win, name='textTR',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(SpacingOfLettersRelativeToCenter, SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
textCL = visual.TextStim(win=win, name='textCL',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(-SpacingOfLettersRelativeToCenter, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
textCM = visual.TextStim(win=win, name='textCM',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
textCR = visual.TextStim(win=win, name='textCR',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(SpacingOfLettersRelativeToCenter, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
textBL = visual.TextStim(win=win, name='textBL',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(-SpacingOfLettersRelativeToCenter, -SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
textBM = visual.TextStim(win=win, name='textBM',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, -SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
textBR = visual.TextStim(win=win, name='textBR',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(SpacingOfLettersRelativeToCenter, -SpacingOfLettersRelativeToCenter), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);


def MapLettersToScreen(Stim):
    NLet = len(Stim)
    if NLet == 1:
        Output = '****'+Stim+'****'
    elif NLet == 2:
        Output = '***'+Stim[0]+'*'+Stim[1]+'***'
    elif NLet == 3:
        Output = '***'+Stim+'***'
    elif NLet == 4:
        Output = Stim[0]+'*'+Stim[1]+'***'+Stim[2]+'*'+Stim[3]
    elif NLet == 5:
        Output = Stim[0]+'*'+Stim[1]+'*'+Stim[2]+'*'+Stim[3]+'*'+Stim[4]
    elif NLet == 6:
        Output = Stim[0:3]+'***'+Stim[3:6]
    elif NLet == 7:
        Output = Stim[0:3]+'*'+Stim[3]+'*'+Stim[4:7]
    elif NLet == 8:
        Output = Stim[0:4]+'*'+Stim[4:8]
    else:
        Output = Stim
    return(Output)
    
    
CurrentStim = 'ABCDEFGHI'

StimOnTime = 4

InStim = MapLettersToScreen(CurrentStim)
# Set the values of the different letters
textTL.setText(InStim[0])
textTM.setText(InStim[1])
textTR.setText(InStim[2])
textCL.setText(InStim[3])
textCM.setText(InStim[4])
textCR.setText(InStim[5])
textBL.setText(InStim[6])
textBM.setText(InStim[7])
textBR.setText(InStim[8])    

# Draw the different letters to the screen
textTL.draw(); textTM.draw(); textTR.draw();
textCL.draw(); textCM.draw(); textCR.draw();
textBL.draw(); textBM.draw(); textBR.draw();
win.flip()
# Prepare the retention cross
core.wait(StimOnTime)    
    
    