Results['DMSBeh1']
# Reorder DMS results

for k in range(1,6):
    for i in Results['DMSBeh1']:
        if (i.find('Rel') >= 0) and (i.find('RT') >= 0) and (i.find('Load'+str(k).zfill(2)) >= 0):
            print(i) 

for k in range(1,10):
    for i in Results['DMSBeh1']:
        if (i.find('Abs') >= 0) and (i.find('RT') >= 0) and (i.find('Load'+str(k).zfill(2)) >= 0):
            print(i) 

