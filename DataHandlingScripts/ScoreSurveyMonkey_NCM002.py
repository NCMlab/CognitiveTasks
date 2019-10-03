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
# import NeuropsychDataFolder
# Load up the data location as a global variable
# AllOutDataFolder = NeuropsychDataFolder.NeuropsychDataFolder
AllInDataFolder = '/Volumes/GoogleDrive/Shared drives/NCMLab/NCM002-MRIStudy/Data/NeuroPsych'
AllOutDataFolder = os.path.join(os.path.split(AllInDataFolder)[0], 'SummaryData')
# From the Neuropsych folder change to the SurveyMonkey Folder
SurveyMonkeyDataFolder = os.path.split(AllInDataFolder)[0]
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


def main():
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
    ExistingDataFileName = LocateOutDataFile(AllOutDataFolder,'NCM002_PANAS')
    # Write PANAS to file
    WriteOutNewdataMoveOldData(AllPANAS.AllPANAS, UpdatedDataFileName, ExistingDataFileName)
    
    ## DEMOGRAPHICS
    AllDemog = Class_Demog.Demograhics()
    AllDemog.ProcessDataFile(DemoData)
    # Create a file name for Demog data 
    UpdatedDataFileName = CreateOutFileName('NCM002_Demog', AllOutDataFolder)
    ExistingDataFileName = LocateOutDataFile(AllOutDataFolder,'NCM002_Demog')
    # Write Demographics to file
    WriteOutNewdataMoveOldData(AllDemog.AllParts, UpdatedDataFileName, ExistingDataFileName)
    AllDemog.AllParts.to_csv(UpdatedDataFileName)
    
    
    ## LIFESTYLE
    AllLife = Class_Lifestyle.Lifestyle()
    AllLife.ProcessData(LifeData)

    # Create a file name for Demog data 
    UpdatedDataFileName = CreateOutFileName('NCM002_Life', AllOutDataFolder)
    ExistingDataFileName = LocateOutDataFile(AllOutDataFolder,'NCM002_Life')
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

def LocateOutDataFile(AllOutDataFolder, BaseFileName):
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


        





    
