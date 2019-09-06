# -*- coding: utf-8 -*-
import pandas  as pd
import csv
import os
import numpy as np
import tkinter
from tkinter import messagebox
import datetime
from dateutil.parser import parse
import sys

__file__ = '/Users/jasonsteffener/Documents/GitHub/CognitiveTasks/DataHandlingScripts/ScoreSurveyMonkey.py'
#__file__ = '/home/jsteffen/GitHub/CognitiveTasks/DataHandlingScripts/ScoreSurveyMonkey.py'
# What folder is this file in?
dir_path = os.path.dirname(os.path.realpath(__file__))
# This will load the config file containing the location of the data folder
# If there is an error it means that the GUI program has not been run.
# The GUI checks to see if thie config file exists. If it does not then it is created.
print(dir_path)
sys.path.append(os.path.join(dir_path,'..','ConfigFiles'))
import NeuropsychDataFolder
# Load up the data location as a global variable
AllOutDataFolder = NeuropsychDataFolder.NeuropsychDataFolder

# From the Neuropsych folder change to the SurveyMonkey Folder
AllOutDataFolder = os.path.split(AllOutDataFolder)[0]
AllOutDataFolder = os.path.join(AllOutDataFolder, 'SurveyMonkey')
# At home lifestyle questionnaire
LifestyleFileName = 'Royal LifestyleBehavior.csv'
# At the lab demographics questionnaire
DemographicsFileName = 'Royal Participant Questionnaire.csv'
# At the lab PANAS questionnaire
PANASFileName = 'PANAS Questionnaire.csv'
LifestyleInputFile = os.path.join(AllOutDataFolder, LifestyleFileName)
DemographicsInputFile = os.path.join(AllOutDataFolder, DemographicsFileName)
PANASInputFile = os.path.join(AllOutDataFolder, PANASFileName)
# Check to see if all three files are present
AreAllThreeFilesPresent(LifestyleInputFile, DemographicsInputFile, PANASInputFile)
# Load the data from all the demographics data file
DemoH1, DemoH2, DemoData = ReadSMFileAsCSV(DemographicsInputFile)
# Load the data from the PANAS file
PANASH1, PANASH2, PANASData = ReadSMFileAsCSV(PANASInputFile)
# Load the data from the Lifestyle file
LifeH1, LifeH2, LifeData = ReadSMFileAsCSV(LifestyleInputFile)


def AreAllThreeFilesPresent(File1, File2, File3):
    # Check to see if all three datafiles are where they belong
    root = tkinter.Tk()
    root.withdraw()
    AllFilesFlag = True
    if not os.path.exists(File1):
        AllFilesFlag = False
        messagebox.showerror('Error', 'Missing Lifestyle questionnaire data file')
    if not os.path.exists(File2):
        AllFilesFlag = False
        messagebox.showerror('Error', 'Missing demographics data file')
    if not os.path.exists(File3):
        AllFilesFlag = False
        messagebox.showerror('Error', 'Missing PANAS data file')
    return AllFilesFlag
                

def ReadSMFileAsCSV(InputFile):
    # Open the file
    fid = open(InputFile,'r', encoding="ISO-8859-1")
    data = csv.reader(fid)
    # Read whole file into a list
    LL = list(data)
    # Close the file
    fid.close()
    # How many participants are in this data set
    NPart = len(LL) - 2
    # The surveyMonkey data has two header lines.
    # This makes it hard to use dataframes
    # Extract header line 1
    HeaderLine1 = LL[0]
    # Extract header line 1
    HeaderLine2 = LL[1]
    # Extract the rest of the rows as the actual participant data
    PartData = LL[2:]
    return HeaderLine1, HeaderLine2, PartData

