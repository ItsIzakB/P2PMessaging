from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#derive

kdf = PBKDF2HMAC (
    algorithm = hashes.SHA256(),
    length =
)
