from socket_client_impl import SocketAttr, SocketIOImpl


connectionData = SocketAttr()
connectionData.port = 23
connectionData.url  = "10.0.1.2"

conn  = SocketIOImpl(connectionData)

conn.connect()
message = "start"

conn.send_message(message)
