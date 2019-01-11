import os 
import importlib
import sys
import datetime

BaseDir = '/home/jsteffen'
BaseDir = '/Users/jasonsteffener'
sys.path.append(os.path.join(BaseDir,'Documents','GitHub','CognitiveTasks','DataHandlingScripts'))
from DataHandlingScriptsPart1 import *

import DataHandlingScriptsPart1
importlib.reload(DataHandlingScriptsPart1)

AllOutDataFolder = os.path.join(BaseDir, 'Dropbox/steffenercolumbia/Projects/MyProjects/NeuralCognitiveMapping/NeuroPsychData/')

df = DataHandlingScriptsPart1.CycleOverDataFolders(AllOutDataFolder)
FN = DataHandlingScriptsPart1.LocateOutDataFile()
df.to_csv(FN)

