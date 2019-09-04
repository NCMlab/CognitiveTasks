#from psychopy import gui##, visual, core, data, event, logging
import NCMPart
import csv
import xlsxwriter
import os
import datetime 
import numpy as np
import os
import fnmatch
import csv
import sys
import pandas
import importlib

importlib.reload(NCMPart)
# Select the file

def SelectSurveyMonkeyFile():
    #inputFileName = gui.fileOpenDlg("../data/SurveyMonkeyExports","","Select export from SurveyMonkey", allowed = "*.csv")
    pass

inputFileName = [u'/home/jsteffen/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/SurveyMonkeyExports/Participant Questionnaire.csv']
inputFileName = [u'/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/SurveyMonkeyExports/Participant Questionnaire.csv']
# open the file  
fid = open(inputFileName[0],'r', encoding="ISO-8859-1")

data = csv.reader(fid)
#data = pandas.read_csv(fid, sep=',', encoding='latin-1')
# Read whole file into a list
LL = list(data)
fid.close()

NPart = len(LL) - 2
HeaderLine1 = LL[0]
HeaderLine2 = LL[1]
PartData = LL[2:]
# Make an object for each participant

def WriteToXLSX(WS,row,part, format2):
    members = ['subid', 'age', 'ageGroup', 'TestDate','DateOB','edu','sex','Ethnicity','BDIscore','GDSscore','DMSCapacity', 'TrimDMSCapacity','FRTCapacity', 'FOSC','PAAerobicMin', 'PABicyclingMin', 'PAJoggingMin', 'PALapSwimMin', 'PALowIntensityMin', 'PARunningMin', 'PATennisMin', 'PAWalkHikeMin','AccDMS_Load01', 'AccDMS_Load02', 'AccDMS_Load03', 'AccDMS_Load04', 'AccDMS_Load05', 'AccDMS_Load06', 'AccFRT_Load01', 'AccFRT_Load02', 'AccFRT_Load03', 'AccFRT_Load04', 'AccFRT_Load05', 'AccFRT_Load06', 'meanCorOnTimeRTDMS_Load01', 'meanCorOnTimeRTDMS_Load02', 'meanCorOnTimeRTDMS_Load03', 'meanCorOnTimeRTDMS_Load04', 'meanCorOnTimeRTDMS_Load05', 'meanCorOnTimeRTDMS_Load06', 'meanCorOnTimeRTFRT_Load01', 'meanCorOnTimeRTFRT_Load02', 'meanCorOnTimeRTFRT_Load03', 'meanCorOnTimeRTFRT_Load04', 'meanCorOnTimeRTFRT_Load05', 'meanCorOnTimeRTFRT_Load06', 'stdCorOnTimeRTDMS_Load01', 'stdCorOnTimeRTDMS_Load02', 'stdCorOnTimeRTDMS_Load03', 'stdCorOnTimeRTDMS_Load04', 'stdCorOnTimeRTDMS_Load05', 'stdCorOnTimeRTDMS_Load06', 'stdCorOnTimeRTFRT_Load01', 'stdCorOnTimeRTFRT_Load02', 'stdCorOnTimeRTFRT_Load03', 'stdCorOnTimeRTFRT_Load04', 'stdCorOnTimeRTFRT_Load05', 'stdCorOnTimeRTFRT_Load06']
    if row == 1:
        # print header row
        ColCount = 0 
        for j in members:
            WS.write(0,ColCount, j)
            ColCount+=1
        for j in part.NIHToolbox.keys():
            
            WS.write(0,ColCount,j)
            ColCount+=1
            
    ColCount = 0           
    for j in members:
        try:
            if j.find('Date') >= 0:
                WS.write(row,ColCount, part.__getattribute__(j),format2)
            else:
                WS.write(row,ColCount, part.__getattribute__(j))
        except:
            print("ERROR")
            
            
            return "ERROR"
        ColCount+=1
    # Write NIH data
    for j in part.NIHToolbox.keys():
        #print(part.NIHToolbox[j])
        WS.write(row,ColCount,str(part.NIHToolbox[j]))
        ColCount+=1        


workbook = xlsxwriter.Workbook('../data/SummaryData_112718.xlsx')
fidOut = open('../data/LongData_112718.csv','w')
#fidOut.write("subid,sex,age,ageGroup,edu,FRTCapacity,DMSCapacity,RelLoad,Load,RT,Correct\n")
fidOut.write("PartID,Sex,Age,AgeGroup,Edu,FRTCap,DMSCap,RunType1blk2str,Load,Acc,ProbeType,RT,ScreenCol,ScreenRow,ScreenPos,SerialPos,")
#fidOut.write("CardSortRaw,PictVocabRT,ListSortRaw,PattCompRaw,PictSeqMemRaw,PictVocabTheta,ReadRecogTheta,PictSeqMemTheta,FlankerRT,")
#fidOut.write("PattCompRT,CartSortRT,PictSeqMemRT,FlankersRaw\n")
# Set a format for date entries
format2 = workbook.add_format({'num_format': 'dd/mm/yy'})
worksheet = workbook.add_worksheet('test2')
RowCount = 1
AllParts = []
PartCount = 0
NIHHeaderFlag = False

for i in PartData:
    print("=================================")
    # Skip rows that are test subjects
    if len(i[9]) == 8:
        if not i[9][5] == '9':
            try:
                # 14 has missing NIH data
                # 15 has missing block data
                # 16 has data that does not look good
                # Empty rows in the survey monkey file need to be removed
                part = NCMPart.NCMParticipant()
                part.MakeParticipant(i)
                #part.ReadBlockDataLong('DMS_Block','DMS',6)
                #part.ReadStairData('DMS')
                
                if NIHHeaderFlag == False:
                    for jj in part.NIHToolbox.keys():
                        fidOut.write('%s,'%(jj))
                    NIHHeaderFlag = True
                    fidOut.write('\n')
                    
                part.WriteLongDataToFile(fidOut)
                print(str(PartCount)+"     "+part.subid)                
#                part.CreateLongDataFRT(part.SubDir, "DMS_Block","DMS", 6, fidOut)
                #print part
                WriteToXLSX(worksheet, RowCount, part,format2)
                RowCount += 1
#                print str(RowCount)+"     "+part.subid
                PartCount += 1
            except:
                print(str(PartCount)+"     "+part.subid)
                print("############# >>>>> Uhh Oh <<<<< ############")
                PartCount += 1
        else:
            print("Skipping: %s"%(i[9]))

workbook.close()
fidOut.close()