"""Network Threading"""
from socket import AF_INET, socket, SOCK_STREAM
import socket as socky
from threading import Thread
import sys
import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import bcrypt
from AESCipher import AESCipher



"""
Done - Adjusted this to be a Client version.
# Finished on 2020.06.22

Done - Adjusted this to be a class. 
# Finished on 2020.06.22

TODO - Look into JSON / YAML data for the storage of the file about the current state?
# Not sure this will work with the encryption I am using.

TODO - Other things.
# Look into doing other things as well. Like how I want them to convert from this to actually a 
# communication between frontend/backend of a different program.

Done - Figure out how to make random key during the program.
# Finished on 2020.06.22

TODO - Add the changing of the key during the sending.
# 


"""



class ClientNetworking():

    def __init__(self, _host_name='', _port=5600, _port2=5700):
        # port3 = 5800
        self._host_name = socky.gethostname()
        print(self._host_name)
        self._host_ip = socky.gethostbyname(self._host_name)
        print(self._host_ip)
        self._host = self._host_ip
        self._port = _port
        self._port2 = _port2
        self.__key__ = hashlib.sha256(b'16-character key').digest()
        self.__key2__ = b'16-character key'
        # SHUFFLES A FUCKING LIST OMG WHY DID I NOT KNOW ABOUT THIS ! 
        # random.shuffle(list)

        self.BUFSIZ = 1024
        self.client_to_close = False
        self.server_to_close = False



    def starting_client(self, _host, _port):
        _address = (_host, _port)
        print(_address, _host, _port)
        # toclose = True  # I don't think I need this to be a thread
        # but since it IS a thread I might as well close it like this...
        # , my_client.send, my_client.receive
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(_address)

        receive_thread = Thread(target=self.receive, args=(client_socket,))
        receive_thread.start()  # If I remove this as a thread it is probably better.
        send_tread = Thread(target=self.send, args=(client_socket,))
        send_tread.start()  # If I remove this as a thread it is probably better.
        # method_to_run(client_socket)
        if self.client_to_close:
            print("client ended")
            sys.exit(0)  # Closes the thread


    def send(self, client_socket):  # event is passed by binders.
        """Handles sending of messages."""
        send_cypher = AESCipher(self.__key__)
        msg = "Hello Thread"
        while not self.client_to_close:
            msg = input()
            msg_encrypted = send_cypher.encrypt(msg)
            # client_socket.send(bytes(msg_encrypted, "utf8"))
            if not self.client_to_close:
                client_socket.send(msg_encrypted)
            print("Sent message :" + msg)
            if msg == "quit":
                self.server_to_close = True
                self.client_to_close = True
                client_socket.close()
                # main_window.quit()
                print("send ended")
                sys.exit(0)
                # exit(0)
        
        self.server_to_close = True
        self.client_to_close = True
        client_socket.close()
        # main_window.quit()
        print("send ended")
        sys.exit(0)


    def receive(self, conn):
        """Handles receiving of messages."""
        receive_cypher = AESCipher(self.__key__)
        try:
            while not self.server_to_close:
                encrypted_msg = conn.recv(self.BUFSIZ).decode("utf8")
                # Insert a new item at the end of the list
                print(encrypted_msg)
                msg = receive_cypher.decrypt(encrypted_msg)
                if isinstance(msg, str):
                    print("" + msg)
                if msg == "quit":
                    self.server_to_close = True
                    self.client_to_close = True
                    conn.close()  # Closes the socket
                    # main_window.quit()
                    print('receive ended')
                    sys.exit(0)  # Closes the thread
                # finally:
                #  combo.txt1.insert(END, "\n")
                #  combo.txt1.configure(state='disabled')
            
            conn.close()  # Closes the socket
            # main_window.quit()
            print('receive ended')
            sys.exit(0)  # Closes the thread
        except ConnectionAbortedError as e:
            print(e)
            sys.exit(0)
        


if __name__ == '__main__':
    my_client = ClientNetworking()
    print("Client waiting...")
    my_client.starting_client(my_client._host, my_client._port)
