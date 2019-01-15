
import datetime 
import numpy as np
import os
import fnmatch
import csv
import sys
import pandas
from dateutil.parser import parse
## TO DO 
# Calculate hit, miss, false alarm and correct rejection
# This will allow calculation of d-prime
# and Cohen's memory capacity K = S*(Hits - FA) where S is the size of the stimulus load
# 
# How does this apply to different task loads?
# How does this compare to the staircase design results?
# 
# Vogel EK, Machizawa MG. Neural activity predicts individual differences in visual working memory capacity. Nature. 2004;428(6984):748-751.
# 
# The cognitive capacities appear to be artifially low for people who made a mistake at the very beginning. 
# Can I re-calculate capacity using all but the first two reversals?
# This may provide a more stable measure.
#

sys.path.insert(0, '../CognitiveTasks')
# import xlsxwriter << install this and use it to create and comment in XLS files
class NCMParticipant(object):
    def __init__(self):
        # specifiy the participant object
        self.subid = -9999
        self.YOB = -9999
        self.MOB = -9999
        self.age = -9999
        self.sex = -9999
        self.ageGroup = -9999
        self.Ethnicity = -9999
        self.edu = -9999
        self.BDIscore = -9999
        self.GDSscore = -9999
        self.LoadLevels = 5;
        
    def MakeParticipant(self, DataList):
        self.RawData = DataList
        self.subid = DataList[9]
        try:
            self.MOB = int(DataList[10])
        except:
            self.MOB = 1
        self.YearPullDownMapping(DataList[11])
#        self.TestDate = datetime.datetime.strptime(DataList[2],'%m/%d/%y %H:%M:%S')
        self.TestDate = parse(DataList[2])#.strftime('%m/%d/%Y %H:%M')
#        self.TestDate = datetime.datetime.strptime(DataList[2],'%m/%d/%y %H:%M')        
        self.DateOB = datetime.datetime(self.YOB,self.MOB,1)
        self.age = self.TestDate - self.DateOB
        self.age = self.age.days/365.0
        self.sex = int(DataList[12])
        self.EducationMapping(DataList[46])
        self.ScoreBeckDepressionIndex(DataList[138:159])
        self.ScoreGeriatricDepressionIndex(DataList[159:189])
        
        self.PAAerobicMin = self.PAScore(DataList[289])
        self.PABicyclingMin = self.PAScore(DataList[287])
        self.PAJoggingMin = self.PAScore(DataList[285])
        self.PALapSwimMin = self.PAScore(DataList[290])
        self.PALowIntensityMin = self.PAScore(DataList[292])
        self.PARunningMin = self.PAScore(DataList[286])
        self.PATennisMin = self.PAScore(DataList[291])
        self.PAWalkHikeMin = self.PAScore(DataList[284])
        self.PAFOSCMapping(DataList[294])
#         # Now work with the Psychopy data
#         self.SubDir = self.FindPsychoPyFolder(self.subid)
#         self.DMSCapacity = self.ReadCapacity(self.SubDir, "CAPACITY_DMS")
#         self.FRTCapacity = self.ReadCapacity(self.SubDir, "CAPACITY_FRT")
#         self.FRTLoadList = self.CreateFRTList(self.FRTCapacity).split(' ')
#         self.DMSLoadList = self.CreateDMSList(self.DMSCapacity).split(' ')
#         self.ReadBlockData('DMS_Block','DMS',6)
#         self.ReadBlockData('FRT_Block','FRT',12)
# #        self.CalcThroughput('DMS')
#         self.StairCaseLoadAnalysis('DMSstair', 'DMS')
#        self.StairCaseLoadAnalysis('FRTstair', 'FRT')
        self.LoadNIHdata()
        # Load the DMS Staircase file
#        self.ReadStairData('DMS')
#        self.CalculateDMSCapacity()
        
                
    def FindPsychoPyFolder(self,subid):
        BaseDir = "../data"
        SubDir = -9999
        # List  folders
        ll = os.listdir(BaseDir)
        # Is this participant in the folder?
        try:
            PartIndex = ll.index(subid)
        except ValueError:
            PartIndex = -9
        if PartIndex >= 0 :
            SubDir = os.path.join(BaseDir,ll[PartIndex])
            # What files are in this participant folder?
        return SubDir


    def ReadCapacity(self,SubDir, SearchString):
        ll = os.listdir(SubDir)
        matching = fnmatch.filter(ll,'*'+SearchString+'*')
        if len(matching) > 0:
            InFile = os.path.join(SubDir,matching[0])
            fid = open(InFile,'r')
            Capacity = float(fid.readline())
            fid.close()
        else:
            Capacity = -9999
        return Capacity

    def ReadBlockData(self,SearchString,TaskTag,RowsPerLoad):
        MinRT = 0.25
        MaxRT = 3.0
        # To Do:
        # Clean up responses that are too fast < 0.25
        # Clean up responses that are outside the response time window of 3 seconds
        # Save total RT, correct RT and incorrect RT
        # Save number correct?
