import os
import glob
from datetime import datetime, timedelta
import csv
import numpy as np
# Create a list of expected results files
# Check to see which result files are present.
# Check for duplicate files and only keep the latest one. 
# Move or rename the old ones

#InputFolder = '/Users/jasonsteffener/Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/99012345/2018_Dec_12_1044_V001'
#LL = NeuroPsychData(InputFolder) 

class NeuroPsychData():
    def __init__(self, InputFolder):
        self.InputFolder = InputFolder
        self.ListOfExpectedResults()
        self.FindParticipantID()
        self.FindResults()
        self.AssignCheckBoxValues()
        
    def ListOfExpectedResults(self):
        # This list could be a structure
        # This list is the list of names in the structure
        # Then each would have a flag as to whether it was found
        # It can each have the results
        TaskList = {}
        TaskList['Stroop_Color'] = {}
        TaskList['Stroop_Color']['Completed'] = False
        
        TaskList['Stroop_Word'] = {}
        TaskList['Stroop_Word']['Completed'] = False  
        TaskList['Stroop_ColorWord'] = {}
        TaskList['Stroop_ColorWord']['Completed'] = False  
        TaskList['WCST'] = {}
        TaskList['WCST']['Completed'] = False  
        TaskList['DigitSpan_Forward'] = {}
        TaskList['DigitSpan_Forward']['Completed'] = False              
        TaskList['DigitSpan_Backward'] = {}
        TaskList['DigitSpan_Backward']['Completed'] = False  
        TaskList['Matrices_Main'] = {}
        TaskList['Matrices_Main']['Completed'] = False  
        TaskList['DMS_Stair'] = {}
        TaskList['DMS_Stair']['Completed'] = False  
        TaskList['DMS_Block'] = {}
        TaskList['DMS_Block']['Completed'] = False  
        TaskList['VSTM_Stair'] = {}
        TaskList['VSTM_Stair']['Completed'] = False                  
        TaskList['VSTM_Block'] = {}
        TaskList['VSTM_Block']['Completed'] = False  
        TaskList['Speed_PatternComp'] = {}
        TaskList['Speed_PatternComp']['Completed'] = False  
        TaskList['Vocab_Antonyms'] = {}
        TaskList['Vocab_Antonyms']['Completed'] = False  
        self.TaskList = TaskList
    
    def AssignCheckBoxValues(self):
        # This maps the tasks onto their respective checkboxes
        self.TaskList['Stroop_Color']['CBLoc'] = 'cbR1C2'
        self.TaskList['Stroop_Word']['CBLoc'] = 'cbR1C3'
        self.TaskList['Stroop_ColorWord']['CBLoc'] = 'cbR1C4'
        self.TaskList['WCST']['CBLoc'] = 'cbR2C2'
        self.TaskList['DigitSpan_Forward']['CBLoc'] = 'cbR7C2'
        self.TaskList['DigitSpan_Backward']['CBLoc'] = 'cbR7C3'
        self.TaskList['Matrices_Main']['CBLoc'] = 'cbR9C3'
        self.TaskList['VSTM_Stair']['CBLoc'] = 'cbR3C3'
        self.TaskList['VSTM_Block']['CBLoc'] = 'cbR3C4'
        self.TaskList['DMS_Stair']['CBLoc'] = 'cbR5C3'
        self.TaskList['DMS_Block']['CBLoc'] = 'cbR5C6'
        self.TaskList['Speed_PatternComp']['CBLoc'] = 'cbR8C2'
        self.TaskList['Vocab_Antonyms']['CBLoc'] = 'cbR6C2'
        
            
    def FindParticipantID(self):
        self.VisitFolder = os.path.split(self.InputFolder)[1]
        BaseDir = os.path.split(self.InputFolder)[0]
        self.PartID = os.path.split(BaseDir)[1]

    def CheckDuplicateFiles(InputFiles, TaskName):
        # If there are multiple files pick the most recent
        # Dates = []
        # Times = []
        # for i in InputFiles:
        #     # Remove the extension
        #     i = os.path.splitext(i)[0]
        #     # Find where in the filename the task name begins
        #     NameIndex = i.find(TaskName)
        #     Dates.append(i[NameIndex+len(TaskName)+1:].split('_')[1:4])
        #     Times.append(i[NameIndex+len(TaskName)+1:].split('_')[4])
        # # Now find out which is the latest
        # for i in Dates:
        #     d    
        #     
        pass
        
    def FindResults(self):
        for j in self.TaskList:
            TempFile = glob.glob(os.path.join(self.InputFolder,(self.PartID+'_'+j+'*.csv')))
             # Ideally the file names shoudl be checked to pick the latest one   
            if len(TempFile) > 0:
                self.TaskList[j]['DataFile'] = TempFile[-1]
                self.TaskList[j]['Completed'] = True
            
    def ReadVSTMData(self):
        j = 'VSTM_Block'
        TempFile = glob.glob(os.path.join(self.InputFolder,(self.PartID+'_'+j+'*.csv')))
        # Load the file
        fid = open(TempFile[0],'r')
        data = csv.reader(fid)
        # Read whole file into a list
        LL = list(data)
        fid.close()
        HeaderLine = LL[0]
        
    def ReadDMSData(self):
        # Find all of the block data files
        j = 'DMS_Block'
        TempFile = glob.glob(os.path.join(self.InputFolder,(self.PartID+'_'+j+'*.csv')))
        # Load the file
        fid = open(TempFile[0],'r')
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

        
        
    def ReadCapacity(self):
        pass
    
    def ReadBlockData(self):
        pass