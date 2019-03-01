from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import sys
import time
import os  # handy system and path functions
ThisScript = sys.argv[0]
ThisFolder = os.path.dirname(ThisScript)
sys.path.append(ThisFolder)

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
# import parameters from a config file
sys.path.append(os.path.join(_thisDir, '..','ConfigFiles'))
from NBackConfig import *

from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle

from psychopy.hardware.emulator import launchScan
import numpy as np
from NBackFunctions import *



NBlocks = len(NBack_Beh1_LoadLevel)
# DISPLAY PARAMETERS FOR THE USER TO CONFIRM
ExpectedTotalTime = NBack_Beh1_IntroOffDuration + NBlocks * (NBack_Beh1_InterBlockTime + NBack_Beh1_InstructionTime + NBack_Beh1_InterStimulusDelay + NBack_Beh1_TimePerTrial + NBack_Beh1_TrialPerBlock)
print("\n>> Blocks: %s"%(NBack_Beh1_LoadLevel))
print(">> Expected Duration: %d\n"%(ExpectedTotalTime))

# NOTES
# April 28, 2016
# The program sometimes crashewhile running. I am thinking that there 
# must have been an error when generating the stimuli which is causing the error.
# I am going to generate the stimuli before the task starts running.

# Store info about the experiment session
# #################
# Store info about the experiment session
expName = u'NBack'  # from the Builder filename that created this script
task = 'Block2Back'
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
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    DataFolder = "../../data"
    PartDataFolder = 'unorganized'
    OutDir = os.path.join(DataFolder, PartDataFolder)
    if not os.path.exists(OutDir):
        os.mkdir(OutDir)
    PartDataFolder = OutDir

Tag = '1'
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = os.path.join(PartDataFolder, '%s_%s_%s_%s_%s' % (expInfo['Participant ID'],expName, task, Tag, expInfo['date']))
CounterBalFlag = 'False'
BGColor = 'grey'
FontColor = 'white'
# #################

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=True,
    dataFileName=filename)

# Make a list of stimuli, one for each block
AllLists = []
for BlockNumber in range(0,NBlocks,1):
    CurrentLoadLevel = int(NBack_Beh1_LoadLevel[BlockNumber])
#    print(CurrentLoadLevel)
#    print(NBack_Beh1_TrialPerBlock)
#    print(NBack_Beh1_NumCorrectPerBlock)
    
    CorrectLocations = CreateStim(CurrentLoadLevel, NBack_Beh1_TrialPerBlock, NBack_Beh1_NumCorrectPerBlock)
#    print(CorrectLocations)
    # Try to assign letters to the list of correct locations
    # If it is not possible then -99 is returned
    List = AssignStimuli(CorrectLocations, NBack_Beh1_TrialPerBlock, NBack_Beh1_StimList, CurrentLoadLevel)
    while not isinstance(List,(list,tuple,np.ndarray)):
        CorrectLocations = CreateStim(CurrentLoadLevel, NBack_Beh1_TrialPerBlock, NBack_Beh1_NumCorrectPerBlock)
        List = AssignStimuli(CorrectLocations, NBack_Beh1_TrialPerBlock, NBack_Beh1_StimList, CurrentLoadLevel)
    AllLists.append(List)

#TotalDurDLG = gui.Dlg(title='Time')
#TotalDurDLG.addText('Total Duration of Experiment')
#TotalDurDLG.addText('%d seconds'%ExpectedTotalTime)
#TotalDurDLG.show()

# FULL SCREEN WINDOW
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
    blendMode=u'avg', useFBO=True,units = 'pix'
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

# Instructions
textInstr1 = visual.TextStim(win=win, name='textInstr1',
    text=NBack_Beh1_Instructions,
    font='Arial',
    units='pix', pos=(0, 0), height=NBack_Beh1_InstructFontSize, wrapWidth=1200, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);   
    
StimulusText = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=NBack_Beh1_TextSize, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

CrossHair = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=NBack_Beh1_TextSize, wrapWidth=None,
    color=u'red', colorSpace=u'rgb', opacity=1,
    depth=0.0)
  
