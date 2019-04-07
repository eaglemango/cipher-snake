import const

CIPHER_NAME = "vigenere"
ACTIONS = [const.Actions.ENCRYPT, const.Actions.DECRYPT]
NEED_KEY = True
DEFAULT_ALPHABETS = [const.LATIN_LOWERCASE, const.LATIN_UPPERCASE, const.CYRILLIC_LOWERCASE, const.CYRILLIC_UPPERCASE]


def encrypt(message, keyword):
    encrypted = []

    shifts = []
    for letter in keyword:
        for alphabet in DEFAULT_ALPHABETS:
            try:
                shifts.append(alphabet.index(letter))

                break
            except ValueError:
                continue

    j = 0
    for letter in message:
        for alphabet in DEFAULT_ALPHABETS:
            try:
                i = alphabet.index(letter)

                encrypted.append(alphabet[(i + shifts[j]) % len(alphabet)])

                j += 1
                j %= len(keyword)

                break
            except ValueError:
                continue
        else:
            encrypted.append(letter)

    return ''.join(encrypted)


def decrypt(message, keyword):
    decrypted = []

    shifts = []
    for letter in keyword:
        for alphabet in DEFAULT_ALPHABETS:
            try:
                shifts.append(alphabet.index(letter))

                break
            except ValueError:
                continue

    j = 0
    for letter in message:
        for alphabet in DEFAULT_ALPHABETS:
            try:
                i = alphabet.index(letter)

                decrypted.append(alphabet[(i - shifts[j]) % len(alphabet)])

                j += 1
                j %= len(keyword)

                break
            except ValueError:
                continue
        else:
            decrypted.append(letter)

    return ''.join(decrypted)
