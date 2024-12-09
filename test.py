import key_encrypt as kdf
import message_encrypt_and_decrypt as med

key = kdf.derive_key(b'password', b'salt')

encrypted_message = med.message_encrypt(key, b"hi, this is plaintext")


decrypted_message = med.message_decrypt(key, encrypted_message)

print(f"Decrypted: Message: {decrypted_message}")
