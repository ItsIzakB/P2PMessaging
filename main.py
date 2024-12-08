import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
salt = os.urandom(16)

#derive

kdf = PBKDF2HMAC (
    algorithm = hashes.SHA256(),
    length = 32,
    salt = salt,
    iterations=10000,
)


key =  kdf.derive(b"password")

kdf = PBKDF2HMAC(
    algorithm = hashes.SHA256(),
    length = 32,
    salt = salt,
    iterations = 10000
)
