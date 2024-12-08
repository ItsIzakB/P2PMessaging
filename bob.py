from client import Client

name = input("Enter Your Name: ")
password = input("Enter Your Password: ")
password_bytes = password.encode('utf-8')
salt = input("Enter Salt: ")
salt_bytes = salt.encode('utf-8')

bob = Client('Bob', b'12345', salt)

bob.start()
