import inspect
import socket
import sys
from _thread import *
from threading import Thread
import pickle
from gameP9 import Game

server = "localhost"
port = 7777
data_size = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as sock_e:
    print("Server Socket Ex: ", sock_e)
    print("Location:         ", inspect.currentframe().f_code.co_name)
    print("Called By:        ", inspect.stack()[1][0].f_code.co_name)


s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, game_id):
    global idCount
    global data_size
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(data_size * 2).decode()

            if game_id in games:
                game = games[game_id]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except Exception as thread_e:
            print("Thread Client Ex: ", thread_e)
            print("Location:         ", inspect.currentframe().f_code.co_name)
            print("Called By:        ", inspect.stack()[1][0].f_code.co_name)
            break

    print("Lost connection")
    try:
        del games[game_id]
        print("Closing Game", game_id)
    except Exception as close_e:
        print("Thread Close Ex: ", close_e)
        print("Location:        ", inspect.currentframe().f_code.co_name)
        print("Called By:       ", inspect.stack()[1][0].f_code.co_name)
    idCount -= 1
    conn.close()


def main():
    global idCount
    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)

        idCount += 1
        p = 0
        game_id = (idCount - 1)//2
        if idCount % 2 == 1:
            games[game_id] = Game(game_id)
            print("Creating a new game...")
        else:
            games[game_id].ready = True
            p = 1
        # start_new_thread(threaded_client, (conn, p, gameId))
        my_thread = Thread(target=threaded_client, args=(conn, p, game_id,))
        # myThread.my_variable = True  # look into this more, control outside of the thread
        my_thread.start()


if __name__ == "__main__":
    main()
