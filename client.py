from socket_impl import MySocket, URL, PORT

conn  = MySocket()

conn.connect(URL, PORT)
conn.mysend("Olá mundo !!")
