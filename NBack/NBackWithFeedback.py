
"""
There needs to be two timers running for each trial. One to time when to 
change the stimulus and the other to record the RTs and when the next trials begins.

"""
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import sys
import time
import os  # handy system and path functions
ThisScript = sys.argv[0]
ThisFolder = os.path.dirname(ThisScript)
sys.path.append(ThisFolder)

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))#.decode(sys.getfilesystemencoding())
# import parameters from a config file
sys.path.append(os.path.join(_thisDir, '..','ConfigFiles'))
from NCM_NeuroPsych_Config import *

from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle

from psychopy.hardware.emulator import launchScan
import numpy as np
import NBackFunctions



NBlocks = len(NBack_Prac1_LoadLevel)
# DISPLAY PARAMETERS FOR THE USER TO CONFIRM
ExpectedTotalTime = NBack_Prac1_IntroOffDuration + NBlocks * (NBack_Prac1_InterBlockTime + NBack_Prac1_InstructionTime + NBack_Prac1_InterStimulusDelay + NBack_Prac1_TimePerTrial + NBack_Beh1_TrialPerBlock)
print("\n>> Blocks: %s"%(NBack_Prac1_LoadLevel))
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
task = 'Prac012'
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
    Tag = sys.argv[3]
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
    Tag = 'BehRun01'


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
AllCorrectLocations = []
for BlockNumber in range(0,NBlocks,1):
    CurrentLoadLevel = int(NBack_Prac1_LoadLevel[BlockNumber])
#    print(CurrentLoadLevel)
#    print(NBack_Prac1_TrialPerBlock)
#    print(NBack_Prac1_NumCorrectPerBlock)
    
    CorrectLocations = NBackFunctions.CreateStim(CurrentLoadLevel, NBack_Prac1_TrialPerBlock, NBack_Prac1_NumCorrectPerBlock)
#    print(CorrectLocations)
    # Try to assign letters to the list of correct locations
    # If it is not possible then -99 is returned
    print(NBack_Prac1_TrialPerBlock)
    print(NBack_Prac1_StimList)
    print(CurrentLoadLevel)
    List = NBackFunctions.AssignStimuliv2(CorrectLocations,NBack_Prac1_TrialPerBlock,NBack_Prac1_StimList,CurrentLoadLevel)
#    List = AssignStimuli(CorrectLocations, NBack_Prac1_TrialPerBlock, NBack_Prac1_StimList, CurrentLoadLevel)
#    while not isinstance(List,(list,tuple,np.ndarray)):
#        CorrectLocations = NBackFunctions.CreateStim(CurrentLoadLevel, NBack_Prac1_TrialPerBlock, NBack_Prac1_NumCorrectPerBlock)
#        List = NBackFunctions.AssignStimuliv2(CorrectLocations, NBack_Prac1_TrialPerBlock, NBack_Prac1_StimList, CurrentLoadLevel)
    AllLists.append(List)
    AllCorrectLocations.append(CorrectLocations)


# WINDOW
win = visual.Window(size=(1200, 900), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
    blendMode=u'avg', useFBO=True,units = 'pix'
    )
    
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Instructions
textInstr1 = visual.TextStim(win=win, name='textInstr1',
    text=NBack_Prac1_Instructions,
    font='Times New Roman',
    units='pix', pos=(0, 0), height=NBack_Prac1_InstructFontSize, wrapWidth=1200, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);   
    
StimulusText = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Times New Roman',
    pos=[0, 0], height=NBack_Prac1_TextSize, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

CrossHair = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Times New Roman',
    pos=[0, 0], height=NBack_Prac1_TextSize, wrapWidth=None,
    color=u'red', colorSpace=u'rgb', opacity=1,
    depth=0.0)
  
