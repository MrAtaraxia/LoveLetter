"""
pygameFront.py
# This goes over how to make the pygame window appear in a certain location.
# This only works on windows!


# """
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
#"""


def until_paren(words):
    current = ""
    for char in words:
        if char == "(":
            # return current
            current += char
            continue
        if char == ")":
            current += char
            return current
        current += char
    return current


import os

os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
from graphviz import Digraph

s = Digraph('structs', filename='structs_again_p.gv',
            node_attr={'shape': 'record'})

with open("LoveLetterServer.py", 'r') as r:
    my_file = r.read().split("\n")
# print(my_file)
current_class = {"name": "", "methods": []}
global_class = {"name": "Global", "methods": []}
all_classes = []
in_class = False
blank_lines = 0
for line in my_file:
    if line == "":
        blank_lines += 1
        if blank_lines > 1:
            in_class = False
            if current_class != {"name": "", "methods": []}:
                all_classes.append(current_class)
                current_class = {"name": "", "methods": []}

    else:
        blank_lines = 0

    if in_class:
        if line.startswith("    def"):
            current_class["methods"].append(until_paren(line[8:-1]))
    if line.startswith("def"):
        global_class["methods"].append(until_paren(line[4:-1]))

    if line.startswith("class"):
        current_class["name"] = until_paren(line[6:-1])
        in_class = True
all_classes.append(global_class)

print("ALL CLASSES: ", all_classes)
struct_name = "struct"
current_struct = ""
for number, cur_class in enumerate(all_classes):
    current_struct += "{" + cur_class["name"] + "|"
    for meth in cur_class["methods"]:
        current_struct += meth + "|"
    current_struct = current_struct[:-1] + "}"  # removes the last | and adds the close
    s.node(struct_name + str(number), current_struct)
    current_struct = ""

# s.node('struct1', '{ Main |{a|__init__}| f}')
# s.node('struct2', '<f0> one|<f1> two')
# s.node('struct3', r'hello\nworld |{ b |{c|<here> d|e}| f}| g | h')

# s.edges([('struct1:f1', 'struct2:f0'), ('struct1:f2', 'struct3:here')])
# dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
# 'test-output/round-table.gv.pdf'
s.view()
# s.render('test-output/round-table.gv', view=True)
# 'test-output/round-table.gv.pdf'
# """

"""
# hello.py - http://www.graphviz.org/content/hello
import os
os.environ["PATH"] += os.pathsep + "C:/Users/admin9/Downloads/Graphviz/bin"
from graphviz import Digraph

# import gv

g = Digraph('G', filename='hello.gv')

g.edge('Hello', 'World')

g.view()
"""