#        SearchString = 'DMS_Block'
#        TaskTag = 'DMS'
#        RowsPerLoad = 6
        ll = os.listdir(self.VisitDir)
        # This is used because I made a change to one of the tasks due to a bug and now
        # extra files are saved andthe structure of the data file has changed
        NewDMSFlag = False
        SearchFor = self.subid + '_'+ SearchString
        matching = fnmatch.filter(ll,SearchFor+'*.csv')
        # remove any files that end in Block or trials which come from the updated
        # DMS_Adaptive_v3 code
        #matchingBlock = fnmatch.filter(ll,SearchString+'*.csv')
        #matchingTrial = fnmatch.filter(ll,SearchString+'*trials.csv')
        #if len(matchingBlock) > 0:
        #    NewDMSFlag = True
            
        #matching = set(matching) - set(matchingBlock)
        #matching = list(set(matching) - set(matchingTrial))                
        matching = matching[-1]
        
        if len(matching) > 0:
            # open the file  
            fid = open(os.path.join(self.VisitDir,matching),'r')
            data = csv.reader(fid)
            # Read whole file into a list
            LL = list(data)
            fid.close()
            HeaderLine = LL[0]
            # find column containing accuracy/RT
            AccCol = HeaderLine.index("resp.corr")
            RTCol = HeaderLine.index("resp.rt")
            Acc = []
            for i in LL:
                Acc.append(i[AccCol])
            # remove the header line
            Acc.pop(0)
            Acc = np.array(Acc)
            # This next line does not work with the new files because of the blank lines after every block
            ##Acc = Acc.astype(np.float)
            RT = []
            for i in LL:
                RT.append(i[RTCol])
            # remove the header line
            RT.pop(0)   
            for i in range(0,self.LoadLevels):
                # The plus i at the end works with the new files because there is a blank line after 
                # every block
#                if NewDMSFlag is True:
                LoadRows = np.array(range(RowsPerLoad*i,RowsPerLoad*i+RowsPerLoad))+i
                #else:
                #    LoadRows = np.array(range(RowsPerLoad*i,RowsPerLoad*i+RowsPerLoad))
                loadRT = [RT[j] for j in LoadRows]

                                
                # Are there any failures to respond?
                # If so remove them
                NotFTR = []
                FTR = []
                count = 0
                for j in loadRT: 
                    if j=='':
                        FTR.append(count)                    
                    else:
                        NotFTR.append(count)
                    count+=1
                if not len(FTR) == 0:
                    loadRT = list(filter(None,loadRT)) # <<< List was added because of an update to the filter function 

                loadRT = np.array(loadRT)
                loadRT = loadRT.astype(np.float)
                    
                # For accuracy any FTRs need to be removed because they are 
                # coded as zero and not empty
                loadAcc = [Acc[j] for j in LoadRows]
                notFTRAcc = []
                if len(FTR) > 0:
                    for j in NotFTR:
                        notFTRAcc.append(loadAcc[j])
                else:
                    notFTRAcc = loadAcc
                notFTRAcc = np.array(notFTRAcc)
                notFTRAcc = notFTRAcc.astype(np.float)
                
                # Find responses within the time window
                CorRT = loadRT[notFTRAcc==1]
                CorRTOnTime = CorRT[(CorRT > MinRT) & (CorRT <= MaxRT)]

             # Only include trials where the response time was on time for calculating accuracy
                notFTRAcc = notFTRAcc[(np.array(loadRT).astype(np.float) > MinRT) & (np.array(loadRT).astype(np.float) <= MaxRT)]   
  
                # Write out response times
                OutStr = 'meanCorOnTimeRT%s_Load%02d'%(TaskTag,i+1)

                try:
                    exec("self.%s=%0.4f"%(OutStr,CorRTOnTime.mean()))
                except:
                    exec("self.%s=-9999"%(OutStr))
                    
                OutStr = 'stdCorOnTimeRT%s_Load%02d'%(TaskTag,i+1)
                try:
                    exec("self.%s=%0.4f"%(OutStr,CorRTOnTime.std()))
                except:
                    exec("self.%s=-9999"%(OutStr))
                    
                OutStr = 'FTR%s_Load%02d'%(TaskTag,i+1)
                try:
                    exec("self.%s=%d"%(OutStr,len(FTR)))
                except:
                    exec("self.%s=-9999"%(OutStr))
                                    
                OutStr = 'Acc%s_Load%02d'%(TaskTag,i+1)
                try:
                    exec("self.%s=%0.4f"%(OutStr,notFTRAcc.mean()))
                except:
                    exec("self.%s=-9999"%(OutStr))
                    
                OutStr = 'NOnTime%s_Load%02d'%(TaskTag,i+1)
                try:
                    exec("self.%s=%0.4f"%(OutStr,len(notFTRAcc)))
                except:
                    exec("self.%s=-9999"%(OutStr))

        else:
            # If the file was not found enter missing data value
            for i in range(0,self.LoadLevels):
                OutStr = 'Acc%s_Load%02d'%(TaskTag,i+1)
                exec("self.%s=%d"%(OutStr,-9999))
                OutStr = 'FTR%s_Load%02d'%(TaskTag,i+1)
                exec("self.%s=%d"%(OutStr,-9999))
                OutStr = 'meanRT%s_Load%02d'%(TaskTag,i+1)
                exec("self.%s=%d"%(OutStr,-9999))
                OutStr = 'stdRT%s_Load%02d'%(TaskTag,i+1)
                exec("self.%s=%d"%(OutStr,-9999))
                
    def StairCaseLoadAnalysis(self, SearchString, TaskTag):
        # SearchString='DMSstair'
        # TaskTag = 'DMS'
        #
        # The idea is to go through the staircase data and organize the trials based 
        # on their load level and to calculate some statistics at each load level.
        # These would be:
        # number of trials at each load
        # Accuracy per load
        # mean response time per load

        ll = os.listdir(self.SubDir)
        matching = fnmatch.filter(ll,SearchString+'*.csv')
        if len(matching) > 0:
            fid = open(os.path.join(self.SubDir,matching[0]),'rU')
            data = csv.reader(fid)
            # Read whole file into a list
            LL = list(data)
            fid.close()
            # open the file  
            data2 = pandas.read_csv(os.path.join(self.SubDir,matching[0]), names=LL[0])
            if TaskTag == 'DMS':
                print('DMS')
                loads = data2.Load.tolist()
            else:
                print('FRT')
                loads = data2.NoiseLevel.tolist()
            # remove the last few rows and the header line
            loads = loads[1:-3]
            # convert to an array
            loads = np.array(loads)
            # Convert to ints
            if TaskTag == 'DMS':
                loads = loads.astype(int)
            else:
                loads = loads.astype(float)
            Correct = data2.Correct.tolist()
            Correct = Correct[1:-3]
            Correct = np.array(Correct)
            Correct = Correct.astype(int)
            RT = data2.RT.tolist()
            RT = RT[1:-3]
            RT = np.array(RT)
            RT = RT.astype(float)        
            for CurLoad in range(0,9,1):
