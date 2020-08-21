
import os
import time
from win32api import GetSystemMetrics
import pygame

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

x, y = width-250, 0

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
screen = pygame.display.set_mode((200,200))

# wait for a while to show the window.
time.sleep(2)

