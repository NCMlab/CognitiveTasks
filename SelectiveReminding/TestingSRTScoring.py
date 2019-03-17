import numpy as np
import importlib
import SRTHandlingResponses
importlib.reload(SRTHandlingResponses)

List1 = ['9', '7', '5', '9', '7', '5', '3', '1', 'b', 'b']
List2 = ['1','2','4','5','x','x','x','x','6','7','a','x']
List3 = ['1','3','4','5','6','9','c','a','3']
List4 = ['1','2','3','5','x','6','7','9','c','3','b','8']
List5 = ['1','3','5','6','7','9','c','x','x','x','a','b','4']
List6 = ['1','2','3','5','x','6','x','7','9','c','3','b','8']

ResponseArray = np.zeros((12,6))
NIntrusionArray = np.zeros(6)
# Make an array that reflects the response table
cList1 = SRTHandlingResponses.CleanSRTResponses(List1)
uniqueResp = list(set(cList1))
uniqueResp.sort()
NIntrusions = np.count_nonzero(np.array(List1) == 'x')
NIntrusionArray[0] = NIntrusions
cList2 = SRTHandlingResponses.CleanSRTResponses(List2)
uniqueResp = list(set(cList2))
uniqueResp.sort()
NIntrusions = np.count_nonzero(np.array(List2) == 'x')
NIntrusionArray[1] = NIntrusions
cList3 = SRTHandlingResponses.CleanSRTResponses(List3)
uniqueResp = list(set(cList3))
uniqueResp.sort()
NIntrusions = np.count_nonzero(np.array(List3) == 'x')
NIntrusionArray[2] = NIntrusions
cList4 = SRTHandlingResponses.CleanSRTResponses(List4)
uniqueResp = list(set(cList4))
uniqueResp.sort()
NIntrusions = np.count_nonzero(np.array(List4) == 'x')
NIntrusionArray[3] = NIntrusions
cList5 = SRTHandlingResponses.CleanSRTResponses(List5)
uniqueResp = list(set(cList5))
uniqueResp.sort()
NIntrusions = np.count_nonzero(np.array(List5) == 'x')
NIntrusionArray[4] = NIntrusions
cList6 = SRTHandlingResponses.CleanSRTResponses(List6)
uniqueResp = list(set(cList6))
uniqueResp.sort()
NIntrusions = np.count_nonzero(np.array(List6) == 'x')
NIntrusionArray[5] = NIntrusions



ResponseArray = SRTHandlingResponses.FillResponseArray(ResponseArray, cList1, 0)
ResponseArray = SRTHandlingResponses.FillResponseArray(ResponseArray, cList2, 1)
ResponseArray = SRTHandlingResponses.FillResponseArray(ResponseArray, cList3, 2)
ResponseArray = SRTHandlingResponses.FillResponseArray(ResponseArray, cList4, 3)
ResponseArray = SRTHandlingResponses.FillResponseArray(ResponseArray, cList5, 4)
ResponseArray = SRTHandlingResponses.FillResponseArray(ResponseArray, cList6, 5)
# 
WordList = [u'THROW', u'LILY', u'FILM', u'DISCREET', u'LOFT', u'BEEF', u'STREET', u'HELMET', u'SNAKE', u'DUG', u'PACK', u'TIN']

# LTS, LTSarray = CalcLongTermStorage(ResponseArray) 
# LTR, LTRarray = CalcLongTermRecall(ResponseArray, LTSarray) 
# 

OutFile = open('tester.csv','w')
SRTHandlingResponses.WriteOutResults(OutFile, ResponseArray, NIntrusionArray, WordList)

OutFile.close()


InFileName = 'tester.csv'
InData = pd.read_csv(InFileName)

InData = InData.set_index('Index')

# Extract just responses from the table.
# I am doing this just in case some modifications to the file take place which 
# would move the exact cells where the derived measures are.
ResponseArray = np.array(InData.iloc[1:12,1:7])
LTS, LTSarray = SRTHandlingResponses.CalcLongTermStorage(ResponseArray) 
LTR, LTRarray = SRTHandlingResponses.CalcLongTermRecall(ResponseArray, LTSarray) 

# OutFile.close()