#                print(CurLoad)
                if TaskTag == 'FRT':
                    CorLoad = loads == (round((CurLoad*0.1)*10))/10
                    CorLoad = CorLoad & (Correct == 1)
                    CurNTrials = float((loads==((round((CurLoad*0.1)*10))/10)).sum())
                else:
                    CorLoad = loads == (CurLoad+1)
                    CorLoad = CorLoad & (Correct == 1)
                    CurNTrials = float((loads==(CurLoad+1)).sum())
                # This was put here because I was getting an error if there were no trials at a load level
                if CurNTrials != 0.0:
                    CurAcc = float(CorLoad.sum()/CurNTrials)
                    CurRT = RT[CorLoad].mean()  
                else:
                    CurAcc = -9999
                    CurRT = -9999
                #print CurAcc
                #print CurRT  
                if TaskTag == 'DMS':
                    OutStr = TaskTag+"stair_"+str(CurLoad+1)+"_N"
                else:
                    OutStr = TaskTag+"stair_"+str(CurLoad)+"_N"
                exec("self.%s=%d"%(OutStr,CurNTrials))
                if TaskTag == 'DMS':
                    OutStr = TaskTag+"stair_"+str(CurLoad+1)+"_Acc"
                else:
                    OutStr = TaskTag+"stair_"+str(CurLoad)+"_Acc"
                if not np.isnan(CurAcc) and not np.isinf(CurAcc):
                    exec("self.%s=%0.4f"%(OutStr,CurAcc))
                else:
                    exec("self.%s=%d"%(OutStr,-9999))
                if TaskTag == 'DMS':
                    OutStr = TaskTag+"stair_"+str(CurLoad+1)+"_RT"
                else:
                    OutStr = TaskTag+"stair_"+str(CurLoad)+"_RT"
                if not np.isnan(CurRT):
                    exec("self.%s=%0.4f"%(OutStr,CurRT))            
                else:
                    exec("self.%s=%d"%(OutStr,-9999))        
    
    def CalcThroughput(self,TaskTag):
        for i in range(0,self.LoadLevels):
            OutStr = 'Acc%s_Load%02d'%(TaskTag,i+1)
            exec("CurrAcc=self.%s"%(OutStr))
            exec("CurrLoad=int(self.%sLoadList[%d])"%(TaskTag,i))
            CurrTP = ((CurrAcc-0.5)/0.5)*CurrLoad
            OutStr = 'TP%s_Load%02d'%(TaskTag,i+1)
            exec("self.%s=%0.3f"%(OutStr,CurrTP))
            
    # These are copy and pasted from the main PsychoPy task
    # They should be imported ...
    def CreateDMSList(self, DMSCapacity):
        Limit = int(round(float(DMSCapacity) + 1))
        if Limit > 9:
            Limit = 9
        elif Limit < 6:
            Limit = 6
        DMSList = {}
        DMSList['6']=[1,2,3,4,5,6]
        DMSList['7']=[1,2,3,5,6,7]
        DMSList['8']=[1,2,4,5,7,8]
        DMSList['9']=[1,2,4,6,8,9]    
        OutList = DMSList[str(Limit)]
        OutList = ' '.join(str(e) for e in OutList)
        return OutList

    def CreateFRTList(self, FRTCapacity):
        Limit = np.float(FRTCapacity)*1.25
        #FRTList = range(0,6,1)Limit,Limit/(6-1))
        FRTList = np.array(range(0,6,1))/(6.0-1)*Limit
        # Convert this array to a string so it can be passed as an argument
        FRTList = ' '.join(str(e) for e in FRTList)
        return FRTList                
                                                                               
    def YearPullDownMapping(self,YOBindex):
        # The YOB pull down menu has changed a few times so I had to export 
        # the from survey monkey two times once with numeric values and once 
        # with the actual text values then I copy and pasted the YOB comlumn 
        # from the text to the numeric file.
        self.YOB = int(YOBindex)
        #OldRange = np.arange(1940,1960+1)
        #YoungRange= np.arange(1985,2001+1)        
        
        #AllRange = np.concatenate((OldRange , [-9999], YoungRange))
        #self.YOB = int(AllRange[int(YOBindex)-1])
        if self.YOB > 1985:
            self.ageGroup = 0
        else:
            self.ageGroup = 1
        
    def EducationMapping(self, EduIndex):
        EduRange = [-9999, 8,9,10,11,12,13,14,15,16,17,20,-8888,-7777,-6666]
        self.edu = EduRange[int(EduIndex)]
        """
        0	Less than 9th grade	8
        1	9th grade	9
        2	10th grade	10
        3	11th grade	11
        4	Graduated from high school	12
        5	1 year of college/university	13
        6	2 years of college/university	14
        7	3 or more years of college/university	15
        8	Graduated from college/university	16
        9	Some graduate school	17
        10	Completed graduate school	20
        11	I don't know	-8888
        12	Prefer not to answer	-9999
        13	Other (please specify)	-7777
        """
    def ScoreBeckDepressionIndex(self, BDIData):
        """
        INTERPRETING THE BECK DEPRESSION INVENTORY (BDI-II)
        Add up the score for each of the 21 questions by counting the number to the right of each
        question you marked. The highest possible total for the whole test would be sixty-three and
        the lowest possible score for the test would be zero. This would mean you circles zero on each
        question. You can evaluate your depression according to the Table below.
        Total Score Levels of Depression
        0-10 = These ups and downs are considered normal
        11-16 = Mild mood disturbance
        17-20 = Borderline clinical depression
        21-30 = Moderate depression
        31-40 = Severe depression
        over 40 = Extreme depression
        A PERSISTENT SCORE OF 17 OR ABOVE INDICATES THAT YOU MAY NEED
        TREATMENT.
        """
        # take all responses and convert them to an array. Then map them to be integers.
        # Sum the result and subtract 21.
        # The Survey has the left most answer as one and on the BDI it is zero.
        # Subtracting 21 makes this modification
