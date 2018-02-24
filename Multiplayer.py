import socket
import threading
import sys
from copy import copy
from Game import Game

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = 10000
        self.playerOne = None
        self.sock.bind((HOST, PORT))
        self.sock.listen(1)
        self.game = None
        print("Server started on " + HOST + ", port: " + str(PORT))
        print("Note: For other players to connect to your game session they must be on the same LAN as you "
              "or you must set up port forwarding on your router. ")
        print("*Disclaimer* : please only invite players you trust to connect to your game session!")
        print("")
        print("Waiting for other players...")
        print("Type 'start game' when all players have joined to start the game.")

    def connectionHandler(self, connection, address):
        while True:
            data = connection.recv(1024)

            if connection == self.playerOne and self.game is None and str(data, 'utf-8') == "start game":
                self.send_msg(bytes("Game Started!", 'utf-8'), self.connections)
                break

            if not data:
                self.connections.remove(connection)
                connection.close()
                print(str(address) + ": disconnected")
                break

            recipients = copy(self.connections)
            recipients.remove(connection)
            self.send_msg(data, recipients)

    def send_msg(self, data, recipients):
        for con in recipients:
            con.send(data)

    def run(self):
        while True:
            connection, address = self.sock.accept()
            threadConnection = threading.Thread(target=self.connectionHandler, args=(connection, address))
            threadConnection.damon = True
            threadConnection.start()
            self.connections.append(connection)
            if len(self.connections)>1: print(str(address) + ": connected")
            elif self.playerOne is None:
                self.playerOne = connection

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))
            if self.game is not None:
                self.game.start()
                break

    def __init__(self, address, show_message=True):
        self.sock.connect(address)
        self.chatMode = True
        self.game = None

        threadInput = threading.Thread(target=self.sendMsg)
        threadInput.daemon = True
        threadInput.start()
        if show_message: print("You connected to " + str(address) )

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))
            if str(data, 'utf-8') == "Game Started!":
                self.game = threading.Thread(target=Game)
                print("The game has been started, press Enter to begin.")


class GameSession:

    @classmethod
    def start_session(cls):
        while True:
            try:
                print("Please choose an option: ")
                print("\t 1. Host a session")
                print("\t 2. Connect to a session")
                inputOption = int(input())
                if inputOption == 1:
                    threadServer = threading.Thread(target=cls.createServer)
                    threadServer.daemon = True
                    threadServer.start()
                    Client( (socket.gethostbyname(socket.gethostname()), 10000), False )
                else:
                    print("Enter the address to connect to: ")
                    addr = str(input())
                    print("Connecting...")
                    Client( (addr, 10000) )
                break
            except TimeoutError:
                print("ERROR: Could not connect to game session. Please check your address entry and try again.")

    @classmethod
    def createServer(cls):
        server = Server()
        server.run()