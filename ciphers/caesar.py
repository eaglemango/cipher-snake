cipher_name = "caesar"
default_alphabets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"]


class Caesar:
    def __init__(self, message, alphabets=None):
        if alphabets is None:
            alphabets = default_alphabets

        self.message = message
        self.alphabets = alphabets

    def encrypt(self, shift):
        abc = {}

        for alphabet in self.alphabets:
            t_shift = shift % len(alphabet)
            abc.update(str.maketrans(alphabet, alphabet[t_shift:] + alphabet[:t_shift]))

        return self.message.translate(abc)

    def decrypt(self, shift):
        abc = {}

        for alphabet in self.alphabets:
            t_shift = shift % len(alphabet)
            abc.update(str.maketrans(alphabet[t_shift:] + alphabet[:t_shift], alphabet))

        return self.message.translate(abc)

# print(Caesar('This message was encrypted using Caesar Cipher (shift is 10).').encrypt(10))
