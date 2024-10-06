import socket

class SocketAttr:
    url  : str = None
    port : int = None


class SocketIOImpl:
    """"""
    _instances = {}

    def __init__(self, data : SocketAttr):
        self.url = data.url
        self.port = data.port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.url, self.port))

    def send_message(self, message: str):
        self.socket.sendall(message.encode())

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
