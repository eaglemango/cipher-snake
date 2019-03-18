cipher_name = "vernam"
actions = ["encrypt", "decrypt"]
need_key = True
default_alphabets = []  # any available symbols in python except ruining terminal session


def encrypt(message, key):
    encrypted = []

    for i in range(len(key)):
        encrypted.append(ord(message[i]) ^ ord(key[i]))

    return ''.join(map(chr, encrypted))


def decrypt(message, key):
    encrypted = []

    for i in range(len(key)):
        encrypted.append(ord(message[i]) ^ ord(key[i]))

    return ''.join(map(chr, encrypted))
