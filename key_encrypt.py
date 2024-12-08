import os

from cryptography.exceptions import InvalidKey
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
salt = os.urandom(16)


#derive
def derive_key(password):
    kdf = PBKDF2HMAC (
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations=10000,
    )


    key =  kdf.derive(password)

    return key

#verify

def verify_pass(password, key):

    try:
        kdf = PBKDF2HMAC(
            algorithm = hashes.SHA256(),
            length = 32,
            salt = salt,
            iterations = 10000,
        )

        kdf.verify (password, key)

        print("Password matches")

    except InvalidKey as e:
        print("Sorry, but your password is incorrect.")
        print("You will now be reported to the FBI.")




