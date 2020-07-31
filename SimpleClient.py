### /bin/env python3
# I like the resources at: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html

# """SimpleChatClientConverted.pyw"""


from socket import AF_INET, socket, SOCK_STREAM, gethostname, gethostbyname
from threading import Thread
import sys



class SimpleClient:

    def __init__(self):
        self._host_name = gethostname()
        self._host_ip = gethostbyname(self._host_name)
        self._send_stack = []
        self._receive_stack = []

        self.HOST = self._host_ip
        self.PORT = 30000
        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.PORT)

        self.CLIENT = socket(AF_INET, SOCK_STREAM)
        self.CLIENT.connect(self.ADDR)

    def receive(self):
        """Handles receiving of messages."""
        while True:
            # combo.txt1.configure(state='disabled')
            msg = ""
            try:
                msg = self.CLIENT.recv(self.BUFSIZ).decode("utf8")
                # Insert a new item at the end of the list

            except OSError:  # Possibly client has left the chat.
                break
            finally:
                self._receive_stack.append(msg)
        # Update to receive the tags and the images.
        print("receive ended I think")

    def send(self):  # event is passed by binders.
        """Handles sending of messages."""
        while True:
            if self._send_stack:
                msg = self._send_stack.pop(0)
            self.CLIENT.send(bytes(msg, "utf8"))
            if msg == "{quit}":
                self.CLIENT.close()
                sys.exit(0)
        # Look for a way to send the tags and the images.

    def sending(self):
        while True:
            msg = input()
            self._send_stack.append(msg)
            # self.send()

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
    my_client = SimpleClient()
    send_thread = Thread(target=my_client.send, args=()).start
    receive_thread = Thread(target=my_client.receive)
    receive_thread.start()
    sending_thread = Thread(target=my_client.sending, args=())
    sending_thread.start()


    # tkinter.mainloop() # Starts GUI execution.
