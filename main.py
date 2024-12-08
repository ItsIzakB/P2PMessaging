from client import Client
import key_encrypt
import message_encrypt_and_decrypt
import threading


def alice_client():
    alice = Client('Alice', b'12345')

def bob_client():
    bob = Client('Bob', b'12345')

def main():
    alice_thread = threading.Thread(target=alice_client)
    bob_thread = threading.Thread(target=bob_client)

    alice_thread.start()
    bob_thread.start()

    alice_thread.join()
    bob_thread.join()


if __name__ == '__main__':
    main()
