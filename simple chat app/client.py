import socket
from threading import Thread

HOST = '127.0.0.1'  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port


def send_message():
    while True:
        message = input()
        print('Me: ', message)
        server.send(message.encode())


def receive_message():
    while True:
        try:
            data = server.recv(1024)
            print(data.decode('utf-8'))
        except:
            continue


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))
    data = server.recv(1024)
    print(data.decode('utf-8'))
    Thread(target=send_message, args=()).start()
    Thread(target=receive_message, args=()).start()
