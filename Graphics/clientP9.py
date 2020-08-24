"""
Client
- A little issue with moving toward the corners
As It does not stop all the time when I am moving the mouse
while clicking on it.

- Now I have to figure out HOW to get it so the OTHER ones do something when
a different one is clicked.

- OK... SO... got the text box working mostly...

It needs... more things though...
OH YEAH I WANTED TO DO THAT... GOD I FORGOT ALL ABOUT THAT GOAL ABOVE...
AND went on to make text box for user input.
...
I am GLAD I wrote that down before or I would have probably NEVER remembered
to actually GO BACK AND DO THAT!...


DONE - Clicking one button, have the other buttons do other things.
Yeah I forgot about that... I will have to see how that goes...
TODO - make it on hover?

TODO - Fix issues with text box. (I want a lot of things for that...)
Selecting (WHICH i think IS A DISASTER IN AND OF ITSELF!) probably...
Clicking and adjusting where the cursor is based on that click.
(That MIGHT be able to be done with the whole text width and height things.
Or looking for collisions with the text elements? IDK...
I will have to look into it more!

TODO - make a scrolling location of the log?

TODO - Make another menu!
Probably the login screen next. To have it DO what I want it to do!
(Able to login and CONTINUE a game!

TODO - Make a settings menu!
I will have to see how I want all of my menus to be...

TODO - Make more button images!
I want different / more button images so I can see what I like the best.
I will have to look into how the ones I am using are designed and go from there?
Other shapes for the buttons? Would that cause issues with the collisions?
IDK






"""
# Original Imports
import inspect
import os
import sys
# Distributed Imports
import pygame
from pygame.locals import *
# Local Imports
from networkP9 import Network

# import pickle

pygame.font.init()

width = 600
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
B_DOWN = pygame.image.load(os.path.join("moreimages", "button_down.png")).convert_alpha()
B_UP = pygame.image.load(os.path.join("moreimages", "button_normal.png")).convert_alpha()
R_DOWN = pygame.image.load(os.path.join("moreimages", "red_button_down.png")).convert_alpha()
R_UP = pygame.image.load(os.path.join("moreimages", "red_button_normal.png")).convert_alpha()
BLUE_BUTTON = [B_UP, B_DOWN]
RED_BUTTON = [R_UP, R_DOWN]


