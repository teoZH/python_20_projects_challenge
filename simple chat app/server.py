import socket
import threading

HOST = '127.0.0.1'
PORT = 50007

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

server.listen(30)

connections = {}


def send_message(conn, message, name):
    for c in connections:
        if conn != connections[c]:
            data = f'{name} : {message}'
            connections[c].send(data.encode())


def tread_client(client, address):
    if not address[1] in connections:
        connections[address[1]] = client
    welcome_message = 'Hello dear user!'
    client.send(welcome_message.encode())
    while True:
        try:
            data = client.recv(1024)
            print(f'User: {address[1]}', data.decode('UTF-8'))
            send_message(client, data.decode('utf-8'), address[1])
        except:
            continue


while True:
    c, a = server.accept()
    print(f'{a[0]}{a[1]}', 'logged in')
    threading.Thread(target=tread_client, args=(c, a)).start()
