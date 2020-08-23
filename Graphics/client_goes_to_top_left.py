"""
Client

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
                 border=None, border_width=0,
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
        :param border: The border color around the button
        :param border_width: The border width around the button
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

    def draw(self, window):
        """
        Drawing the button on the window.

        :param window: The surface that is going to be drawn on.
        :return: None
        """
        cur_x, cur_y = self.x, self.y

        if self.updating:
            cur_x, cur_y = self.current_x, self.current_y
            print(cur_x, cur_y)

        if not self.is_clicked:
            if type(self.bg_up) == tuple or type(self.bg_up) == str:
                pygame.draw.rect(window, self.bg_up, (cur_x, cur_y, self.width, self.height))
            else:
                window.blit(self.bg_up, (cur_x, cur_y))
            text = self.font.render(self.text, 1, self.text_color)
            window.blit(text, (cur_x + round(self.width / 2) - round(text.get_width() / 2),
                               cur_y + round(self.height / 2) - round(text.get_height() / 2)))

        else:
            if type(self.bg_down) == tuple or type(self.bg_down) == str:
                pygame.draw.rect(window, self.bg_down, (cur_x, cur_y, self.width, self.height))
            else:
                window.blit(self.bg_down, (cur_x, cur_y))
            text = self.font.render(self.text, 1, self.text_color)
            window.blit(text, (cur_x + round(self.width / 2) - round(text.get_width() / 2),
                               cur_y + round(self.height / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            self.is_clicked = True
            self.was_clicked = True
            self.action()
            return True
        else:
            return False

    def move_release(self, pos):
        """
        Not sure if I want this or if I want to have "this" be more about moving them around...

        :param pos: The position of the mouse
        :return: None
        """
        if self.is_clicked:
            x1 = pos[0]
            y1 = pos[1]
            if (self.x > x1 or x1 > self.x + self.width) or \
                    (self.y > y1 or y1 > self.y + self.height):
                self.is_clicked = False

    def release(self):
        """
        When the mouse releases the button

        :return: None
        """
        self.is_clicked = False

    def update(self):
        if self.was_clicked:
            self.updating = True
            self.was_clicked = False
            # generated = [[u, v] for u, v in self.generator_moving_to(0, 0, 50)]
            self.making_changes(0, 0, 100)
            # self.current_x = self.x + generated[0][0]
            # self.current_y = self.y + generated[0][0]
            self.count = 1
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
        print("DX and DY:",self.d_x, self.d_y)


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
    menu_color1 = (255, 0, 0)
    menu_color2 = (0, 0, 0)
    menu_color3 = (0, 0, 255)
    menu_buttons = [Button("Click to Play!", 0, 0, 300, 100, menu_color1, menu_color2, menu_title),
                    Button("Options", 0, 0, 120, 80, RED_BUTTON, menu_color2, menu_font, button1_action),
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
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    on_menu = False
                    quit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        on_menu = False
                        quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for button in menu_buttons:
                        if button.click(pos):
                            if button.text == "Click to Play!":
                                print("button clicked!")
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