class Button:
    def __init__(self, text: str, x: int, y: int, w: int, h: int,
                 bg=None, text_color=None, font=None,
                 action=None,
                 border_width=0, border=None,
                 rotation=None, scale=1):
        """
        SO MANY PARAMAMTERS... omg...

        :param text: The Text that is going to be on the button
        :param x: The x position of the button
        :param y: The y position of the button
        :param w: The width of the button
        :param h: The height of the button
        :param bg: The background of the button (sprite or color)
        :param text_color: The color of the text on the button
        :param font: The font of the text on the button
        :param action: The action that happens when you click the button
        :param border_width: The border width around the button
        :param border: The border color around the button
        :param rotation: The amount of rotation on the button
        :param scale: The scale of the button
        """
        self.text = text
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        if bg is None:
            self.bg_down = self.bg_up = (0, 0, 0)
        elif type(bg) == tuple:
            self.bg_down = self.bg_up = bg
        elif type(bg) == list:
            self.bg = bg
            self.bg_up = pygame.transform.scale(self.bg[0], (self.width, self.height))
            self.bg_down = pygame.transform.scale(self.bg[1], (self.width, self.height))

        elif type(bg) == pygame.sprite():
            pass

        if text_color is None:
            self.text_color = (0, 0, 0)
        else:
            self.text_color = text_color
        if font is None:
            self.font = pygame.font.SysFont("comicsans", 25)
        else:
            self.font = font
        self.action = action
        if border is None:
            self.border = (255, 255, 255)
        else:
            self.border = border
        self.border_width = border_width
        self.rotation = rotation
        self.scale = scale
        self.is_clicked = False

        self.was_clicked = False
        self.updating = False
        self.d_x = 0
        self.d_y = 0
        self.current_x = self.x
        self.current_y = self.y
        self.count = 0
        self.forward = True
        self.pause = False

    def draw(self, window):
        """
        Drawing the button on the window.

        :param window: The surface that is going to be drawn on.
        :return: None
        """
        # cur_x, cur_y = self.current_x, self.current_x
        wid, hei = self.width, self.height
        if self.border_width > 0:
            print(self.border_width, self.x)
            pygame.draw.rect(window, self.border, (cur_x, cur_y, wid, hei))
            cur_x = self.x + self.border_width
            cur_y = self.y + self.border_width
            wid   = self.width - self.border_width * 2
            hei   = self.height - self.border_width * 2
            self.bg_up = pygame.transform.scale(self.bg[0], (wid, hei))
            self.bg_down = pygame.transform.scale(self.bg[1], (wid, hei))

        if self.updating:
            cur_x, cur_y = self.current_x, self.current_y
            # print(cur_x, cur_y, self.pause)


        if not self.is_clicked:
            if type(self.bg_up) == tuple or type(self.bg_up) == str:
                pygame.draw.rect(window, self.bg_up, (cur_x, cur_y, wid, hei))
            else:
                window.blit(self.bg_up, (cur_x, cur_y))
            text = self.font.render(self.text, 1, self.text_color)
            window.blit(text, (cur_x + round(wid / 2) - round(text.get_width() / 2),
                               cur_y + round(hei / 2) - round(text.get_height() / 2)))

        else:
            if type(self.bg_down) == tuple or type(self.bg_down) == str:
                pygame.draw.rect(window, self.bg_down, (cur_x, cur_y, wid, hei))
            else:
                window.blit(self.bg_down, (cur_x, cur_y))
            text = self.font.render(self.text, 1, self.text_color)
            window.blit(text, (cur_x + round(wid / 2) - round(text.get_width() / 2),
                               cur_y + round(hei / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        cur_x, cur_y = self.x, self.y
        if self.updating:
            cur_x, cur_y = self.current_x, self.current_y
        if cur_x <= x1 <= cur_x + self.width and cur_y <= y1 <= cur_y + self.height:
            self.is_clicked = True

            if self.updating:
                self.pause = True
            else:
                self.was_clicked = True

            if self.action:
                self.action()
            return True
        else:
            return False

    def hover(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        cur_x, cur_y = self.x, self.y
        if cur_x <= x1 <= cur_x + self.width and cur_y <= y1 <= cur_y + self.height:
            return True
        else:
            return False

    def move_release(self, pos):
        """
        Not sure if I want this or if I want to have "this" be more about moving them around...

        :param pos: The position of the mouse
        :return: None
        """
        # Still has issues with holding down and moving the mouse
        # to maintain the paused effect... Not sure why though.
        # if not self.hover(pos):
        #    self.is_clicked = False
        #    self.release()
        pass

        """
        if self.is_clicked:
            x1 = pos[0]
            y1 = pos[1]
            if (self.x > x1 or x1 > self.x + self.width) or \
                    (self.y > y1 or y1 > self.y + self.height):
                self.is_clicked = False
                self.release()  # That SHOULD take care of all of that I believe
            else:
                if self.pause:
                    self.pause = True
                    # """

    def release(self):
        """
        When the mouse releases the button

        :return: None
        """
        self.is_clicked = False
        if self.pause:
            self.pause = False

    def update(self):
        if self.was_clicked:
            self.updating = True
            self.was_clicked = False
            self.making_changes(0, 0, 100)
            self.count = 1
        if self.pause:
            return
        if self.count == 0:
            self.updating = False
            self.forward = True
        if self.updating:
            if self.count >= 100 and self.forward:
                self.forward = False
            self.current_x = self.x - self.d_x * self.count
            self.current_y = self.y - self.d_y * self.count
            if self.forward:
                self.count += 1
            else:
                self.count -= 1

    def making_changes(self, des_x, des_y, steps):
        self.d_x = ((self.x - des_x) / steps)
        self.d_y = ((self.y - des_y) / steps)
        # print("DX and DY:", self.d_x, self.d_y)

    def animate(self):
        self.making_changes(width - self.width, 0, 100)
        self.updating = True
        self.count = 1


class InputTextBox:
    def __init__(self, text, x, y, w, h,
                 bg=None, text_color=None, font=None, ):
        self.displayed_text = text
        self.active = False
        self.inputted_text = ""
        self.cursor_location = 0
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.cursor_color = (100, 100, 100)
        if bg is None:
            self.bg_down = (50, 50, 50)
            self.bg_up = (0, 0, 0)
        elif type(bg) == tuple:
            self.bg_up = bg
            # new_bg = []
            # for num in bg:
            #    new_bg.append((num + 50) % 256)
            self.bg_down = tuple((i - 25) % 256 for i in list(bg))
        elif type(bg) == list:
            self.bg = bg
            self.bg_up = pygame.transform.scale(self.bg[0], (self.width, self.height))
            self.bg_down = pygame.transform.scale(self.bg[1], (self.width, self.height))

        elif type(bg) == pygame.sprite():
            pass

        if text_color is None:
            self.text_color = (0, 0, 0)
        else:
            self.text_color = text_color
        if font is None:
            self.font = pygame.font.SysFont("comicsans", 25)
        else:
            self.font = font

        self.count = 0

    def adding_to_string(self, event):
        if self.active:
            if event.key in [pygame.K_BACKSPACE]:
                if self.cursor_location > 0:
                    print(self.inputted_text[:self.cursor_location])
                    print(self.inputted_text[self.cursor_location:])
                    self.inputted_text = self.inputted_text[:self.cursor_location - 1] + \
                                         self.inputted_text[self.cursor_location:]
                # self.inputted_text = self.inputted_text[0:-1]
                self.cursor_location -= 1
            elif event.key in [pygame.K_DELETE]:
                if self.cursor_location < len(self.inputted_text):
                    self.inputted_text = self.inputted_text[:self.cursor_location] + \
                                         self.inputted_text[self.cursor_location + 1:]
                    # self.inputted_text.
                    pass
            elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                print(self.inputted_text, self.cursor_location)
                self.inputted_text = ""
                self.cursor_location = 0
            elif event.key in [pygame.K_ESCAPE, pygame.K_F1, pygame.K_F2, pygame.K_F3, pygame.K_F4,
                               pygame.K_F5, pygame.K_F6, pygame.K_F7, pygame.K_F8, pygame.K_F9,
                               pygame.K_F10, pygame.K_F11, pygame.K_F12, pygame.K_F13, pygame.K_F14,
                               pygame.K_F15]:
                return
            elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                               pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_a, pygame.K_b,
                               pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h,
                               pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
                               pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t,
                               pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z,
                               pygame.K_SPACE]:
                self.inputted_text += event.unicode
                self.cursor_location += 1
            elif event.key in [pygame.K_LEFT]:
                if self.cursor_location > 0:
                    self.cursor_location -= 1
            elif event.key in [pygame.K_RIGHT]:
                if self.cursor_location < len(self.inputted_text):
                    self.cursor_location += 1


            else:
                print("Else Input!")

    def draw(self, window):
        """
        Drawing the text box on the window.
        Now it also does the indicator!

        :param window: The surface that is going to be drawn on.
        :return: None
        """
        cur_x, cur_y = self.x, self.y
        align_left = True
        using_text = self.inputted_text
        text_left = cur_x + 5
        if self.inputted_text == "" and not self.active:
            using_text = self.displayed_text
            align_left = False
        if not self.active:
            if type(self.bg_up) == tuple or type(self.bg_up) == str:
                pygame.draw.rect(window, self.bg_up, (cur_x, cur_y, self.width, self.height))
            else:
                window.blit(self.bg_up, (cur_x, cur_y))
            text = self.font.render(using_text, 1, self.text_color)
            text_top = cur_y + round(self.height / 2) - round(text.get_height() / 2)
            if not align_left:
                text_left = cur_x + round(self.width / 2) - round(text.get_width() / 2)
            window.blit(text, (text_left, text_top))

        else:
            if self.count < 15:
                if type(self.bg_down) == tuple or type(self.bg_down) == str:
                    pygame.draw.rect(window, self.bg_down, (cur_x, cur_y, self.width, self.height))
                else:
                    window.blit(self.bg_down, (cur_x, cur_y))
                text = self.font.render(using_text, 1, self.text_color)
                text_top = cur_y + round(self.height / 2) - round(text.get_height() / 2)
                window.blit(text, (text_left, text_top))
            else:
                # using_text = using_text + "|" #  self.cursor_location
                left_width = self.get_text_width(using_text[:self.cursor_location])
                # using_text = using_text[:self.cursor_location] + "|" + using_text[self.cursor_location:]
                if type(self.bg_down) == tuple or type(self.bg_down) == str:
                    pygame.draw.rect(window, self.bg_down, (cur_x, cur_y, self.width, self.height))
                else:
                    window.blit(self.bg_down, (cur_x, cur_y))
                text = self.font.render(using_text, 1, self.text_color)
                cursor = self.font.render("|", 1, self.cursor_color)

                text_top = cur_y + round(self.height / 2) - round(text.get_height() / 2)
                window.blit(text, (text_left, text_top))
                window.blit(cursor, (text_left + left_width - 2, text_top))

            self.count = (self.count + 1) % 30

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        cur_x, cur_y = self.x, self.y
        # if self.updating:
        #    cur_x, cur_y = self.current_x, self.current_y
        if self.active:
            if cur_x <= x1 <= cur_x + self.width and cur_y <= y1 <= cur_y + self.height:
                print("Find the LOCATION of the cursor!")
        if cur_x <= x1 <= cur_x + self.width and cur_y <= y1 <= cur_y + self.height:
            self.active = True
        else:
            self.active = False

    def get_text_height(self):
        font_obj = self.font.render("A", False, (0, 0, 0))
        font_rect = font_obj.get_rect()

        return font_rect.height

    def get_text_width(self, text):
        font_obj = self.font.render(text, False, (0, 0, 0))
        font_rect = font_obj.get_rect()

        return font_rect.width


def button1_action():
    print("Button 1 was clicked!")
    # move_sprite()


def button2_action():
    print("Button 2 was clicked!")


def button3_action():
    print("Button 3 was clicked!")


def button4_action():
    print("Button 4 was clicked!")


def redrawWindow(win, game, p, buttons):
    global width, height
    win.fill((128, 128, 128))

    if not (game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255, 0, 0), True)
        win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Your Move", 1, (0, 255, 255))
        win.blit(text, (30, 100))

        text = font.render("Opponents", 1, (0, 255, 255))
        win.blit(text, (330, 100))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (0, 0, 0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, (0, 0, 0))
            elif game.p1Went:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if game.p2Went and p == 1:
                text2 = font.render(move2, 1, (0, 0, 0))
            elif game.p2Went:
                text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))

        if p == 1:
            win.blit(text2, (50, 250))
            win.blit(text1, (350, 250))
        else:
            win.blit(text1, (50, 250))
            win.blit(text2, (350, 250))

        for button in buttons:
            button.draw(win)

    pygame.display.update()