#        if BDIData
        if not '' in BDIData:
            self.BDIscore = sum(map(int, np.array(BDIData)))-21
            
            
    def ScoreGeriatricDepressionIndex(self, GDSData):
        """ Yes is saved as a ONE
        No is saved as a TWO
        Score one point if the following responses are made and zero if this 
        choice was not made:
        2,1,1,1,2,1,  2,1,2,1,1,1,  1,1, 2,1,1,1,2,1,2,1,1,1,1,1,2,1,2,2
        
        Normal = 0 - 9
        Mild Depression = 10 - 19
        Sever Depression = 20 - 30
        """
        GDSAnswerKey = np.array([2,1,1,1,2,1,  2,1,2,1,1,1,  1,1, 2,1,1,1,2,1,2,1,1,1,1,1,2,1,2,2])
        if not '' in GDSData:
            GDSData = np.array(map(int, np.array(GDSData)))
            # How does this compare to the answer key
            self.GDSscore = sum(GDSAnswerKey==GDSData)


        
        
        
    """
    Notes from NBA paper analyses
        % The EX values correspond to time per week engaged in various activities.
        
        % The EX measures need to be recoded into time in hours
        rEX = EX331(ind,:);
        rEX(find(rEX == 1)) = 10/60;
        rEX(find(rEX == 2)) = 20/60;
        rEX(find(rEX == 3)) = 1;
        rEX(find(rEX == 4)) = 1.5;
        rEX(find(rEX == 5)) = 2.5;
        rEX(find(rEX == 6)) = 5;
        rEX(find(rEX == 7)) = 7;
        
        % recode based on METs
        MET = zeros(size(rEX));
        MET(:,1) = rEX(:,1).*3.5; % Walking or hiking
        MET(:,2) = rEX(:,2).*7; % Jogging (completing one mile in over ten minutes)
        MET(:,3) = rEX(:,3).*10; % Running (completing one mile in under ten minutes)
        MET(:,4) = rEX(:,4).*7; % Bicycling
        MET(:,5) = rEX(:,5).*6.5; % Aerobic exercise, aerobic dance, or using exercise machines
        MET(:,6) = rEX(:,6).*10; % Lap swimming
        MET(:,7) = rEX(:,7).*7; % Tennis, squash, or racquetball
        MET(:,8) = rEX(:,8).*2.5; % ;Low intensity exercise (such as yoga, stretching, and toning)
        MET(:,9) = FOSC331(ind); % stairs
        
        % Try a subset analysis based on different activities
        
        %ind = find(MET(:,2));
        
        % THe questionnire had this question:
        % 9. How many flights of stairs do you climb daily
        
        % None 1-2 3-4 5-9 10-14 more than 15
        % Recode FOSC
        rFOSC = FOSC331(ind);
        rFOSC(find(FOSC331(ind) == 1)) = 1.5;
        rFOSC(find(FOSC331(ind) == 2)) = 3.5;
        rFOSC(find(FOSC331(ind) == 3)) = 7;
        rFOSC(find(FOSC331(ind) == 4)) = 12;
        rFOSC(find(FOSC331(ind) == 5)) = 16;
        
        
        rFOSCPerWeek = rFOSC*7;
        StepsPerMinute = 70;
        rFOSCHoursPerWeek = rFOSCPerWeek/StepsPerMinute;
        MetsPerHourStairClimbing = 8.5;
        MET(ind,9) = rFOSCHoursPerWeek*MetsPerHourStairClimbing;
        
        % Map 
        uFOSC = [1; unique(rFOSC)];
        uFOSCMET = uFOSC*7;
        uFOSCMET = uFOSCMET/StepsPerMinute;
        uFOSCMET = uFOSCMET*MetsPerHourStairClimbing;
        [unique(rFOSC) unique(MET(:,9))] % stairs climber per week in METs
        
        % One flight of stairs per daya for a week is 0.85 METs
        % Walking
        [unique(rEX(:,1)) unique(MET(:,1))] % walking quantity in METS per week
    """
    
    def PAScore(self,PAIndex):
        if PAIndex == '':
            PAIndex = '0'
        PARange = [-9999, 0, 10/60.0, 20/60.0, 1, 1.5, 2.5, 4.5, 7, -8888, -7777]
        return PARange[int(PAIndex)]
        """
        1: None 
        2: 1-19 min
        3: 20-59 min 
        4: 1 hr 
        5: 1.5 hr 
        6: 2-3 hr 
        7: 4-5 hr 
        8: 7+ hr
        9: I don't know
        10: Prefer not to answer
        """
        
                        
    def PAFOSCMapping(self, FOSCIndex):
        """3. How many flights of stair * do you climb daily?
            1:  None                0 
            2:  1-2                 1.5
            3:  3-4                 3.5
            4:  5-9                 7
            5:  10-14               12
            6:  15+                 16
            I don't know            -8888
            Prefer not to answer    -9999
            """
        FOSCRange = [-9999,0,1.5,3.5,7,12,16,-8888,-7777]
        self.FOSC = FOSCRange[int(FOSCIndex)]


    def ReadStairData(self, TaskTag):
        ll = os. listdir(self.VisitDir)
        matchingStair = fnmatch.filter(ll,'*'+TaskTag+'_Stair*.csv')
        if len(matchingStair) > 0:
            fid = open(os.path.join(self.VisitDir,matchingStair[0]),'rU')
            data = csv.reader(fid)
            # Read whole file into a list
            LL = list(data)
            fid.close()
            
            HeaderLine = LL[0]
            # Cycle over file and extract all of the trials and create a list of dictionaries
            # RT, Accuracy, Load, Positive Trial, Serial Position, Screen Position
            # Remover Header line
            LL = LL[1:]
            EndReason = LL[-3]
            EndHeader = LL[-2]
            EndSummary = LL[-1]
            LL = LL[0:-3]
                    
            data = []
            for j in LL:
                tempDict = dict()
                tempDict['RT'] = float(j[6])
                tempDict['ProbeType'] = int(j[8])
                StudySet = j[9]
                ProbeLet = j[10]
                tempDict['SerialPos'] = StudySet.find(ProbeLet) + 1
                tempDict['Load'] = int(j[1])
                tempDict['Acc'] = int(j[4])
                # Map the probe letter to the screen position
                tempDict['ScreenPos'] = self.ScreenPositionMap(int(j[1]),str(StudySet.find(ProbeLet)))
                tempDict['ScreenRow'] = self.ScreenPositionRowCol(str(tempDict['ScreenPos']))[0]
                tempDict['ScreenCol'] = self.ScreenPositionRowCol(str(tempDict['ScreenPos']))[1]
                data.append(tempDict)
            self.LongStaircaseData = data
        else:
            self.LongStaircaseData = -9999