InstrLevel0 = visual.ImageStim(win,image=os.path.join(ThisFolder,'ZeroBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(NBack_Beh1_InstructionFigureSize, NBack_Beh1_InstructionFigureSize))
InstrLevel1 = visual.ImageStim(win,image=os.path.join(ThisFolder,'OneBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(NBack_Beh1_InstructionFigureSize,NBack_Beh1_InstructionFigureSize))
InstrLevel2 = visual.ImageStim(win,image=os.path.join(ThisFolder,'TwoBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(NBack_Beh1_InstructionFigureSize,NBack_Beh1_InstructionFigureSize))
InstrLevel3 = visual.ImageStim(win,image=os.path.join(ThisFolder,'ThreeBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(NBack_Beh1_InstructionFigureSize,NBack_Beh1_InstructionFigureSize))
    
ThankYouScreen = visual.TextStim(win=win, ori=0, name='text',
    text=u'Thank You',    font=u'Arial',
    pos=[0, 0], height = NBack_Beh1_TextSize, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

resp = event.BuilderKeyResponse()  # create an object of type KeyResponse

# Set up the clocks
TrialClock = core.Clock()
CountDownClock = core.CountdownTimer()
ElapsedTimeClock = core.Clock()


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



# Cross hair
ElapsedTimeClock.reset()
CountDownClock.reset()
CountDownClock.add(NBack_Beh1_IntroOffDuration)
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
    CurrentLoadLevel = int(NBack_Beh1_LoadLevel[BlockNumber])
    if CurrentLoadLevel == 0:
        Instructions = InstrLevel0
    elif CurrentLoadLevel == 1:
        Instructions = InstrLevel1
    elif CurrentLoadLevel == 2:
        Instructions = InstrLevel2
    elif CurrentLoadLevel == 3:
        Instructions = InstrLevel3
    List = AllLists[BlockNumber]
    print("Using block number %d, with load %d"%(BlockNumber,CurrentLoadLevel)) 
    # CorrectLocations = CreateStim(CurrentLoadLevel,ExpParameters['TrialPerBlock'],ExpParameters['NumCorrectPerBlock'])
    # List = AssignStimuli(CorrectLocations,ExpParameters['TrialPerBlock'],ExpParameters['StimList'],CurrentLoadLevel)
    print List                        
    # Instructions
    CountDownClock.add(NBack_Beh1_InstructionTime)
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
        # Remove the stimulus and present the crosshair. This tells the participant that 
        # the stimulus letter has changed. Otherwise, it is not possible to tell apart
        # consecutive identical stimuli.
        CountDownClock.add(NBack_Beh1_InterStimulusDelay)        
        CrossHair.draw()
        win.flip()
        while CountDownClock.getTime() > 0:
            theseKeys = event.getKeys()
            if "escape" in theseKeys:
                win.flip()
                core.quit() 
        CountDownClock.add(NBack_Beh1_TimePerTrial)
        # Present the stimulus
        StimulusText = visual.TextStim(win=win, ori=0, name='text',
                text=item,    font=u'Arial',
                pos=[0, 0], height = NBack_Beh1_TextSize, wrapWidth=None,
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
        thisExp.addData('LoadLevel', NBack_Beh1_LoadLevel) 
        thisExp.nextEntry()

                
    CountDownClock.add(NBack_Beh1_InterBlockTime)        
    CrossHair.draw()
    win.flip()
    while CountDownClock.getTime() > 0:
        theseKeys = event.getKeys()
        if "escape" in theseKeys:
            win.flip()
            core.quit() 

# Thank you screen
CountDownClock.add(NBack_Beh1_ThankYouOnTime)
ThankYouScreen.draw()
win.flip()
while CountDownClock.getTime() > 0:
    theseKeys = event.getKeys()
    if "escape" in theseKeys:
        win.flip()
        core.quit() 

thisExp.saveAsWideText(filename+'.csv') 
win.close()
core.quit()
        
    