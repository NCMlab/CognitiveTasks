from psychopy import locale_setup, gui, visual, core, data, event, logging
import numpy as np  # whole numpy lib is available, prepend 'np.'
import os  # handy system and path functions
import sys  # to get file system encoding
import random

# Visual Task components
# circle
# countdown 3
# countdown 2
# countdown 1
# instructions
# thank you
# white plus sign
# green plus sign
# red plus sign

#
# Timers
# overall timer
# component timer

# Timings
FontSize = 60
FontSizeUnits = 'pix'
GridCount = 7 # Number of circles to have on each row
GridSize = 160 # The size of the grid for which the circles on on
CircleSize = (GridSize*2)/GridCount # The circle size so that they are all just touching
OffSet = range(-GridSize+int(CircleSize/2),GridSize-int(CircleSize/2),int(CircleSize))
MaskLocations = np.arange(0,1+GridCount**2)
# units=FontSizeUnits
# height=FontSize
StimOnTime = 1.0
RetOnTime = 3.0
ProbeOnTime= 2.7
MaskOnTime = 0.3
# This is the intertrial interval. This experimental component is part of the trial.
ITITime = 0.5 #1.0
# This is the time between blocks. Note that between each block of trials there
# is also the 3-2-1 countdown. Therefore, the full interblock interval is this value PLUS 
# the countdown time, which is 3 seconds.
InterBlockTime = 6 #13.0
# This is a delay component for use after instructions and before the first Block and at the
# the end before the thank you screen
ShortDelayTime = 5 #16.0
NumberOfBlocks = 5

## These are great for testing quickly
#  StimOnTime = .25
#RetOnTime = .25
#ProbeOnTime= .25
#ITITime = .25
TotalTrialTime = StimOnTime + RetOnTime + ProbeOnTime + ITITime

countDown = core.CountdownTimer()
# Store info about the experiment session
expName = u'VSTM'  # from the Builder filename that created this script
expInfo = {'Participant ID':'', 'Session':'001'}
PartDataFolder = 'unorganized'
Tag = '1'

# Setup the Window
win = visual.Window(
    size=(800, 600), fullscr=False, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units=FontSizeUnits)
    
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
    
resp = event.BuilderKeyResponse()
# Circle
# This is a single component that will be displayed on the screen multiple times while
# changing arounds its position

circle = visual.Polygon(
    win=win, name='polygon',units='pix', 
    edges=128, size=(CircleSize, CircleSize),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Cross hairs
RedCross = visual.TextStim(win=win, name='RedCross',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-9.0);
WhiteCross = visual.TextStim(win=win, name='RedCross',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
GreenCross = visual.TextStim(win=win, name='RedCross',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1,
    depth=-9.0);
    
# Instructions
textInstr1 = visual.TextStim(win=win, name='textInstr1',
    text='Ready to start the main experiment?\nRemember:\nPress [LEFT] if the circle WAS in the set.\nPress [DOWN] if the circle was NOT in the set.\n\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press any key.',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize*0.75, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);   
    
# Initialize components for Routine "Countdown"
text3 = visual.TextStim(win=win, name='text3',
    text='3',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text2 = visual.TextStim(win=win, name='text2',
    text='2',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text1 = visual.TextStim(win=win, name='text1',
    text='1',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
    
textThankyou = visual.TextStim(win=win, name='textThankyou',
    text='Thank you for participating!',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);    
    
    

# For each block change the selection list 

# Need instructions and wait
textInstr1.setAutoDraw(True)
# Put the probe dot on the screen
win.flip()
# Start the probe timer

WaitingFlag = True
while WaitingFlag is True:
    theseKeys = event.getKeys(keyList=['escape','5'])
    if 'escape' in theseKeys:
        core.quit()
    elif '5' in theseKeys:
        WaitingFlag = False
        textInstr1.setAutoDraw(False)
    else:
        pass        
        
# Need intro Blocks
# Turn on the cross hair
WhiteCross.setAutoDraw(True)
win.flip()
countDown.reset() 
WhiteCross.setAutoDraw(True)
countDown.add(InterBlockTime - 3)
while countDown.getTime() > 0:
    pass
win.flip()
# Turn on the countdown timer
WhiteCross.setAutoDraw(False)

text3.setAutoDraw(True)
countDown.add(1)
win.flip()
while countDown.getTime() > 0:
    pass
text3.setAutoDraw(False)
text2.setAutoDraw(True)
countDown.add(1)
win.flip()
while countDown.getTime() > 0:
    pass    
text2.setAutoDraw(False)
text1.setAutoDraw(True)
countDown.add(1)
win.flip()
while countDown.getTime() > 0:
    pass    
win.flip()
text1.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
Blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('VSTMBlockListv1.csv'),
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
            
    print(rows)
    