#            print(" >>> Cannot Find Staircase file <<<")
             
    def ReadVSTMStairData(self, TaskTag):
        ll = os. listdir(self.SubDir)
        matchingStair = fnmatch.filter(ll,TaskTag+'stair*.csv')
        if len(matchingStair) > 0:
            fid = open(os.path.join(self.SubDir,matchingStair[0]),'rU')
            data = csv.reader(fid)
            # Read whole file into a list
            LL = list(data)
            fid.close()
        else:
            print(" >>> Cannot Find Staircase file <<<")
        HeaderLine = LL[0]
        # Cycle over file and extract all of the trials and create a list of dictionaries
        # RT, Accuracy, Load, Positive Trial, Serial Position, Screen Position
        # Remover Header line
        LL = LL[1:]
        EndReason = LL[-3]
        EndHeader = LL[-2]
        EndSummary = LL[-1]
        LL = LL[0:-3]
                
        data = []
        for j in LL:
            tempDict = dict()
            tempDict['RT'] = float(j[3])

            tempDict['Load'] = int(j[1])
            tempDict['Acc'] = int(j[2])
            data.append(tempDict)
        self.VSTMLongStaircaseData = data

    def ScreenPositionRowCol(self, ScreenPos):
        return {
            '1':[1,1],                
            '2':[1,2],
            '3':[1,3],
            '4':[2,1],
            '5':[2,2],
            '6':[2,3],
            '7':[3,1],
            '8':[3,2],
            '9':[3,3],
                }.get(ScreenPos, [-1,-1])

    def ScreenPositionMap(self, Load, SerialPos):
        if Load == 1:
            return {
                '0': 5,
                }.get(SerialPos,-1)
        elif Load == 2:
            return {
                '0' : 4,
                '1' : 6,
                }.get(SerialPos,-1)
        elif Load == 3:
            return {
                '0' : 4,
                '1' : 5,
                '2' : 6,
                }.get(SerialPos,-1)
        elif Load == 4:
            return {
                '0' : 1,
                '1' : 3,
                '2' : 7,
                '3' : 9,
                }.get(SerialPos,-1)
        elif Load == 5:
            return {
                '0' : 1,
                '1' : 3,
                '2' : 5,
                '3' : 7,
                '4' : 9,
                }.get(SerialPos,-1)
        elif Load == 6:
            return {
                '0' : 1,
                '1' : 2,
                '2' : 3,
                '3' : 7,
                '4' : 8,
                '5' : 9,
                }.get(SerialPos,-1)      
        elif Load == 7:
            return {
                '0' : 1,
                '1' : 2,
                '2' : 3,
                '3' : 5,
                '4' : 7,
                '5' : 8,
                '6' : 9,
                }.get(SerialPos,-1)             
        elif Load == 8:
            return {
                '0' : 1,
                '1' : 2,
                '2' : 3,
                '3' : 4,
                '4' : 6,
                '5' : 7,
                '6' : 8,
                '7' : 9,
                }.get(SerialPos,-1)            
        elif Load == 9:
            return {
                '0' : 1,
                '1' : 2,
                '2' : 3,
                '3' : 4,
                '4' : 5,
                '5' : 6,
                '6' : 7,
                '7' : 8,
                '8' : 9,
                }.get(SerialPos,-1)           
                
            
        
        
            
        

    def ReadBlockDataLong(self, SearchString, TaskTag, RowsPerLoad):
        # SearchString = 'DMS_Block'
