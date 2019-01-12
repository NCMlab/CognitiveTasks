from psychopy import locale_setup, gui, visual, core, data, event, logging
import numpy as np  # whole numpy lib is available, prepend 'np.'
import os  # handy system and path functions
import sys  # to get file system encoding
import random

# Visual Task components
# circle5
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

ProbeColor = 'blue'

# Timings
FontSize = 60
FontSizeUnits = 'pix'
GridCount = 6 # Number of circles to have on each row
GridSize = 52*GridCount + 1 # The size of the grid for which the circles on on
CircleSize = (GridSize*2)/GridCount # The circle size so that they are all just touching
OffSet = range(-GridSize+int(CircleSize/2),GridSize-int(CircleSize/2),int(CircleSize))
MaskLocations = np.arange(0,1+GridCount**2)
# units=FontSizeUnits
# height=FontSize
StimOnTime = 1.5
RetOnTime = 3.0
ProbeOnTime= 2.0
MaskOnTime = 0.3
# This is the intertrial interval. This experimental component is part of the trial.
ITITime = 1.0 #1.0
# This is the time between blocks. Note that between each block of trials there
# is also the 3-2-1 countdown. Therefore, the full interblock interval is this value PLUS 
# the countdown time, which is 3 seconds.
InterBlockTime = 5 #13.0
# This is a delay component for use after instructions and before the first Block and at the
# the end before the thank you screen
ShortDelayTime = 5 #16.0
NumberOfBlocks = 5
NTrialsPerBlock = 6

## These are great for testing quickly
#  StimOnTime = .25
#RetOnTime = .25
#ProbeOnTime= .25
#ITITime = .25
TotalTrialTime = StimOnTime + RetOnTime + ProbeOnTime + ITITime

countDown = core.CountdownTimer()
# Store info about the experiment session
# #################
# Store info about the experiment session
expName = u'VSTM'  # from the Builder filename that created this script
task = 'Block'
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
    LoadList = sys.argv[3].split(' ')
    LoadList = np.array(LoadList)
    LoadList = LoadList.astype(np.int)

    Tag = sys.argv[4]
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    DataFolder = "../../data"
    PartDataFolder = 'unorganized'
    OutDir = os.path.join(DataFolder, PartDataFolder)
    if not os.path.exists(OutDir):
        os.mkdir(OutDir)
    LoadList = np.array(range(1,6,1)) ### <<<<<<<<<<<<<<<<<<<
    LoadList = LoadList.astype(np.int)
    
    Tag = 'BehRun1'
    PartDataFolder = OutDir
 
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = os.path.join(PartDataFolder, '%s_%s_%s_%s_%s' % (expInfo['Participant ID'],expName, task, Tag, expInfo['date']))
CounterBalFlag = 'False'
BGColor = 'grey'
FontColor = 'white'
# #################


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#OutDir =  '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
#filename = OutDir + '%s_%s_%s' % (expName, expInfo['Participant ID'], expInfo['date'])
#


# Setup the Window
win = visual.Window(
    size=(800, 600), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=BGColor, colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units=FontSizeUnits)
    
expInfo['date'] = data.getDateStr()  # add a simple timestamp
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#OutDir = '..' + os.sep + '..' + os.sep + '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep

dataFile = open(filename+'.csv', 'w')

#filename = OutDir + '%s%s_%s_%s' % (expName, Tag, expInfo['Participant ID'], expInfo['date'])
print(filename)

#OutDir = '..' + os.sep + '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
#filename = OutDir + '%s%s_%s_%s' % (expName, task, expInfo['Participant ID'], expInfo['date'])
#print(filename)
#dataFile = open(filename+'.csv', 'w')
dataFile.write('Trial,Load,TrialStartTime,Resp,Corr,RT,CorrectRT,ProbeType,ProbeLoc,')
for i in np.arange(max(LoadList)):
    dataFile.write('StimLoc%02d,'%(i+1))
dataFile.write('\n')


# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=False,
    dataFileName=filename)
    
thisResp = event.BuilderKeyResponse()
# Circle
# This is a single component that will be displayed on the screen multiple times while
# changing arounds its position

