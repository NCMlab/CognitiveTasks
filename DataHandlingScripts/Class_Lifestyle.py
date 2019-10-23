# -*- coding: utf-8 -*-
# import datetime
from dateutil.parser import parse
import pandas as pd
import collections
import numpy as np


class Lifestyle(object):
# Define a class for the demographic data for each participant
    def __init__(self):
        self.PartID = -9999
        self.TestDate = -9999
        self.BDI = -9999
        self.GDS = -9999
        self.SCD = -9999

        
    def to_dict(self):
        outDict = collections.OrderedDict()
        outDict['PartID'] = self.PartID
        outDict['TestDate'] = self.TestDate
        outDict['BDI'] = self.BDI
        outDict['GDS'] = self.GDS
        outDict['SCD'] = self.SCD
        outDict['IADLClass'] = self.IADLClass
        outDict['IADLNumMiss'] = self.IADLNumMiss
        outDict['IADLMeal'] = self.IADLMeal
        outDict['IADLSomeDep'] = self.IADLSomeDep
        outDict['SlpSatis'] = self.SlpSatis
        outDict['SlpAvgHours'] = self.SlpAvgHours
        outDict['SlpFallAslp'] = self.SlpFallAslp
        outDict['SlpFallDurTrbl'] = self.SlpFallDurTrbl
        outDict['SlpFallProbDay'] = self.SlpFallProbDay
        outDict['SlpWake'] = self.SlpWake
        outDict['SlpWakeDurTrbl'] = self.SlpWakeDurTrbl
        outDict['SlpWakeProbDay'] = self.SlpWakeProbDay
        outDict['SlpActDreams'] = self.SlpActDreams
        outDict['SlpActDreamsDurTrbl'] = self.SlpActDreamsDurTrbl
        outDict['SlpLegDiscomfort'] = self.SlpLegDiscomfort
        outDict['SlpLegRest'] = self.SlpLegRest
        outDict['SlpLegRestDurTrbl'] = self.SlpLegRestDurTrbl
        outDict['SlpLegProbCount'] = self.SlpLegProbCount
        outDict['SlpLegDisappear'] = self.SlpLegDisappear
        outDict['SlpLegNight'] = self.SlpLegNight
        
        return outDict

    def ProcessData(self, LifeData):
        AllLife = []
        for i in LifeData:
            temp = Lifestyle()
            temp.ProcessOneRowData(i)
            AllLife.append(temp)
        # Convert the list of objects to a pandas dataframe    
        AllLife = pd.DataFrame.from_records([s.to_dict() for s in AllLife])
        # Set the index 
        self.AllLife = AllLife.set_index('PartID')    
        
            
    def ProcessOneRowData(self, OneRow):
        self.TestDate = parse(OneRow[2])
        self.PartID = int(OneRow[9])
        # Subjective Cognitive Decline
        # These questions have responses such as: Yes/No/I don't know/Prefer not to answer
        SCD1 = slice(65,69)
        SCD2 = slice(89, 107)
        self.SCD = self.SubjectCognitiveDecline(OneRow[SCD1], OneRow[SCD2])
        # Beck Depression Scale
        BDI = slice(201, 222)
        self.BDI = self.ScoreBeckDepressionIndex(OneRow[BDI])

        GDS = slice(222, 252)
        self.GDS = self.ScoreGeriatricDepressionIndex(OneRow[GDS])
        IADL = slice(32, 54)
        self.ScoreIADL(OneRow[IADL])
        Sleep = slice(11,30)
        self.ScoreSleep(OneRow[Sleep])

    def ScoreSleep(self, SleepData):
        # How satisfied or dissatisfied are you with your current sleep pattern?
        # 1 Very Satisfied
        # 2 Satisfied
        # 3 Neutral
        # 4 Dissatisfied
        # 5 Very Dissatisfied
        # 6 I don't know
        # 7 Prefer not to answer

        self.SlpSatis = SleepData[0]
        # During the past month, on average, how many hours of actual sleep did you get at night? (This may be different than the number of hours you spend in bed.)
        self.SlpAvgHours = SleepData[1]
        # Over the last month, how often did it take you more than 30 minutes to fall asleep?
            # 1 Never
            # 2 <1/week
            # 3 Once or twice/week
            # 4 3-5 times/week
            # 5 6-7 times/week
            # 6 I don't know
            # 7 Prefer not to answer
        self.SlpFallAslp = SleepData[2]
        # For how many months have you had this trouble going to sleep?
        self.SlpFallDurTrbl = SleepData[3]
        # To what extent do you consider your problem falling asleep to interfere with your daily functioning (for example, from daytime fatigue, ability to function at work/daily chores, concentration, memory, mood, etc.).
            # Not at all
            # A little
            # Somewhat
            # Much
            # Very much
            # I don't know
            # Prefer not to answer
        self.SlpFallProbDay = SleepData[4]
        # Over the last month, how often did you wake in the middle of the night or too early in the morning and found it difficult to fall asleep again?
        self.SlpWake = SleepData[5]
        # For how many months have you had this trouble staying asleep?
        self.SlpWakeDurTrbl = SleepData[6]
        # To what extent do you consider your problem staying asleep to interfere with your daily functioning (for example, from daytime fatigue, ability to function at work/daily chores, concentration, memory, mood, etc.)?
        self.SlpWakeProbDay = SleepData[7]
        # Over the last month, how often do you find it difficult to stay awake during your normal waking hours when you want to?
        self.SlpDayTired = SleepData[8]
        # For how many months have you had trouble staying awake?
        self.SlpDayTiredDurTrbl = SleepData[9]
        # To what extent do you consider your problem staying awake to interfere with your daily functioning?
        self.SlpDayTiredProbDay = SleepData[10]
        # Have you ever been told, or suspected yourself, that you seem to acted out your dreams" while asleep (for example, punching, flailing your arms in the air, making running movements, etc.)?
        self.SlpActDreams = SleepData[11]
        # For how many months have you had this "acting out" of your dreams?
        self.SlpActDreamsDurTrbl = SleepData[12]
        # Do you have, or have you sometimes experienced, recurrent, uncomfortable feelings or sensations in your legs while sitting or lying down?
        self.SlpLegDiscomfort = SleepData[13]
        # Do you have, or have you sometimes experienced, a recurrent need or urge to move your legs while sitting or lying down?
        self.SlpLegRest = SleepData[14]
        # For how many months have you had these uncomfortable feelings or urge to move?
        self.SlpLegRestDurTrbl = SleepData[15]
        # Over the last month, how many times (per week, on average) have you experienced these uncomfortable feelings or urge to move?
        self.SlpLegProbCount = SleepData[16]
        # Do these uncomfortable feelings or sensations in your legs, or the urge to move, disappear/improve when you are active or moving around?
        self.SlpLegDisappear = SleepData[17]
        # Are these uncomfortable feelings, or this urge to move, worse in the evening or at night compared with the morning?
        self.SlpLegNight = SleepData[18]
        
        
    def ScoreIADL(self, IADLData):
        # Questions about:
        # Telephone
        # Travel
        # Groceries
        # Prepare meals
        # Housework
        # Take your own medicines
        # Handle money
        IADLNumMiss = self.IADLCountMissingValues(IADLData)
        IADLMeal = self.MealPlanning(IADLData, [10, 11, 12])
        IADLSomeDep = self.IADLSomeDependence(IADLData)
        IADLClassTemp = self.IADLClassificationTemp(IADLSomeDep, IADLNumMiss)
        IADLClass = self.IADLClassification(IADLClassTemp, IADLMeal)
        self.IADLClass = IADLClass
        self.IADLNumMiss = IADLNumMiss
        self.IADLMeal = IADLMeal
        self.IADLSomeDep = IADLSomeDep
        
    def IADLClassification(self, IADLClassTemp, IADLMeal):
        # 5) OARS scale: Basic and Instrumental Activities of Daily Living Classification
        Cond3Flag1 = (IADLMeal == 1) and (IADLClassTemp == 0 or IADLClassTemp == 1)
        Cond3Flag2 = IADLClassTemp == 2
        if (IADLMeal == 0 and IADLClassTemp == 0):
            # No functional impairment
            IADLClass = 1
        elif (IADLMeal == 0 and IADLClassTemp == 1):
            # Mild impairment
            IADLClass = 2
        elif Cond3Flag1 or Cond3Flag2:
            # Moderate Impairment
            IADLClass = 3
        elif IADLClassTemp == 3:
            # Severe Impairment
            IADLClass = 4
        elif IADLClassTemp == 4:
            # Severe Impairment
            IADLClass = 5
        else: IADLClass = 9
        return IADLClass
        
    def IADLClassificationTemp(self, IADLSomeDep, IADLNumMissing):
        # 4) OARS scale: Basic and Instrumental Activities of Daily Living Classification (Excluding Meal
        # Preparation) – Intermediate Derived Variable
        Cond1Flag1 = ((IADLSomeDep == 1 or IADLSomeDep == 2 or IADLSomeDep == 3) and (IADLNumMissing == 0))
        Cond1Flag2 = ((IADLSomeDep == 1 or IADLSomeDep == 2) and (IADLNumMissing == 1))
        Cond1Flag3 = ((IADLSomeDep == 1) and (IADLNumMissing == 2))        
        Cond2Flag1 = ((IADLSomeDep == 4 or IADLSomeDep == 5) and (IADLNumMissing == 0))
        Cond2Flag2 = ((IADLSomeDep == 4) and (IADLNumMissing == 1))        
        Cond3Flag1 = ((IADLSomeDep == 6 or IADLSomeDep == 7) and (IADLNumMissing == 0))
        Cond3Flag2 = ((IADLSomeDep == 6) and (IADLNumMissing == 1))        
                                  
        if (IADLSomeDep == 0 and IADLNumMissing == 0):
            IADLClass = 0
        elif Cond1Flag1 or Cond1Flag2 or Cond1Flag3:
            IADLClass = 1
        elif Cond2Flag1 or Cond2Flag2:
            IADLClass = 2
        elif Cond3Flag1 or Cond3Flag2:
            IADLClass = 3
        elif IADLSomeDep >= 8:
            IADLClass = 4
        else:
            IADLClass = 9
        return IADLClass
        
    def IADLSumSomeDependence(self):
        # 6) OARS scale: Sum of Some Dependence and Complete Dependence (Excluding Meal
        # Preparation)
        # This is the same as the some dependence but treats missing values differently and it is skipped
        pass
        
    def IADLSomeDependence(self, IADLData):
        # 3) OARS scale: Sum of Some Dependence and Complete Dependence (Excluding Meal
        # Preparation) – Temporary Variable
        SomeDepTelephone = self.IADLSomeDependenceOneVariable(IADLData, [0,1,2])
        SomeDepTravels   = self.IADLSomeDependenceOneVariable(IADLData, [3,5,6])
        SomeDepGroceries = self.IADLSomeDependenceOneVariable(IADLData, [7,8,9])
        SomeDepHousework = self.IADLSomeDependenceOneVariable(IADLData, [13,14,15])
        SomeDepMoney     = self.IADLSomeDependenceOneVariable(IADLData, [0,1,2])
        return SomeDepTelephone + SomeDepTravels + SomeDepGroceries + SomeDepHousework + SomeDepMoney
                        
                
    def IADLSomeDependenceOneVariable(self, Data, Columns):
        # Is there any dependence?
        if Data[Columns[1]] == '1' or Data[Columns[2]] == '1':
            SomeDep = 1
        else:
            SomeDep = 0
        return SomeDep
        
        
    def MealPlanning(self, Data, Columns):
        # 2) OARS Scale: Some or Complete Dependence for Meal Preparation - Intermediate Derived
        # Variable
        # Meal planning
        if (Data[Columns[0]] != '1' and Data[Columns[1]] != '1' and Data[Columns[2]] != '1'):
            IADLMeal = -9999
        elif (Data[Columns[1]] == '1' or Data[Columns[2]] == '1'):
            IADLMeal = 1
        elif Data[Columns[0]] == '1':
            IADLMeal = 0
        return IADLMeal
                    
    def IADLCountMissingValues(self, IADLData):
        # OARS Scale: Number of Missing Items (Excluding Meal Preparation)
        # Find the number of missing data values
        # Telephone missing values
        TelephoneMissing = self.IADLFindMissingValue(IADLData, [0,1,2])   
        # Travel missing values
        TravelsMissing = self.IADLFindMissingValue(IADLData, [3,5,6])   
        # Groceries missing values
        GroceriesMissing = self.IADLFindMissingValue(IADLData, [7,8,9])   
        # Housework 
        HouseworkMissing = self.IADLFindMissingValue(IADLData, [13,14,15])          
        # Handle Money
        MoneyMissing = self.IADLFindMissingValue(IADLData, [19,20,21])     
        # How many missing values?
        IADLNumMissing = TelephoneMissing + TravelsMissing + GroceriesMissing + HouseworkMissing + MoneyMissing
        return IADLNumMissing

    def IADLFindMissingValue(self, Data, Columns):
        # Missing values occur when all three questions related to an activity are 
        # not equal to yes
        Missing = -9999
        if (Data[Columns[0]] != '1' and Data[Columns[1]] != '1' and Data[Columns[2]] != '1'):
            Missing = 1
        elif (Data[Columns[0]] == '1' or Data[Columns[1]] == '1' or Data[Columns[2]] == '1'):
            Missing = 0    
        return Missing
        
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
        BDIscore = -9999
        if not '' in BDIData:
            BDIData = [int(numeric_string) for numeric_string in BDIData]
            BDIscore = sum(BDIData) - 21
            #BDIscore = sum(map(int, np.array(BDIData)))-21
        return BDIscore
            
            
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
        GDSscore = -9999
        GDSAnswerKey = np.array([2,1,1,1,2,1,2,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,1,1,1,1,2,1,2,2])
        if not '' in GDSData:
            GDSData = [int(numeric_string) for numeric_string in GDSData]
            # GDSData = np.array(map(int, np.array(GDSData)))
            # How does this compare to the answer key
            GDSscore = sum(GDSAnswerKey==GDSData)
        return GDSscore
    
    def SexMapping(Value): 
        pass
    
    def GenderMapping():
        pass
        
    def SubjectCognitiveDecline(self, SCDdata1, SCDdata2):
        # The responses are spreadover two sections of the data file
        # Sum up the number of yes answers
        # 1 - Yes
        # 2 - No
        # 3 - I don't know
        # 4 - I prefer not to answer
        NumberOfYeses = 0
        for index in SCDdata1:
            if index == '1':
                NumberOfYeses += 1
        for index in SCDdata2:
            if index == '1':
                NumberOfYeses += 1
        return NumberOfYeses 
        
#         # Instrucmental Activities of Daily Living 
#     IADL = slice(32, 53)
#     # Loneliness 
#     # These questions have responses such as: Yes/More or less/No
#     Loneliness = slice(55, 60)
#   
#     # Subjective Cognitive Decline
#     # These questions have responses such as: Yes/No/I don't know/Prefer not to answer
#     SCD1 = slice(65,69)
#     SCD2 = slice(89, 107)
#     SCDscore = SubjectCognitiveDecline(i[SCD1], i[SCD2])
# 
#     # Social Participation
#     # I am not sure how to score this
#     # (109, 147), skip 126
#     #
#     # Social Networks
#     # 149, 198, skip 195
#     # Depression Scale
#     BDS = slice(201, 222)
#     # ScoreBeckDepressionIndex(i[BDS])
#     GDS = slice(222, 252)
#     ScoreGeriatricDepressionIndex(i[GDS])


        