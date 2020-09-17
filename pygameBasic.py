# standard imports
import random
# Other imports
import pygame
import keyboard
# Local imports

# ADJUSTING THE ORDER OF THE LIST
#
# mylist.insert(0, mylist.pop(mylist.index(targetvalue)))


# Event List:
# Events that come from the system will have a guaranteed set of member attributes based on the type. The following is a list event types with their specific attributes.
#
# QUIT              none
# ACTIVEEVENT       gain, state
# KEYDOWN           key, mod, unicode, scancode
# KEYUP             key, mod
# MOUSEMOTION       pos, rel, buttons
# MOUSEBUTTONUP     pos, button
# MOUSEBUTTONDOWN   pos, button
# JOYAXISMOTION     joy, axis, value
# JOYBALLMOTION     joy, ball, rel
# JOYHATMOTION      joy, hat, value
# JOYBUTTONUP       joy, button
# JOYBUTTONDOWN     joy, button
# VIDEORESIZE       size, w, h
# VIDEOEXPOSE       none
# USEREVENT         code
#
#
# New in pygame 1.9.2.
#
# On MacOSX when a file is opened using a pygame application, a USEREVENT with its code attribute set to pygame.USEREVENT_DROPFILE is generated. There is an additional attribute called filename where the name of the file being accessed is stored.
#
# USEREVENT         code=pygame.USEREVENT_DROPFILE, filename
#
#
# New in pygame 1.9.5.
#
# When compiled with SDL2, pygame has these additional events and their attributes.
#
# AUDIODEVICEADDED   which, iscapture
# AUDIODEVICEREMOVED which, iscapture
# FINGERMOTION       touch_id, finger_id, x, y, dx, dy
# FINGERDOWN         touch_id, finger_id, x, y, dx, dy
# FINGERUP           touch_id, finger_id, x, y, dx, dy
# MULTIGESTURE       touch_id, x, y, pinched, rotated, num_fingers
# TEXTEDITING        text, start, length
# TEXTINPUT          text
#
#
# New in pygame 2.0.0.
#
# pygame can recognize text or files dropped in its window. If a file is dropped, file will be its path. The DROPTEXT event is only supported on X11.
#
# DROPBEGIN
# DROPCOMPLETE
# DROPFILE        file
# DROPTEXT        text
#
#
# New in pygame 2.0.0.
#
# Events reserved for pygame.midipygame module for interacting with midi input and output. use.
#
# MIDIIN
# MIDIOUT

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
TEXT_COLOR = BLACK
BG_COLOR = GREEN
FG_COLOR = BLUE
CIRCLE_COLOR = BLUE
FPS = 60


def main_game_loop(w, h):
    # global running, screen
    running = True
    pygame.init()
    pygame.display.list_modes()
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("BASIC")
    pygame.display.update()
    c_sprites = []
    c_color = CIRCLE_COLOR
    my_clock = pygame.time.Clock()
    my_clock.tick(FPS)
    # c_sprites.insert()
    while running:
        print(my_clock.get_fps())
        pygame.display.set_caption(str(my_clock.get_fps()))
        draw_screen(screen, c_sprites)
        c_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        ev = pygame.event.get()

        for event in ev:
            running = main_event_loop(event, c_sprites, c_color)



def main_event_loop(event, sprites, color):
    if event.type == pygame.QUIT:
        return False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_down_event(event, sprites, color)
    if event.type == pygame.MOUSEMOTION:
        mouse_motion_event(event)
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_up_event(event)
    if event.type == pygame.KEYDOWN:
        return key_down_event(event)
    if event.type == pygame.KEYUP:
        key_down_event(event)
    return True


def mouse_down_event(event, sprites, color):
    size = 20
    sprites.append(make_circle(size, color))
    # draw_circle(screen)
    pygame.display.update()


def mouse_motion_event(event):
    # If left button is clicked.
    if event.buttons[0] == 1:
        print(event.pos, "LEFT BUTTON!")
    # If middle button is clicked.
    if event.buttons[1] == 1:
        print(event.pos, "MIDDLE BUTTON!")
    # If right button is clicked.
    if event.buttons[2] == 1:
        print(event.pos, "RIGHT BUTTON!")


def mouse_up_event(event):
    # MOUSEBUTTONUP     pos, button
    pass


def key_down_event(event):
    if event.key == pygame.K_ESCAPE:
        return False


def key_up_event(event):
    if event.key == pygame.K_ESCAPE:
        return False


def get_pos():
    pos = pygame.mouse.get_pos()
    return pos


def make_circle(size, color):
    pos = get_pos()
    return "CIRCLE", color, pos, size


def draw_screen(screen, sprites):
    screen.fill(BG_COLOR)

    for sprite in sprites:
        if sprite[0] == "CIRCLE":
            draw_circle(screen, sprite[3], sprite[2], sprite[1])

    pygame.display.update()


def draw_circle(screen, size, pos, color=CIRCLE_COLOR):
    # pos = get_pos()
    pygame.draw.circle(screen, color, pos, size)


if __name__ == "__main__":
    (width, height) = (200, 300)
    main_game_loop(width, height)