circle = visual.Polygon(
    win=win, name='polygon',units='pix', 
    edges=128, size=(CircleSize, CircleSize),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
    
ProbeCircle = visual.Polygon(
    win=win, name='polygon',units='pix', 
    edges=128, size=(CircleSize, CircleSize),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=ProbeColor, lineColorSpace='rgb',
    fillColor=ProbeColor, fillColorSpace='rgb',
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
    color='black', colorSpace='rgb', opacity=1,
    depth=-9.0);
GreenCross = visual.TextStim(win=win, name='RedCross',
    text='+',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color='green', colorSpace='rgb', opacity=1,
    depth=-9.0);
    
# Instructions
textInstr1 = visual.TextStim(win=win, name='textInstr1',
    text='Press [LEFT] if the circle WAS in the set.\nPress [DOWN] if the circle was NOT in the set.\n\nTry to respond as quickly and as accurately as possible.',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize*0.75, wrapWidth=1200, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);   
    
# Initialize components for Routine "Countdown"
text3 = visual.TextStim(win=win, name='text3',
    text='3',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);
text2 = visual.TextStim(win=win, name='text2',
    text='2',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=-1.0);
text1 = visual.TextStim(win=win, name='text1',
    text='1',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=-2.0);
    
textThankyou = visual.TextStim(win=win, name='textThankyou',
    text='Thank you for participating!',
    font='Times New Roman',
    units=FontSizeUnits, pos=(0, 0), height=FontSize, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);    
    
RunningClock = core.Clock()

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

# set up handler to look after randomisation of conditions etc
Blocks = data.TrialHandler(nReps=NumberOfBlocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,trialList=[None],
    seed=None, name='Blocks')

RunningClock.reset()
# ###########################
# INTRO BlockCount
# Need intro Blocks
# Turn on the cross hair
WhiteCross.setAutoDraw(True)
win.flip()
countDown.reset() 
WhiteCross.setAutoDraw(True)
countDown.add(InterBlockTime)
while countDown.getTime() > 0:
    pass
win.flip()
# Turn on the countdown timer
WhiteCross.setAutoDraw(False)
# ###########################
# BLOCK LOOP
thisExp.addLoop(Blocks)  # add the loop to the experiment
thisBlock = Blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

BlockCount = 0
for thisBlock in Blocks:
    currentLoop = Blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
            
    CurrentLoad = LoadList[BlockCount]
    countDown.reset()   
    
#   321
    text3.setAutoDraw(True)
    countDown.add(1)
    
    # Prepare the stimuli
    # Make sure there are an equal number of probe pos and Neg
    ProbeList = np.concatenate((np.zeros(int(NTrialsPerBlock/2)),np.ones(int(NTrialsPerBlock/2))))
    # Shuffle the list
    ProbeList = ProbeList[np.random.permutation(NTrialsPerBlock)]
    
    # prepare the trials
    trials = data.TrialHandler(nReps=NTrialsPerBlock, method='sequential', 
    extraInfo=expInfo, originPath=-1,trialList=[None],
    seed=None, name='trials')
    
    
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
#   TRIAL LOOP

    TrialCount = 0
    for thisTrial in trials:
        countDown.add(StimOnTime)
        GreenCross.setAutoDraw(True)
        TrialStartTime = RunningClock.getTime()
        theseKeys = event.getKeys()
        Locations = np.random.permutation(GridCount**2)[0:CurrentLoad]
        print(thisTrial)
        # Create the probe Locations    
        PosProbeLocation = Locations[np.random.permutation(CurrentLoad)[0]]
        NotLocations = np.arange(0,GridCount**2)
        NotLocations = [x for x in NotLocations if x not in Locations]
        #NegProbeLocation = np.random.randint(0,len(NotLocations),1)[0]
        NegProbeLocation = NotLocations[np.random.permutation(len(NotLocations))[0]]
        
        if ProbeList[TrialCount] == 1:
            corr = 'left'
        else:
            corr = 'down'

        # Make sure the Locations does not include the central location because 
        # the cross hair is to remain on the screen
        count = 0
        for y_offset in OffSet:
            for x_offset in OffSet:
               for stim in [circle]:
                   stim.pos = [x_offset, y_offset]
                   if (count in Locations):
                       stim.draw()
                   count += 1
        
        CurrentTime = RunningClock.getTime()

        # Put the circles on the screen
        win.flip()
        
        # Prepare the mask dots
        count = 0
        for y_offset in OffSet:
            for x_offset in OffSet:
               for stim in [circle]:
                   stim.pos = [x_offset, y_offset]
                   if (count in MaskLocations):
                       stim.draw()
                   count += 1
        while countDown.getTime() > 0:
            pass        
        
        # Put the mask dots on the screen
        #GreenCross.setAutoDraw(False)
        win.flip()
        countDown.add(MaskOnTime)
        while countDown.getTime() > 0:
            pass
        
        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
            
        print(countDown.getTime())
  
        # Clear any button presses
        event.clearEvents(eventType='keyboard')
        
        # Take the dots off the screen and put the cross hair up 
        win.flip()       
        countDown.add(RetOnTime)
        
        # Prepare the probe dot during the retention time
        ProbeLoc = -99
        if ProbeList[TrialCount] == 0:
            count = 0
            ProbeLoc = NegProbeLocation
            for y_offset in OffSet:
                for x_offset in OffSet:
                   for stim in [ProbeCircle]:
                       stim.pos = [x_offset, y_offset]
                       if (count in [NegProbeLocation]):
                           stim.draw()
                       count += 1
        elif ProbeList[TrialCount] == 1:
            count = 0
            ProbeLoc = PosProbeLocation
            for y_offset in OffSet:
                for x_offset in OffSet:
                   for stim in [ProbeCircle]:
                       stim.pos = [x_offset, y_offset]
                       if (count in [PosProbeLocation]):
                           stim.draw()
                       count += 1
                       
                   
        while countDown.getTime() > 0:
            pass
    # Turn off the cross hair
        GreenCross.setAutoDraw(True)
        # Put the probe dot on the screen
        win.flip()
        thisResp.clock.reset()
        # Start the probe timer
        countDown.add(ProbeOnTime)
        event.clearEvents(eventType='keyboard')
        print(countDown.getTime())
        thisResp.keys = -99
        thisResp.rt = -99
        # Changethis while loop to have a flag
        # The flag is set to false if a response is made or if the timer elapses
        continueRoutine = True 
        while continueRoutine:
        # while countDown.getTime() > 0:
            theseKeys = event.getKeys(keyList=['escape','left', 'right','1','2'])
            if 'escape' in theseKeys:
                core.quit()
            elif len(theseKeys) > 0:  # at least one key was pressed
                thisResp.keys = theseKeys[-1]  # just the last key pressed
                thisResp.rt = thisResp.clock.getTime()
                continueRoutine = False
                # was this 'correct'?
                #if (thisResp.keys == str(corr)) or (thisResp.keys == corr):
                #    print('Correct')
                #    thisResp.corr = 1
                #else:
                #    print('incorrect')
                #    thisResp.corr = 0    
                #break
                if CounterBalFlag == 'False':
                    if corr == 'left':
                        if ((thisResp.keys == corr) or (thisResp.keys == str(corr))):
                            thisResp.corr = 1
                        elif ((thisResp.keys == '1') or (thisResp.keys == '1')):
                            thisResp.corr = 1
                        else:
                            thisResp.corr = 0
                    if corr == 1:
                        if ((thisResp.keys == corr) or (thisResp.keys == str(corr))):
                            thisResp.corr = 1
                        elif ((thisResp.keys == 'left') or (thisResp.keys == 'left')):
                            thisResp.corr = 1
                        else:
                            thisResp.corr = 0
                    if corr == 'right':
                        if ((thisResp.keys == corr) or (thisResp.keys == str(corr))):
                            thisResp.corr = 1
                        elif ((thisResp.keys == '2') or (thisResp.keys == '2')):
                            thisResp.corr = 1
                        else:
                            thisResp.corr = 0    
                    if corr == 2:
                        if ((thisResp.keys == corr) or (thisResp.keys == str(corr))):
                            thisResp.corr = 1
                        elif ((thisResp.keys == 'right') or (thisResp.keys == 'right')):
                            thisResp.corr = 1
                        else:
                            thisResp.corr = 0
                    break
                elif CounterBalFlag == 'True':
                    if corr == 'left':
                        if ((thisResp.keys == corr) or (thisResp.keys == str(corr))):
                            thisResp.corr = 0
                        elif ((thisResp.keys == '1') or (thisResp.keys == '1')):
                            thisResp.corr = 0
                        else:
                            thisResp.corr = 1
                    if corr == 1:
                        if ((thisResp.keys == corr) or (thisResp.keys == str(corr))):
                            thisResp.corr = 0
                        elif ((thisResp.keys == 'left') or (thisResp.keys == 'left')):
                            thisResp.corr = 0
                        else:
                            thisResp.corr = 1
                    if corr == 'down':
                        if ((thisResp.keys == corr) or (thisResp.keys == str(corr))):
                            thisResp.corr = 0
                        elif ((thisResp.keys == '2') or (thisResp.keys == '2')):
                            thisResp.corr = 0
                        else:
                            thisResp.corr = 1    
                    if corr == 2:
                        if ((thisResp.keys == corr) or (thisResp.keys == str(corr))):
                            thisResp.corr = 0
                        elif ((thisResp.keys == 'right') or (thisResp.keys == 'right')):
                            thisResp.corr = 0
                        else:
                            thisResp.corr = 1                
                    break
               # This should turn off the dots if there has been a response
                
            if countDown.getTime() > 0:
                pass       
            else:
                continueRoutine = False
        
        GreenCross.setAutoDraw(False)
        RedCross.setAutoDraw(True)
        win.flip()
        while countDown.getTime() > 0:    
            pass
        # prepare the cross hair

#        if thisResp.rt == -99:
#            print("In the IF part")
#            GreenCross.setAutoDraw(False)
#            RedCross.setAutoDraw(True)
#        else:
#            print("In the ELSE part")
#            GreenCross.setAutoDraw(False)
#            RedCross.setAutoDraw(True)
#            countDown.add(ProbeOnTime - thisResp.rt)
#        # take the dot off the screen
#        print("Remove dots")
#        win.flip()
#        print(countDown.getTime())
        countDown.add(ITITime)

        RedCross.setAutoDraw(False)
        
        print("Checking for responses")
            # Change the response to zero and one for later pivot tables
        CorrectResp = 0
        RT = thisResp.rt
        # If there is no response then the RT is an empty list
        if type(RT) == list:
            RT = 0.0
        if thisResp.corr == 1:
            CorrectResp = 1
            CorrectRT = RT
        else:
            CorrectRT = 0
        
        print(RT)
        print(CorrectRT)
        dataFile.write('%i,%i,%s, %s, %i,%0.3f,%0.4f,%i, %i,' %(TrialCount,CurrentLoad, TrialStartTime, thisResp.keys, CorrectResp,RT,CorrectRT, ProbeList[TrialCount], ProbeLoc))
        for ii in Locations:
            dataFile.write('%i,'%(ii))
        dataFile.write('\n')
        trials.addData('CurrentTime',CurrentTime)
        trials.addData('Response.keys',thisResp.keys)
        trials.addData('Response.corr', thisResp.corr)
        if thisResp.keys != None:  # we had a response
            trials.addData('Response.rt', thisResp.rt)
        thisExp.nextEntry()
        print("Finished Trial")
        TrialCount += 1
        while countDown.getTime() > 0:
            pass
            
    WhiteCross.setAutoDraw(True)
    countDown.add(InterBlockTime - 3)
    while countDown.getTime() > 0:
        pass
    WhiteCross.setAutoDraw(False)    
    win.flip()
# Turn on the countdown timer
    BlockCount += 1    


dataFile.write(',,%s\n'%(RunningClock.getTime()))
textThankyou.setAutoDraw(True)
countDown.add(5)
win.flip()
while countDown.getTime() > 0:
    pass   
win.flip()

thisExp.saveAsWideText(filename+'.csv')    
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()    