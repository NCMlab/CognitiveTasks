from __future__ import absolute_import, division
from psychopy import sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'


import pyglet
one = pyglet.resource.media('NumberSounds/7.wav')


one.play()
pyglet.app.run()

pyglet.app.exit()


player = pyglet.media.Player()
player.queue(one)
player.queue(two)
player.queue(three)
player.play(explosion)pyglet.app.run()
pyglet.app.run()

