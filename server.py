import socket
from socket_client_impl import SocketAttr

class Server:
    """ Class represents a server socket. """

    _inst = {}

    def __init__(self, data : SocketAttr):
        super().__init__()
        self.url = data.url
        self.port = data.port

    def run(self) -> None:
        """ Running the server Socket"""
        self.__set_tcp_socket()
        self.__bind_port()

        while True:
            connection,  client_address = self.socket.accept()

            with connection:
                print(f"Client connected !! {client_address}")

                while True:
                    data : str = connection.recv(2048)
                    if not data: break
                    print(">> ",data.decode())

    def __set_tcp_socket(self) -> None:
        """ Create a tcp socket to data stream """
        self.socket : socket.SocketType  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __bind_port(self) -> None:
        """ Bind the port of host """

        self.socket.bind((self.url, self.port))
        self.socket.listen(1)
        print("Setup Completed !", end="\n")

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            instance = super().__call__(*args, **kwargs)
            cls._inst[cls] = instance

        return cls._inst[cls]

dataAttr      = SocketAttr()
dataAttr.port = 1027
dataAttr.url  = "10.0.1.11"

Server(dataAttr).run()