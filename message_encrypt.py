import key_encrypt as kdf
import secrets
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

password = b'password'


key = kdf.derive_key(password)



block_size = 8 # 56-bits for DES

iv = secrets.token_bytes(block_size)

print(f"Generated IV : {iv}")

cipher  = DES.new(key, DES.MODE_CBC, iv=iv)

plaintext = b'hi'
padded_plaintext = pad(plaintext, DES.block_size)

ciphertext = cipher.encrypt(padded_plaintext)
print(f"Raw CipherText:  {ciphertext}")
print(f"Hex CipherText: {ciphertext.hex()}")

