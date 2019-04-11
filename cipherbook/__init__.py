import importlib
import os

book = dict()

for cipher in os.listdir("./cipherbook"):
    if cipher.endswith(".py") and cipher != "__init__.py":
        book[cipher[:-3]] = importlib.import_module("." + cipher[:-3], "cipherbook")
