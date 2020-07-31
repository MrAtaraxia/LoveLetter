#!/usr/bin/env python3
# I like the resources at: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html

# """SimpleChatClientConverted.pyw"""

# It WORKS. MOSTLY...
# It still has the issue of making the 2nd gui.
# OK I got rid of or commented out top and now it appears to only be one GUI.\
# good...
# Ok so I probably want to subtract 1 from the end of the select statement...
# That will probably be good then... I will have to try it out.
# It will hopefully allow for it to select everything without including an unneeded return.
# Then I can add a return to after I receive from anything so that it will break things up right for
# From this one and from the old one. (how the server sees the data)
"""Script for Tkinter GUI chat client."""
"""
CURRENT VERSION... IDK ...
On 2019 NOV 03:
I have FINALLY gotten images to work in the text. I am not sure exactly WHY it works now but not before.
But that is a thing for a different day. I 'think' the extra render did it but I am not positive yet.
I will look into it later. Also these only work on the bottom line right now.
I need to figure out how to get this and FONT changes to be sent to the server
and then from the server send them to the top parts of the screen.
Mostly I want it to NOTICE that these things are in the text field. THEN I can do something about it.
"""

"""
TO DO For chat:
Figure out how to send image locations in the text and the images.
Figure out how to send the font / color/ background changes that are done on txt2 to server and then txt1.

Make it more Object Oriented.
Clean up the rest of things on the program.

Mostly what I want right now is being able to send what I have on bottom to server
and receive similar on the top. Actually I suppose I COULD make the top work with images.
It would just require a difference in parsing the data I receive and having the catches
for whatever images I want to be included in it.

I just don't know how to make images on the bottom go to the top.
I can, 'probably'/'eventually' make text from the bottom spawn the images on the top.

My question is how do I get the stupid info out of a tag.
If I set the color of the text or background to whichever I selected...
HOW do I PULL that info BACK OUT?!?
Or should I IGNORE THAT and instead put the info into an array or something else as well
And thus pull the info out of there instead?
Which is what I will probably do because I have NO idea how to pull it out of the other place...

I CAN also make tags for when I use IMAGES... Yeah... THAT will probably be what I do about it as well.
I just don't know WHAT to do about if the IMAGE is DELETED afterwards... MEH!!!
Or I will just take their method and not use images on txt2 and save them from txt1 after it comes from the server.



# """

from PIL import Image as Im, ImageTk  # for when I am using emotes in my chat... eventually... or something
from socket import AF_INET, socket, SOCK_STREAM, gethostname, gethostbyname
from threading import Thread
# import PIL.Image
from tkinter import *
from tkinter import font
from tkinter.colorchooser import *
import tkinter
import tkinter.ttk as ttk
import sys
import textwrap
import getpass


class SimpleClient:

    def __init__(self):
        self._host_name = gethostname()
        self._host_ip = gethostbyname(self._host_name)

        self.HOST = self._host_ip
        self.PORT = 30000
        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.PORT)

        self.CLIENT = socket(AF_INET, SOCK_STREAM)
        self.CLIENT.connect(self.ADDR)

    def receive(self):
        """Handles receiving of messages."""
        widthOfOutput = 30
        while True:
            # combo.txt1.configure(state='disabled')
            msg = ""
            try:

                msg = self.CLIENT.recv(self.BUFSIZ).decode("utf8")
                # Insert a new item at the end of the list

            except OSError:  # Possibly client has left the chat.
                break
            finally:
                print(msg)
        # Update to receive the tags and the images.

    def send(self, event=None):  # event is passed by binders.
        """Handles sending of messages."""
        msg = input()
        self.CLIENT.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            self.CLIENT.close()
            sys.exit(0)
        # Look for a way to send the tags and the images.
        #

    def on_closing(self, event=None):
        """This function is to be called when the window is closed."""
        try:

            # combo.txt2.set("{quit}")
            self.send()
        except Exception:
            exit(0)
            sys.exit(0)
        exit(0)
        sys.exit(0)


if __name__ == "__main__":
    """host_name = gethostname()
    host_ip = gethostbyname(host_name)
    HOST = host_ip
    PORT = 30000

    BUFSIZ = 1024
    ADDR = (HOST, PORT)"""

    # client_socket = socket(AF_INET, SOCK_STREAM)
    # print(ADDR)
    # client_socket.connect(ADDR)
    my_client = SimpleClient
    receive_thread = Thread(target=my_client.receive, args=())
    receive_thread.start()
    send_thread = Thread(target=my_client.send, args=())
    send_thread.start()


    # tkinter.mainloop() # Starts GUI execution.
