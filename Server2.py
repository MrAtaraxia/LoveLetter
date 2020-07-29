"""Network Threading"""
from socket import AF_INET, socket, SOCK_STREAM
import socket as socky
from _thread import interrupt_main
from threading import Thread, currentThread
import sys
import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import bcrypt
import keyboard
from AESCipher import AESCipher

import random
import string

"""
Done - Adjusted this to be a Server version.
# Finished on 2020.06.22

Done - Adjusted this to be a class. 
# Finished on 2020.06.22

Done - Change this so that it sends to all clients when it sends.
# FINISHES on 2020.07.01

TODO - Figure out SOME WAY TO MAKE THIS BE ABLE TO QUIT...
# I will have to see if the old one could quit on the server side.

TODO - Look into JSON / YAML data for the storage of the file about the current state?
# Not sure this will work with the encryption I am using.

TODO - Other things.
# Look into doing other things as well. Like how I want them to convert from this to actually a 
# communication between frontend/backend of a different program.

Done - Figure out how to make random key during the program.
# Finished on 2020.06.22

TODO - Add the changing of the key during the sending.
# 

TODO - Look into what happens when you have 2 messages received at the same time.
# Could I use the echo I will make to 'check' if the message was received?
# Do I want to have an added "received _ " echos ?

TODO - If I loose internet during this. How can I still keep going?
# Yeah my network is not the best.

TODO - How to handle people 'reconnecting'. I will probably need to have accounts... 
# Start with a text file and just have them be hashed usernames / passwords?

TODO - Ask the user when they connect for a username / password. ?

TODO - Have a way for the user to SAVE the password when they run it...
# Or have the username / password in the input when it is called?
# or enviorment saved things... I am not sure I remember those well enough.
# I will have to see how I want to do this.
# ALSO how to 'keep people logged in'.



"""


def trial_exit():
    print("Trying to escape!")
    sys.exit()


def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)


def hashing():
    plain_text = b"Something"
    salt = bcrypt.gensalt(12)
    plain2 = b'Something'
    salt2 = b'$2b$12$.x8r5zYBrOzfCQkrSSSzUO'
    password2 = b'$2b$12$H9BKQIoX4waMphRKR7sk/O3wD636zTls8EK2t9MhJSnRFzH8/dgz.'
    password = get_hashed_password(plain_text)
    print(plain_text, salt, password)
    print(check_password(plain_text, password))
    print(plain2, salt2, password2)
    print(check_password(plain2, password2))


class ServerNetworking():

    def __init__(self, _host_name='', _key=hashlib.sha256(b'16-character key').digest(), _port=5600, _port2=5700):
        # port3 = 5800
        self._host_name = _host_name
        self._host_ip = socky.gethostbyname(self._host_name)
        self._host = self._host_ip
        self._port = _port
        self._port2 = _port2
        self._key = _key
        self._key2 = b'16-character key'
        self.send_stack = []
        self.BUFSIZ = 1024
        self.client_to_close = False
        self.server_to_close = False
        self.clients = []

        self.new_key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        print(self.new_key)
        # print(_host)
        # PORT = 5000
        # BUFSIZ = 1024

    def starting_server(self, _host, _port, method_to_run1):
        _address = (_host, _port)
        self.server_to_close = False
        SERVER = socket(AF_INET, SOCK_STREAM)
        SERVER.bind(_address)
        count = 1
        try:
            thread2 = Thread(target=self.sending, args=())
            thread2.start()
            while not self.server_to_close:
                SERVER.listen(5)
                print('Server started.')
                while 'connected':
                    conn, addr = SERVER.accept()  # Hmm..
                    # send_screen_size(conn)
                    print('Client', count, ' connected IP:', addr)
                    client_name = "Client" + str(count)
                    self.clients.append({"Name": client_name, "Address": addr, "Conn": conn})
                    thread1 = Thread(target=method_to_run1, args=(conn, client_name))
                    thread1.start()

                    count += 1
        except OSError as e:
            print(e)
            conn.close()
            sys.exit(0)
        except socket.error:
            print('hopefully shutting down...')
        finally:
            print('server ended')
            thread1.continue_running = False
            thread2.continue_running = False
            sys.exit(0)  # Closes the thread

    def receive(self, conn, client_name):
        """Handles receiving of messages."""
        receive_cypher = AESCipher(self._key)
        self.server_to_close
        try:
            t = currentThread()
            while getattr(t, "do_run", True):
                encrypted_msg = conn.recv(self.BUFSIZ).decode("utf8")
                # Insert a new item at the end of the list
                # print(encrypted_msg)
                msg = receive_cypher.decrypt(encrypted_msg)

                # Now I want to add it to the stack so it can be echoed to everyone.
                self.send_stack.append({"SendType": "All", "From": client_name, "Message": msg})
                if isinstance(msg, str):
                    print("Received message :" + msg)
                if isinstance(msg, dict):
                    print("DO THINGS WITH THE DICT!")
                if isinstance(msg, list):
                    print("DO THINGS WITH THE LIST!")
                if msg == "quit":
                    server_to_close = True
                    conn.close()  # Closes the socket
                    # so that didn't do that...
                    interrupt_main()
                    # main_window.quit()
                    print('receive ended')
                    break  # This instead of sys.exit(0) ?
                    # sys.exit(0)  # Closes the thread

            # finally:
            #  combo.txt1.insert(END, "\n")
            #  combo.txt1.configure(state='disabled')
        except socket.error:
            print("hopefully shutting down.")
        finally:
            conn.close()

    def send(self, client_socket: str, message_to_send: str):  # event is passed by binders.
        """
        Handles sending of messages.
        client_socket(str)
        message_to_send(str)
        """
        send_cypher = AESCipher(self._key)
        msg_encrypted = send_cypher.encrypt(message_to_send)
        # client_socket.send(bytes(msg_encrypted, "utf8"))
        client_socket.send(msg_encrypted)
        if isinstance(message_to_send, str):
            print("" + message_to_send)
        if message_to_send == "quit":
            client_socket.close()
            # main_window.quit()
            print("send ended")
            sys.exit(0)
            # exit(0)

    def send_all(self, message_from, message):

        for client in self.clients:
            self.send(client["Conn"], str(message_from) + " : " + message)

    def sending(self):
        """
        Handles sending of messages.
        client_socket(str)
        """
        print("Hello Thread")
        try:
            t = currentThread()
            while getattr(t, "do_run", True):
                if self.send_stack != []:
                    current_message = self.send_stack.pop()
                    print(current_message)
                    if current_message["SendType"] == "All":
                        self.send_all(current_message["From"], current_message["Message"])
                    # else:
                    #    self.send()
        except OSError as e:
            print(e)
            interrupt_main()
            raise

            #    if input():
            # msg = input()
            # if self.send_stack[self.send_stack.length-1]("SendType") == "All":

            # else:
            #    msg = self.send_stack.pop
            # self.send()

    def change_passphrase(self, new_pass):
        self._key2 = new_pass
        self.send_stack.append(self._key2)


def main():
    host_name = socky.gethostname()
    myserver = ServerNetworking(host_name)
    try:
        print("Server waiting...")
        myserver.starting_server(myserver._host, myserver._port, myserver.receive)
        sys.exit()
    except KeyboardInterrupt as k:
        print(k)
        raise
    finally:
        sys.exit()

if __name__ == '__main__':
    # hashing()
    main()
