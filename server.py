import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 12345))

server_socket.listen(1)

print("Server: Waiting for chatters to join")

conn, addr = server_socket.accept()

print('Successful connection')


while True:
    data = conn.recv(1024)

    print(f'Client: {data.decode()}')

    if not data:
        break

    response = input("Server: ")
    conn.send(response.encode())

conn.close()