InstrLevel0 = visual.ImageStim(win,image=os.path.join(ThisFolder,'ZeroBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(NBack_Prac1_InstructionFigureSize, NBack_Prac1_InstructionFigureSize))
InstrLevel1 = visual.ImageStim(win,image=os.path.join(ThisFolder,'OneBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(NBack_Prac1_InstructionFigureSize,NBack_Prac1_InstructionFigureSize))
InstrLevel2 = visual.ImageStim(win,image=os.path.join(ThisFolder,'TwoBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(NBack_Prac1_InstructionFigureSize,NBack_Prac1_InstructionFigureSize))
InstrLevel3 = visual.ImageStim(win,image=os.path.join(ThisFolder,'ThreeBackInstructions.png'),
    mask=None,
    pos=(0.0,0.0),
    size=(NBack_Prac1_InstructionFigureSize,NBack_Prac1_InstructionFigureSize))
    
ThankYouScreen = visual.TextStim(win=win, ori=0, name='text',
    text=u'Thank You',    font=u'Times New Roman',
    pos=[0, 0], height = NBack_Prac1_TextSize, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

Feedback = visual.TextStim(win=win, ori=0, name='text',
    text=u'text',    font=u'Times New Roman',
    pos=[0, 100], height = NBack_Prac1_TextSize, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
    
resp = event.BuilderKeyResponse()  # create an object of type KeyResponse

# Set up the clocks
TrialClock = core.Clock()
CountDownClock = core.CountdownTimer()
LetterOnCountDownClock = core.CountdownTimer()
ElapsedTimeClock = core.Clock()

# Need instructions and wait
textInstr1.setAutoDraw(True)
# Put the probe dot on the screen
win.flip()
# Start the probe timer

WaitingFlag = True
while WaitingFlag is True:
    theseKeys = event.getKeys(keyList=['escape','return'])
    if 'escape' in theseKeys:
        core.quit()
    elif 'return' in theseKeys:
        WaitingFlag = False
        textInstr1.setAutoDraw(False)
    else:
        pass        



# Cross hair
ElapsedTimeClock.reset()
CountDownClock.reset()
CountDownClock.add(NBack_Prac1_IntroOffDuration)
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
    CurrentLoadLevel = int(NBack_Prac1_LoadLevel[BlockNumber])
    CorrectLocations = AllCorrectLocations[BlockNumber]
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
    # Instructions
    CountDownClock.add(NBack_Prac1_InstructionTime)
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
    print(CorrectLocations)
    StimulusText = visual.TextStim(win=win, ori=0, name='text',
        text='temp',    font=u'Times New Roman',
        pos=[0, 0], height = NBack_Prac1_TextSize, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=0.0)   
    
    CountDownClock.reset()
    for item in List:
        # Remove the stimulus and present the crosshair. This tells the participant that 
        # the stimulus letter has changed. Otherwise, it is not possible to tell apart
        # consecutive identical stimuli.
        
        # To do: For each trial present the letter first and then the cross hair
        # record responses untiul the end of the cross hair time
        
        
        # Add Letter time and ITI to timer
        LetterOnCountDownClock.reset()
        CountDownClock.add(NBack_Prac1_InterStimulusDelay + NBack_Prac1_TimePerTrial)   
        LetterOnCountDownClock.add(NBack_Prac1_TimePerTrial)
        # Present the stimulus
        StimulusText.text = item
        CrossHair.setAutoDraw(False)
        StimulusText.setAutoDraw(True)
        Feedback.setAutoDraw(False)
        win.flip()
        # Now that the letter is on the screen reset the timer used for recording RTs
        TrialClock.reset()
        # Now that the timers are started and the letter is on the screen for this trial
        # Enter a while loop
        # CHeck the trial time
        while CountDownClock.getTime() > 0:
            # CHeck to see how long the letter has been on the screen with teh second running
            # timer
            if LetterOnCountDownClock.getTime() < 0:
                # Turn off the letter
                StimulusText.setAutoDraw(False)
                # turn on the cross hair
                CrossHair.setAutoDraw(True)
                # put them on the screen
                win.flip()
            # Check to see if any keys have been pressed
            # This works for any key
            theseKeys = event.getKeys()
            if "escape" in theseKeys:
                win.flip()
                win.close()
                core.quit() 
            elif len(theseKeys) > 0:
                # This must be a response
                CurrentRT = TrialClock.getTime()
                # Take the last key pressed
                thisExp.addData('KeyPress',theseKeys[-1])
                thisExp.addData('RT',CurrentRT)
                if (count + 1) in CorrectLocations:
                    print("TRUE")
                    thisExp.addData('Correct','1')
                    Feedback.text = 'Correct'
                else:
                    thisExp.addData('Correct','0')
                    Feedback.text = 'Wrong'
                resp.KeyPress = theseKeys[-1]
                resp.RT = CurrentRT
                CurrentRT = TrialClock.getTime()
                Feedback.setAutoDraw(True)
                print("%02d: %s Key press: %s in %0.4f sec"%(count,item,theseKeys[-1],CurrentRT))

        thisExp.addData('ElapsedTime',ElapsedTimeClock.getTime())

        thisExp.addData('count',count)
        thisExp.addData('Block',BlockNumber+1)
        thisExp.addData('Stimulus',item)
        thisExp.addData('LoadLevel', NBack_Prac1_LoadLevel) 
        if (count + 1) in CorrectLocations:
            thisExp.addData('Expected',1)
        else:
            thisExp.addData('Expected',0)
        thisExp.nextEntry()
        count += 1
    # Make sure the cross hair is not shown
    CrossHair.setAutoDraw(False)            
    CountDownClock.add(NBack_Prac1_InterBlockTime)        
    CrossHair.draw()
    win.flip()
    while CountDownClock.getTime() > 0:
        theseKeys = event.getKeys()
        if "escape" in theseKeys:
            win.flip()
            core.quit() 

# Thank you screen
CountDownClock.add(NBack_Prac1_ThankYouOnTime)
ThankYouScreen.draw()
win.flip()
while CountDownClock.getTime() > 0:
    theseKeys = event.getKeys()
    if "escape" in theseKeys:
        win.flip()
        core.quit() 

#thisExp.saveAsWideText(filename+'.csv') 
win.close()
core.quit()
        
    