import numpy as np
ConfigFile = 'VSTM_Test_Config'
print("Loading up the config file: %s"%(ConfigFile))
Str = 'from %s import *'%(ConfigFile)
exec(Str)
FixedLocations = True
# Prepare the stimuli
CurrentLoad = 7
CurrentRun = 1
TrialCount = 3
if FixedLocations:
    Locations = AllLocations[CurrentLoad - 1][CurrentRun][TrialCount]
    ProbeList = AllProbes[CurrentLoad][CurrentRun]
    CurrentProbeLocation = AllProbes[CurrentLoad - 1][CurrentRun][TrialCount]
else:
    # Make sure there are an equal number of probe pos and Neg
    ProbeList = np.concatenate((np.zeros(int(VSTM_NTrialsPerBlock/2)),np.ones(int(VSTM_NTrialsPerBlock/2))))
    # Shuffle the list
    ProbeList = ProbeList[np.random.permutation(VSTM_NTrialsPerBlock)]