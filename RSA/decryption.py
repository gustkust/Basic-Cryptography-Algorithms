def decryption(private_key, msg):
    res = [chr((i**private_key[0]) % private_key[1]) for i in msg]
    return ''.join(res)