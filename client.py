import socket
import message_encrypt_and_decrypt as med
import key_encrypt as kdf
import threading
class EncryptMessage:
    def __init__(self, socket, key):
        self.socket = socket
        self.key = key

    def run(self):
        while True:
            message = input("You: ")
            print()
            if message.lower == "exit":
                print("Exiting...")
                break
            encrypted_message = med.message_encrypt(self.key, message.encode())
            self.socket.send(encrypted_message)

class DecryptMessage:
    def __init__(self, socket, key):
        self.socket = socket
        self.key = key

    def run(self):
        while True:
            response = self.socket.recv(1024)
            try:
                decrypted_message = med.message_decrypt(self.key, response)
                print(f"Client: {decrypted_message.decode()}")
            except ValueError as e:
                print(f"{response}")
                print(f"decryption error:  {e}")

class Client:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        print(password)

        self.c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.c_socket.connect(('127.0.0.1', 12345))

        print(f"{self.name} connected")
        self.key = kdf.derive_key(password)

    def start(self):

        encrypt_thread = threading.Thread(target=EncryptMessage(self.c_socket, self.key).run)
        decrypt_thread = threading.Thread(target=DecryptMessage(self.c_socket, self.key).run)

        encrypt_thread.start()
        decrypt_thread.start()

        encrypt_thread.join()
        decrypt_thread.join()
        self.c_socket.close()

