### /bin/env python3
# I like the resources at: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html

# """SimpleClient.py"""

# Official
from socket import AF_INET, socket, SOCK_STREAM, gethostname, gethostbyname
import sys
from threading import Thread
import time
# Other
import keyboard


class SimpleClient:

    def __init__(self):
        self._host_name = gethostname()
        self._host_ip = gethostbyname(self._host_name)
        self._send_stack = []
        self._receive_stack = []
        self._running = True

        self.HOST = self._host_ip
        self.PORT = 30000
        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.PORT)

        self.CLIENT = socket(AF_INET, SOCK_STREAM)
        self.CLIENT.connect(self.ADDR)

        # Start turning networking into stacks.
        self.start_client()

    def start_client(self):
        send_thread = Thread(target=self.send, args=())
        send_thread.start()
        receive_thread = Thread(target=self.receive)
        receive_thread.start()

    def receive(self):
        """Handles receiving of messages."""
        while self._running:
            msg = ""
            try:
                msg = self.CLIENT.recv(self.BUFSIZ).decode("utf8")

            except OSError:  # Possibly client has left the chat.
                break
            finally:
                self._receive_stack.append(msg)
        # Update to receive the tags and the images.
        print("receive ended I think")

    def send(self):  # event is passed by binders.
        """Handles sending of messages."""
        while self._running:
            if self._send_stack:
                msg = self._send_stack.pop(0)
                self.CLIENT.send(bytes(msg, "utf8"))
                if msg == "{quit}":
                    self.stop()
                    self.CLIENT.close()
                    sys.exit(0)
        # Look for a way to send the tags and the images.

    def sending(self):
        while self._running:
            user_input = input()
            self._send_stack.append(user_input)
            print(self._send_stack)

    def receiving(self):
        while self._running:
            if self._receive_stack:
                msg = self._receive_stack.pop(0)
                print(msg)

    def stop(self, event=None):
        """This function is to be called when the window is closed."""
        self._running = False
        keyboard.send("enter")
        try:
            self.send()
        except Exception as e:
            print(e)
            exit(0)
            sys.exit(0)
        exit(0)
        sys.exit(0)


if __name__ == "__main__":
    my_client = SimpleClient()
    sending_thread = Thread(target=my_client.sending, args=())
    sending_thread.start()
    receiving_thread = Thread(target=my_client.receiving).start()


    # tkinter.mainloop() # Starts GUI execution.
