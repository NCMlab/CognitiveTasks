import datetime
from dateutil.parser import parse
import pandas as pd
import collections

class Demograhics(object):
# Define a class for the demographic data for each participant
    def __init__(self):
        self.PartID = -9999
        self.TestDate = -9999
        self.Age = -9999
        self.Sex = -9999
        self.Gender = -9999
        self.Edu = -9999

    def ProcessDataFile(self, DemoData):
        AllParts = []
        for i in DemoData:
            temp = Demograhics()
            temp.ProcessDemographicsDataOneRow(i)
            AllParts.append(temp)
        # Convert the list of objects to a pandas dataframe    
        AllParts = pd.DataFrame.from_records([s.to_dict() for s in AllParts])
        # Set the index 
        self.AllParts = AllParts.set_index('PartID')                    

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
        outDict = collections.OrderedDict()
        outDict['PartID'] = self.PartID
        outDict['TestDate'] = self.TestDate
        outDict['Age'] = self.Age
        outDict['Sex'] = self.Sex
        outDict['Gender'] = self.Gender
        outDict['Edu'] = self.Edu
        return outDict
        
