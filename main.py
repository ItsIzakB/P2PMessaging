from client_socket import client_socket
import key_encrypt
import message_encrypt_and_decrypt
import threading


def alice_client():
    alice = client_socket('Alice', b'12345')

def bob_client():
    bob = client_socket('Bob', b'12345')

def main():
    alice_thread = threading.Thread(target=alice_client)
    bob_thread = threading.Thread(target=bob_client)

    alice_thread.start()
    bob_thread.start()

    alice_thread.join()
    bob_thread.join()


if __name__ == '__main__':
    main()