#        TaskTag = 'DMS'
 #       RowsPerLoad = 6
        ll = os. listdir(self.SubDir)
        # This is used because I made a change to one of the tasks due to a bug and now
                # extra files are saved andthe structure of the data file has changed
        NewDMSFlag = False
        matching = fnmatch.filter(ll,SearchString+'*.csv')
                # remove any files that end in Block or trials which come from the updated
                # DMS_Adaptive_v3 code
        matchingBlock = fnmatch.filter(ll,SearchString+'*Blocks.csv')
        matchingTrial = fnmatch.filter(ll,SearchString+'*trials.csv')
        
        if len(matchingBlock) > 0:
            NewDMSFlag = True
                
        matching = set(matching) - set(matchingBlock)
        matching = list(set(matching) - set(matchingTrial))      
        
        fid = open(os.path.join(self.SubDir,matching[0]),'rU')
        data = csv.reader(fid)
        # Read whole file into a list
        LL = list(data)
        fid.close()
        # Remove the header row
        HeaderRow = LL[0]
        AccIndex = HeaderRow.index('resp.corr')
        RTIndex = HeaderRow.index('resp.rt')        
        LL = LL[1:]
        data = []
        for i in LL:
            # Check the row to make sure there is data in it
            if len(i[0]) > 0:
                data.append(self.BlockDataFindPosition(i, AccIndex, RTIndex))
        self.LongBlockData = data
        
    def BlockDataFindPosition(self, DataRow, AccIndex, RTIndex):
        # Convert to an array
        DataRow = np.array(DataRow)
        tempDict = dict()

        StudySetIndices = [7,8,6,2,1,10,3,4,0]
        # Extract the studey set from the elements of this data row
        StudySet = DataRow[StudySetIndices]
        # concatenate the array of elements
        StudySet = ''.join(StudySet)
        # remove the stars
        StudySet = StudySet.replace('*','')        
        ProbeLet = DataRow[5].upper()
        tempDict['Load'] = len(StudySet)
        if StudySet.find(ProbeLet) >= 0:
            tempDict['ProbeType'] = 1
        else:        
            tempDict['ProbeType'] = -1            
        tempDict['ScreenPos'] = StudySet.find(ProbeLet)
        tempDict['SerialPos'] = StudySet.find(ProbeLet) + 1

        tempDict['Acc'] = int(DataRow[AccIndex])
        if len(DataRow[RTIndex]) > 0:
            tempDict['RT'] = float(DataRow[RTIndex])
        else:
            tempDict['RT'] = -9999
        # Map the probe letter to the screen position
        tempDict['ScreenPos'] = self.ScreenPositionMap(tempDict['Load'],str(StudySet.find(ProbeLet)))
        tempDict['ScreenRow'] = self.ScreenPositionRowCol(str(tempDict['ScreenPos']))[0]
        tempDict['ScreenCol'] = self.ScreenPositionRowCol(str(tempDict['ScreenPos']))[1]

        return tempDict
                                                                    
    def LoadNIHdata(self):
        # Take the data file from the NIH export and run a pivot table on it. 
        NIHFile = "../data/NIHToolboxExports/AssessmentDataAll.csv"
        fid = open(NIHFile,'rU')
        data = csv.reader(fid)
        # Read whole file into a list
        LL = list(data)
        fid.close()
        HeaderLine = LL[0]
        HeaderLine = HeaderLine[1:]
        # remove header line
        LL = LL[1:]
        subid = []

        for i in LL:
            subid.append(i[0])

        # Find this subject
        try:
            SubIndex = subid.index(self.subid)      
            ThisSubData = LL[SubIndex]
            # remove subid 
            ThisSubData = ThisSubData[1:]
            # Create a dictionary to hold all the NIH values
            self.NIHToolbox = {}
            for i in HeaderLine:
                exec("self.NIHToolbox['%s']=%s"%(i,ThisSubData[HeaderLine.index(i)]))
        except:
            print("This subject is not in the NIH list")
            self.NIHToolbox = {}
            for i in HeaderLine:
                exec("self.NIHToolbox['%s']=%s"%(i,-9999))

            

            
    def WriteLongDataToFile(self, fidOut):  

        for i in self.LongBlockData:
            fidOut.write("%s,%d,%0.2f,%d,%d,%0.3f,%0.3f,%d,"%(self.subid,self.sex,self.age,self.ageGroup,self.edu,self.FRTCapacity,self.DMSCapacity,1))
            fidOut.write('%d,%d,%d,%0.4f,%d,%d,%d,%d,'%(i['Load'],i['Acc'],i['ProbeType'],i['RT'],i['ScreenCol'],i['ScreenRow'],i['ScreenPos'],i['SerialPos']))
            for k in self.NIHToolbox.keys():
                fidOut.write('%0.4f,'%(self.NIHToolbox[k]))
            fidOut.write("\n")
            
        for i in self.LongStaircaseData:
            fidOut.write("%s,%d,%0.2f,%d,%d,%0.3f,%0.3f,%d,"%(self.subid,self.sex,self.age,self.ageGroup,self.edu,self.FRTCapacity,self.DMSCapacity,2))
            fidOut.write('%d,%d,%d,%0.4f,%d,%d,%d,%d,'%(i['Load'],i['Acc'],i['ProbeType'],i['RT'],i['ScreenCol'],i['ScreenRow'],i['ScreenPos'],i['SerialPos']))
            for k in self.NIHToolbox.keys():
                fidOut.write('%0.4f,'%(self.NIHToolbox[k]))
            fidOut.write("\n")

