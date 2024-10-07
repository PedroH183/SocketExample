import socket 

""" Script to validate if the port is open in a host """

ip = socket.gethostbyname('10.0.1.11')
PORT = 50

try:
    serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serv.bind((ip,PORT))
except:
    print('[OPEN] Port open : ', PORT)
    serv.close()