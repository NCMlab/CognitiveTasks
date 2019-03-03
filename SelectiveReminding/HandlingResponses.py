InitialList = ['9', '7', '5', '9', '7', '5', '3', '1', 'b', 'b']

def CleanSRTResponses(InitialList):
    # Remove duplicates but preserve the order
    CleanList = []
    for i in InitialList:
        if i not in CleanList:
            CleanList.append(i)
    return CleanList
    

def FillResponseArray(ResponseArray, CleanList, TrialNumber)
    # For each response enter them in the Response array

    
            
# Make an array that reflects the response table
ResponseArray = np.zeros((12,6))
TrialNumber = 1
ResponseCount  = 1 # What order were responses made?
for i in CleanList:
    # check whether it is a number or a letter
    if i.isdigit():
        ResponseValue = int(i) - 1 # To make the response a position in the array
    elif i == 'a':
        ResponseValue = 9
    elif i == 'b':
        ResponseValue = 10
    elif i == 'c':
        ResponseValue = 11
    ResponseArray[ResponseValue, TrialNumber - 1] = ResponseCount
    ResponseCount += 1
ResponseArray
    
        