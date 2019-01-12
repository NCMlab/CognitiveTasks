from psychopy import core, visual,  data, event, gui
from psychopy.tools.filetools import fromFile, toFile
import time, numpy, random
import os
import sys

task = 'FRTstair_'
expInfo = {'Max Trials':150, 'Participant ID':'', 'Session':'001'}
PartDataFolder = 'unorganized'
if len(sys.argv) > 1:
    expInfo['Participant ID'] = sys.argv[1]
    PartDataFolder = sys.argv[1]
else:
    dlg = gui.DlgFromDict(dictionary=expInfo)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = task
#expInfo['Participant ID'] = 'TestGUI'

FontColor = 'white'
BGColor = 'grey'

#make a text file to save data
#OutDir = '..' + os.sep + '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
DropBoxFolder = os.path.join('/Users','jasonsteffener','Dropbox','steffenercolumbia','Projects','MyProjects','NeuralCognitiveMapping')
# OutDir = '..' + os.sep + 'data' + os.sep + PartDataFolder + os.sep
OutDir = os.path.join(DropBoxFolder, 'data',PartDataFolder)

# If the subject path does not exist, than make it
if not os.path.exists(OutDir):
    os.mkdir(OutDir)
fileName = OutDir + os.sep + '%s%s_%s' % (task, expInfo['Participant ID'], expInfo['date'])

dataFile = open(fileName+'.csv', 'w') #a simple text file with 'comma-separated-values'
# Put a header line into the output fileName
dataFile.write('Trial,NoiseLevel,Resp,Correct,ElapsedTime,RT,CorrectRT\n')
StairCasefileName = os.path.join('data',expInfo['expName'] + expInfo['Participant ID'] + "_" + expInfo['date']+'Staircase.txt')

dataFile1=open(OutDir + os.sep+'CAPACITY_%s%s_%s.txt' % (task, expInfo['Participant ID'], expInfo['date']),'w')



# tempDataFile = open(os.path.join('data','temp'+fileName+'.txt'),'w')

#create window and stimuli
# win = visual.Window([800,600],allowGUI=True, monitor='testMonitor', units='norm')
# Full screen

win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=BGColor, colorSpace='rgb',
    blendMode='avg', useFBO=True, units = 'pix')
    
trials1 = data.TrialHandler(nReps=1, method='random', 
    trialList=data.importConditions('FRTPsychopyFiles/FRTStairCaseTrials.csv'),
    seed=None, name='trials1')

#and some handy clocks to keep track of time
globalClock = core.Clock()
trialClock = core.Clock()
ITItime = 0.5
MaxTime = 7 # minutes
MaxTrials = expInfo['Max Trials'] # End after this many trials
NumberOfReversals = 20

WaitText = visual.TextStim(win=win, name='WaitText',
    #text='Remember:\nPress [LEFT] when the pictures are of the same person\nPress [DOWN] if the pictures are NOT of the same person\n\nTry to respond as quickly and as accurately as possible.\n\n When you are ready to proceed press the [LEFT] or [DOWN] key.',
    text='Remember:\nPress [LEFT] for the SAME person.\nPress [RIGHT] for DIFFERENT people.\nThis time, you will NOT receive feedback after your responses.\n\nTry to respond as quickly and as accurately as possible.\n\nWhen you are ready to proceed, press the [LEFT] or [RIGHT] key.',
    font='Times New Roman',
    pos=(0, 0), height=40, wrapWidth=1000, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0);
CountDownText = visual.TextStim(win=win, name='CountDown',
    text='CountDown',
    font='Times New Roman',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color=FontColor, colorSpace='rgb', opacity=1,
    depth=0.0); 
    
#WhiteMask = visual.ImageStim(
#    win=win, name='WhiteMask',units='pix', 
#    image='WhiteMask.JPG', mask=None,
#    ori=0, pos=[-160,0], size=[300, 350],
#    color=[1,1,1], colorSpace='rgb', opacity=1.0,
#    flipHoriz=False, flipVert=False,
#    texRes=128, interpolate=True, depth=-1.0)
    
