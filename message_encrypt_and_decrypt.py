import key_encrypt as kdf
import secrets
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64




def message_encrypt(key, plaintext):

    block_size = 8 # 56-bits for DES

    iv = secrets.token_bytes(block_size)

    print(f"Generated IV : {iv}")

    cipher = DES.new(key, DES.MODE_CBC, iv=iv)


    #using a pkcs7 padding style
    padded_plaintext = pad(plaintext, DES.block_size)

    ciphertext = cipher.encrypt(padded_plaintext)
    print(f"Raw CipherText:  {ciphertext}")
    print(f"Hex CipherText: {ciphertext.hex()}")

    return ciphertext


def message_decrypt(key, encrypted_message):
    iv_and_ciphertext = encrypted_message
    iv = iv_and_ciphertext[:8]
    ciphertext = iv_and_ciphertext[8:]



    cipher = DES.new(key, DES.MODE_CBC, iv)

    padded_plaintext = cipher.decrypt(ciphertext)

    plaintext = unpad(padded_plaintext, DES.block_size)

    return plaintext.decode()






