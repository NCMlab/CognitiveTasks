from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import sys
import os  # handy system and path functions
ThisScript = sys.argv[0]
ThisFolder = os.path.dirname(ThisScript)
sys.path.append(ThisFolder)


from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle

from psychopy.hardware.emulator import launchScan
import numpy as np
from NBackFunctions import *


# EXPERIMENTAL INFORMATION
expName = u'NBack'  # <<< This is where you specify the name of the experiment which makes it easier to differentiate the results files.
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# OUTPUT FILENAME
filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# MRI INFORMATION FOR SYNCHRONIZATION
MR_settings = { 
    'TR': 2.000, # duration (sec) per volume
    'volumes': 5, # number of whole-brain 3D volumes / frames
    'sync': '5', # character to use as the sync timing event; assumed to come at start of a volume
    'skip': 0, # number of volumes lacking a sync pulse at start of scan (for T1 stabilization)
    'sound': False # in test mode only, play a tone as a reminder of scanner noise
    }

# DISPLAY PARAMETERS FOR THE USER TO CONFIRM
infoDlg = gui.DlgFromDict(MR_settings, title='MRI Settings')

# Create an N-back task
ExpParameters = {
    'LoadLevel': '01230123',
    'TimePerTrial': 1.5, # seconds
    'TrialPerBlock': 14,
    'StimList': 'ABCDEFGHJKLMNPRSTVWYZ',
    'ResponseKeys':['1','2','3','4','5','6','7','8','9','0'],
    'NumCorrectPerBlock': 4,
    'IntroOffDuration': 36,
    'OffDuration' : 28,
    'InstrTime': 6,
    'TextSize': 0.2,
    'InterStimulusDelay': 0.5
}

NBlocks = len(ExpParameters['LoadLevel'])
# DISPLAY PARAMETERS FOR THE USER TO CONFIRM
infoDlg = gui.DlgFromDict(ExpParameters, title='Experimental Parameters')
ExpectedTotalTime = ExpParameters['IntroOffDuration'] + NBlocks * (ExpParameters['OffDuration'] + ExpParameters['InstrTime'] + (ExpParameters['InterStimulusDelay']+ExpParameters['TimePerTrial'])*ExpParameters['TrialPerBlock'])
print "Expected Duration: %d"%ExpectedTotalTime

TotalDurDLG = gui.Dlg(title='Time')
TotalDurDLG.addText('Total Duration of Experiment')
TotalDurDLG.addText('%d seconds'%ExpectedTotalTime)
TotalDurDLG.show()


# FULL SCREEN WINDOW
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
    blendMode=u'avg', useFBO=True,
    )
    
# PARTIAL SCREEN WINDOW
#win = visual.Window(size=[800,600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
#    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
#    blendMode=u'avg', useFBO=True,
#    )

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess


StimulusText = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=ExpParameters['TextSize'], wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

CrossHair = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=ExpParameters['TextSize'], wrapWidth=None,
    color=u'red', colorSpace=u'rgb', opacity=1,
    depth=0.0)
    
