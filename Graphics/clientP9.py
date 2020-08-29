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
DONE - Added borders/border width. it appears to be working correctly now.
DONE - Not working correctly. Has wrong hover location when moving.
I used x instead of cur_x etc.
DONE - make it on adjust the border on hover?
Now it does the basic of things.
DONE!! - make it go on hover or back when removed.
MOVE and STAY THERE WHILE HOVERING!

My opinion of the problem with this is:
The fact that I have multiple things I want them to do.
Well not exactly that. Its more that I have things that I WANT them to do
but the things That I have them doing now are in the way of them!
So I will have to disable what I have now to make those work... Meh..


Since I WILL want it to go on hover I will probably need to do that completely
Hmm...
make them go into a row on hover?
I might want to make things like that...
Where I can make lots of functions and mix and match them to work how I want them to
aka Have an on hover method that I would put a call to the change border method
Or the move around method.
It would be interesting to see how it all works out.
Well I should probably also add a method for changing between images as well.
DONE - BASIC selecting... kind of... it has both of the sides of the 'select' there now
I have to make it fill in soon though.
DONE - FILL IN the selection
adjusted the order of things to blit so it shows the indicator while selecting
DONE - Can type characters at any point in the string now, based on the indicatior.

DONE - Clicking on a location to put the cursor there...
I think this is all set up now.

DONE - Shift clicking a location to select the text.
(should be the same as the other once I get the clicking down.. I think)
It was rather easy as it only required setting start location before moving end location.

DONE - Mouse clicking and dragging to select text...
This will basically be 'finishing' the click location above!
I also changed it up to make it call a function to do it. instead
of having the same code in 2 different places.

DONE - Add copying / cuting and pasting...
I don't think this should be too bad once I have my selection...
but we will see...
And I gave each of them their own functions.
so cutting(), pasting(), and copying()
This way if I DO make the stupid right click menu I can easily put them in it.

DONE - Shift arrow keys to select things.
Already done.. not sure when I DID do this but it is already working...
Mostly Done - Fix issues with text box. (I want a lot of things for that...)
Selecting (WHICH i think IS A DISASTER IN AND OF ITSELF!) probably...

DONE - Mapped all of the mouse buttons, in case I want to do the right click for menu thing.

DONE - Fix issues with delete and backspace while selecting text.
This should be working correctly now!

DONE - Add more of the keyboard to this!
all the special characters I think...
Nearly all of the keyboard on an English keyboard should be working now.

DONE - DO i WANT a right click menu here?
Basic right click menu added. It doesn't DO anything
or have any CHOICES on it but it is a right click menu!

Do I WANT it to only be on when I have right clicked ON the selected text?
Or do I want a DIFFERENT one when I am not on it?

2020-08-28 - Friday -
Done- PROGRESS BARS.
Flat ones
Circular Ones
And I kind of went a little cooky with the circular ones and now
I might use it as an indicator because it is that interesting.

I have also been thinking about WHAT I want to do about the general UI UX design
of this whole thing.
And it is causing me annoyances...
Because I don't think I have the skills to currently do what I want to do.
Or I don't know someone who would be willing to guide me through the graphic part of it.
I THINK I can program it fine now... probably...
I just don't have a clear enough VISION of the stupid thing
to be able to be like, YES THAT is what I want...

I suppose I will have to Tear apart what I like / don't like about both.

THAT might help me with the whole thing...

Ok.

DONE - Make a Scroll bar...
It does scroll
but you can't click on it TO scroll
not yet at least...
Also put another text input
at the bottom of that whole thing
and it now inputs to above
the only problem is that I had to REMOVE the other thing
the one where it dealt with hovering it
so it would not do the other things below it
Which is annoying
I will have to look for a different way to deal with that...
Yep.

SO The NEW
TODO - Figure out better way to not click things beneath top things.
I might want to go through and use an "active" thing?
To think about later.


OK... Let's try this one again...
TODO - WORD wrap.






TODO - Add options to the right click menu.
Do I want EVERYTHING to have it's OWN right click
thing inside of it or do I want the right click method
to call the thing?

TODO - Add a lock to the buttons about where they are going?
AKA so that once they are going one direction, they can not be told to go a different one?
SO it doesn't modify d_x d_y if you are currently using them?

