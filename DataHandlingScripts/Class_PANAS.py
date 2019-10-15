# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import collections

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
        if self.Session == 1:
            self.PANASDate1 = TestDate
            self.PANASHour1 = HourOfDay
            self.PANASPos1 = PositiveScore
            self.PANASNeg1 = NegativeScore
        else:
            self.PANASDate2 = TestDate
            self.PANASHour2 = HourOfDay
            self.PANASPos2 = PositiveScore
            self.PANASNeg2 = NegativeScore
    
    def ProcessDataFile(self, Data):
        # Create a list of PANAS objects for each data row
        AllPANAS = []
        for i in Data:
            temp = PANAS()
            temp.ProcessPANASOneRow(i)
            AllPANAS.append(temp)
        
        # Convert the list of objects to a pandas dataframe    
        AllPANAS = pd.DataFrame.from_records([s.to_dict() for s in AllPANAS])
        # AllPANAS = AllPANAS.set_index('PartID')
        # Combine sessions
        self.AllPANAS = self.PANASFindBothSessions(AllPANAS)
        # Set the index 
        # self.AllPANAS = AllPANAS.set_index('PartID')

    def PANASFindBothSessions(self, AllPANASData):
        # For each item in the PANAS list extract the participant ID
        # If it is a session 1
        # Look to see if there is a session 2 for the same participant ID
        # Cycle over the data
        ListIndexToDrop = []
        for index1, row in AllPANASData.iterrows():
            # for each row extract the participant ID and the session
            CurrentPartID = row['PartID']
            CurrentSession = row['Session']
            # If this is a session 1, then look for session 2
            if CurrentSession == 1:
                # cycle over the data again
                for index2, row2 in AllPANASData.iterrows():
                    tempPartID = row2['PartID']
                    tempSession = row2['Session']
                    # Check to see if this row is session two or not
                    if tempPartID == CurrentPartID:
                        # Same participant ID
                        if tempSession == 2:
                            print('Found one %d and %d'%(index1, index2))
                            AllPANASData = self.PANASCombineTwoRows(AllPANASData, index1, index2)
                            # Keep track of the indices to drop
                            ListIndexToDrop.append(index2)
        # Drop the session 2 rows
        AllPANASData = AllPANASData.drop(ListIndexToDrop)
        return AllPANASData
                        
    def PANASCombineTwoRows(self, AllPANAS, index1, index2):
        # Now that two rows have been identified as being two sessions from one particopant,
        # They need to be combined.
        AllPANAS.at[index1,'PANASPos2'] = AllPANAS.at[index2,'PANASPos2']
        AllPANAS.at[index1,'PANASNeg2'] = AllPANAS.at[index2,'PANASNeg2']
        AllPANAS.at[index1,'PANASHour2'] = AllPANAS.at[index2,'PANASHour2']
        AllPANAS.at[index1,'PANASDate2'] = AllPANAS.at[index2,'PANASDate2']
        # AllPANAS[index1,'PANASPos2'] = AllPANAS[index2,'PANASPos2']
        # AllPANAS[index1,'PANASNeg2'] = AllPANAS[index2,'PANASNeg2']
        # AllPANAS[index1,'PANASHour2'] = AllPANAS[index2,'PANASHour2']
        # AllPANAS[index1,'PANASDate2'] = AllPANAS[index2,'PANASDate2']
        return AllPANAS            
                                    
    def to_dict(self):
        outDict = collections.OrderedDict()
        outDict['PartID'] = self.PartID
        outDict['Session'] = self.Session
        outDict['PANASDate1'] = self.PANASDate1
        outDict['PANASDate2'] = self.PANASDate2
        outDict['PANASHour1'] = self.PANASHour1
        outDict['PANASHour2'] = self.PANASHour2
        outDict['PANASPos1'] = self.PANASPos1
        outDict['PANASNeg1'] = self.PANASNeg1
        outDict['PANASPos2'] = self.PANASPos2
        outDict['PANASNeg2'] = self.PANASNeg2
        return outDict