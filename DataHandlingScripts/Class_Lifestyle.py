import datetime
from dateutil.parser import parse
import pandas as pd
import collections


class Lifestyle(object):
# Define a class for the demographic data for each participant
    def __init__(self):
        self.PartID = -9999
        self.TestDate = -9999
        self.BDI = -9999
        self.GDS = -9999
        
    def ProcessData():
        for OneRow in LifeData:
            ProcessOneRowData(OneRow)
            
    def ProcessOneRowData(OneRow):
        # Subjective Cognitive Decline
        # These questions have responses such as: Yes/No/I don't know/Prefer not to answer
        SCD1 = slice(65,69)
        SCD2 = slice(89, 107)
        SCDscore = SubjectCognitiveDecline(OneRow[SCD1], OneRow[SCD2])
        # Depression Scale
        BDS = slice(201, 222)
        
        # ScoreBeckDepressionIndex(i[BDS])
        GDS = slice(222, 252)
        ScoreGeriatricDepressionIndex(OneRow[GDS])


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