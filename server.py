class MyServer:
    """ Class represents a server socket. """

    def __init__(self):
        super().__init__()

    def run(self):
        """ Running the server Socket"""

        print("Socket initializing...")
        connection, addr = self.__bind()

        print('Conectado ::  ' + addr[0] + ':' + str(addr[1]))
        connection.send(b'Connection: OK\n')

        # receiving messages from client
        self.__myreceive(connection)
        connection.close()

    def __bind(self):
        """ Bind the port of host """

        self.sock.bind(('0.0.0.0', 1025))
        self.sock.listen(1)
        return self.sock.accept()

    def __myreceive():
        # TODO : implement this method
        pass

s = MyServer().run()