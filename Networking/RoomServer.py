import math
from threading import Thread
from SimpleServer import SimpleServer as Networking


def make_love_letter():
    import LoveLetterServer as Game
    Game.main_game_loop()


def make_tic_tac_toe():
    pass


def make_networking(network_server):
    # network_server.starting_server()
    network_server.accept_incoming_connections()


def create_network():
    network = Networking()
    network.SERVER.listen(5)
    net_server = Thread(target=make_networking, args=(network,))
    # print(network._send_stack)
    # print(network._receive_stack)
    net_server.start()


def to_display(message="", sep="", end="\n"):
    # global network
    print(message, sep=sep, end=end)
    # sending = {"SendType": "All", "From": "client", "Message": message}
    # network._send_stack.append(sending)


def to_receive():
    return input()


def something():
    pass


class ObjectMenu:
    def __init__(self, title="Text Tabletop"):
        # self.name = name
        self.title = title
        self.sub_title = "Welcome to tha main menu."
        self.sub_menu = "submenu"
        self.button1 = "Love Letter"
        self.button2 = "TicTacToe"
        self.button3 = "Log"

    def draw_menu(self):
        to_display("-"*41)
        to_display("-" + " " * math.floor((40-len(self.title))/2) + self.title +
                   math.floor((40-len(self.title))/2) * " " + "-")
        to_display("-"*41)
        # Draw buttons with a for loop?
        # Depending on how I set up the buttons?
        to_display("-" + " " + "1 : " + self.button1 + (34-len(self.button1))*" "+"-")
        to_display("-" + " " + "2 : " + self.button2 + (34-len(self.button2))*" "+"-")
        to_display("-" + " " + "3 : " + self.button3 + (34-len(self.button3))*" "+"-")
        to_display("-" + " " + "quit to quit." + 25*" "+"-")
        to_display("-"*41)

    def button_one(self):
        print("Now starting: " + self.button1)
        make_love_letter()

    def button_two(self):
        print("Now starting: " + self.button2)
        make_tic_tac_toe()


def main_menu_loop(*args, **kwargs):
    # The main menu.
    menu = ObjectMenu(*args, **kwargs)
    continue_the_menu = True
    using_exit = False
    # print(game.deck)
    while continue_the_menu:
        menu.draw_menu()
        to_display("What do you want to do?")
        the_input = to_receive()
        if the_input == "1":
            menu.button_one()
        if the_input == "2":
            menu.button_two()
        if (the_input.lower()) == "quit":
            continue_the_menu = False
            using_exit = True

    end_menu(using_exit)


def end_menu(if_exit):
    end = False
    if if_exit:
        end = True
    while not end:
        to_display("Would you like to play again Y/N?")
        the_input = to_receive()
        if the_input.lower() == "y" or the_input.lower() == "yes" or the_input.lower() == "(y)es":
            main_menu_loop()
            end = True  # This will make it so there are not multiple of these afterwards.
        elif the_input.lower() == "n" or the_input.lower() == "no" or the_input.lower() == "(n)o":
            end = True
        elif the_input.lower() == "o" or the_input.lower() == "or":
            to_display("Seriously...")
        else:
            to_display("Please enter (Y)es or (N)o")


def thing():
    pass


if __name__ == "__main__":
    main_menu_loop()
