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

# This is the time between blocks. Note that between each block of trials there
# is also the 3-2-1 countdown. Therefore, the full interblock interval is this value PLUS 
# the countdown time, which is 3 seconds.
VSTM_InterBlockTime = 20.0

# This is a delay component for use after instructions and before the first Block and at the
# the end before the thank you screen
VSTM_ShortDelayTime = 5# 16.0

VSTM_ThankYouOnTime = 3