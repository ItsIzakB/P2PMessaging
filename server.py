import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 12345))

server_socket.listen(1)

print("waiting for other guy")

conn, addr = server_socket.accpet()

print('successful connection')


while True:
    data = conn.recv(1024)

    print(f'Client: {data.decode()}')

    if not data:
        break

    response = input("Hi im the Server")
    conn.send(response.encode())

conn.close()