Clicking and adjusting where the cursor is based on that click.
(That MIGHT be able to be done with the whole text width and height things.
Or looking for collisions with the text elements? IDK...
I will have to look into it more!
ADD COPYING AND PASTING Ctrl + C / Ctrl + V / Ctrl + Z

DONE - Made a hideable location for the chat to be on.

DONE - Made buttons for top and bottom of the scroll area.
DONE - Added text and the ability to add text to the scroll area.


Done - Make a scroll bar!
if not long, don't display.


DONE - Make it so that on hovering it doesn't interact with what is below it.
put a continue somewhere in it I believe.
This worked, though I didn't do it right when I started it
So it took longer than I expected it to. Mostly because I
was planning to put a return variable in for it
but then relaized it would cause other issues
so I just used its normal variables to do it.
I think that worked out fine.

TODO - Add word wrap to the thing as well.
# find the first space from the right.
if len(words) > window length
input a /r after it?

DONE - Make a scroll bar location.
The location is there... though it doesn't have anything special about it.
TODO - Put a sprite on it that can only move up and down.


TODO - Make a scroll bar that works to scroll around the chat log.


TODO - Put a different input text under the chat log, as it should be.


TODO - I do REALLY want a log that can be viewed through this...

DONE - MAKE scrollable ACTUALLY scrollable!!!
Mostly... It works from the BUTTONS... So yeah. it scrolls at least!!!

TODO - Make it so that it can be scrolled from the mouse wheel.


TODO - make a scrolling location of the log?
I can do what was in video for a basic one. Last x messages
But for the full log... I am not sure yet how to do the scroll bar for it.
I suppose I should make a 'scroll bar' first
and then try and use it for other things afterwards.
Also the ability to hide chat!

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

TODO - bring in drag and drop from other one.

TODO - bring in hand of cards.

TODO - Look into how I set it up so I didn't pick up everything on drag and drop.

TODO - make stackable things!
PUT A NUMBER OF COUNT ABOVE THINGS
How...
if drag and dropping thing.
    if hover stack.
        (show color to indicate stacking if release)
        release to stack


TODO - make right click menu thing.
Is this just a bunch of organized buttons???
I REALLY REALLY REALLY NEED to pull the functions OUT of the button class...
Have them as other methods that can be CALLED so that not every button is FORCED
to do that SAME THING. Yep!


might be able to do it with how i did the on click for the buttons.
each thing is going to need a menu defined after that...
OR JUST A REGULAR MENU!?!
create menu with top left at mouse point.
stays until clicked on other part of screen.

TODO - Make escape bring up the menu instead of exiting the game. From there there will be a quit button!
Continue
Other
IDK
Quit


TODO - yep there is still a LOT to do and this isnt even at the game stage yet!
we shall see how it goes!



I DO ALSO REALLY WANT TO FIX THE STUPID ISSUES WITH it saying all the pygame things are errors!
And figure out how to get / adjust like I was able to with the guy in the bottom right corner
in this version of pycharm!

Oh and look into what potato has put out recently. I did like his old videos.

TODO - ALSO get it so I can move around the map like I used to.
Click and dragging on the map, moves the 'camera' around?
If nothing is 'selected' have keys move around the map?

TODO - Look at A LOT of old projects and see how they are / if I want to use any parts of them or not!

TODO - Look at how this uses pickle, and look into YAML / JSON and see if I want to use those instead.

TODO - Decide how I want to break this program up for client / server things.

TODO - Make it so it automatically downloads the files that it needs if it does not have them!

I do have a LONG todo list now so this will hopefully be interesting!

TODO - LOOK INTO how to make it so the buttons run from the mouse!
Like if within 20 pixels will move in the other direction.
Would be interesting.

TODO - PAUSE MENU -
Resume
Settings
Quit Match
Exit Game

TODO - Make UI Elements.
List of things on the left like there are in TableTopSimulator?


TODO - Make the UI Elements drag and drop able so they can have it how they want it.
How would I want to have to customized though?
Have a seperate screen for adjusting things? Or have it always be able to be accidently moved?
Hmm...

TODO - Make the words wrap
TODO - Make the words pull the thing to the window.
(Probably similar to the scrolling down for the Text window.)



END GOAL:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I want 2 + sets of actions:

if in_hand:
    hovering -> moves it up, spreads other cards
    (if I'm too lazy I can just have it project up above the cards)
    left clicking -> selects it. (have be outside of card size?)
    right clicking -> ?
    click+drag -> drags it. (to be played)


if on board:
    hovering -> zooms in?
    left clicking -> select it?
    right click -> produce menu about it.
    click + drag -> move it.
    drag onto similar -> stack it

OHHHHH Modify them so the boarder is CLEAR!!!
That actually sounds VERY interesting!




"""
# Original Imports
import inspect
import os
import sys
# Distributed Imports
import pygame
import pygame.gfxdraw
from pygame.locals import *
# Local Imports
from networkP9 import Network
import math

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
B_BUTTON = {"up": B_UP, "down": B_DOWN}
R_BUTTON = {"up": R_UP, "down": R_DOWN}


class Card:
    def __init__(self):
        pass


class ProgressBar:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.progress = .20
        self.border = (0, 0, 0)
        self.bar = (0, 150, 0)

    def draw(self, window):
        if self.progress > 1:
            self.progress -= 1
        self.progress += 0.01
        pygame.draw.rect(window, self.border, (self.x, self.y, self.w, self.h), 2)
        innerPos = (self.x + 3, self.y + 3)
        innerSize = ((self.w - 6) * self.progress, self.h - 6)
        pygame.draw.rect(window, self.bar, (*innerPos, *innerSize))


class CircularProgressBar:
    # Highlighting things...
    # Loading screen
    # Actually a progress bar / hp bar...
    # Other...

    def __init__(self):
        self.percentage = 50
        self.surface = pygame.Surface((100, 100))
        self.curve_start = 0
        self.curve_end = 120

    def draw(self, window):
        color = (0, 0, 0)
        my_surface = pygame.Surface([20, 20], pygame.SRCALPHA, 32)
        my_surface.convert_alpha()
        center = (10, 10)
        radius = 5
        # pygame.draw.circle(my_surface, color, center, radius)
        # circle(surface, x, y, r, color) -> None
        # aacircle(surface, x, y, r, color) -> None
        # filled_circle(surface, x, y, r, color)
        # pygame.gfxdraw.filled_circle(my_surface, center[0], center[1], radius, color)
        # filled_ellipse(surface, x, y, rx, ry, color) -> None
        # pygame.gfxdraw.filled_ellipse(window,200, 200, 31, 11, color)
        # pygame.draw.circle
        # for degree in range(0, 180, 1):   # RIGHT SIDE ONLY
        # for degree in range(-90, 90, 1):  # TOP ONLY
        mod_color = color[0]
        if self.curve_start > 360:
            self.curve_start -= 360
            self.curve_end -= 360
        self.curve_start += 6
        if self.curve_end > 360:
            self.curve_end -= 360
            self.curve_start -= 360
        self.curve_end += 6
        for degree in range(self.curve_start, self.curve_end, 1):
            mod_color = (mod_color - 2) % 255

            pygame.draw.circle(my_surface, (mod_color, 0, 0), center, radius)
            self.rotate_around_point(window, my_surface, (300, 300), degree, 50)

        mod_color = color[0]
        for degree in range(self.curve_start - 180, self.curve_end - 180, 1):
            mod_color = (mod_color - 2) % 255

            pygame.draw.circle(my_surface, (mod_color, 0, 0), center, radius)
            self.rotate_around_point(window, my_surface, (300, 300), degree, 50)

    def rotate_around_point(self, window, card_to_rotate, point_to_rotate_around, rotate_to_degrees, radius_yep):
        rotation = -rotate_to_degrees
        rotation = rotation % 360
        rotation_in_radians = (rotate_to_degrees - 90) / 180
        rotation_in_radians = rotation_in_radians % 2
        point_of_rotation_x, point_of_rotation_y = point_to_rotate_around
        radius = radius_yep
        # print(type(card_to_rotate))
        rotated_card = card_to_rotate
        # if type(card_to_rotate) == str:
        if isinstance(card_to_rotate, pygame.Surface):
            rotated_card = card_to_rotate
        if isinstance(card_to_rotate, Card):
            rotated_card = pygame.transform.rotate(card_to_rotate, rotation)
        x = point_of_rotation_x + radius * math.cos(rotation_in_radians * math.pi)
        y = point_of_rotation_y + radius * math.sin(rotation_in_radians * math.pi)
        new_rect = rotated_card.get_rect()
        new_x, new_y, new_width, new_height = new_rect
        window.blit(rotated_card, (x - new_width / 2, y - new_height / 2))


class HideableChat:
    # Do I want middle click to be another scroll method?
    def __init__(self):
        self.width = 90
        self.height = 30
        self.scroll_input_height = 25
        self.text_area_border = 5
        self.x = 0
        self.y = height - self.height
        self.text1 = "show chat"
        self.text2 = "hide chat"
        self.clicked = False
        self.hovered = False
        self.t_color = (100, 100, 100)
        self.b_color = (0, 0, 0)
        self.font = pygame.font.SysFont("roboto/Roboto-Thin.ttf", 16)
        self.d_color = (100, 100, 100)
        self.display_x = 0
        self.display_w = 200
        self.display_h = 350 + self.scroll_input_height + self.text_area_border * 2
        self.display_y = height - self.display_h
        self.s_color = (150, 150, 150)
        self.s_b_color = (25, 25, 25)
        self.scroll_w = 20
        self.scroll_x = self.display_x + self.display_w - self.scroll_w
        self.scroll_y = self.display_y
        self.scroll_h = self.display_h - self.scroll_input_height - self.text_area_border * 2
        self.scroll_bar_clicked = False
        self.scroll_bar = pygame.Surface((self.scroll_w, self.scroll_h - 2 * self.scroll_w))
        self.current_scroll_bar = self.scroll_bar
        self.scroll_bar.fill(self.s_color)
        self.scroll_font = pygame.font.SysFont("roboto/Roboto-Thin.ttf", 16)
        self.scroll_percent = 1

        self.scroll_up_button = Button("/\\", self.scroll_x, self.scroll_y, self.scroll_w, self.scroll_w, self.s_color,
                                       (200, 200, 200), self.scroll_font, {"click": self.scrollup})
        self.scroll_down_button = Button(r"\/", self.scroll_x, height - self.scroll_w -
                                         self.scroll_input_height - self.text_area_border * 2,
                                         self.scroll_w,
                                         self.scroll_w, self.s_color,
                                         (200, 200, 200), self.scroll_font, {"click": self.scrolldown})
        self.text_area_back = (200, 200, 200)
        self.text_area_text = (100, 100, 100)
        # self.text_area_font = pygame.font.SysFont("comicsans", 20)
        self.text_area_font = pygame.font.SysFont("roboto/Roboto-Thin.ttf", 16)
        self.text_to_write = ["word1 and we write more potato and potatio because i i i i i i i i i i i i i  i i why not and more ok yep",
                              "word2", "Again", "word1", "word2", "Again", "word2", "Again", "word2", "Again",
                              "up", "Yep", "keep", "it", "up"]
        self.word_wrap_count = 0
        self.text_area_x = self.text_area_border
        self.text_area_y = height - self.display_h + self.text_area_border
        self.text_area_w = self.display_w - 2 * self.text_area_border - self.scroll_w
        self.text_area_h = self.display_h - 3 * self.text_area_border - self.scroll_input_height
        # self.scrollable_area_h =
        self.scrolled_amount = 0
        self.scrolled_change = 0
        self.scroll_input = InputTextBox("Input Text Here", self.text_area_border,
                                         height-self.scroll_input_height- self.text_area_border,
                                         self.text_area_w, self.scroll_input_height, (255, 255, 255),
                                         (0, 0, 0), self.text_area_font, self.text_to_write)

    def draw(self, window):
        cur_x = self.x
        cur_y = self.y
        wid = self.width
        hei = self.height
        text = self.text1
        text_wid = self.text_area_w - 3 * self.text_area_border
        if self.clicked:
            #  Drawing the border
            pygame.draw.rect(window, self.d_color, (self.display_x, self.display_y, self.display_w, self.display_h))
            pygame.draw.rect(window, self.s_b_color, (self.scroll_x, self.scroll_y, self.scroll_w, self.scroll_h))
            text = self.text2
            #  Drawing the scroll things
            self.scroll_up_button.draw(window)
            self.scroll_down_button.draw(window)
            current_scroll_bar = self.scroll_bar
            if self.display_h < (self.get_text_height(self.scroll_font) + 8) * (len(self.text_to_write) + 2):
                if self.scroll_percent != (self.display_h / ((self.get_text_height(self.scroll_font) + 8) *
                                                             (len(self.text_to_write) + 1 + self.word_wrap_count))):
                    self.scroll_percent = (self.display_h / ((self.get_text_height(self.scroll_font) + 8) *
                                                             (len(self.text_to_write) + 1 + self.word_wrap_count)))
                    # scale(Surface, (width, height)
                    self.current_scroll_bar = pygame.transform.scale(current_scroll_bar,
                                                                     (self.scroll_w,
                                                                      round((self.scroll_h - 2 * self.scroll_w) *
                                                                            self.scroll_percent)))
            thing = (self.scrolled_amount / (self.scroll_h - (self.get_text_height(self.scroll_font) +8) *
                                             (len(self.text_to_write) + 1 + self.word_wrap_count)))
            prev_height = (self.scroll_h - 2 * self.scroll_w)
            current_height = prev_height * self.scroll_percent
            window.blit(self.current_scroll_bar, (self.scroll_x,
                                                  self.scroll_y +
                                                  self.scroll_w + (prev_height - current_height)*thing))
            #  Drawing the text.
            current_y = 10 + self.scrolled_amount
            text_height = self.get_text_height(self.text_area_font)
            scrollable_area = pygame.Surface((self.text_area_w, self.text_area_h))
            scrollable_area.fill(self.text_area_back)
            for number, to_render in enumerate(self.text_to_write):
                # WORD WRAP... Probably
                if text_wid < self.get_text_width(to_render, self.font):
                    i_font = self.font
                    count_wraps = 0
                    current_issue = to_render
                    while text_wid < self.get_text_width(current_issue, i_font):
                        goes_past_at = 0
                        break_at = 0
                        for i in range(len(current_issue)):
                            if text_wid < self.get_text_width(current_issue[:i], i_font):
                                goes_past_at = i
                                break
                        # print(goes_past_at)
                        for i in range(goes_past_at, 0, -1):
                            if current_issue[i].isspace():
                                break_at = i
                                break
                        # print(break_at)
                        if break_at == 0:
                            to_rend = current_issue[:goes_past_at-1]
                            current_issue = current_issue[goes_past_at - 1:]
                        else:
                            to_rend = current_issue[:break_at]
                            current_issue = current_issue[break_at+1:]
                        # print(to_rend)
                        # print(current_issue)
                        render_text = self.font.render(to_rend, 1, self.t_color)
                        scrollable_area.blit(render_text, (self.text_area_x, current_y))
                        current_y += text_height + 8
                        count_wraps += 1
                        if text_wid > self.get_text_width(current_issue, self.font):
                            to_render = current_issue
                    self.word_wrap_count = count_wraps
                render_text = self.font.render(to_render, 1, self.t_color)
                scrollable_area.blit(render_text, (self.text_area_x, current_y))
                current_y += text_height + 8
                # window.blit(render_text, (self.text_area_x, current_y))
            window.blit(scrollable_area, (self.text_area_x, self.text_area_y))
            self.scroll_input.draw(window)
        pygame.draw.rect(window, self.b_color, (cur_x, cur_y, wid, hei))
        rendered_text = self.font.render(text, 1, self.t_color)
        window.blit(rendered_text, (cur_x + round(wid / 2) - round(rendered_text.get_width() / 2),
                                    cur_y + round(hei / 2) - round(rendered_text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        cur_x = self.scroll_x
        cur_y = self.scroll_y
        if cur_x <= x1 <= cur_x + self.scroll_w and cur_y <= y1 <= cur_y + self.scroll_h:
            self.scroll_bar_clicked = True
        cur_x = self.x
        cur_y = self.y
        if cur_x <= x1 <= cur_x + self.width and cur_y <= y1 <= cur_y + self.height and self.clicked is False:
            self.clicked = True
            self.y -= self.display_h
        elif cur_x <= x1 <= cur_x + self.width and cur_y <= y1 <= cur_y + self.height and self.clicked is True:
            self.clicked = False
            self.y += self.display_h
        self.scroll_down_button.click(pos)
        self.scroll_up_button.click(pos)
        self.scroll_input.click(pos)

    def movement(self, pos):
        if self.scroll_bar_clicked:
            print("movement")

    def release(self):
        self.scroll_bar_clicked = False
        self.scrolled_change = 0

    def hover(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        cur_x = self.display_x
        cur_y = self.display_y
        if cur_x <= x1 <= cur_x + self.display_w and cur_y <= y1 <= cur_y + self.display_h:
            self.hovered = True
        else:
            self.hovered = False

    def scrollup(self, pos):
        if self.scrolled_amount < 0:
            # self.scrolled_amount += 5
            self.scrolled_change = 3

    def scrolldown(self, pos):
        if self.scrolled_amount > self.scroll_h - (self.get_text_height(self.scroll_font) +
                                                   8) * (len(self.text_to_write) + 1 + self.word_wrap_count):
            # self.scrolled_amount -= 5
            self.scrolled_change = -3

    def update(self):
        if self.scrolled_change != 0:
            print(self.scrolled_change)
            print(self.scroll_h - (self.get_text_height(self.scroll_font) + 8) * (len(self.text_to_write) + 1
                                                                                  + self.word_wrap_count))
            if self.scroll_h - \
                    (self.get_text_height(self.scroll_font) + 8) * \
                    (len(self.text_to_write) + 1 + self.word_wrap_count) < self.scrolled_amount < 0:
                self.scrolled_amount += self.scrolled_change
                print("update1", self.scrolled_amount)
            elif self.scrolled_amount == 0 and self.scrolled_change < 0:
                self.scrolled_amount += self.scrolled_change
                print("update2", self.scrolled_amount)
            elif self.scroll_h - \
                    (self.get_text_height(self.scroll_font) + 8) * \
                    (len(self.text_to_write) + 1 + self.word_wrap_count) >= self.scrolled_amount >= self.scroll_h - \
                    (self.get_text_height(self.scroll_font) + 8) * \
                    (len(self.text_to_write) + 2 + self.word_wrap_count) and self.scrolled_change > 0:
                self.scrolled_amount += self.scrolled_change
                print("update3", self.scrolled_amount)
            # elif self.scrolled_amount < 0:
            #    self.scrolled_amount += self.scrolled_change
            #    print("Update2", self.scrolled_amount)
            else:
                self.scrolled_change = 0

    @staticmethod
    def get_text_height(font):
        font_obj = font.render("A", False, (0, 0, 0))
        font_rect = font_obj.get_rect()

        return font_rect.height

    @staticmethod
    def get_text_width(text, font):
        font_obj = font.render(text, False, (0, 0, 0))
        font_rect = font_obj.get_rect()

        return font_rect.width


class RightClickMenu:
    def __init__(self, text_color, back_color, *args):
        self.menu_buttons = args
        self.x = 0
        self.y = 0
        self.clicked = False
        if text_color == None:
            self.t_color = (150, 0, 0)
        else:
            self.t_color = text_color
        if back_color == None:
            self.b_color = (100, 100, 100)
        else:
            self.b_color = back_color
        self.width = 80
        self.height = 40

    def right_click(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.clicked = True

    def left_click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        cur_x = self.x
        cur_y = self.y
        if cur_x <= x1 <= cur_x + self.width and cur_y <= y1 <= cur_y + self.height:
            pass
        else:
            self.clicked = False

    def draw(self, window):
        if self.clicked:
            x1 = self.x
            y1 = self.y
            pygame.draw.rect(window, self.b_color, (x1, y1, self.width, self.height))


class Button:
    def __init__(self, text: str, x: int, y: int, w: int, h: int,
                 bg=None, text_color=None, font=None,
                 actions=None,
                 b_width=0, b_color=None,
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
        :param c_action: The action that happens when you click the button
        :param h_action: The action that happens when you hover the button
        :param b_width: The border width around the button
        :param b_color: The border color around the button
        :param rotation: The amount of rotation on the button
        :param scale: The scale of the button
        """
        self.xy = {"x": x, "y": y, "cur_x": x, "cur_y": y, "width": w, "height": h, "dx": 0, "dy": 0, "count": 0}
        self.text = {"text": text, "color": text_color, "text_back_color": None, "font": font}
        if self.text["color"] is None:
            self.text["color"] = (0, 0, 0)
        if self.text["font"] is None:
            self.text["font"] = pygame.font.SysFont("comicsans", 25)
        self.rotation = {"is": False, "amount": rotation, "bgs": bg}
        self.scale = {"is": False, "amount": scale, "bgs": bg}
        self.border = {"color": b_color, "width": b_width, "current": b_color, "forward": True}
        """self.action = {"click": c_action, "hover": h_action, "release": r_action, "move": m_action,
                       "c_hand": c_action, "h_hand": h_action, "m_hand": c_action,
                       "c_table": c_action, "h_table": h_action, "m_table": c_action}"""
        if actions != None:
            print(actions)
        self.action = actions

        temp = (0, 0, 0)
        self.bg = {"o_u": temp, "o_h": temp, "o_d": temp,
                   "s_u": temp, "s_h": temp, "s_d": temp}
        if type(bg) == tuple or type(bg) == str:
            self.bg = {"o_u": bg, "o_h": bg, "o_d": bg,
                       "s_u": bg, "s_h": bg, "s_d": bg}
        elif type(bg) == dict:
            # print("LIST!")
            self.bg = {"o_u": bg["up"], "o_h": bg["up"], "o_d": bg["down"],
                       "s_u": pygame.transform.scale(bg["up"], (self.xy["width"], self.xy["height"])),
                       "s_d": pygame.transform.scale(bg["down"], (self.xy["width"], self.xy["height"])),
                       "s_h": pygame.transform.scale(bg["up"], (self.xy["width"], self.xy["height"]))}

        self.clicked = {"is": False, "was": False, "forward": True,
                        "pause": False, "count": 0, "max": 0, "update": False}
        self.hovered = {"is": False, "was": False, "forward": True,
                        "pause": False, "count": 0, "max": 0, "update": False}
        self.updated = {"is": False, "was": False, "forward": True,
                        "pause": False, "count": 0, "max": 0, "update": False}
        self.all_mod = [self.clicked, self.hovered, self.updated]

    def draw(self, window):
        """
        Drawing the button on the window.

        :param window: The surface that is going to be drawn on.
        :return: None
        """
        cur_x, cur_y = self.xy["x"], self.xy["y"]

        if self.clicked["update"] or self.hovered["update"] or self.updated["update"]:
            cur_x, cur_y = self.xy["cur_x"], self.xy["cur_y"]
        wid, hei = self.xy["width"], self.xy["height"]
        if self.border["width"] > 0:
            pygame.draw.rect(window, self.border["current"], (cur_x, cur_y, wid, hei))
            cur_x = cur_x + self.border["width"]
            cur_y = cur_y + self.border["width"]
            wid = self.xy["width"] - self.border["width"] * 2
            hei = self.xy["height"] - self.border["width"] * 2
            self.bg["s_u"] = pygame.transform.scale(self.bg["o_u"], (wid, hei))
            self.bg["s_d"] = pygame.transform.scale(self.bg["o_d"], (wid, hei))

            # print(cur_x, cur_y, self.pause)

        if not self.clicked["is"]:
            if type(self.bg["s_u"]) == tuple or type(self.bg["s_u"]) == str:
                pygame.draw.rect(window, self.bg["s_u"], (cur_x, cur_y, wid, hei))
            else:
                window.blit(self.bg["s_u"], (cur_x, cur_y))

        else:
            if type(self.bg["s_d"]) == tuple or type(self.bg["s_d"]) == str:
                pygame.draw.rect(window, self.bg["s_d"], (cur_x, cur_y, wid, hei))
            else:
                window.blit(self.bg["s_d"], (cur_x, cur_y))
        text = self.text["font"].render(self.text["text"], 1, self.text["color"])
        window.blit(text, (cur_x + round(wid / 2) - round(text.get_width() / 2),
                           cur_y + round(hei / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        cur_x, cur_y = self.xy["x"], self.xy["y"]
        # if self.action != None:
        #    self.action["click"](pos)
        """if self.action["click"] is not None:
            print(self.action["click"])"""
        if self.clicked["update"]:  # Still not sure about this one
            cur_x, cur_y = self.xy["cur_x"], self.xy["cur_y"]
        if cur_x <= x1 <= cur_x + self.xy["width"] and cur_y <= y1 <= cur_y + self.xy["height"]:
            if self.clicked["is"] is False:
                self.clicked["is"] = True
                # self.clicked["was"] = True

            if self.clicked["update"]:
                self.clicked["pause"] = True
            else:
                self.clicked["was"] = True

            if self.action:
                if self.action["click"]:
                    self.action["click"](pos)
            return True
        else:
            return False

    def hover(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        cur_x, cur_y = self.xy["cur_x"], self.xy["cur_y"]
        if cur_x <= x1 <= (cur_x + self.xy["width"]) and cur_y <= y1 <= (cur_y + self.xy["height"]):
            if not self.hovered["is"]:
                self.hovered["is"] = True
                self.hovered["was"] = True
                self.hovered["forward"] = True
            return True
        else:
            self.hovered["is"] = False
            self.hovered["forward"] = False
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

    def release(self):
        """
        When the mouse releases the button

        :return: None
        """
        self.clicked["is"] = False
        if self.clicked["pause"]:
            self.clicked["pause"] = False

    @staticmethod
    def other_update(my_dics):
        if my_dics["was"]:
            my_dics["update"] = True
            my_dics["was"] = False
            my_dics["count"] = 1

    def update(self):
        if self.hovered["was"]:
            self.hovered["was"] = False
            if not self.hovered["update"]:
                self.making_changes(width / 2, height - 100, 50, self.hovered)
                self.hovered["update"] = True
                self.hovered["count"] = 1
        # print("hovered was", self.hovered["update"], self.hovered["was"], self.hovered["is"], self.hovered["count"])

        if self.clicked["was"]:
            self.clicked["update"] = True
            self.clicked["was"] = False
            self.making_changes(0, 0, 100, self.clicked)
            self.clicked["count"] = 1

        # if self.hovered["pause"]:
        #     return
        # if self.clicked["pause"]:
        #     return

        if self.hovered["count"] == 0:
            self.hovered["update"] = False
            self.hovered["forward"] = True

        if self.clicked["count"] == 0:
            self.clicked["update"] = False
            self.clicked["forward"] = True

        if self.clicked["update"]:
            if self.clicked["count"] >= self.clicked["max"] and self.clicked["forward"]:
                self.clicked["forward"] = False
            self.xy["cur_x"] = self.xy["x"] - self.xy["d_x"] * self.clicked["count"]
            self.xy["cur_y"] = self.xy["y"] - self.xy["d_y"] * self.clicked["count"]
            if self.clicked["forward"]:
                self.clicked["count"] += 1
            else:
                self.clicked["count"] -= 1

        if self.hovered["update"]:
            # if self.hovered["count"] <= self.hovered["max"] and self.hovered["forward"]:
            #     self.hovered["forward"] = False
            # print(self.xy["d_x"], self.hovered["count"])
            self.xy["cur_x"] = self.xy["x"] - self.xy["d_x"] * self.hovered["count"]
            self.xy["cur_y"] = self.xy["y"] - self.xy["d_y"] * self.hovered["count"]
            # print(self.xy["cur_x"], self.xy["cur_y"])
            if self.hovered["forward"] and self.hovered["count"] < self.hovered["max"]:
                self.hovered["count"] += 1
            if not self.hovered["forward"]:
                self.hovered["count"] -= 1

        if not self.hovered["update"] and not self.clicked["update"] and not self.updated["update"]:
            self.xy["cur_x"] = self.xy["x"]
            self.xy["cur_y"] = self.xy["y"]

    def making_changes(self, des_x, des_y, steps, my_dict):
        self.xy["d_x"] = ((self.xy["x"] - des_x) / steps)
        self.xy["d_y"] = ((self.xy["y"] - des_y) / steps)
        my_dict["max"] = steps
        my_dict["count"] = 1
        my_dict["update"] = True
        # print("DX and DY:", self.d_x, self.d_y)

    def animate(self):
        self.making_changes(width - self.xy["width"], 0, 100, self.clicked)

    def change_border_color(self, change):
        change_by = -5
        if change:
            if type(self.border["current"]) == tuple:
                self.border["current"] = tuple((i + change_by) % 256 for i in list(self.border["current"]))
        else:
            self.border["current"] = self.border["color"]

    def move_while_true(self, condition):
        if condition:
            self.making_changes(300, 300, 50)


class InputTextBox:
    def __init__(self, text, x, y, w, h,
                 bg=None, text_color=None, font=None, to_write_to=None):
        self.displayed_text = text
        self.active = False
        self.inputted_text = ""
        self.cursor_location = 0
        self.cursor_start_location = None
        self.mouse_clicked = False
        self.clipboard = ""
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.shift = False
        self.ctrl = False
        self.alt = False
        self.word_wrap = False
        self.select_color = (100, 100, 100)
        self.cursor_color = (20, 20, 20)
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
        self.to_write_to = to_write_to

    def copying(self):
        if self.cursor_start_location is not None:
            if self.cursor_start_location < self.cursor_location:
                first_term = self.cursor_start_location
                second_term = self.cursor_location
            else:
                second_term = self.cursor_start_location
                first_term = self.cursor_location
            self.clipboard = self.inputted_text[first_term:second_term]

    def cutting(self):
        if self.cursor_start_location is not None:
            if self.cursor_start_location < self.cursor_location:
                first_term = self.cursor_start_location
                second_term = self.cursor_location
            else:
                second_term = self.cursor_start_location
                first_term = self.cursor_location
            self.clipboard = self.inputted_text[first_term:second_term]
            self.inputted_text = self.inputted_text[:first_term] + self.inputted_text[second_term:]
            self.cursor_location = first_term
            self.cursor_start_location = None

    def pasting(self):
        if self.cursor_start_location is not None:
            if self.cursor_start_location < self.cursor_location:
                first_term = self.cursor_start_location
                second_term = self.cursor_location
            else:
                second_term = self.cursor_start_location
                first_term = self.cursor_location
            self.inputted_text = self.inputted_text[:first_term] + self.inputted_text[second_term:]
            self.cursor_location = first_term
            self.cursor_start_location = None
        self.inputted_text = self.inputted_text[:self.cursor_location] + \
                             self.clipboard + \
                             self.inputted_text[self.cursor_location:]
        self.cursor_location += len(self.clipboard)

    def deleting(self):
        if self.cursor_start_location is not None:
            if self.cursor_start_location < self.cursor_location:
                first_term = self.cursor_start_location
                second_term = self.cursor_location
            else:
                second_term = self.cursor_start_location
                first_term = self.cursor_location
            self.inputted_text = self.inputted_text[:first_term] + self.inputted_text[second_term:]
            self.cursor_location = first_term
            self.cursor_start_location = None

    def adding_to_string(self, event):
        if self.active:
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_BACKSPACE]:
                    if self.cursor_location > 0:
                        if self.cursor_start_location is not None:
                            self.deleting()
                        else:
                            self.inputted_text = self.inputted_text[:self.cursor_location - 1] + \
                                                 self.inputted_text[self.cursor_location:]
                            self.cursor_location -= 1
                elif event.key in [pygame.K_DELETE]:
                    if self.cursor_start_location is not None:
                        self.deleting()
                    else:
                        if self.cursor_location < len(self.inputted_text):
                            self.inputted_text = self.inputted_text[:self.cursor_location] + \
                                                 self.inputted_text[self.cursor_location + 1:]
                elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    self.cursor_start_location = None
                    self.to_write_to.append(self.inputted_text)
                    print(self.inputted_text, self.cursor_location)
                    self.inputted_text = ""
                    self.cursor_location = 0
                elif event.key in [pygame.K_ESCAPE, pygame.K_F1, pygame.K_F2, pygame.K_F3, pygame.K_F4,
                                   pygame.K_F5, pygame.K_F6, pygame.K_F7, pygame.K_F8, pygame.K_F9,
                                   pygame.K_F10, pygame.K_F11, pygame.K_F12, pygame.K_F13, pygame.K_F14,
                                   pygame.K_F15]:
                    self.cursor_start_location = None
                    return
                elif event.key in [pygame.K_c] and self.ctrl:
                    # ctrl C - Copy
                    print("CTRL-C")
                    self.copying()
                    print(self.clipboard)

                elif event.key in [pygame.K_x] and self.ctrl:
                    # ctrl X - Cut
                    print("CTRL-X")  # Copies like ctrl - c
                    self.cutting()
                    print(self.clipboard)

                elif event.key in [pygame.K_v] and self.ctrl:
                    # ctrl V - Paste
                    print("CTRL-V")
                    self.pasting()
                    print(self.clipboard)

                elif event.key in [pygame.K_a] and self.ctrl:
                    # ctrl A - Select All
                    print("CTRL-A")
                    self.cursor_start_location = 0
                    self.cursor_location = len(self.inputted_text)
                elif self.ctrl:
                    # dealing with all of the ctrl ones so they don't add random stuff
                    pass
                elif self.alt:
                    # dealing with all of the alt ones so they don't add random stuff
                    pass
                elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                   pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_a, pygame.K_b,
                                   pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h,
                                   pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n,
                                   pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t,
                                   pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z,
                                   pygame.K_SPACE, pygame.K_EXCLAIM, pygame.K_QUOTEDBL, pygame.K_HASH,
                                   pygame.K_DOLLAR, pygame.K_AMPERSAND, pygame.K_QUOTE, pygame.K_LEFTPAREN,
                                   pygame.K_RIGHTPAREN, pygame.K_ASTERISK, pygame.K_PLUS, pygame.K_COMMA,
                                   pygame.K_MINUS, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_COLON,
                                   pygame.K_SEMICOLON, pygame.K_LESS, pygame.K_EQUALS, pygame.K_GREATER, pygame.K_AT,
                                   pygame.K_QUESTION, pygame.K_LEFTBRACKET, pygame.K_BACKSLASH, pygame.K_RIGHTBRACKET,
                                   pygame.K_CARET, pygame.K_UNDERSCORE, pygame.K_BACKQUOTE, pygame.K_TAB,
                                   pygame.K_KP_PERIOD, pygame.K_KP_DIVIDE, pygame.K_KP_MULTIPLY,
                                   pygame.K_KP_MINUS, pygame.K_KP_PLUS, pygame.K_KP_EQUALS, pygame.K_KP0,
                                   pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5,
                                   pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]:
                    # stops selecting text
                    self.cursor_start_location = None
                    # adds the new key to the location of the indicator.
                    self.inputted_text = self.inputted_text[:self.cursor_location] + \
                                         event.unicode + \
                                         self.inputted_text[self.cursor_location:]
                    # increases the indicator to after the new input.
                    self.cursor_location += 1
                elif event.key in [pygame.K_LEFT]:
                    print("lshift?", self.cursor_start_location)
                    if self.shift:
                        if self.cursor_start_location is None:
                            self.cursor_start_location = self.cursor_location
                    else:
                        self.cursor_start_location = None
                    if self.cursor_location > 0:
                        self.cursor_location -= 1
                elif event.key in [pygame.K_RIGHT]:
                    if self.shift:
                        if self.cursor_start_location is None:
                            self.cursor_start_location = self.cursor_location
                    else:
                        self.cursor_start_location = None
                    if self.cursor_location < len(self.inputted_text):
                        self.cursor_location += 1
                elif event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    self.shift = True
                elif event.key in [pygame.K_RCTRL, pygame.K_LCTRL]:
                    self.ctrl = True
                elif event.key in [pygame.K_RALT, pygame.K_LALT]:
                    self.alt = True

                else:
                    print("Else Input!")

            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    self.shift = False
                if event.key in [pygame.K_RCTRL, pygame.K_LCTRL]:
                    self.ctrl = False
                if event.key in [pygame.K_RALT, pygame.K_LALT]:
                    self.alt = False
                    print("Unshift", self.shift)

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
            left_width = self.get_text_width(using_text[:self.cursor_location])
            start_width = self.get_text_width(using_text[:self.cursor_start_location])
            if type(self.bg_down) == tuple or type(self.bg_down) == str:
                pygame.draw.rect(window, self.bg_down, (cur_x, cur_y, self.width, self.height))
            else:
                window.blit(self.bg_down, (cur_x, cur_y))

            text = self.font.render(using_text, 1, self.text_color)
            cursor = self.font.render("|", 1, self.cursor_color)

            text_top = cur_y + round(self.height / 2) - round(text.get_height() / 2)
            if self.cursor_start_location is not None:
                # Draw selection!
                # window.blit(cursor, (text_left + start_width - 2, text_top))
                if left_width < start_width:
                    pygame.draw.rect(window, self.select_color,
                                     (text_left + left_width,
                                      text_top, start_width - left_width, self.get_text_height()))
                else:
                    pygame.draw.rect(window, self.select_color,
                                     (text_left + start_width,
                                      text_top, left_width - start_width, self.get_text_height()))
            if self.count < 15:
                window.blit(cursor, (text_left + left_width - 2.5, text_top))
            window.blit(text, (text_left, text_top))

            self.count = (self.count + 1) % 30

    def mouse_update(self, x, y, curx, cury):
        x1 = x
        y1 = y
        cur_x = curx
        cur_y = cury
        if cur_x <= x1 <= cur_x + self.width and cur_y <= y1 <= cur_y + self.height:
            using_text = self.inputted_text
            text_left = cur_x + 5
            text = self.font.render(using_text, 1, self.text_color)
            text_top = cur_y + round(self.height / 2) - round(text.get_height() / 2)
            best_number = 0
            for i in range(len(using_text) + 1):
                temp_width = self.get_text_width(using_text[:i])
                current_left = x1 + 2.5 - text_left
                current_amount = abs(temp_width - current_left)
                if i == 0:
                    best_amount = current_amount
                elif current_amount < best_amount:
                    best_number = i
                    best_amount = current_amount
            return best_number

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        cur_x, cur_y = self.x, self.y
        # if self.updating:
        #    cur_x, cur_y = self.current_x, self.current_y
        if self.active:
            best_num = self.mouse_update(x1, y1, cur_x, cur_y)
            if self.cursor_start_location is not None and self.shift:
                pass
            elif self.shift:
                self.cursor_start_location = self.cursor_location
            else:
                self.cursor_start_location = None
            self.cursor_location = best_num
            self.mouse_clicked = True

        if cur_x <= x1 <= cur_x + self.width and cur_y <= y1 <= cur_y + self.height:
            self.active = True
        else:
            self.active = False

    def mouse_drag(self, pos):
        if self.active:
            x1 = pos[0]
            y1 = pos[1]
            cur_x, cur_y = self.x, self.y
            if self.mouse_clicked:
                best_num = self.mouse_update(x1, y1, cur_x, cur_y)
                if self.cursor_start_location is not None:
                    pass
                else:
                    self.cursor_start_location = self.cursor_location
                self.cursor_location = best_num
                self.mouse_clicked = True

    def release(self):
        self.mouse_clicked = False

    def get_text_height(self):
        font_obj = self.font.render("A", False, (0, 0, 0))
        font_rect = font_obj.get_rect()

        return font_rect.height

    def get_text_width(self, text):
        font_obj = self.font.render(text, False, (0, 0, 0))
        font_rect = font_obj.get_rect()

        return font_rect.width


def click_1(pos):
    print("b1 Clicked!")
    print(pos[0], pos[1])


def release_1():
    print("b1 released!")


def hover_1():
    print("b1 hover!")


def move_1():
    print("b1 hover!")


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
    menu_chat = HideableChat()
    c_bar = CircularProgressBar()
    right_menu = RightClickMenu((100, 0, 0), (50, 50, 50), "menu1", "menu2")
    my_progress = ProgressBar(100, 300, 200, 20)
    menu_color1 = (255, 0, 0)
    menu_color2 = (0, 0, 0)
    menu_color3 = (0, 0, 255)
    menu_text_box = [InputTextBox("Input Text Here", 0, 0, 400, 100, (255, 255, 255),
                                  (0, 0, 0), font_regular, menu_chat.text_to_write)]
    my_dict1 = {"click": click_1, "release": release_1, "hover": hover_1, "move": move_1}
    my_dict2 = {"click": click_1}
    my_dict3 = {"click": click_1}
    my_dict4 = {"click": click_1}
    menu_buttons = [Button("Click to Play!", 0, 0, 300, 100, menu_color1, menu_color2, menu_title),
                    Button("Options", 0, 0, 120, 80, R_BUTTON, menu_color2, menu_font, my_dict1, ),
                    Button("Rules", 0, 0, 120, 80, R_BUTTON, menu_color2, menu_font, my_dict2),
                    Button("Print", 0, 0, 120, 80, B_BUTTON, menu_color2, menu_font, my_dict3),
                    Button("Quit", 0, 0, 120, 80, B_BUTTON, menu_color2, menu_font, my_dict4)
                    ]
    menu_buttons[0].xy["x"] = int(width / 10 - menu_buttons[0].xy["width"] / 10) * 5
    menu_buttons[0].xy["y"] = int(height / 10 - menu_buttons[0].xy["height"] / 10) * 3
    menu_buttons[1].xy["x"] = int(width / 10 - menu_buttons[1].xy["width"] / 10) * 3
    menu_buttons[1].xy["y"] = int(height / 10 - menu_buttons[1].xy["height"] / 10) * 6
    menu_buttons[2].xy["x"] = int(width / 10 - menu_buttons[2].xy["width"] / 10) * 7
    menu_buttons[2].xy["y"] = int(height / 10 - menu_buttons[2].xy["height"] / 10) * 6
    menu_buttons[3].xy["x"] = int(width / 10 - menu_buttons[3].xy["width"] / 10) * 3
    menu_buttons[3].xy["y"] = int(height / 10 - menu_buttons[3].xy["height"] / 10) * 8
    menu_buttons[4].xy["x"] = int(width / 10 - menu_buttons[4].xy["width"] / 10) * 7
    menu_buttons[4].xy["y"] = int(height / 10 - menu_buttons[4].xy["height"] / 10) * 8

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
            c_bar.draw(screen)
            my_progress.draw(screen)
            for box in menu_text_box:
                box.draw(screen)
            right_menu.draw(screen)
            menu_chat.draw(screen)
            pygame.display.update()

            for event in pygame.event.get():
                for box in menu_text_box:
                    box.adding_to_string(event)
                menu_chat.scroll_input.adding_to_string(event)
                if event.type == pygame.QUIT:
                    on_menu = False
                    quit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        on_menu = False
                        quit_game = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        menu_chat.click(pos)
                        # if menu_chat.clicked:
                            # This SHOULD stop other things from interacting under it.
                            # continue
                        right_menu.left_click(pos)
                        for menu in menu_text_box:
                            menu.click(pos)
                        menu_chat.scroll_input.click(pos)
                        for button in menu_buttons:
                            if button.click(pos):
                                buttons_clicked = True
                                print("button clicked!")
                                if button.text["text"] == "Click to Play!":
                                    on_menu = False
                                    break
                                if button.text["text"] == "Quit":
                                    on_menu = False
                                    quit_game = True
                                    break
                    if event.button == 3:
                        right_menu.right_click(pos)
                    if event.button == 2:
                        print("Middle click!")
                    if event.button == 4:
                        print("Mouse Wheel Up!")
                    if event.button == 5:
                        print("Mouse Wheel Down!")
                    if event.button == 7:
                        print("Top Other Button (forward usually)!")
                    if event.button == 6:
                        print("Bottom Other Button (back usually)!")

                if event.type == pygame.MOUSEBUTTONUP:
                    for button in menu_buttons:
                        button.release()
                    for box in menu_text_box:
                        box.release()
                    menu_chat.release()
                    menu_chat.scroll_input.release()
                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    menu_chat.hover(pos)
                    menu_chat.movement(pos)
                    if menu_chat.hovered:
                        continue
                    for box in menu_text_box:
                        box.mouse_drag(pos)
                    menu_chat.scroll_input.mouse_drag(pos)
                    for button in menu_buttons:
                        button.move_release(pos)
                        button.hover(pos)
            for button in menu_buttons:
                button.change_border_color(button.hovered["is"])
            if buttons_clicked:
                for button in menu_buttons:
                    if button.clicked["count"] < 1:
                        buttons_clicked = False
                    if button.clicked["update"]:
                        continue
                    button.animate()
            menu_chat.update()
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
