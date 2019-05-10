

AllOutDataFolder = '/media/jsteffen/Data001/NCMTeamDrive/NCMLab/NCM002/Data/NeuroPsych'
subid = '9999999'
Visid = '2019_May_10_0918_V001'
VisitFolder = os.path.join(AllOutDataFolder, subid, Visid)
Results = LoadRawData(os.path.join(AllOutDataFolder, subid, Visid),subid)


FlatResults = FlattenDict(Results)
         

    Data = ReadFile(VisitFolder, subid, 'VSTM_Block_BehRun1_')
    Dir = 'Backward'
    Results = ProcessNeuroPsychFunctions.ProcessVSTMBlockv2(Data)
    print('\tDS Backward loaed')


Dir = 'Forward'
ProcessDigitSpan(Data, Dir)


