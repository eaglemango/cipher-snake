cipher_name = "caesar"
default_alphabets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"]


def encrypt(message, shift):
    abc = {}

    for alphabet in default_alphabets:
        shift %= len(alphabet)
        abc.update(str.maketrans(alphabet, alphabet[shift:] + alphabet[:shift]))

    return message.translate(abc)


def decrypt(message, shift):
    abc = {}

    for alphabet in default_alphabets:
        shift %= len(alphabet)
        abc.update(str.maketrans(alphabet[shift:] + alphabet[:shift], alphabet))

    return message.translate(abc)
