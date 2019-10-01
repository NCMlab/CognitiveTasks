# -*- coding: utf-8 -*-
# import pandas  as pd
import csv
import os
import numpy as np
import tkinter
from tkinter import messagebox
import datetime
# from dateutil.parser import parse
import sys
# import collections
import glob
import shutil
import Class_PANAS
import Class_Demog
import Class_Lifestyle
import importlib

# importlib.reload(Class_PANAS)
importlib.reload(Class_Lifestyle)

BaseDir = '/home/jsteffen/'
BaseDir = '/Users/jasonsteffener/Documents/'

__file__ = os.path.join(BaseDir, 'GitHub/CognitiveTasks/DataHandlingScripts/ScoreSurveyMonkey.py')
#__file__ = '/home/jsteffen/GitHub/CognitiveTasks/DataHandlingScripts/ScoreSurveyMonkey.py'
# What folder is this file in?
dir_path = os.path.dirname(os.path.realpath(__file__))
# Append the data handling script folder to the system path
sys.path.append(dir_path)


# This will load the config file containing the location of the data folder
# If there is an error it means that the GUI program has not been run.
# The GUI checks to see if thie config file exists. If it does not then it is created.
sys.path.append(os.path.join(dir_path,'..','ConfigFiles'))
import NeuropsychDataFolder
# Load up the data location as a global variable
AllOutDataFolder = NeuropsychDataFolder.NeuropsychDataFolder

# From the Neuropsych folder change to the SurveyMonkey Folder
SurveyMonkeyDataFolder = os.path.split(AllOutDataFolder)[0]
SurveyMonkeyDataFolder = os.path.join(SurveyMonkeyDataFolder, 'SurveyMonkey')
# At home lifestyle questionnaire
LifestyleFileName = 'Royal LifestyleBehavior.csv'
# At the lab demographics questionnaire
DemographicsFileName = 'Royal Participant Questionnaire.csv'
# At the lab PANAS questionnaire
PANASFileName = 'PANAS Questionnaire.csv'
LifestyleInputFile = os.path.join(SurveyMonkeyDataFolder, LifestyleFileName)
DemographicsInputFile = os.path.join(SurveyMonkeyDataFolder, DemographicsFileName)
PANASInputFile = os.path.join(SurveyMonkeyDataFolder, PANASFileName)

# Check to see if all three files are present
AreAllThreeFilesPresent(LifestyleInputFile, DemographicsInputFile, PANASInputFile)
# Load the data from all the demographics data file
DemoH1, DemoH2, DemoData = ReadSMFileAsCSV(DemographicsInputFile)
# Load the data from the PANAS file
PANASH1, PANASH2, PANASData = ReadSMFileAsCSV(PANASInputFile)
# Load the data from the Lifestyle file
LifeH1, LifeH2, LifeData = ReadSMFileAsCSV(LifestyleInputFile)

## PANAS
AllPANAS = Class_PANAS.PANAS()
AllPANAS.ProcessDataFile(PANASData)
# Create a file name for PANAS data 
UpdatedDataFileName = CreateOutFileName('NCM002_PANAS', AllOutDataFolder)
ExistingDataFileName = LocateOutDataFile('NCM002_PANAS')
# Write PANAS to file
WriteOutNewdataMoveOldData(AllPANAS.AllPANAS, UpdatedDataFileName, ExistingDataFileName)

## DEMOGRAPHICS
AllDemog = Class_Demog.Demograhics()
AllDemog.ProcessDataFile(DemoData)
# Create a file name for Demog data 
UpdatedDataFileName = CreateOutFileName('NCM002_Demog', AllOutDataFolder)
ExistingDataFileName = LocateOutDataFile('NCM002_Demog')
# Write Demographics to file
WriteOutNewdataMoveOldData(AllDemog.AllParts, UpdatedDataFileName, ExistingDataFileName)
AllDemog.AllParts.to_csv(UpdatedDataFileName)


## LIFESTYLE
AllLife = Class_Lifestyle.Lifestyle()
AllLife.ProcessData(LifeData)
AllList.AllLife
# Create a file name for Demog data 
UpdatedDataFileName = CreateOutFileName('NCM002_Life', AllOutDataFolder)
ExistingDataFileName = LocateOutDataFile('NCM002_Life')
# Write Demographics to file
WriteOutNewdataMoveOldData(AllLife.AllLife, UpdatedDataFileName, ExistingDataFileName)
AllLife.AllLife.to_csv(UpdatedDataFileName)


def CreateOutFileName(BaseFileName, AllOutDataFolder):
    # Create a file to hold processed data using the time and date
    # to indicate when it was made
    now = datetime.datetime.now()
    NowString = now.strftime("_updated_%b-%d-%Y_%H-%M.csv")
    NewOutFileName = os.path.join(AllOutDataFolder, BaseFileName + NowString)
    return NewOutFileName

def LocateOutDataFile(BaseFileName):
    # Locate an existing processed data file and if it does not exist, then make it.
    # What files exist with this name?
    Files = glob.glob(os.path.join(AllOutDataFolder, BaseFileName + '*.csv'))
    now = datetime.datetime.now()
    NowString = now.strftime("_updated_%b-%d-%Y_%H-%M.csv")
    NewOutFileName = BaseFileName + NowString
    if len(Files) == 0:
        FileName = os.path.join(AllOutDataFolder, NewOutFileName)
    else:
        # this will open an existing file
        FileName = Files[-1] 
    return FileName

def WriteOutNewdataMoveOldData(UpdatedData, UpdatedDataFileName, ExistingDataFileName):
    # Move the old file 
    OldDataFolder = os.path.join(AllOutDataFolder, 'OldResultFiles')
    # if the folder for old data does not exist, then make it
    if not os.path.exists(OldDataFolder):
        os.mkdir(OldDataFolder)
    # change the name of the results file so it is not confused with current data
    MovedDataFile = os.path.join(OldDataFolder, 'X_'+os.path.basename(ExistingDataFileName))
    shutil.move(ExistingDataFileName, MovedDataFile)
    # Now that the old data is moved, write out the updated data
    UpdatedData.to_csv(UpdatedDataFileName, index = False, float_format='%.3f')    
    
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
    
    
    




    
#BaseDir = '/Users/jasonsteffener'
#FileName = os.path.join(BaseDir,'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/SurveyMonkeyExports/Participant Questionnaire.csv')
Data = LoadSMFile(InputFile)

OutData = RestructureSM(Data)