LEFTimage = visual.ImageStim(
    win=win, name='LEFTimage',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[-160,0], size=[300, 350],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
    
LEFTnoiseimage = visual.ImageStim(
    win=win, name='LEFTnoiseimage',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-160, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
RIGHTimage = visual.ImageStim(
    win=win, name='RIGHTimage',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[160, 0], size=[300, 350],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
RIGHTnoiseimage = visual.ImageStim(
    win=win, name='RIGHTnoiseimage',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(160, 0), size=(300, 350),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
# White ITI
whiteITI = visual.TextStim(win=win, name='whiteITI',
    text='+',
    font='Courier',
    pos=(0, 0), height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
    
staircase = data.StairHandler(startVal = 1,
                          stepType = 'lin', stepSizes=[0.1],
                          nUp=1, nDown=3,  # will home in on the 80% threshold
                          nReversals = NumberOfReversals,minVal = 0,maxVal = 1.0)
TrialCount = 1
CurrentTrial = 0
Ntrials = len(trials1.trialList)
# Create a random order to the trials1
RandomTrialOrder = numpy.random.permutation(Ntrials)
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
for thisStep in staircase:
    if CurrentTrial == Ntrials:
        CurrentTrial = 0
        # reset the randomness
        RandomTrialOrder = numpy.random.permutation(Ntrials)
    # Extract the parameters for this trial
    CurrentRandomTrial = RandomTrialOrder[CurrentTrial]
    thisTrials1 = trials1.trialList[CurrentRandomTrial]
    for paramName in thisTrials1.keys():
        exec('{} = thisTrials1[paramName]'.format(paramName))  

    print 'TrialN:' + str(CurrentTrial)+'ThisStep: '+str(thisStep)+'Corr: '+str(corr)
    FaceOpacity = thisStep                    
    NoiseOpacity = 1.0 - FaceOpacity
    # Set the opacity of the noise and face images
    # update component parameters for each repeat

    LEFTimage.setOpacity(FaceOpacity)
    LEFTimage.setImage(os.path.join('FRTPsychopyFiles',imageL))
    LEFTnoiseimage.setOpacity(NoiseOpacity)
    LEFTnoiseimage.setImage(os.path.join('FRTPsychopyFiles',imageLn))
    RIGHTimage.setOpacity(FaceOpacity)
    RIGHTimage.setImage(os.path.join('FRTPsychopyFiles',imageR))
    RIGHTnoiseimage.setOpacity(NoiseOpacity)
    RIGHTnoiseimage.setImage(os.path.join('FRTPsychopyFiles',imageRn))
    
    LEFTimage.draw()
    LEFTnoiseimage.draw()
    RIGHTimage.draw()
    RIGHTnoiseimage.draw()
# It may be possible to increase the brighness of an image using a white mask. 
# See this discussion: https://groups.google.com/forum/#!topic/psychopy-users/iXiC5tb4zC4
#    WhiteMask.setOpacity(0.1)
#    WhiteMask.draw()
    
    
    win.flip()
    trialClock.reset()
    # Get a response
    k = ['']
    KeyBoardCount = 0
    while k[0] not in ['escape', 'esc'] and KeyBoardCount < 1:
        k = event.waitKeys()
        KeyBoardCount += 1
        RT = trialClock.getTime()
    # Is this respone correct?
    #if k[-1] == str(thisTrials1.corr):
    if k[-1] == str(corr):    
        # YES
        print k[-1]
        thisResp = 1
    else:
        # NO
        print k[-1]
        thisResp = -1
    # Remove the faces and relace with the white cross hair
    whiteITI.draw()
    win.flip()
    core.wait(ITItime)
    
    staircase.addData(thisResp) 
        # Change the response to zero and one for later pivot tables
    CorrectResp = 0
    if thisResp == 1:
        CorrectResp = 1
    CorrectRT = 0
    if thisResp == 1:
        CorrectRT = RT
    
    dataFile.write('%i,%.2f,%s,%i,%0.3f,%0.4f,%0.4f\n' %(TrialCount,NoiseOpacity, k[-1],CorrectResp,globalClock.getTime(),RT,CorrectRT))

    CurrentTrial += 1
    # Check for an overall elapsed time and a total trial count
    # If either of these are exceeded, then end the experiment
    if len(staircase.data) > MaxTrials:
        win.close()
        EndFlag = 'MaxTrialsExceeded'
        dataFile.write('%s\n'%(EndFlag))
        Capacity = 1-numpy.mean(staircase.reversalIntensities)
        dataFile1.write('%0.4f'%(Capacity))
        print 
        print "Ending because the maximum number of trials was reached."
        print
        print "Capacity is: %0.4f"%(Capacity)        
        print "Number of reversals: %i"%(len(staircase.reversalPoints))
        dataFile.write('%s,%s,%s\n'%('NumTrials','NumReversals','Capacity'))
        dataFile.write('%i,%i,%0.4f\n'%(len(staircase.data),len(staircase.reversalPoints),Capacity))
        dataFile.close()
        # write capacity to a file so it can be read from the main program
        #tempDataFile.write('%0.4f'%(Capacity))
        #tempDataFile.close()
        staircase.saveAsText(StairCasefileName,delim=',')
        core.quit()
    if globalClock.getTime() > MaxTime*60:
        win.close()
        EndFlag = 'TimeExceeded'
        dataFile.write('%s\n'%(EndFlag))
        Capacity = 1-numpy.mean(staircase.reversalIntensities)
        dataFile1.write('%0.4f'%(Capacity))
        print 
        print "Ending because Time was exceeded."
        print
        print "Capacity is: %0.4f"%(Capacity)  
        print "Number of reversals: %i"%(len(staircase.reversalPoints))
        dataFile.write('%s,%s,%s\n'%('NumTrials','NumReversals','Capacity'))
        dataFile.write('%i,%i,%0.4f\n'%(len(staircase.data),len(staircase.reversalPoints),Capacity))
        dataFile.close()
        # write capacity to a file so it can be read from the main program
        #tempDataFile.write('%0.4f'%(Capacity))
        #tempDataFile.close()
        staircase.saveAsText(StairCasefileName,delim=',')
        core.quit()
    if "escape" in k:
        win.close()
        EndFlag = 'UserEscape'
        dataFile.write('%s\n'%(EndFlag))
        Capacity = 1-numpy.mean(staircase.reversalIntensities)
        dataFile1.write('%0.4f'%(Capacity))
        print
        print "Ending because Escape was pressed."
        print
        print "Capacity is: %0.4f"%(Capacity)  
        print "Number of reversals: %i"%(len(staircase.reversalPoints))
        dataFile.write('%s,%s,%s\n'%('NumTrials','NumReversals','Capacity'))
        dataFile.write('%i,%i,%0.4f\n'%(len(staircase.data),len(staircase.reversalPoints),Capacity))
        dataFile.close()
        # write capacity to a file so it can be read from the main program
        #tempDataFile.write('%0.4f'%(Capacity))
        #tempDataFile.close()
        staircase.saveAsText(StairCasefileName,delim=',')
        core.quit()
        
    TrialCount += 1
    #
print EndFlag


Capacity = 1-numpy.mean(staircase.reversalIntensities)
dataFile1.write('%0.4f'%(Capacity))
print
print "Capacity is: %0.4f"%(Capacity)     
print "Number of reversals: %i"%(len(staircase.reversalPoints))
dataFile.write('%s,%s,%s\n'%('NumTrials','NumReversals','Capacity'))
dataFile.write('%i,%i,%0.4f\n'%(len(staircase.data),len(staircase.reversalPoints),Capacity))
dataFile.close()
# write capacity to a file so it can be read from the main program
# tempDataFile.write('%0.4f'%(Capacity))
# tempDataFile.close()

staircase.saveAsText(StairCasefileName,delim=',')
win.close()
core.quit()