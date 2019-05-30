import numpy as np

VSTM_ProbeColor = 'blue'

# Timings
VSTM_FontSize = 60
VSTM_FontSizeUnits = 'pix'
VSTM_BGColor = 'grey'
VSTM_FontColor = 'white'
VSTM_GridSizeScale = 52;

# The circles are presented in a grid. The next parameter sets the number of circles
# in the grid. If VSTM_GridCount is 6, then there will be a 6 by 6 grid of circles.
VSTM_GridCount = 6 # Number of circles to have on each row

# The following are timing parameters
VSTM_StimOnTime = 2.5 # How long the circles are on the screen
# The following is for the visual mask
VSTM_MaskOnTime = 0.3 # How long the complete grid of circles are on the screen.
VSTM_RetOnTime = 3.2 # How long is the retention period
VSTM_ProbeOnTime= 2.5 # How long does the person have to respond
# This is the intertrial interval. This experimental component is part of the trial.
VSTM_ITITime = 1.0 #1.0

VSTM_NumberOfBlocks = 5
VSTM_NTrialsPerBlock = 6
# The following are only used if a fixed dot order is requested otherwise the dot locations
# are created on the fly
# This probe list needs to be of length equal to the number of trials per block times 
# the number of blocks
ProbeList1 = np.array([0,0,0,1,1,1])
ProbeList2 = np.array([0,1,0,0,1,1])
ProbeList3 = np.array([0,0,1,1,1,0])
ProbeList4 = np.array([1,1,0,1,0,0])
ProbeList5 = np.array([0,1,0,1,1,0])
ProbeList6 = np.array([0,1,1,0,0,1])
# Make three lists depending on the run
ProbeListRun1 = np.concatenate((ProbeList1,ProbeList2,ProbeList3,ProbeList4,ProbeList5,ProbeList6))
ProbeListRun2 = np.concatenate((ProbeList4,ProbeList5,ProbeList2,ProbeList1,ProbeList3,ProbeList6))
ProbeListRun3 = np.concatenate((ProbeList1,ProbeList2,ProbeList6,ProbeList3,ProbeList5,ProbeList4))
# The location lists are based on a 6-x-6 grid and 6 trials per block
# Load 1
LocationsLoad1List1 = np.array([[29],[2],[25],[31],[9],[13]])
ProbeList1Run1 = np.array([5,28,33,31,9,13])
LocationsLoad1List2 = np.array([[4],[32],[21],[2],[35],[12]])
ProbeList1Run2 = np.array([24,28,3,8,35,12])
LocationsLoad1List3 = np.array([[6],[7],[14],[1],[21],[9]])
ProbeList1Run3 = np.array([9,23,29,1,21,9])
# Load 2
LocationsLoad2List1 = np.array([[21,23],[19,34],[1,3],[25,29],[1,34],[27,28]])
ProbeList2Run1 = np.array([28,19,32,5,34,27])
LocationsLoad2List2 = np.array([[35,6],[3,11],[8,33],[9,10],[12,15],[10,17]])
ProbeList2Run2 = np.array([4,3,24,10,12,30])
LocationsLoad2List3 = np.array([[11,4],[2,5],[18,31],[10,29],[3,5],[10,19]])
ProbeList2Run3 = np.array([23,2,25,33,5,19])


LocationsLoad3List1 = np.array([[5,30,10],[3,21,33],[8,16,22],[ 5, 15, 34],[ 3, 26, 33],[ 6, 18, 24]])
ProbeList3Run1 = np.array([20,11,8,15,33,26])
LocationsLoad3List2 = np.array([[9,27,6],[2,14,18],[5,23,24],[ 4,  7, 34],[18, 19, 22],[ 4,  8, 15]])
ProbeList3Run2 = np.array([12,2,17,20,19,15])
LocationsLoad3List3 = np.array([[18,12,27],[7,8,13],[6,33,34],[11, 12, 25],[23, 30, 33],[0, 3, 6]])
ProbeList3Run3 = np.array([5,7,33,9,17,6])

LocationsLoad4List1 = np.array([[16,33,24,5],[ 6, 17, 22, 29],[ 2, 20, 26, 31],[ 3,  5, 25, 28],[ 0, 13, 31, 33],[ 7, 10, 17, 34]])
ProbeList4Run1 = np.array([16,6,0,28,10,27])
LocationsLoad4List2 = np.array([[9,27,24,34],[ 1, 19, 23, 25],[19, 21, 32, 35],[11, 22, 34, 35],[ 8, 28, 31, 33],[ 3,  9, 14, 17]])
ProbeList4Run2 = np.array([3,5,13,11,28,9])
LocationsLoad4List3 = np.array([[23,34,7,30],[ 0, 16, 23, 28],[12, 21, 22, 35],[ 6, 15, 27, 31],[ 4,  9, 29, 33],[ 2,  3,  4, 25]])
ProbeList4Run3 = np.array([17,33,12,15,29,13])

