import pandas  as pd
import os

def LoadSMFile(FileName):
    Data = pd.read_csv(FileName, sep=',', encoding='latin-1')    
    return Data

def RestructureSM(InData):    
    indices = [i for i, c in enumerate(InData.columns) if not c.startswith('Unnamed')]
    questions = [c for c in InData.columns if not c.startswith('Unnamed')]
    slices = [slice(i, j) for i, j in zip(indices, indices[1:] + [None])]
    for q in slices:
        print(InData.iloc[:, q])  # Use `display` if using Jupyter 
    dd = [InData.iloc[:, q].apply(parse_response, axis=1)[1:] for q in slices]
    OutData = pd.concat(dd, axis=1)
    OutData.columns = questions
    return OutData
    
def parse_response(s):
    try:
        return s[~s.isnull()][0]
    except IndexError:
        return np.nan



BaseDir = '/Users/jasonsteffener'
FileName = os.path.join(BaseDir,'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/data/SurveyMonkeyExports/Participant Questionnaire.csv')
Data = LoadSMFile(FileName)

OutData = RestructureSM(Data)