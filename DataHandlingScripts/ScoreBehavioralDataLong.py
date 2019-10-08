import os
import importlib
import sys
import pandas as pd
import csv
import datetime
import NCMPartv2
import ScoreNIHToolbox
import glob
import numpy as np
importlib.reload(ScoreNIHToolbox)
importlib.reload(NCMPartv2)

BaseDir = '/home/jsteffen'
#BaseDir = '/Users/jasonsteffener'
sys.path.append(os.path.join(BaseDir,'Documents','GitHub','CognitiveTasks','DataHandlingScripts'))


inputFileName = os.path.join(BaseDir,'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/SurveyMonkeyExports/Participant Questionnaire.csv')
# open the file  
fid = open(inputFileName,'r', encoding="ISO-8859-1")

data = csv.reader(fid)
#data = pandas.read_csv(fid, sep=',', encoding='latin-1')
# Read whole file into a list
LL = list(data)
fid.close()

fidOut = open('TestLongData.csv','w')
fidOut.write('partID, sex, age, ageGr, edu, DMSCap, DataSource, Load, Acc, ProbeType, RT, ScCol, ScRow, ScPos, SerPos,')
fidOut.write('FlankerDiff,FlankerCong,PictVocabTheta,Handedness,CrystalComp,FlankerIncong,Sex,CardSort,FluidComp,CognTotalComp,PattComp,CognEarlyChildComp,ListSort,PictSeqTheta,PictSeq,Education,OralRead,FlankerNCor,Age\n')


NPart = len(LL) - 2
HeaderLine1 = LL[0]
HeaderLine2 = LL[1]
PartData = LL[2:]
PartCount = 0
DataList = []
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
                part = NCMPartv2.NCMParticipant()
                part.MakeParticipant(i)
                part.ReadBlockDataLong('DMS_Block','DMS',6)
                part.ReadStairData('DMS')
                
                DataList.append(part)
                part.WriteLongDataToFile(fidOut)
#                print str(RowCount)+"     "+part.subid
                PartCount += 1
            except:
                print(str(PartCount)+"     "+part.subid)
                print("############# >>>>> Uhh Oh <<<<< ############")
                PartCount += 1
        else:
            print("Skipping: %s"%(i[9]))
