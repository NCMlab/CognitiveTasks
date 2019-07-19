import numpy as np
#
VSTM_ProbeColor = 'blue'
VSTM_Instructions = 'Press [INDEX Finger] if the circle WAS in the set.\nPress [MIDDLE Finger] if the circle was NOT in the set.\n\nTry to respond as quickly and as accurately as possible.\n\nPress [5] to begin.'

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
# This is the time between blocks. Note that between each block of trials there
# is also the 3-2-1 countdown. Therefore, the full interblock interval is this value PLUS 
# the countdown time, which is 3 seconds.
VSTM_InterBlockTime = 20
# This is a delay component for use after instructions and before the first Block and at the
# the end before the thank you screen
VSTM_ShortDelayTime = 16.0

VSTM_ThankYouOnTime = 3
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
ProbeList = []
ProbeList.append(ProbeList1)
ProbeList.append(ProbeList2)
ProbeList.append(ProbeList3)
ProbeList.append(ProbeList4)
ProbeList.append(ProbeList5)
ProbeList.append(ProbeList6)
# Make three lists depending on the run
ProbeListRun1 = np.concatenate((ProbeList1,ProbeList2,ProbeList3,ProbeList4,ProbeList5,ProbeList6))
ProbeListRun2 = np.concatenate((ProbeList4,ProbeList5,ProbeList2,ProbeList1,ProbeList3,ProbeList6))
ProbeListRun3 = np.concatenate((ProbeList1,ProbeList2,ProbeList6,ProbeList3,ProbeList5,ProbeList4))
# The location lists are based on a 6-x-6 grid and 6 trials per block
LocationsLoad1List1 = np.array([[18],[13],[28],[12],[3],[21]])
ProbeLoad1List1 = np.array([24,13,28,25,25,21])
LocationsLoad1List2 = np.array([[29],[18],[21],[8],[24],[11]])
ProbeLoad1List2 = np.array([3,18,21,12,6,11])
LocationsLoad1List3 = np.array([[14],[29],[15],[13],[24],[28]])
ProbeLoad1List3 = np.array([13,29,15,27,2,28])

LocationsLoad2List1 = np.array([[22,30],[8,10],[0,19],[12,34],[9,11],[14,24]])
ProbeLoad2List1 = np.array([32,27,0,12,9,21])
LocationsLoad2List2 = np.array([[15,16],[4,17],[10,33],[5,18],[3,27],[32,34]])
ProbeLoad2List2 = np.array([28,7,33,18,3,9])
LocationsLoad2List3 = np.array([[6,17],[23,31],[21,33],[8,22],[15,16],[3,30]])
ProbeLoad2List3 = np.array([7,3,21,22,15,35])

LocationsLoad3List1 = np.array([[10,24,29],[5,11,17],[7,12,32],[4,18,26],[28,29,35],[0,4,19]])
ProbeLoad3List1 = np.array([18,17,0,0,28,0])
LocationsLoad3List2 = np.array([[8,13,26],[24,28,35],[8,14,29],[0,4,26],[6,10,14],[9,13,20]])
ProbeLoad3List2 = np.array([20,35,7,18,14,13])
LocationsLoad3List3 = np.array([[19,26,32],[5,20,24],[12,14,17],[19,28,33],[20,27,32],[26,34,35]])
ProbeLoad3List3 = np.array([1,24,34,35,20,26])

LocationsLoad4List1 = np.array([[3,13,29,35],[7,18,25,31],[21,26,28,33],[18,22,23,25],[5,16,17,20],[13,18,19,30]])
ProbeLoad4List1 = np.array([23,18,8,22,17,6])
LocationsLoad4List2 = np.array([[26,28,31,32],[8,11,19,33],[14,23,30,34],[20,22,26,32],[1,16,28,34],[15,26,27,29]])
ProbeLoad4List2 = np.array([25,33,15,22,1,2])
LocationsLoad4List3 = np.array([[12,13,34,35],[21,23,26,29],[9,13,22,30],[3,4,18,34],[9,21,26,30],[5,13,18,35]])
ProbeLoad4List3 = np.array([4,23,28,18,9,32])

