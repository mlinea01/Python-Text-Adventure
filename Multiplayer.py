import socket
import threading
import sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = 10000
        self.sock.bind((HOST, PORT))
        self.sock.listen(1)
        print("Server started on " + HOST + ", port: " + PORT)
        print("Note: For other players to connect to your game session they must be on the same LAN as you"
              "or you must set up port forwarding on your router. ")
        print("*Disclaimer* : please only invite players you trust to connect to your game session!")

    def connectionHandler(self, connection, address):
        while True:
            data = connection.recv(1024)
            for con in self.connections:
                if con != connection: con.send(data)
            if not data:
                self.connections.remove(connection)
                connection.close()
                print(str(address) + ": disconnected")
                break

    def run(self):
        while True:
            connection, address = self.sock.accept()
            threadConnection = threading.Thread(target=self.connectionHandler, args=(connection, address))
            threadConnection.damon = True
            threadConnection.start()
            self.connections.append(connection)
            if len(self.connections)>1: print(str(address) + ": connected")

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))

    def __init__(self, address):
        self.sock.connect(address)

        threadInput = threading.Thread(target=self.sendMsg)
        threadInput.daemon = True
        threadInput.start()
        print("Connected to " + str(address) )

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))


class GameSession:

    def __init__(self):
        while True:
            try:
                print("Please choose an option: ")
                print("\t 1. Host a session")
                print("\t 2. Connect to a session")
                inputOption = int(input())
                if inputOption == 1:
                    threadServer = threading.Thread(target=self.createServer)
                    threadServer.daemon = True
                    threadServer.start()
                    Client( (socket.gethostbyname(socket.gethostname()), 10000) )
                else:
                    print("Enter the address to connect to: ")
                    addr = str(input())
                    print("Connecting...")
                    Client( (addr, 10000) )
                break
            except TimeoutError:
                print("ERROR: Could not connect to game session. Please check your address entry and try again.")

    def createServer(self):
        server = Server()
        server.run()