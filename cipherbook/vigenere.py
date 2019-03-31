cipher_name = "vigenere"
actions = ["encrypt", "decrypt"]
need_key = True
default_alphabets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"]


def encrypt(message, keyword):
    encrypted = []

    shifts = []
    for letter in keyword:
        for alphabet in default_alphabets:
            try:
                shifts.append(alphabet.index(letter))

                break
            except ValueError:
                continue

    j = 0
    for letter in message:
        for alphabet in default_alphabets:
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
        for alphabet in default_alphabets:
            try:
                shifts.append(alphabet.index(letter))

                break
            except ValueError:
                continue

    j = 0
    for letter in message:
        for alphabet in default_alphabets:
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
