from client import Client
try:
    name = input("Enter Your Name: ")
    password = input("Enter Your Password: ")
    password_bytes = password.encode('utf-8')
    salt = input("Enter Salt: ")
    salt_bytes = salt.encode('utf-8')

    alice = Client('Alice', password_bytes, salt_bytes)
    alice.start()
except ConnectionRefusedError as e:
    print("Failed to connect to server")