LocationsLoad5List1 = np.array([[ 4,  6, 16, 30, 33],[ 8,  9, 11, 26, 32],[ 2, 19, 23, 32, 35],[ 5, 13, 18, 23, 30],[ 1,  5, 19, 27, 31],[ 4,  5, 12, 13, 22]])
ProbeList5Run1 = np.array([])
LocationsLoad5List2 = np.array([[10, 20, 28, 30, 33],[12, 19, 29, 30, 31],[ 1, 17, 28, 29, 30],[ 1,  7, 20, 23, 31],[ 5,  7, 11, 20, 33],[ 1,  9, 15, 25, 32]])
ProbeList5Run2 = np.array([])
LocationsLoad5List3 = np.array([[ 1,  3, 15, 27, 28],[ 0,  8, 12, 19, 22],[ 4, 13, 15, 19, 23],[ 6,  7, 15, 28, 29],[ 5,  7, 14, 22, 34],[ 2,  9, 11, 15, 24]])
ProbeList5Run3 = np.array([])

LocationsLoad6List1 = np.array([29,5,11,25,13,3])
ProbeList6Run1 = np.array([])
LocationsLoad6List2 = np.array([21,6,2,7,32,19])
ProbeList6Run2 = np.array([])
LocationsLoad6List3 = np.array([35,28,34,20,33,23])
ProbeList6Run3 = np.array([])