#        fidOut.write("%s,%d,%0.2f,%d,%d,%0.3f,%0.3f,%d,%s,%0.4f,%s,"%(self.subid,self.sex,self.age,self.ageGroup,self.edu,self.FRTCapacity,self.DMSCapacity)
    
    def CalculateDMSCapacity(self):
        StairLoad = []
        # Extract just the load values form the staircase data
        for i in self.LongStaircaseData:
            StairLoad.append(i['Load'])
            
        Rev = []
        # find out when the load is increasing and when it is decreasing
        Up = False
        Down = False
        Previous = 0
        for i in StairLoad:
            if i > Previous:
                Up = True
                Rev.append(1)
            elif i < Previous:
                Down = True
                Rev.append(-1)
            else:
                Rev.append(Rev[-1])
            Previous = i
        # any changes in the direction are reversals
        Rev = np.diff(Rev)
        Rev = np.nonzero(Rev)[0]
        RevLoads = np.array(StairLoad)[Rev]
        Capacity = RevLoads.mean()
        # Caluclate a trimmed capacity also excluding the first two reversals
        TrimRevLoads = RevLoads[2:]
        TrimCapacity = TrimRevLoads.mean()
        self.DMS['RecalcCapacity'] = Capacity
        self.DMS['TrimDMSCapacity'] = TrimCapacity

    def CalculateVSTMCapacity(self):
        StairLoad = []
        # Extract just the load values form the staircase data
        for i in self.VSTMLongStaircaseData:
            StairLoad.append(i['Load'])
            
        Rev = []
        # find out when the load is increasing and when it is decreasing
        Up = False
        Down = False
        Previous = 0
        for i in StairLoad:
            if i > Previous:
                Up = True
                Rev.append(1)
            elif i < Previous:
                Down = True
                Rev.append(-1)
            else:
                Rev.append(Rev[-1])
            Previous = i
        # any changes in the direction are reversals
        Rev = np.diff(Rev)
        Rev = np.nonzero(Rev)[0]
        RevLoads = np.array(StairLoad)[Rev]
        Capacity = RevLoads.mean()
        # Caluclate a trimmed capacity also excluding the first two reversals
        TrimRevLoads = RevLoads[2:]
        TrimCapacity = TrimRevLoads.mean()
        self.RecalcCapacity = Capacity
        self.TrimVSTMCapacity = TrimCapacity
 
               
    def __str__(self):
        print("Participant ID: %s"%(self.subid))
        print("Test date: %s"%(self.TestDate))
        print("Age: %0.2f"%(self.age))
        print("Sex: %d"%(self.sex))
        print("Edu: %d"%(self.edu))
        print("BDI: %d out of 63"%(self.BDIscore))
        print("GDS: %d out of 63"%(self.GDSscore))
        print("Physial Activity (hours)")
        print("  Aerobic: %0.2f"%(self.PAAerobicMin))
        print("  Bicycling : %0.2f"%(self.PABicyclingMin))
        print("  Jogging: %0.2f"%(self.PAJoggingMin))
        print("  Lap Swim: %0.2f"%(self.PALapSwimMin))
        print("  Low Intensity: %0.2f"%(self.PALowIntensityMin))
        print("  Running: %0.2f"%(self.PARunningMin))
        print("  Tennis: %0.2f"%(self.PATennisMin))
        print("  Walk-Hike: %0.2f"%(self.PAWalkHikeMin))
        print("Flights of Stairs Climbed daily: %0.2f"%(self.FOSC))
        print
        print("Delayed Match to Sample Task")
        if not self.DMSCapacity == -9999:
            print("  Capacity: %0.4f"%(self.DMSCapacity))
            print("          meanRT   Acc   FTR")
            print("  Load %s: %0.3f, %0.2f,   %d"%(self.DMSLoadList[0],self.meanRTDMS_Load01,self.AccDMS_Load01,self.FTRDMS_Load01)) 
            print("  Load %s: %0.3f, %0.2f,   %d"%(self.DMSLoadList[1],self.meanRTDMS_Load02,self.AccDMS_Load02,self.FTRDMS_Load02)) 
            print("  Load %s: %0.3f, %0.2f,   %d"%(self.DMSLoadList[2],self.meanRTDMS_Load03,self.AccDMS_Load03,self.FTRDMS_Load03)) 
            print("  Load %s: %0.3f, %0.2f,   %d"%(self.DMSLoadList[3],self.meanRTDMS_Load04,self.AccDMS_Load04,self.FTRDMS_Load04)) 
            print("  Load %s: %0.3f, %0.2f,   %d"%(self.DMSLoadList[4],self.meanRTDMS_Load05,self.AccDMS_Load05,self.FTRDMS_Load05)) 
            print("  Load %s: %0.3f, %0.2f,   %d"%(self.DMSLoadList[5],self.meanRTDMS_Load06,self.AccDMS_Load06,self.FTRDMS_Load06)) 
        else:
            print(" ---> No Data <--- ")
        print
        print("Degraded Faces Task")
        if not self.FRTCapacity == -9999:
            print("  Capacity: %0.4f"%(self.FRTCapacity))
            print("                  meanRT   Acc   FTR")
            print("  Load %8s: %0.3f, %0.2f,   %d"%(self.FRTLoadList[0],self.meanRTFRT_Load01,self.AccFRT_Load01,self.FTRFRT_Load01)) 
            print("  Load %8s: %0.3f, %0.2f,   %d"%(self.FRTLoadList[1],self.meanRTFRT_Load02,self.AccFRT_Load02,self.FTRFRT_Load02)) 
            print("  Load %8s: %0.3f, %0.2f,   %d"%(self.FRTLoadList[2],self.meanRTFRT_Load03,self.AccFRT_Load03,self.FTRFRT_Load03)) 
            print("  Load %8s: %0.3f, %0.2f,   %d"%(self.FRTLoadList[3],self.meanRTFRT_Load04,self.AccFRT_Load04,self.FTRFRT_Load04)) 
            print("  Load %8s: %0.3f, %0.2f,   %d"%(self.FRTLoadList[4],self.meanRTFRT_Load05,self.AccFRT_Load05,self.FTRFRT_Load05)) 
            print("  Load %8s: %0.3f, %0.2f,   %d"%(self.FRTLoadList[5],self.meanRTFRT_Load06,self.AccFRT_Load06,self.FTRFRT_Load06)) 
        else:
            print(" ---> No Data <--- ")
        return ""

    