class PANAS(object):
    def __init__(self):
        self.PartID = -9999
        self.PANASDate1 = -9999
        self.PANASDate2 = -9999
        self.PANASHour1 = -9999
        self.PANASHour2 = -9999
        self.PANASPos1 = -9999
        self.PANASNeg1 = -9999
        self.PANASPos2 = -9999
        self.PANASNeg2 = -9999

    def ProcessPANASOneRow(self, OneRowOfData):
        """ Scoring:
        Positive Affect Score: 
            Add the scores on items 1, 3, 5, 9, 10, 12, 14, 16, 17, and 19. 
            Scores can range from 10 – 50, with higher scores representing higher levels of positive affect.
        Mean Scores: 33.3 (SD±7.2)
        
        Negative Affect Score: Add the scores on items 2, 4, 6, 7, 8, 11, 13, 15, 18, and 20. Scores can
        range from 10 – 50, with lower scores representing lower levels of negative affect.
        Mean Score: 17.4 (SD ± 6.2)
        
        Watson, D., Clark, L. A., & Tellegen, A. (1988). Development and validation of brief measures of positive
        and negative affect: the PANAS scales. Journal of personality and social psychology, 54(6), 1063.
        """
        self.PartID = int(OneRowOfData[9])
        TestDate = OneRowOfData[2]
        self.Session = int(OneRowOfData[10])
        
        TimeOfDayIndex = int(OneRowOfData[11]) - 1
        # TIME OF DAY MAPPING
        TimeMapping = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
        HourOfDay = TimeMapping[TimeOfDayIndex]
        
        # POSITIVE
        # Questions in the survey
        PositiveQuestionsIndex = np.array([1,3,5,9,10,12,14,16,17,19])
        # Recale the question numbers to their placement in teh SurveyMonkey file
        PositiveQuestionsIndex += 11
        PositiveScore = 0
        for i in PositiveQuestionsIndex:
            if len(OneRowOfData[i]) > 0:
                PositiveScore += int(OneRowOfData[i])

        # NEGATIVE
        # Questions in the survey
        NegativeQuestionsIndex = np.array([1,4,6,7,8,11,13,15,18,20])
        # Recale the question numbers to their placement in teh SurveyMonkey file
        NegativeQuestionsIndex += 11
        NegativeScore = 0
        for i in NegativeQuestionsIndex:
            if len(OneRowOfData[i]) > 0:
                NegativeScore += int(OneRowOfData[i])
        # Add the values according to the test date
        if Session == 1:
            self.PANASDate1 = TestDate
            self.PANASHour1 = HourOfDay
            self.PANASPos1 = PositiveScore
            self.PANASNeg1 = NegativeScore
        else:
            self.PANASDate2 = TestDate
            self.PANASHour2 = HourOfDay
            self.PANASPos2 = PositiveScore
            self.PANASNeg2 = NegativeScore
            
    def to_dict(self):
        return {
            'PartID': self.PartID,
            'Session': self.Session,
            'PANASDate1': self.PANASDate1,
            'PANASDate2': self.PANASDate2,
            'PANASHour1': self.PANASHour1,
            'PANASHour2': self.PANASHour2,
            'PANASPos1': self.PANASPos1,
            'PANASNeg1': self.PANASNeg1,
            'PANASPos2': self.PANASPos2,
            'PANASNeg2': self.PANASNeg2,
        }
        

class Demograhics(object):
# Define a class for the demographic data for each participant
    def __init__(self):
        self.PartID = -9999
        self.TestDate = -9999
        self.Age = -9999
        self.Sex = -9999
        self.Gender = -9999
        self.Edu = -9999

    def ProcessDemographicsDataOneRow(self, DemoDataRow):
        # Find exam date
        self.TestDate = parse(DemoDataRow[2])
        self.PartID = int(DemoDataRow[9])
        # Find the birth month and year
        BirthMonth = self.BirthMonth(DemoDataRow[10])
        BirthYear = self.BirthYear(DemoDataRow[11])
        # Find age
        self.FindAge(BirthMonth, BirthYear)
        self.Sex = DemoDataRow[12]
        self.Gender = DemoDataRow[14]
        # Map the education onto years
        self.EducationMapping(DemoDataRow[64])
  
    def EducationMapping(self, EduData):
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
        EduRange = [-9999, 8,9,10,11,12,13,14,15,16,17,20,-8888,-7777,-6666]
        if len(EduData) > 0:
            self.Edu = EduRange[int(EduData)]
        else:
            self.Edu = -9999

    def BirthMonth(self, Data):
        if len(Data) > 0:
            BirthMonth = int(Data)  
        else:
            # Set birth month to January if it is not entered
            BirthMonth = 1
        return BirthMonth

    def BirthYear(self, Data):
        if len(Data) > 0:
            BirthYear = int(Data)  
        else:
            # Set birth year to -9999 if it is not entered
            BirthYear = -9999
        return BirthYear

    def FindAge(self, BirthMonth, BirthYear):
        if BirthYear != -9999:
            DateOfBirth = datetime.datetime(BirthYear,BirthMonth,1)
            self.Age = self.TestDate - DateOfBirth
            self.Age = self.Age.days/365.0
        else:
            self.Age = -9999
                                
    def to_dict(self):
        return {
            'PartID': self.PartID,
            'TestDate': self.TestDate,
            'Age': self.Age,
            'Sex': self.Sex,
            'Gender': self.Gender,
            'Edu': self.Edu,
        }

