cipher_name = "atbash"
actions = ["encrypt", "decrypt"]
need_key = False
default_alphabets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"]


def encrypt(message):
    abc = {}

    for alphabet in default_alphabets:
        abc.update(str.maketrans(alphabet, alphabet[::-1]))

    return message.translate(abc)


def decrypt(message):
    abc = {}

    for alphabet in default_alphabets:
        abc.update(str.maketrans(alphabet[::-1], alphabet))

    return message.translate(abc)