"""
    SubID = 10
MOB = 11
YOB = 12
Sex = 13
SexOther = 14
Ethincity = range(15,21+1,1)
Language = range(22,46+1,1)
Education = 47
HandWriting = range(49,54+1,1)
HandDrawing
HandThrowing
HandScissors
HandToothbrush
HandKnife
HandSpoon
HandBroom
HandMatch
HandBox
HandCompMouse
HandDoor
HandHammer
HandBrush
HandCup
BeckDepression = range(139,159+1,1)
GeriatricDepression = range(160,189+1,1)
FOSC = 295
Eyesight = 296
"""

""" SCRAPS
    def CreateLongDataFRT(self,SubDir, SearchString, TaskTag, RowsPerLoad, fidOut):
        
        ll = os. listdir(SubDir)
        # This is used because I made a change to one of the tasks due to a bug and now
                # extra files are saved andthe structure of the data file has changed
        NewDMSFlag = False
        matching = fnmatch.filter(ll,SearchString+'*.csv')
                # remove any files that end in Block or trials which come from the updated
                # DMS_Adaptive_v3 code
        matchingBlock = fnmatch.filter(ll,SearchString+'*Blocks.csv')
        matchingTrial = fnmatch.filter(ll,SearchString+'*trials.csv')
        
        if len(matchingBlock) > 0:
            NewDMSFlag = True
                
        matching = set(matching) - set(matchingBlock)
        matching = list(set(matching) - set(matchingTrial))      
        
        
        
        fid = open(os.path.join(SubDir,matching[0]),'rb')
        data = csv.reader(fid)
        # Read whole file into a list
        LL = list(data)
        fid.close()
        
        
        HeaderLine = LL[0]
                    # find column containing accuracy/RT
        AccCol = HeaderLine.index("resp.corr")
        RTCol = HeaderLine.index("resp.rt")
        Acc = []
        for i in LL:
            Acc.append(i[AccCol])
                    # remove the header line
        Acc.pop(0)
        Acc = np.array(Acc)
                    # This next line does not work with the new files because of the blank lines after every block
                    ##Acc = Acc.astype(np.float)
        RT = []
        for i in LL:
            RT.append(i[RTCol])
        # remove the header line
        RT.pop(0)   
        for i in range(0,self.LoadLevels):
            # The plus i at the end works with the new files because there is a blank line after 
            # every block
            if NewDMSFlag is True:
                LoadRows = np.array(range(RowsPerLoad*i,RowsPerLoad*i+RowsPerLoad))+i
            else:
                LoadRows = np.array(range(RowsPerLoad*i,RowsPerLoad*i+RowsPerLoad))
            loadRT = [RT[j] for j in LoadRows]
            # Are there any failures to respond?
            NotFTR = []
            FTR = []
            count = 0
            for j in loadRT: 
                if j=='':
                    FTR.append(count)                    
                else:
                    NotFTR.append(count)
                count+=1
            if not len(FTR) == 0:
                loadRT = filter(None,loadRT) 
            loadRT = np.array(loadRT)
            loadRT = loadRT.astype(np.float)
            loadAcc = [Acc[j] for j in LoadRows]
        
            for ii in range(0,len(loadRT)):
                if TaskTag == 'DMS':
                    fidOut.write("%s,%d,%0.2f,%d,%d,%0.3f,%0.3f,%d,%s,%0.4f,%s,"%(self.subid,self.sex,self.age,self.ageGroup,self.edu,self.FRTCapacity,self.DMSCapacity,i,self.DMSLoadList[i],loadRT[ii],loadAcc[ii]))
                elif TaskTag == 'FRT':
                    fidOut.write("%s,%d,%0.2f,%d,%d,%0.3f,%0.3f,%d,%s,%0.4f,%s,"%(self.subid,self.sex,self.age,self.ageGroup,self.edu,self.FRTCapacity,self.DMSCapacity,i,self.FRTLoadList[i],loadRT[ii],loadAcc[ii]))
                for jj in self.NIHToolbox.itervalues():
                    fidOut.write("%0.4f,"%(jj))
                fidOut.write("\n")
"""