import socket
import message_encrypt_and_decrypt as med
import key_encrypt as kdf


class client_socket:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        password = b'password'
        print(password)

        c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c_socket.connect(('127.0.0.1', 12345))

        print("Start chatting!")

        while True:

            message = input()
            encoded_message = message.encode()

            key = kdf.derive_key(password)

            encrypted_message = med.message_encrypt(key, encoded_message)

            c_socket.send(encrypted_message)

            if message.lower() == 'exit':
                print("Exiting the application")
                break

            response = c_socket.recv(1024)

            message = med.message_decrypt(response)

            print(f'Server: {message.decode()}')

        c_socket.close()
