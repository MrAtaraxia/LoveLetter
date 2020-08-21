"""
pygameFront.py
# This goes over how to make the pygame window appear in a certain location.
# This only works on windows!

"""
#  Default Imports
import cProfile     # Not sure how I am going to use this. What it does exactly...
import os
import pstats, io
import sys
import time
#  Other Imports
import pygame
#  My imports


if os.name == "nt":     # Windows
    from win32api import GetSystemMetrics   # pip install pypiwin32 OR pip install pywin32
if os.name == "posix":  # Linux
    print("This does not currently work on linux.")
if os.name == "mac?":   # Mac?
    print("This does not currently work on mac.")

#my_profile = cProfile.Profile()
#my_profile.enable()

#print(my_profile)

screen_width = 640
screen_height = 480

if os.name == "nt":
    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)

width = 320
height = 240
x, y = screen_width-width-2, 2

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
screen = pygame.display.set_mode((width, height))

# wait for a while to show the window.
time.sleep(1)

#my_profile.disable()
#s = io.StringIO()
#sortby = 'cumulative'
#ps = pstats.Stats(my_profile, stream=s).sort_stats(sortby)
#ps.print_stats()
#print(s.getvalue())
#my_profile.dump_stats('mypygame.txt')

os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz 2.44.1/bin"
from graphviz import Digraph
# sys.path.append(r"C:\Program Files\Graphviz 2.44.1\bin")
# print(sys.path)
dot = Digraph(comment='The Round Table')
dot  #doctest: +ELLIPSIS
dot.node('A', 'King Arthur')
dot.node('B', 'Dude 1')
dot.node('L', 'Dude L')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
os.path
print(dot.source)  # doctest: +NORMALIZE_WHITESPACE

# dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
# 'test-output/round-table.gv.pdf'
dot.render('test-output/round-table.gv', view=True)
'test-output/round-table.gv.pdf'
