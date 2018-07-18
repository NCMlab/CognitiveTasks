"""measure your JND in orientation using a staircase method"""

from psychopy import core, visual,  data, event , gui
from psychopy.tools.filetools import fromFile, toFile
import time, random
import numpy as np
import os
import sys

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
        

expInfo = {'Max Trials':150, 'Participant ID':'', 'Session':'001'}
PartDataFolder = 'unorganized'
if len(sys.argv) > 1:
    expInfo['Participant ID'] = sys.argv[1]
    PartDataFolder = sys.argv[1]
    FontSize = int(sys.argv[2])
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    FontSize = 60
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    
task = 'DMSstair_'
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = task


#make a text file to save data
#fileName = expInfo['expName'] + expInfo['Participant ID'] + "_"+ expInfo['date']
OutDir = '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
# If the subject path does not exist, than make it
if not os.path.exists(OutDir):
    os.mkdir(OutDir)
fileName = OutDir + '%s_%s_%s' % (task, expInfo['Participant ID'], expInfo['date'])

dataFile = open(fileName+'.csv', 'w')#a simple text file with 'comma-separated-values'
dataFile1=open(OutDir + 'CAPACITY_%s%s_%s.txt' % (task, expInfo['Participant ID'], expInfo['date']),'w')

# Put a header line into the output fileName
dataFile.write('Trial,Load,LevelIndex,Resp,Correct,ElapsedTime,RT,CorrectRT,ProbeType,Study,Probe\n')
StairCasefileName = os.path.join('data',expInfo['expName'] + expInfo['Participant ID']  + "_" + expInfo['date']+'Staircase.csv')
       
#create window and stimuli
# SMall screen
# win = visual.Window([800,600],allowGUI=True, monitor='testMonitor', units='norm')
# Full screen
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units = 'pix')

ProbeColor = 'blue'

# Timing
StimOnTime = 2.5
RetOnTime = 3.5
ProbeOnTime= 2.5
ITITime = 1.0
MaxTime = 7 # minutes
MaxTrials = expInfo['Max Trials'] # End after this many trials
NumberOfReversals = 20


FontSizeUnits = 'pix'
# This next value is based off of the units so be careful changing the units
SpacingOfLettersRelativeToCenter = 80
'''
MaxTime = 1
StimOnTime = 0.25
RetOnTime = 0.25
ProbeOnTime= 0.25
ITITime = 0.25
win = visual.Window(
    size=(800, 600), fullscr=False, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units = 'pix')
 '''  
    
#and some handy clocks to keep track of time
globalClock = core.Clock()
trialClock = core.Clock()

Nloads =  9
# How to shuffle the lists?


# Prepare the stimuli for display
WaitText = visual.TextStim(win=win, name='WaitText',
    #text='Remember:\nPress [LEFT] for IN the set\nPress [DOWN] for NOT in the set\n\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed press the [LEFT] or [DOWN] key.',
    text='Press [LEFT] if the letter WAS in the set.\nPress [DOWN] if the letter WAS NOT in the set.\nYou will NOT receive feedback after each trial.\nTry to respond as quickly and as accurately as possible.',
    font='Times New Roman',units=FontSizeUnits, 
    pos=(0, 0), height=40, wrapWidth=1200, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0);
CountDownText = visual.TextStim(win=win, name='CountDown',
    text='CountDown',units=FontSizeUnits, 
    font='Times New Roman',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0); 
    
textITI = visual.TextStim(win=win, name='textITI',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=0.0);
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
textDelay = visual.TextStim(win=win, name='textDelay',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1,
    depth=-10.0);
textProbe = visual.TextStim(win=win, name='textProbe',
    text='default text',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color=ProbeColor, colorSpace='rgb', opacity=1,
    depth=-11.0);

