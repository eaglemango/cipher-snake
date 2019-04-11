import enum

LATIN_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
LATIN_UPPERCASE = LATIN_LOWERCASE.upper()

CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
CYRILLIC_UPPERCASE = CYRILLIC_LOWERCASE.upper()


class Actions(enum.Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    CRACK = "crack"