LocationsLoad5List1 = np.array([[7,8,16,18,20],[1,3,15,19,26],[0,4,6,8,22],[19,24,25,27,29],[7,13,30,34,35],[2,4,5,9,12]])
ProbeLoad5List1 = np.array([29,1,6,34,23,5])
LocationsLoad5List2 = np.array([[8,9,20,29,30],[2,10,13,28,31],[4,22,29,30,34],[1,2,8,19,25],[5,7,12,18,34],[3,4,13,27,35]])
ProbeLoad5List2 = np.array([0,28,29,17,6,35])
LocationsLoad5List3 = np.array([[7,10,24,27,35],[6,8,17,21,26],[0,5,12,30,34],[7,19,22,28,31],[8,23,25,27,33],[4,9,16,21,30]])
ProbeLoad5List3 = np.array([12,8,12,2,1,4])

LocationsLoad6List1 = np.array([[15,18,27,30,32,34],[0,8,11,12,23,26],[1,4,14,29,33,35],[15,18,22,26,32,34],[2,7,11,28,29,35],[3,13,23,25,31,34]])
ProbeLoad6List1 = np.array([9,11,13,32,2,5])
LocationsLoad6List2 = np.array([[7,11,16,18,23,33],[1,5,17,19,25,29],[3,8,11,23,24,28],[1,13,18,21,25,33],[6,7,12,23,24,32],[3,15,17,18,20,22]])
ProbeLoad6List2 = np.array([34,17,14,25,6,14])
LocationsLoad6List3 = np.array([[3,11,15,22,24,34],[5,7,8,10,14,25],[13,16,26,27,29,30],[3,7,17,18,19,20],[2,12,21,22,23,25],[4,5,9,11,29,33]])
ProbeLoad6List3 = np.array([7,7,1,7,12,6])

LocationsLoad7List1 = np.array([[7,11,12,14,17,19,25],[0,6,9,10,18,22,35],[2,19,20,24,26,32,33],[0,5,18,23,27,34,35],[2,4,9,14,19,28,29],[3,15,20,22,25,26,34]])
ProbeLoad7List1 = np.array([7,35,34,23,15,21])
LocationsLoad7List2 = np.array([[5,11,15,18,22,31,32],[0,10,24,27,28,34,35],[8,9,14,16,18,23,25],[0,6,15,22,27,28,29],[5,8,10,13,14,24,26],[3,9,12,15,18,20,27]])
ProbeLoad7List2 = np.array([11,0,7,6,21,33])
LocationsLoad7List3 = np.array([[5,6,8,26,29,30,35],[0,9,13,16,22,28,31],[6,10,14,26,30,32,35],[3,4,23,27,28,31,34],[6,9,12,14,16,24,25],[0,8,15,21,27,29,33]])
ProbeLoad7List3 = np.array([6,28,25,4,17,20])

LocationsLoad8List1 = np.array([[1,4,12,19,30,31,33,34],[11,13,15,21,25,27,28,32],[0,1,5,7,8,20,26,35],[2,6,23,27,28,29,33,34],[1,4,7,9,13,15,26,32],[2,5,8,10,27,33,34,35]])
ProbeLoad8List1 = np.array([9,7,10,23,26,27])
LocationsLoad8List2 = np.array([[3,6,13,17,18,21,32,35],[0,2,8,20,24,25,30,31],[3,5,9,13,23,27,32,33],[0,15,17,18,19,24,28,34],[1,5,12,22,27,29,30,32],[2,8,14,15,25,26,28,34]])
ProbeLoad8List2 = np.array([16,16,22,28,12,26])
LocationsLoad8List3 = np.array([[1,5,17,22,30,31,33,35],[8,9,13,14,18,21,25,27],[2,5,7,12,15,19,20,22],[4,8,11,18,21,23,28,30],[2,3,9,12,20,22,27,31],[4,5,10,15,17,25,29,35]])
ProbeLoad8List3 = np.array([19,16,11,4,22,15])

