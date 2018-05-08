import psychopy.visual
import psychopy.event

bg_colour = [0,0,0]

oval_fill_colour = [1, 1, 1]


GridCount = 7 # Number of circles to have on each row
GridSize = 160 # The size of the grid for which the circles on on
CircleSize = (GridSize*2)/GridCount # The circle size so that they are all just touching
OffSet = range(-GridSize+CircleSize/2,GridSize-CircleSize/2,CircleSize)
win = psychopy.visual.Window(
    size=[1200, 800],
    units="pix",
    fullscr=False,
    color=bg_colour
)


circle = psychopy.visual.Circle(
    win=win, name='polygon',units='pix', 
    edges=128, size=(CircleSize, CircleSize),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# This is the list of circles to be displayed
# This list startes at the bottom left
Display = [1,2,8,9,17,25,33,41,49]
row_count = 0
count = 0
for y_offset in OffSet:
    for x_offset in OffSet:
        for stim in [circle]:
            stim.pos = [x_offset, y_offset]
            if (count+1 in Display):
                stim.draw()
            count += 1
win.flip()

psychopy.event.waitKeys()

win.close()