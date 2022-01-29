import socket
import threading
from copy import copy
import enum
import time
from functools import partial

class Clients:
    ALL = -1


class IO:

    @classmethod
    def accept_all_inputs(cls, input_data):
        return True

    @classmethod
    def get_input(cls, player, message, check=None, time_out=-1):
        if check is None:
            check = partial(IO.accept_all_inputs)
        valid = False
        input_data = None
        while not valid:
            input_data = ServerIO().get_server_input(player, message, time_out)
            valid = check(input_data=input_data)
            if not valid: IO.print_text("Invalid Input! Please try again.", [player])
        return input_data

    @classmethod
    def print_text(cls, text, players=None):
        Server.print_text(text, players)
        time.sleep(0.2)

    @classmethod
    def get_num_players(cls):
        return Server.get_num_players()

    @classmethod
    def check_num_in_range(cls, minimum, maximum, input_data=""):
        try:
            if int(input_data) >= minimum and int(input_data) <= maximum:
                return True
            else:
                return False
        except ValueError:
            return False

    @classmethod
    def check_not_null(cls, input_data):
        return input_data != "null"

    @classmethod
    def check_in_list(cls, input_data, list_data):
        for item in list_data:
            if input_data == item:
                return True
        return False

    @classmethod
    def stop_waiting_for_input(cls, player_num):
        Server.clear_player_input_flag(player_num)


class ServerIO:
    def get_server_input(self, player, message="", time_out=-1):
        Server.print_text(message, [player])
        Server.set_player_input_flag(player)
        player_input = None
        while Server.get_player_input_flag(player):
            player_input = Server.get_player_input(player)
            time.sleep(0.1)
            time_out -= 1
            if time_out == 0:
                break
        return player_input



class ServerStatus(enum.Enum):
    MultiplayerLobby = enum.auto()
    WaitingToStartGame = enum.auto()
    StartGame = enum.auto()
    GameStarted = enum.auto()


class Server:
    connections = []
    status = ServerStatus.MultiplayerLobby
    playersReady = []
    waiting_for_input = []
    player_input_buffer = []
    playerOne = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @classmethod
    def create_server(cls):
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = 10000
        cls.sock.bind((HOST, PORT))
        cls.sock.listen(1)

        print("Server started on " + HOST + ", port: " + str(PORT))
        print("Note: For other players to connect to your game session they must be on the same LAN as you "
              "or you must set up port forwarding on your router. ")
        print("*Disclaimer* : please only invite players you trust to connect to your game session!")
        print("")
        print("Waiting for other players...")
        print("Type 'start game' when all players have joined to start the game.")

    @classmethod
    def startNewGame(cls):
        from Game import Game
        cls.game = threading.Thread(target=Game)
        cls.game.start()

    @classmethod
    def connectionHandler(cls, connection, address):
        from Game import Game
        while True:
            data = connection.recv(1024)
            str_data = str(data, 'utf-8')

            player_num = cls.get_player_num(connection)
            if cls.waiting_for_input[player_num] is True:
                cls.player_input_buffer[player_num] = str_data
                continue

            if cls.status == ServerStatus.WaitingToStartGame and not cls.playersReady.__contains__(connection):
                cls.playersReady.append(connection)
                if len(cls.playersReady) >= len(cls.connections):
                    cls.status = ServerStatus.StartGame

            if cls.status == ServerStatus.MultiplayerLobby and connection == cls.playerOne \
                    and str(data, 'utf-8') == "start game":
                cls.status = ServerStatus.WaitingToStartGame
                cls.print_text(ClientTrigger.game_starting)

                wait_for_host = threading.Thread(target=cls.connectionHandler, args=(connection, address))
                wait_for_host.daemon = True
                wait_for_host.start()

                while cls.status != ServerStatus.StartGame:
                    time.sleep(0.5)

                cls.status = ServerStatus.GameStarted
                cls.startNewGame()
                break

            if not data:
                cls.connections.remove(connection)
                connection.close()
                print(str(address) + ": disconnected")
                break

            if cls.status == ServerStatus.MultiplayerLobby:
                recipients = copy(cls.connections)
                recipients.remove(connection)
                cls.send_msg(data, recipients)

    @classmethod
    def print_text(cls, text, players=None):
        send_to = []
        if players is None:
            send_to = cls.connections
        else:
            try:
                for p in players:
                    send_to.append(cls.connections[p])
            except TypeError:
                send_to.append(cls.connections[players])

        cls.send_msg(bytes(text, 'utf-8'), send_to)
        time.sleep(0.01)

    @classmethod
    def send_msg(cls, data, recipients):
        for con in recipients:
            con.send(data)

    @classmethod
    def set_player_input_flag(cls, player):
        cls.waiting_for_input[player] = True

    @classmethod
    def clear_player_input_flag(cls, player):
        cls.waiting_for_input[player] = False

    @classmethod
    def get_player_input_flag(cls, player):
        return cls.waiting_for_input[player]

    @classmethod
    def get_player_input(cls, player):
        buffer = copy(cls.player_input_buffer[player])
        cls.player_input_buffer[player] = None
        if buffer is not None:
            cls.clear_player_input_flag(player)
        return buffer

    @classmethod
    def get_player_num(cls, connection):
        i = 0
        while i < len(cls.connections):
            if cls.connections[i] == connection:
                return i
            i += 1

    @classmethod
    def get_num_players(cls):
        return len(cls.connections)

    @classmethod
    def run(cls):
        while True:
            connection, address = cls.sock.accept()
            threadConnection = threading.Thread(target=cls.connectionHandler, args=(connection, address))
            threadConnection.damon = True
            threadConnection.start()
            cls.connections.append(connection)
            cls.waiting_for_input.append(False)
            cls.player_input_buffer.append(None)
            if len(cls.connections)>1: print(str(address) + ": connected")
            elif cls.playerOne is None:
                cls.playerOne = connection


class ClientStatus(enum.Enum):
    Chat = enum.auto()
    WaitingForGameStart = enum.auto()
    GameStarted = enum.auto()

class ClientTrigger:
    game_starting = "game_starting"
    get_input = "get_input"

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            data = input("")
            if self.status == ClientStatus.WaitingForGameStart:
                self.status = ClientStatus.GameStarted
                self.sock.send(bytes("go", 'utf-8'))
                print("Waiting for all other players to be ready to start...")
                # break
            else:
                if len(data) == 0:
                    data = "null"
                self.sock.send(bytes(data, 'utf-8'))

    def __init__(self, address, show_message=True):
        self.sock.connect(address)
        self.chatMode = True
        self.status = ClientStatus.Chat

        threadInput = threading.Thread(target=self.sendMsg)
        threadInput.daemon = True
        threadInput.start()
        if show_message:
            print("You connected to " + str(address))

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            text_data = str(data, 'utf-8')
            if text_data == ClientTrigger.game_starting:
                if self.status == ClientStatus.Chat:
                    self.status = ClientStatus.WaitingForGameStart
                    print("The game is ready to start, press Enter to begin.")
            elif text_data.__contains__(ClientTrigger.get_input):
                output_data = input(text_data.replace(ClientTrigger.get_input, ""))
                if len(output_data) == 0:
                    output_data = "null"
                self.sock.send(bytes(output_data, 'utf-8'))
            else:
                print(text_data)

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
                    threadServer = threading.Thread(target=cls.create_server)
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
    def create_server(cls):
        Server.create_server()
        Server.run()