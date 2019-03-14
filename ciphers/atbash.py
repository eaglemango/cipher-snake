cipher_name = "caesar"
default_alphabets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"]


class Atbash:
    def __init__(self, message, alphabets=None):
        if alphabets is None:
            alphabets = default_alphabets

        self.message = message
        self.alphabets = alphabets

    def encrypt(self):
        abc = {}

        for alphabet in self.alphabets:
            abc.update(str.maketrans(alphabet, alphabet[::-1]))

        return self.message.translate(abc)

    def decrypt(self):
        abc = {}

        for alphabet in self.alphabets:
            abc.update(str.maketrans(alphabet[::-1], alphabet))

        return self.message.translate(abc)

# print(Atbash('This message was encrypted using atbash.').encrypt())
