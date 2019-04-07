import const

CIPHER_NAME = "atbash"
ACTIONS = [const.Actions.ENCRYPT, const.Actions.DECRYPT]
NEED_KEY = False
DEFAULT_ALPHABETS = [const.LATIN_LOWERCASE, const.LATIN_UPPERCASE, const.CYRILLIC_LOWERCASE, const.CYRILLIC_UPPERCASE]


def encrypt(message):
    abc = {}

    for alphabet in DEFAULT_ALPHABETS:
        abc.update(str.maketrans(alphabet, alphabet[::-1]))

    return message.translate(abc)


def decrypt(message):
    abc = {}

    for alphabet in DEFAULT_ALPHABETS:
        abc.update(str.maketrans(alphabet[::-1], alphabet))

    return message.translate(abc)
