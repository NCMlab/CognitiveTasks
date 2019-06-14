#import numpy as np
NumberofTrials = 6
VSTM_GridCount = 6 

ProbeList1 = np.array([0,0,0,1,1,1])
ProbeList2 = np.array([0,1,0,0,1,1])
ProbeList3 = np.array([0,0,1,1,1,0])
ProbeList4 = np.array([1,1,0,1,0,0])
ProbeList5 = np.array([0,1,0,1,1,0])
ProbeList6 = np.array([0,1,1,0,0,1])
ProbeList = []
ProbeList.append(ProbeList1)
ProbeList.append(ProbeList2)
ProbeList.append(ProbeList3)
ProbeList.append(ProbeList4)
ProbeList.append(ProbeList5)
ProbeList.append(ProbeList6)
NProbeOptions = len(ProbeList)
# cycle over the load levels that you want  lists for
for CurrentLoad in range(12):
    # For the trial now pick the probe locations
    # Pick a probe order
    CurrentProbeList = ProbeList[np.random.permutation(NProbeOptions)[0]]

    # cycle over the number of lists that you want to generate    
    for k in range(0,3):
        # generate a random list of locations
        temp = sort(np.random.permutation(VSTM_GridCount**2)[0:CurrentLoad+1])
        # Set the previous trial to be the same as the temp list
        PastTrial = temp
        # keep track of the number of trials that have been generated
        count = 0
        # Start the list of locations
        AllLocations = []
        CurrentProbes = []
        # Make sure that the current trial does not overlap in any way to the previous trial's locations
        while count < NumberofTrials:
            # Use this to start the while loop which will continue until a newa dn different trial is created
            AnyFlag = True
            while AnyFlag: 
                # If no elements of the new trial match the previous trial then the flag will remain false and the while loop will end
                AnyFlag = False
                # Create a new list
                temp = sort(np.random.permutation(VSTM_GridCount**2)[0:CurrentLoad+1])    
                # Check each element of this trial against the previous trial
                for i in PastTrial:
                    if (temp == i).any():
                        # This will keep the while loop going 
                        AnyFlag = True
            # A new trial was found         
            PastTrial = temp
            # Add it to the list
            AllLocations.append(temp)

            
            CurrentProbe = CurrentProbeList[count]
    
            # Negative probe
            if CurrentProbe == 0:
                AnyFlag = True
                while AnyFlag: 
                    # If no elements of the new trial match the previous trial then the flag will remain false and the while loop will end
                    AnyFlag = False
                    tempProbe = np.random.permutation(VSTM_GridCount**2)[0]
                    # Is this probe in the trial?
                    for oneTrial in AllLocations:
                        if (oneTrial == tempProbe).any():
                            AnyFlag = True
                        # Also check to make sure that the negative probe does not match any of the previous locations
                    
                CurrentProbes.append(tempProbe)
            else:
                # Pick a random location from the list
                CurrentProbes.append(temp[np.random.permutation(CurrentLoad+1)[0]])
            count += 1
            
        # Generate the string for use in the config code
        Str = 'LocationsLoad'+str(CurrentLoad+1) + 'List' + str(k+1) + ' = np.array(['
        
        for i in AllLocations:
            Str = Str +'['
            for j  in i:
                Str = Str + str(j) + ','
            Str = Str[0:-1] + '],'
            
        Str = Str[0:-1]+'])'

        # Probe location string
        ProbeList1Run1 = np.array([5,28,33,31,9,13])
        Str2 = 'ProbeLoad' + str(CurrentLoad+1) + 'List' + str(k+1) + ' = np.array(['
        for j in CurrentProbes:
            Str2 = Str2 + str(j) + ','
        Str2 = Str2[0:-1] +'])'
        Str2
        
        print(Str)
        print(Str2)
    print()
        
        
            
        