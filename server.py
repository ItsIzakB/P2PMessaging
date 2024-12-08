import socket
import threading
def handle_clients(client1, client2):
    while True:
        msg = client1.recv(1024)

        if not msg:
            print("Client 1 disconnected")
            break

        client2.send(msg)

        msg = client2.recv(1024)

        if not msg:
            print("Client 2 disconnected")
            break
        client1.send(msg)


    client1.close()
    client2.close()






server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1', 12345))

server_socket.listen(2)

print("Server: Waiting for 2 people to join")

clients = []

while len(clients) < 2:
    conn, addr = server_socket.accept()
    print("Chatter joined")
    clients.append(conn)


print('Successful connection')
threading.Thread(target=handle_clients, args=(clients[0], clients[1])).start()


# while True:
#     data = conn.recv(1024)
#
#     print(f'Client: {data.decode()}')
#
#     if not data:
#         break
#
#     response = input("Server: ")
#     conn.send(response.encode())
#
# conn.close()
