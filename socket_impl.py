import socket
MSGLEN = 30
URL, PORT = "localhost", 5000

class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def _connect(self, host, port):
        self.sock.connect((host, port))

    def _myreceive(self, connection):

        while True:
            chunk = connection.recv(2048)
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            print(chunk.decode())