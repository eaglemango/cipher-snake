import const

CIPHER_NAME = "vernam"
ACTIONS = [const.Actions.ENCRYPT, const.Actions.DECRYPT]
NEED_KEY = True
DEFAULT_ALPHABETS = []  # any


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
