import key_encrypt as kdf
import secrets
from Crypto.Cipher import DES

password = b'password'


key = kdf.derive_key(password)

block_size = 7 # 56-bits for DES

iv = secrets.token_bytes(block_size)

print(f"Generated IV : {iv}")



