import socket 

""" Script to validate if the port is open in a host """

ip = socket.gethostbyname('0.0.0.0')
PORT = 1025

try:
    serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serv.bind((ip,PORT))
except:
    print('[OPEN] Port open : ', PORT)
    serv.close()