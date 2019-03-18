cipher_name = "caesar"
actions = ["encrypt", "decrypt", "crack"]
need_key = True
default_alphabets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"]


def encrypt(message, shift):
    abc = {}

    shift = int(shift)

    for alphabet in default_alphabets:
        shift %= len(alphabet)
        abc.update(str.maketrans(alphabet, alphabet[shift:] + alphabet[:shift]))

    return message.translate(abc)


def decrypt(message, shift):
    abc = {}

    shift = int(shift)

    for alphabet in default_alphabets:
        shift %= len(alphabet)
        abc.update(str.maketrans(alphabet[shift:] + alphabet[:shift], alphabet))

    return message.translate(abc)


freq = {
    'e': 0.127,
    't': 0.0906,
    'a': 0.0817,
    'o': 0.0751,
    'i': 0.0697,
    'n': 0.0675,
    's': 0.0633,
    'h': 0.0609,
    'r': 0.0599,
    'd': 0.0425,
    'l': 0.0403,
    'c': 0.0278,
    'u': 0.0276,
    'm': 0.0241,
    'w': 0.0236,
    'f': 0.0223,
    'g': 0.0202,
    'y': 0.0197,
    'p': 0.0193,
    'b': 0.0149,
    'v': 0.0098,
    'k': 0.0077,
    'x': 0.0015,
    'j': 0.0015,
    'q': 0.0010,
    'z': 0.0005,
    'о': 0.1097,
    'е': 0.0845,
    'а': 0.0801,
    'и': 0.0735,
    'н': 0.0670,
    'т': 0.0626,
    'с': 0.0547,
    'р': 0.0473,
    'в': 0.0454,
    'л': 0.0440,
    'к': 0.0349,
    'м': 0.0321,
    'д': 0.0298,
    'п': 0.0281,
    'у': 0.0262,
    'я': 0.0201,
    'ы': 0.0190,
    'ь': 0.0174,
    'г': 0.0170,
    'з': 0.0165,
    'б': 0.0159,
    'ч': 0.0144,
    'й': 0.0121,
    'х': 0.0097,
    'ж': 0.0094,
    'ш': 0.0073,
    'ю': 0.0064,
    'ц': 0.0048,
    'щ': 0.0036,
    'э': 0.0032,
    'ф': 0.0026,
    'ъ': 0.0004,
    'ё': 0.0004
}


def crack(message):
    possible_shift = 0
    min_difference = 100000

    for shift in range(33):
        temp_difference = 0

        temp_message = decrypt(message, shift).lower()

        for symbol in set(temp_message):
            if symbol in freq:
                temp_difference += abs(freq[symbol] - temp_message.count(symbol) / len(message))

        if temp_difference < min_difference:
            min_difference = temp_difference
            possible_shift = shift

    return decrypt(message, possible_shift)