def game_main_loop():
    game_buttons = [Button("Rock", 25, 300, 100, 50, (0, 0, 0)),
                    Button("Scissors", 225, 300, 100, 50, (255, 0, 0)),
                    Button("Paper", 425, 300, 100, 50, (0, 255, 0))]

    global screen
    clock = pygame.time.Clock()
    connection = Network()
    player = int(connection.get_player_number())
    print("You are player", player)

    game_quit = False
    while game_quit is False:
        clock.tick(60)
        try:
            game = connection.send("get")
        except Exception as run_e:
            print("Run Exception: ", run_e)
            print("Location:      ", inspect.currentframe().f_code.co_name)
            print("Called By:     ", inspect.stack()[1][0].f_code.co_name)
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(screen, game, player, game_buttons)
            pygame.time.delay(500)
            try:
                game = connection.send("reset")
            except Exception as e:
                print(e)
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You Won!", 1, (255, 0, 0))
            elif game.winner() == -1:
                text = font.render("Tie Game!", 1, (255, 0, 0))
            else:
                text = font.render("You Lost...", 1, (255, 0, 0))

            screen.blit(text, (width / 2 - text.get_width() / 2,
                               height / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(2000)

        player_action = game_handle_keys(game_buttons, connection, game, player)
        if player_action == "QUIT":
            game_quit = True
            return game_quit

        redrawWindow(screen, game, player, game_buttons)


def game_handle_keys(buttons, connect, game_name, player_number):
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            return "QUIT"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "QUIT"
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.click(pos) and game_name.connected():
                    if player_number == 0:
                        if not game_name.p1Went:
                            connect.send(button.text)
                    else:
                        if not game_name.p2Went:
                            connect.send(button.text)


def menu_screen():
    font_big = pygame.font.SysFont("comicsans", 60)
    font_regular = pygame.font.SysFont("comicsans", 30)
    menu_title = font_big
    menu_font = font_regular
    buttons_clicked = False
    menu_color1 = (255, 0, 0)
    menu_color2 = (0, 0, 0)
    menu_color3 = (0, 0, 255)
    menu_text_box = [InputTextBox("Input Text Here", 0, 0, 400, 100, (255, 255, 255),
                                  (0, 0, 0), font_regular)]
    menu_buttons = [Button("Click to Play!", 0, 0, 300, 100, menu_color1, menu_color2, menu_title),
                    Button("Options", 0, 0, 120, 80, RED_BUTTON, menu_color2, menu_font, button1_action, 5,
                           (0, 0, 0)),
                    Button("Rules", 0, 0, 120, 80, RED_BUTTON, menu_color2, menu_font, button2_action),
                    Button("Print", 0, 0, 120, 80, BLUE_BUTTON, menu_color2, menu_font, button3_action),
                    Button("Quit", 0, 0, 120, 80, BLUE_BUTTON, menu_color2, menu_font, button4_action)
                    ]
    menu_buttons[0].x = int(width / 10 - menu_buttons[0].width / 10) * 5
    menu_buttons[0].y = int(height / 10 - menu_buttons[0].height / 10) * 3
    menu_buttons[1].x = int(width / 10 - menu_buttons[1].width / 10) * 3
    menu_buttons[1].y = int(height / 10 - menu_buttons[1].height / 10) * 6
    menu_buttons[2].x = int(width / 10 - menu_buttons[2].width / 10) * 7
    menu_buttons[2].y = int(height / 10 - menu_buttons[2].height / 10) * 6
    menu_buttons[3].x = int(width / 10 - menu_buttons[3].width / 10) * 3
    menu_buttons[3].y = int(height / 10 - menu_buttons[3].height / 10) * 8
    menu_buttons[4].x = int(width / 10 - menu_buttons[4].width / 10) * 7
    menu_buttons[4].y = int(height / 10 - menu_buttons[4].height / 10) * 8

    on_menu = True
    quit_game = False
    global screen
    clock = pygame.time.Clock()

    while not quit_game:
        while on_menu:
            clock.tick(30)
            screen.fill((128, 128, 128))
            # text = font.render("Click to Play!", 1, (255, 0, 0))
            # screen.blit(text, ((width / 2 - text.get_width() / 2), 200))
            for button in menu_buttons:
                button.draw(screen)
            for box in menu_text_box:
                box.draw(screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    on_menu = False
                    quit_game = True
                if event.type == pygame.KEYDOWN:
                    for box in menu_text_box:
                        box.adding_to_string(event)
                    if event.key == pygame.K_ESCAPE:
                        on_menu = False
                        quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for box in menu_text_box:
                        box.click(pos)

                    for button in menu_buttons:
                        if button.click(pos):
                            buttons_clicked = True
                            print("button clicked!")
                            if button.text == "Click to Play!":
                                on_menu = False
                                break
                            if button.text == "Quit":
                                on_menu = False
                                quit_game = True
                                break
                if event.type == pygame.MOUSEBUTTONUP:
                    for button in menu_buttons:
                        button.release()
                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    for button in menu_buttons:
                        button.move_release(pos)
            if buttons_clicked:
                for button in menu_buttons:
                    if button.count < 1:
                        buttons_clicked = False
                    if button.updating:
                        continue
                    button.animate()

            for button in menu_buttons:
                button.update()

        if not quit_game:
            quit_game = game_main_loop()
    pygame.quit()
    sys.exit()


def main():
    while True:
        menu_screen()


if __name__ == "__main__":
    main()
