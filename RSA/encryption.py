def encryption(public_key, msg="Gentlemen, a short view back to the past. Thirty y"):
    res = [(ord(i)**public_key[0]) % public_key[1] for i in msg]
    return res