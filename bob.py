from client import Client

try:
    # name = input("Enter Your Name: ")
    # password = input("Enter Your Password: ")
    # password_bytes = password.encode('utf-8')
    # salt = input("Enter Salt: ")
    # salt_bytes = salt.encode('utf-8')

    alice = Client('Bob', b'pass', b'\x12\x34\x56\x78\x9a\xbc\xde\xf0\x11\x22\x33\x44\x55\x66\x77\x88')
    alice.start()
except ConnectionRefusedError as e:
    print("Failed to connect to server")
