import inspect
import pickle
import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 7777
        self.message_size = 2048
        self.addr = (self.server, self.port)
        self.player_number = self.connect()

    def get_player_number(self) -> str:
        return self.player_number

    def connect(self) -> str:
        try:
            self.client.connect(self.addr)
            return self.client.recv(self.message_size).decode()
        except Exception as connect_e:
            print('Network Connect Issue: ', connect_e)
            print(inspect.stack()[0][3])
            print(inspect.stack()[1][3])

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(self.message_size*2))
        except socket.error as sock_e:
            print('Network Send Issue: ', sock_e)
            print(inspect.stack()[0][3])
            print(inspect.stack()[1][3])