LocationsLoad9List1 = np.array([[3,8,9,11,12,20,24,25,29],[2,4,7,10,13,17,27,32,35],[0,9,14,18,24,25,26,29,31],[2,3,4,10,12,20,23,28,33],[0,5,7,8,14,17,18,24,30],[2,3,6,9,15,16,19,21,32]])
ProbeLoad9List1 = np.array([17,13,21,30,30,3])
LocationsLoad9List2 = np.array([[6,10,11,12,14,16,23,24,29],[1,5,8,9,13,22,27,30,33],[0,2,7,15,16,18,21,23,25],[3,11,12,13,14,20,22,31,34],[4,5,6,9,10,15,25,30,32],[12,17,23,26,27,29,33,34,35]])
ProbeLoad9List2 = np.array([3,5,19,19,4,27])
LocationsLoad9List3 = np.array([[0,2,11,17,19,20,26,30,33],[4,9,10,13,14,18,22,25,35],[0,1,2,3,6,8,12,21,30],[5,10,13,15,18,22,23,24,25],[0,4,9,11,27,28,29,30,34],[2,3,8,10,13,16,18,23,24]])
ProbeLoad9List3 = np.array([21,9,32,31,0,23])

LocationsLoad10List1 = np.array([[3,5,6,10,11,14,16,18,34,35],[2,7,8,12,15,17,25,26,29,32],[0,1,3,9,10,11,13,16,27,35],[4,5,6,8,12,20,28,29,32,34],[9,10,14,16,18,19,23,25,26,33],[0,3,6,7,11,12,21,22,24,34]])
ProbeLoad10List1 = np.array([8,12,19,28,18,30])
LocationsLoad10List2 = np.array([[5,10,12,14,18,20,21,23,26,29],[2,6,7,8,9,16,19,30,32,35],[4,5,11,13,21,23,24,28,29,31],[0,1,9,14,15,20,22,27,30,34],[2,6,8,10,18,23,25,28,32,33],[1,4,5,9,14,16,19,21,26,34]])
ProbeLoad10List2 = np.array([22,19,33,14,23,3])
LocationsLoad10List3 = np.array([[7,12,19,23,24,25,27,28,29,33],[2,4,5,8,17,18,26,30,32,34],[0,11,12,13,15,20,21,22,24,25],[3,5,6,7,8,9,28,32,33,34],[10,16,17,19,23,25,26,27,30,31],[1,3,11,18,22,24,28,32,33,35]])
ProbeLoad10List3 = np.array([21,5,6,33,26,14])

LocationsLoad11List1 = np.array([[2,3,4,11,16,19,25,27,28,31,33],[5,14,15,17,23,24,26,29,30,34,35],[1,2,3,8,10,18,20,21,25,32,33],[0,4,7,9,12,14,17,19,26,30,31],[1,6,10,16,18,21,22,24,33,34,35],[7,8,9,11,12,14,23,26,27,28,29]])
ProbeLoad11List1 = np.array([2,23,12,14,13,13])
LocationsLoad11List2 = np.array([[2,3,14,19,20,21,22,24,25,27,28],[0,1,4,6,9,11,18,23,30,31,33],[2,8,10,14,16,17,19,21,24,25,34],[0,3,11,12,13,20,23,26,28,32,33],[2,8,9,10,14,15,16,25,27,30,34],[3,6,13,17,20,22,23,24,31,33,35]])
ProbeLoad11List2 = np.array([28,1,13,3,7,29])
LocationsLoad11List3 = np.array([[0,6,7,12,16,20,21,23,25,29,33],[2,4,10,11,14,18,19,24,27,30,32],[0,6,7,15,16,17,21,22,26,34,35],[3,4,8,9,14,18,24,25,28,29,30],[1,7,12,13,17,22,23,26,27,31,35],[6,8,9,10,24,25,28,29,32,33,34]])
ProbeLoad11List3 = np.array([6,10,1,25,5,5])