InstrLevel0 = visual.ImageStim(win,image=os.path.join(ThisFolder,'ZeroBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(1.5,1.5))
InstrLevel1 = visual.ImageStim(win,image=os.path.join(ThisFolder,'OneBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(1.0,1.0))
InstrLevel2 = visual.ImageStim(win,image=os.path.join(ThisFolder,'TwoBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(1.5,1.5))
InstrLevel3 = visual.ImageStim(win,image=os.path.join(ThisFolder,'ThreeBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(1.5,1.5))
    
ThankYouScreen = visual.TextStim(win=win, ori=0, name='text',
    text=u'Merci',    font=u'Arial',
    pos=[0, 0], height=ExpParameters['TextSize'], wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)


resp = event.BuilderKeyResponse()  # create an object of type KeyResponse

# Set up the clocks
TrialClock = core.Clock()
CountDownClock = core.CountdownTimer()
ElapsedTimeClock = core.Clock()


# PRESENT THE SCREEN TO WAIT FOR THE MRI TRIGGER
vol = launchScan(win, MR_settings,  mode='Scan')

# Cross hair
ElapsedTimeClock.reset()
CountDownClock.reset()
CountDownClock.add(ExpParameters['IntroOffDuration'])
CrossHair.draw()
win.flip()
while CountDownClock.getTime() > 0:
    theseKeys = event.getKeys()
    if "escape" in theseKeys:
        win.flip()
        win.close()
        core.quit() 
for BlockNumber in range(0,NBlocks,1):
    # Change this so that it delivers very specific blocks
    # Use a list of load levels. The number of blocks is the list length and the load is the value in the List
    #
    CurrentLoadLevel = int(ExpParameters['LoadLevel'][BlockNumber])
    if CurrentLoadLevel == 0:
        Instructions = InstrLevel0
    elif CurrentLoadLevel == 1:
        Instructions = InstrLevel1
    elif CurrentLoadLevel == 2:
        Instructions = InstrLevel2
    elif CurrentLoadLevel == 3:
        Instructions = InstrLevel3
        
    print "Using block number %d, with load %d"%(BlockNumber,CurrentLoadLevel)    
    CorrectLocations = CreateStim(CurrentLoadLevel,ExpParameters['TrialPerBlock'],ExpParameters['NumCorrectPerBlock'])
    List = AssignStimuli(CorrectLocations,ExpParameters['TrialPerBlock'],ExpParameters['StimList'],CurrentLoadLevel)
    print List                        
    # Instructions
    CountDownClock.add(ExpParameters['InstrTime'])
    thisExp.addData('Stimulus','Instructions')
    thisExp.addData('ElapsedTime',ElapsedTimeClock.getTime())
    thisExp.nextEntry()
    TrialClock.reset()
    # Present the instructions
    Instructions.draw()   
    win.flip()
    while CountDownClock.getTime() > 0:
        theseKeys = event.getKeys()
        if "escape" in theseKeys:
            win.flip()
            win.close()
            core.quit() 
            
                
    # present a block of stimuli
    count = 0
    print CorrectLocations
    for item in List:
        CountDownClock.add(ExpParameters['TimePerTrial'])
        # Present the stimulus
        StimulusText = visual.TextStim(win=win, ori=0, name='text',
                text=item,    font=u'Arial',
                pos=[0, 0], height=ExpParameters['TextSize'], wrapWidth=None,
                color=u'white', colorSpace=u'rgb', opacity=1,
                depth=0.0)    
        StimulusText.draw()
        win.flip()
        TrialClock.reset()
        thisExp.addData('ElapsedTime',ElapsedTimeClock.getTime())
        while CountDownClock.getTime() > 0:
            theseKeys = event.getKeys()
            if "escape" in theseKeys:
                win.flip()
                win.close()
                core.quit() 
            elif len(theseKeys) > 0:
                # This must be a response
                CurrentRT = TrialClock.getTime()
                thisExp.addData('KeyPress',theseKeys[-1])
                thisExp.addData('RT',CurrentRT)
                if (count + 1) in CorrectLocations:
                    print "TRUE"
                    thisExp.addData('Correct','Y')
                else:
                    thisExp.addData('Correct','N')
                resp.KeyPress = theseKeys[-1]
                resp.RT = CurrentRT
                CurrentRT = TrialClock.getTime()
                print "%02d: %s Key press: %s in %0.4f sec"%(count,item,theseKeys[-1],CurrentRT)
        count += 1
        thisExp.addData('count',count)
        thisExp.addData('Block',BlockNumber+1)
        thisExp.addData('Stimulus',item)
        thisExp.addData('LoadLevel',ExpParameters['LoadLevel'])
        thisExp.nextEntry()
        # Remove the stimulus and present the crosshair. This tells the participant that 
        # the stimulus letter has changed. Otherwise, it is not possible to tell apart
        # consecutive identical stimuli.
        CountDownClock.add(ExpParameters['InterStimulusDelay'])        
        CrossHair.draw()
        win.flip()
        while CountDownClock.getTime() > 0:
            theseKeys = event.getKeys()
            if "escape" in theseKeys:
                win.flip()
                core.quit() 
                
    CountDownClock.add(ExpParameters['OffDuration'])        
    CrossHair.draw()
    win.flip()
    while CountDownClock.getTime() > 0:
        theseKeys = event.getKeys()
        if "escape" in theseKeys:
            win.flip()
            core.quit() 

# Thank you screen
CountDownClock.add(20)
ThankYouScreen.draw()
win.flip()
while CountDownClock.getTime() > 0:
    theseKeys = event.getKeys()
    if "escape" in theseKeys:
        win.flip()
        core.quit() 

win.close()
core.quit()
        
    