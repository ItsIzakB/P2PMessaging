import key_encrypt as kdf

password = b'password'


key = kdf.derive_key(password)

kdf.verify_pass(password, key)
