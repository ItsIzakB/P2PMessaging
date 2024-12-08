import socket


print("Enter your Name: ")
name = input()
c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_socket.connect(('127.0.0.1', 12345))

print("Start chatting!")

while True:

    message = input(f"{name}: ")
    c_socket.send(message)

    if message.lower() == 'exit':
        print("Exiting the application")
        break

    response = c_socket.recv(1024)

    print(f'Server: {response.decode()}')

c_socket.close()