LocationsLoad12List1 = np.array([[2,3,6,14,15,16,17,19,20,25,31,33],[0,4,9,10,21,22,23,27,30,32,34,35],[1,3,6,12,16,17,18,19,24,29,31,33],[2,4,5,7,9,11,13,14,23,27,32,34],[1,3,6,12,21,22,24,26,28,29,31,35],[5,8,9,10,14,15,16,18,20,23,27,32]])
ProbeLoad12List1 = np.array([8,4,3,26,8,16])
LocationsLoad12List2 = np.array([[0,7,9,11,14,16,19,25,27,32,33,35],[2,3,6,10,13,15,17,18,24,26,29,31],[1,4,7,8,14,16,20,21,22,25,30,33],[2,5,6,12,13,15,18,23,28,29,31,32],[1,3,7,17,20,21,24,25,26,27,30,35],[0,4,8,9,10,14,18,19,22,23,29,33]])
ProbeLoad12List2 = np.array([24,24,21,34,34,33])
LocationsLoad12List3 = np.array([[0,1,12,13,14,15,17,19,24,26,30,35],[5,6,8,9,16,18,22,23,27,28,32,33],[0,1,3,4,11,17,21,24,25,29,31,35],[5,7,9,10,12,15,18,19,20,27,32,34],[11,13,14,17,22,23,24,25,26,30,31,33],[3,6,7,9,15,16,18,20,21,28,32,34]])
ProbeLoad12List3 = np.array([16,16,17,2,2,32])

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
# LocationsLoad13 = np.array([LocationsLoad13List1,LocationsLoad13List2,LocationsLoad13List3])
# LocationsLoad14 = np.array([LocationsLoad14List1,LocationsLoad14List2,LocationsLoad14List3])
# LocationsLoad15 = np.array([LocationsLoad15List1,LocationsLoad15List2,LocationsLoad15List3])
# Create a list of these that can be indexed for load
ProbeLoad1 = np.array([ProbeLoad1List1, ProbeLoad1List2, ProbeLoad1List3])
ProbeLoad2 = np.array([ProbeLoad2List1, ProbeLoad2List2, ProbeLoad2List3])
ProbeLoad3 = np.array([ProbeLoad3List1, ProbeLoad3List2, ProbeLoad3List3])
ProbeLoad4 = np.array([ProbeLoad4List1, ProbeLoad4List2, ProbeLoad4List3])
ProbeLoad5 = np.array([ProbeLoad5List1, ProbeLoad5List2, ProbeLoad5List3])
ProbeLoad6 = np.array([ProbeLoad6List1, ProbeLoad6List2, ProbeLoad6List3])
ProbeLoad7 = np.array([ProbeLoad7List1, ProbeLoad7List2, ProbeLoad7List3])
ProbeLoad8 = np.array([ProbeLoad8List1, ProbeLoad8List2, ProbeLoad8List3])
ProbeLoad9 = np.array([ProbeLoad9List1, ProbeLoad9List2, ProbeLoad9List3])
ProbeLoad10 = np.array([ProbeLoad10List1, ProbeLoad10List2, ProbeLoad10List3])
ProbeLoad11 = np.array([ProbeLoad11List1, ProbeLoad11List2, ProbeLoad11List3])
ProbeLoad12 = np.array([ProbeLoad12List1, ProbeLoad12List2, ProbeLoad12List3])
# ProbeLoad13 = np.array([ProbeList13Run1, ProbeList13Run2, ProbeList13Run3])
# ProbeLoad14 = np.array([ProbeList14Run1, ProbeList14Run2, ProbeList14Run3])
# ProbeLoad15 = np.array([ProbeList15Run1, ProbeList15Run2, ProbeList15Run3])
AllLocations=([LocationsLoad1, LocationsLoad2, LocationsLoad3, LocationsLoad4, LocationsLoad5, LocationsLoad6, LocationsLoad7, LocationsLoad8, LocationsLoad9, LocationsLoad10, LocationsLoad11, LocationsLoad12])
AllProbes = ([ProbeLoad1,ProbeLoad2,ProbeLoad3,ProbeLoad4,ProbeLoad5,ProbeLoad6,ProbeLoad7,ProbeLoad8,ProbeLoad9,ProbeLoad10,ProbeLoad11,ProbeLoad12])