LocationsLoad7List1 = np.array([28,2,13,26,19,25,1])
LocationsLoad7List2 = np.array([34,29,17,0,13,20,3])
LocationsLoad7List3 = np.array([27,33,18,19,5,26,9])
LocationsLoad8List1 = np.array([14,9,25,8,5,13,30,19])
LocationsLoad8List2 = np.array([17,21,25,3,30,14,24,10])
LocationsLoad8List3 = np.array([24,9,31,27,15,2,7,35])
LocationsLoad9List1 = np.array([0,1,6,7,9,11,24,25,28])
LocationsLoad9List2 = np.array([1,3,7,8,10,15,19,27,29])
LocationsLoad9List3 = np.array([3,4,13,14,15,24,26,31,35])
LocationsLoad10List1 = np.array([1,3,8,9,12,13,14,16,27,30])
LocationsLoad10List2 = np.array([1,5,6,9,14,16,23,24,30,33])
LocationsLoad10List3 = np.array([2,3,7,9,22,25,26,30,31,35])
LocationsLoad11List1 = np.array([5,8,12,17,18,21,23,29,30,34,35])
LocationsLoad11List2 = np.array([1,5,6,10,11,13,14,20,21,24,28])
LocationsLoad11List3 = np.array([0,4,7,11,12,14,19,25,26,27,31])
LocationsLoad12List1 = np.array([ 4,  8,  9, 11, 14, 17, 18, 21, 23, 26, 30, 34])
LocationsLoad12List2 = np.array([ 2,  4, 10, 15, 17, 19, 20, 23, 24, 25, 26, 32])
LocationsLoad12List3 = np.array([ 2,  4,  5,  8,  9, 13, 17, 18, 21, 23, 24, 26])
LocationsLoad13List1 = np.array([ 0,  6,  7, 10, 11, 14, 16, 17, 18, 19, 21, 33, 34])
LocationsLoad13List2 = np.array([ 2,  3,  8,  9, 10, 12, 14, 16, 19, 27, 30, 33, 35])
LocationsLoad13List3 = np.array([ 6,  7,  9, 11, 12, 13, 18, 19, 22, 24, 25, 32, 35])
LocationsLoad14List1 = np.array([ 1,  4,  7, 11, 15, 16, 17, 19, 20, 21, 22, 24, 32, 34])
LocationsLoad14List2 = np.array([ 1,  3,  8,  9, 10, 12, 15, 17, 19, 26, 27, 29, 30, 31])
LocationsLoad14List3 = np.array([ 1,  2,  5,  6, 13, 15, 16, 21, 22, 25, 26, 28, 33, 35])
LocationsLoad15List1 = np.array([ 0,  4,  6,  9, 11, 17, 20, 21, 22, 25, 26, 28, 32, 34, 35])
LocationsLoad15List2 = np.array([ 1,  5,  6,  7,  8, 10, 12, 13, 16, 18, 25, 26, 27, 29, 31])
LocationsLoad15List3 = np.array([ 0,  1,  6,  7, 18, 19, 22, 23, 25, 26, 27, 30, 32, 34, 35])
# Create a three dimensional grid out of this that is Trial-x-List
LocationsLoad1 = np.array([LocationsLoad1List1,LocationsLoad1List2,LocationsLoad1List3])
LocationsLoad2 = np.array([LocationsLoad2List1,LocationsLoad2List2,LocationsLoad2List3])
LocationsLoad3 = np.array([LocationsLoad3List1,LocationsLoad3List2,LocationsLoad3List3])
LocationsLoad4 = np.array([LocationsLoad4List1,LocationsLoad4List2,LocationsLoad4List3])
LocationsLoad5 = np.array([LocationsLoad5List1,LocationsLoad5List2,LocationsLoad5List3])
LocationsLoad6 = np.array([LocationsLoad6List1,LocationsLoad6List2,LocationsLoad6List3])
LocationsLoad7 = np.array([LocationsLoad7List1,LocationsLoad7List2,LocationsLoad7List3])
LocationsLoad8 = np.array([LocationsLoad8List1,LocationsLoad8List2,LocationsLoad8List3])
LocationsLoad9 = np.array([LocationsLoad9List1,LocationsLoad9List2,LocationsLoad9List3])
LocationsLoad10 = np.array([LocationsLoad10List1,LocationsLoad10List2,LocationsLoad10List3])
LocationsLoad11 = np.array([LocationsLoad11List1,LocationsLoad11List2,LocationsLoad11List3])
LocationsLoad12 = np.array([LocationsLoad12List1,LocationsLoad12List2,LocationsLoad12List3])
LocationsLoad13 = np.array([LocationsLoad13List1,LocationsLoad13List2,LocationsLoad13List3])
LocationsLoad14 = np.array([LocationsLoad14List1,LocationsLoad14List2,LocationsLoad14List3])
LocationsLoad15 = np.array([LocationsLoad15List1,LocationsLoad15List2,LocationsLoad15List3])
# Create a list of these that can be indexed for load
ProbeLoad1 = np.array([ProbeList1Run1, ProbeList1Run2, ProbeList1Run3])
ProbeLoad2 = np.array([ProbeList2Run1, ProbeList2Run2, ProbeList2Run3])
ProbeLoad3 = np.array([ProbeList3Run1, ProbeList3Run2, ProbeList3Run3])
ProbeLoad4 = np.array([ProbeList4Run1, ProbeList4Run2, ProbeList4Run3])
ProbeLoad5 = np.array([ProbeList5Run1, ProbeList5Run2, ProbeList5Run3])
# ProbeLoad6 = np.array([ProbeList6Run1, ProbeList6Run2, ProbeList6Run3])
# ProbeLoad7 = np.array([ProbeList7Run1, ProbeList7Run2, ProbeList7Run3])
# ProbeLoad8 = np.array([ProbeList8Run1, ProbeList8Run2, ProbeList8Run3])
# ProbeLoad9 = np.array([ProbeList9Run1, ProbeList9Run2, ProbeList9Run3])
# ProbeLoad10 = np.array([ProbeList10Run1, ProbeList10Run2, ProbeList10Run3])
# ProbeLoad11 = np.array([ProbeList11Run1, ProbeList11Run2, ProbeList11Run3])
# ProbeLoad12 = np.array([ProbeList12Run1, ProbeList12Run2, ProbeList124Run3])
# ProbeLoad13 = np.array([ProbeList13Run1, ProbeList13Run2, ProbeList13Run3])
# ProbeLoad14 = np.array([ProbeList14Run1, ProbeList14Run2, ProbeList14Run3])
# ProbeLoad15 = np.array([ProbeList15Run1, ProbeList15Run2, ProbeList15Run3])
AllLocations=([LocationsLoad1, LocationsLoad2, LocationsLoad3, LocationsLoad4, LocationsLoad5, LocationsLoad6, LocationsLoad7, LocationsLoad8, LocationsLoad9, LocationsLoad10, LocationsLoad11, LocationsLoad12,LocationsLoad13, LocationsLoad14, LocationsLoad15])
AllProbes = ([ProbeLoad1,ProbeLoad2,ProbeLoad3,ProbeLoad4,ProbeLoad5])
# This is the time between blocks. Note that between each block of trials there
# is also the 3-2-1 countdown. Therefore, the full interblock interval is this value PLUS 
# the countdown time, which is 3 seconds.
VSTM_InterBlockTime = 2.0 #<<<<< 20

# This is a delay component for use after instructions and before the first Block and at the
# the end before the thank you screen
VSTM_ShortDelayTime = 5# 16.0

VSTM_ThankYouOnTime = 3