AllParts = []
for i in DemoData:
    temp = Participant()
    temp.ProcessDemographicsDataOneRow(i)
    AllParts.append(temp)

# Create a list of PANAS objects for each data row
AllPANAS = []
for i in PANASData:
    temp = PANAS()
    temp.ProcessPANASOneRow(i)
    AllPANAS.append(temp)
# Convert the list of objects to a pandas dataframe    
AllPANAS = pd.DataFrame.from_records([s.to_dict() for s in AllPANAS])

def PANASCombineRows(AllPANAS):
    # For each item in the PANAS list extract the participant ID
    # If it is a session 1
    # Look to see if there is a session 2 for the same participant ID
    # Cycle over the data
    for index, row in AllPANAS.iterrows():
        # for each row extract the participant ID and the session
        CurrentPartID = row['PartID']
        CurrentSession = row['Session']
        # If this is a session 1, then look for session 2
        if CurrentSession == 1:
            # cycle over the data again
            for index2, row2 in AllPANAS.iterrows():
                tempPartID = row2['PartID']
                tempSession = row2['Session']
                # Check to see if this row is session two or not
                if tempPartID == CurrentPartID:
                    # Same participant ID
                    if tempSession == 2:
                        print('Found one')




def DefineDataColumns():
    # Sleep pattern 
    Sleep = arange(11,29)
    # 11: 
        # Very Satisfied ....................................................... 1
        # Satisfied ................................................................ 2
        # Neutral .................................................................. 3
        # Dissatisfied ........................................................... 4
        # Very Dissatisfied ................................................... 5
        # [DO NOT READ] Don’t know/No answer ............. 8
        # [DO NOT READ] Refused ................................... 9
        #     • Eight questions
        # • Overall sleep satisfaction (from Insomnia Sleep Index)
        # • Sleep duration (Pittsburgh Sleep Quality Index [PSQI])
        # • Sleep onset insomnia (Insomnia Sleep Index)
        # • Sleep maintenance insomnia (Insomnia Sleep Index)
        # • Daytime somnolence (adapted from PSQI)
        # • Restless legs syndrome (adapted from REST questionnaire)
        # • REM sleep behaviour disorder (from validated approach
        # used at the Sacré-Coeur sleep disorders centre)
    # Instrucmental Activities of Daily Living 
    IADL = slice(32, 53)
    # Loneliness 
    # These questions have responses such as: Yes/More or less/No
    Loneliness = slice(55, 60)
  
    # Subjective Cognitive Decline
    # These questions have responses such as: Yes/No/I don't know/Prefer not to answer
    SCD1 = slice(65,69)
    SCD2 = slice(89, 107)
    SCDscore = SubjectCognitiveDecline(i[SCD1], i[SCD2])

    # Social Participation
    # I am not sure how to score this
    # (109, 147), skip 126
    #
    # Social Networks
    # 149, 198, skip 195
    # Depression Scale
    BDS = slice(201, 222)
    # ScoreBeckDepressionIndex(i[BDS])
    GDS = slice(222, 252)
    ScoreGeriatricDepressionIndex(i[GDS])
    # Education
    # This comes from another survey
    # Nutrition
    # Language 
    # Health
    
    
    



def ScoreBeckDepressionIndex(BDIData):
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
        BDIData = [int(numeric_string) for numeric_string in BDIData]
        BDIscore = sum(BDIData) - 21
        #BDIscore = sum(map(int, np.array(BDIData)))-21
    return BDIscore
        
        
def ScoreGeriatricDepressionIndex(GDSData):
    """ Yes is saved as a ONE
    No is saved as a TWO
    Score one point if the following responses are made and zero if this 
    choice was not made:
    2,1,1,1,2,1,  2,1,2,1,1,1,  1,1, 2,1,1,1,2,1,2,1,1,1,1,1,2,1,2,2
    
    Normal = 0 - 9
    Mild Depression = 10 - 19
    Sever Depression = 20 - 30
    """
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
    
def SubjectCognitiveDecline(SCDdata1, SCDdata2):
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
    
#BaseDir = '/Users/jasonsteffener'
#FileName = os.path.join(BaseDir,'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/SurveyMonkeyExports/Participant Questionnaire.csv')
Data = LoadSMFile(InputFile)

OutData = RestructureSM(Data)