# White ITI
whiteITI = visual.TextStim(win=win, name='whiteITI',
    text='+',
    font='Times New Roman',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
# Green ITI
greenITI = visual.TextStim(win=win, name='greenITI',
    text='+',
    font='Times New Roman',
    pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1,
    depth=0.0);

    
# Number of trials in the file

# Each trial is extracted like this.
# This extracts the letter values for each locatio on the screen and sets them to 
# the different parameter names. The results is a variable for each location on 
# The screen.


#create the staircase handler
staircase = data.StairHandler(startVal = 9,
                          stepType = 'lin', stepSizes=[1],
                          nUp=1, nDown=3,  # will home in on the 80% threshold
                          nReversals = NumberOfReversals,minVal = 1,maxVal = Nloads)
                          

# Create counter for each load level
TrialCount = 1
count = [1]*Nloads
MaxCount = 24
CurrentLoad = 1
EndFlag = 'EndedNormal'
# Add the wait block
continueRoutine = True
WaitText.draw()
win.flip()
k = ['']
KeyBoardCount = 0
while k[0] not in ['escape', 'esc'] and KeyBoardCount < 1:
    k = event.waitKeys()
    KeyBoardCount += 1
    
# Add a count down block
CountDownTime = 1
CountDownText.text = '3'
CountDownText.draw()
win.flip()
core.wait(CountDownTime)
CountDownText.text = '2'
CountDownText.draw()
win.flip()
core.wait(CountDownTime)
CountDownText.text = '1'
CountDownText.draw()
win.flip()
core.wait(CountDownTime)

globalClock.reset()
LettersInThisTrial = ''
LastTrial = ''
CurrentCount = 0
for thisStep in staircase:
    CurrentCount += 1
    print '--------------'
    print 'ThisStep: '+str(thisStep)
    # Reset clock
    t = 0
    trialClock.reset()
    CurrentLoad = int(Nloads + 1 - thisStep)  
    LetterList = 'BCDFGHJKLMNPQRSTVXYZ'
    LettersToRemove = list(set(LastTrial))
    tempLetterList = list(LetterList)
    for j in LettersToRemove:
        tempLetterList[tempLetterList.index(j)] = ''
    # remove empty locations from the list
    tempLetterList = [x for x in tempLetterList if x] 
    # Create the lost of curent stimulus letters
    CurrentStim = ''
    CurrentStimIndex = np.random.permutation(len(tempLetterList))[0:CurrentLoad]
    for j in CurrentStimIndex:
        CurrentStim += tempLetterList[j]
    # Is the probe in teh set?
    Probe = np.round(np.random.uniform())
    if bool(Probe):
        # Yes, the probe is in the set
        CurrentProbe = CurrentStim[np.random.permutation(len(CurrentStim))[0]]
        corr = 'left'
    else:
        # Remove the current stim letters from the available letter set
        for j in CurrentStim:
            tempLetterList[tempLetterList.index(j)] = ''
        # remove empty locations from the list
        tempLetterList = [x for x in tempLetterList if x] 
        CurrentProbe = tempLetterList[np.random.permutation(len(tempLetterList))[0]]
        corr = 'down'
    CurrentProbe = CurrentProbe.lower()    
    LastTrial = CurrentStim + CurrentProbe.upper()
    InStim = MapLettersToScreen(CurrentStim)
    
    # What count are we for this load level?
      
    # If so choose a different set of letters.
    # The exception is with load level 9. For this case make sure 8 of the lettters are unique and 
    # The current probe is NOT part of the previous trial.

    


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
    textProbe.setText(CurrentProbe)
    # Draw the different letters to the screen
    textTL.draw(); textTM.draw(); textTR.draw();
    textCL.draw(); textCM.draw(); textCR.draw();
    textBL.draw(); textBM.draw(); textBR.draw();
    win.flip()
    # Prepare the retention cross
    core.wait(StimOnTime)
    greenITI.draw()
    win.flip()
    core.wait(RetOnTime)
    
    textProbe.draw()
    win.flip()
    trialClock.reset()
    # Add the ITI during delay
    # Add the probe letter

    # What is the correct response for this trial?
    # Get a response
    k = ['']
    KeyBoardCount = 0
    while k[0] not in ['escape', 'esc'] and KeyBoardCount < 1:
        k = event.waitKeys()
        KeyBoardCount += 1
        RT = trialClock.getTime()
    # Is this respone correct?
    if k[-1] == str(corr):
        # YES
        print k[-1]
        thisResp = 1
    else:
        # NO
        print k[-1]
        thisResp = -1
    staircase.addData(thisResp) 
    # Change the response to zero and one for later pivot tables
    CorrectResp = 0
    if thisResp == 1:
        CorrectResp = 1
    CorrectRT = 0
    if thisResp == 1:
        CorrectRT = RT
    # Is this a positive or negative probe?
    PosProbe = -1
    if CorrectResp == 1 and k[-1] == 'left':
        PosProbe = 1
    # Add this respone to the data file
    dataFile.write('%i,%i,%i,%s,%i,%0.3f,%0.4f,%0.4f,%i,%s,%s\n' %(TrialCount,CurrentLoad, CurrentCount, k[-1],CorrectResp,globalClock.getTime(),RT,CorrectRT,PosProbe,CurrentStim,CurrentProbe))


    # Add an ITI between trials
    textITI.draw()
    win.flip()
    core.wait(ITITime)
    TrialCount += 1

    # Check for an overall elapsed time and a total trial count
    # If either of these are exceeded, then end the experiment
    if len(staircase.data) > MaxTrials:
        win.close()
        EndFlag = 'MaxTrialsExceeded'
        dataFile.write('%s\n'%(EndFlag))
        Capacity = 10-np.mean(staircase.reversalIntensities)
        dataFile1.write('%0.4f'%(Capacity))
        print 
        print "Ending because the maximum number of trials was reached."
        print
        print "Capacity is: %0.4f"%(Capacity)        
        print "Number of reversals: %i"%(len(staircase.reversalPoints))
        dataFile.write('%s,%s,%s\n'%('NumTrials','NumReversals','Capacity'))
        dataFile.write('%i,%i,%0.4f\n'%(len(staircase.data),len(staircase.reversalPoints),Capacity))
        dataFile.close()
        staircase.saveAsText(StairCasefileName,delim=',')
        core.quit()
    if globalClock.getTime() > MaxTime*60:
        win.close()
        EndFlag = 'TimeExceeded'
        dataFile.write('%s\n'%(EndFlag))
        Capacity = 10-np.mean(staircase.reversalIntensities)
        dataFile1.write('%0.4f'%(Capacity))
        print 
        print "Ending because Time was exceeded."
        print
        print "Capacity is: %0.4f"%(Capacity)  
        print "Number of reversals: %i"%(len(staircase.reversalPoints))        
        dataFile.write('%s,%s,%s\n'%('NumTrials','NumReversals','Capacity'))
        dataFile.write('%i,%i,%0.4f\n'%(len(staircase.data),len(staircase.reversalPoints),Capacity))
        dataFile.close()
        staircase.saveAsText(StairCasefileName,delim=',')
        core.quit()
    if "escape" in k:
        win.close()
        EndFlag = 'UserEscape'
        dataFile.write('%s\n'%(EndFlag))
        Capacity = 10-np.mean(staircase.reversalIntensities)
        dataFile1.write('%0.4f'%(Capacity))
        print
        print "Ending because Escape was pressed."
        print
        print "Capacity is: %0.4f"%(Capacity)  
        print "Number of reversals: %i"%(len(staircase.reversalPoints))
        dataFile.write('%s,%s,%s\n'%('NumTrials','NumReversals','Capacity'))
        dataFile.write('%i,%i,%0.4f\n'%(len(staircase.data),len(staircase.reversalPoints),Capacity))
        dataFile.close()
        staircase.saveAsText(StairCasefileName,delim=',')
        core.quit()
print EndFlag

Capacity = 10-np.mean(staircase.reversalIntensities)
Capacity = Capacity
dataFile1.write('%0.4f'%(Capacity))
print
print "Capacity is: %0.4f"%(Capacity)     
print "Number of reversals: %i"%(len(staircase.reversalPoints))
dataFile.write('%s,%s,%s\n'%('NumTrials','NumReversals','Capacity'))
dataFile.write('%i,%i,%0.4f\n'%(len(staircase.data),len(staircase.reversalPoints),Capacity))
dataFile.close()
staircase.saveAsText(StairCasefileName,delim=',')
win.close()
core.quit()