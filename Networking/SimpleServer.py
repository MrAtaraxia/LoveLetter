##   /usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
import traceback
from socket import AF_INET, socket, SOCK_STREAM, gethostbyname, gethostname
from threading import Thread
import logging


class SimpleServer:

    def __init__(self, debug=True):
        self.debug = debug
        self.running = True
        if self.debug:
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s — %(message)s',
                                datefmt='%Y-%m-%d_%H:%M:%S',
                                handlers=[logging.FileHandler('chat.log', encoding='utf-8')])
        self.clients = {}
        self.addresses = {}
        self._host_name = gethostname()
        self._host_ip = gethostbyname(self._host_name)
        self._send_stack = []
        self._receive_stack = []

        self.HOST = self._host_ip
        self.PORT = 30000
        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.PORT)
        print(self.ADDR)

        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.bind(self.ADDR)

    def accept_incoming_connections(self):
        """Sets up handling for incoming clients."""
        try:
            while self.running:
                try:
                    client, client_address = self.SERVER.accept()
                    # logging.info("%s:%s has connected." % client_address)
                    self.information("%s:%s has connected." % client_address)
                    client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
                    self.addresses[client] = client_address
                    Thread(target=self.handle_client, args=(client,)).start()
                except (SystemExit, KeyboardInterrupt):
                    self.information("Exiting....")
                    self.stop()
                    break
                except Exception as ex:
                    self.information("======> Fatal Error....\n" + str(ex))
                    self.information(traceback.format_exc())
                    self.running = False
                    self.stop()
                    raise
        except (SystemExit, KeyboardInterrupt):
            self.information("Force Exiting....")
            # self.stop()
            raise

    def stop(self):
        self.running = False
        try:
            socket(AF_INET, SOCK_STREAM).connect((self.HOST, self.PORT))
        except ConnectionRefusedError:
            pass
        self.SERVER.close()

    def handle_client(self, client):  # Takes client socket as argument.
        """Handles a single client connection."""
        try:
            running = True
            while running:
                try:
                    name = client.recv(self.BUFSIZ).decode("utf8")
                except Exception as e:
                    self.information(e)
                    self.information("Client disconnected before giving a name.")
                    client.close()
                    break
                welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
                client.send(bytes(welcome, "utf8"))
                msg = "%s has joined the chat!" % name
                self.information(msg)
                # logging.info(msg)
                self.broadcast(bytes(msg, "utf8"))
                self.clients[client] = name

                while self.running:
                    msg = client.recv(self.BUFSIZ)
                    if msg != bytes("{quit}", "utf8"):
                        print(client)
                        self.broadcast(msg, name + ": ")
                        self.information(name + " : " + msg.decode("utf8"))
                    else:
                        client.send(bytes("{quit}", "utf8"))
                        client.close()
                        del self.clients[client]
                        self.broadcast(bytes("%s has left the chat." % name, "utf8"))
                        self.information("%s has left the chat." % name)
                        running = False
                        break
        except WindowsError as e:
            self.information(e)
            self.information(name + " : CONNECTION LOST. DISCONNECTED.")
            # logging.info(name + ": CONNECTION LOST. DISCONNECTED.")

    def broadcast(self, msg, prefix=""):  # prefix is for name identification.
        """Broadcasts a message to all the clients."""

        for sock in self.clients:
            try:
                sock.send(bytes(prefix, "utf8") + msg)
            except Exception:
                continue

    def information(self, message):
        print(message)
        logging.info(message)


if __name__ == "__main__":
    my_server = SimpleServer()
    my_server.SERVER.listen(5)
    print("Waiting for connection...")
    logging.info("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=my_server.accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
