# Cipher Snake

Cipher Snake is a cryptography toolkit, which allows you to work with various ciphers in different ways.
It is based on the Cipher Book - library, which makes ciphers performing more flexible.

## About Cipher Book

Cipher Book's first aim is making cipher processing easy.
Everyone can create own ciphers by using certain template and add it to Book.
If you need some specific cipher for your purposes, you can easily expand your Book with it.

## Usage

Cipher Snake is easy to use. Now it can be used only from console, but in the future there will be an exciting GUI.

### General usage

`$ python ciphersnake.py action -c CIPHER [-k KEY] [-i INPUT_FILE] [-o OUTPUT_FILE]`

### Examples

`$ python ciphersnake.py encrypt -c caesar -k 7`

`python ciphersnake.py decrypt -c atbash`