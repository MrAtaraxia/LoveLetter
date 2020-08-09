from threading import Thread

from SimpleServer import SimpleServer as Networking
import LoveLetterServer as Game


def make_networking(network_server):
    # network_server.starting_server()
    network_server.accept_incoming_connections()


# GLOBALS:
network = Networking()

# Starting the SERVER
global network
network.SERVER.listen(5)
net_server = Thread(target=make_networking, args=(network,))
# print(network._send_stack)
# print(network._receive_stack)
net_server.start()

print("potato")

print("yep")
