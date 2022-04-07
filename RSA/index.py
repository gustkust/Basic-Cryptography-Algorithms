from key_generator import generate_keys
from encryption import encryption
from decryption import decryption


public_key, private_key = generate_keys()
print(public_key, private_key)
encrypted = encryption(public_key)
decrypted = decryption(private_key, encrypted)
print(encrypted)
print(decrypted)