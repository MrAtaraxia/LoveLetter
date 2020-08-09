from threading import Thread

from SimpleServer import SimpleServer as Networking
import LoveLetterServer as Game


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


class ObjectMenu:
    def __init__(self, name):
        self.name = name
        self.title = "Text Tabletop"
        self.sub_menu = "submenu"
        

    def draw_menu(self):
        pass


def main_menu_loop(*args, **kwargs):
    # The main game.
    menu = ObjectMenu(*args, **kwargs)
    continue_the_game = True
    using_exit = False
    # print(game.deck)
    while continue_the_game:
        menu.draw_menu()
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
    thing()
