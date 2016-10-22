default_alphabets = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']


class Caesar:
    def __init__(self, message, alphabets=default_alphabets):
        """
        Creates a Caesar Cipher object.
        :param message: message you will operate with
        :type message: string
        :param alphabets: list of strings, containing lowercase, uppercase letters and other symbols of alphabet
        :type alphabets: list
        """

        self.message = message
        self.alphabets = alphabets

    def encrypt(self, shift):
        """
        Encrypts message using Caesar Cipher.
        :param shift: shift of the alphabet
        :type shift: int
        :return: encrypted message
        :rtype: str
        """

        abc = {}
        for alphabet in self.alphabets:
            t_shift = shift % len(alphabet)
            abc.update(str.maketrans(alphabet, alphabet[t_shift:] + alphabet[:t_shift]))

        return self.message.translate(abc)

    def decrypt(self, shift):
        """
        Decrypts encrypted message using Caesar Cipher.
        :param shift: shift of the alphabet
        :type shift: int
        :return: decrypted message
        :rtype: str
        """

        abc = {}
        for alphabet in self.alphabets:
            t_shift = shift % len(alphabet)
            abc.update(str.maketrans(alphabet[t_shift:] + alphabet[:t_shift], alphabet))

        return self.message.translate(abc)

# print(Caesar('This message was encrypted using Caesar Cipher (shift is 10).').encrypt(10))
