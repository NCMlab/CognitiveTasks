import collections
Results['DMSBeh1']
# Reorder DMS results

def ReorderDMSResults(Results):
    # When the results are calculated it is easier to code the scoring based on load
    # but this is order hard to read at the output.
    # This code reorders results based on the measure instead of the load
    # What measures to cycle over
    MeasureList = ['RT', 'Acc','NResp']
    # what type of measures to cycle over
    TypeList = ['Rel', 'Abs']
    # create an empty ordered dictionary
    Res = collections.OrderedDict()
    for Type in TypeList:
        for Tag in MeasureList:
            for k in range(1,11):
                for i in Results:
                    if (i.find(Type) >= 0) and (i.find(Tag) >= 0) and (i.find('Load'+str(k).zfill(2)) >= 0):
                        Res[i] = Results['DMSBeh1'][i]
    return Res
                    
Res


for k in range(1,10):
    for i in Results['DMSBeh1']:
        if (i.find('Abs') >= 0) and (i.find('RT') >= 0) and (i.find('Load'+str(k).zfill(2)) >= 0):
            Res[i] = Results['DMSBeh1'][i]
            print(i) 

