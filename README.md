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

```
$ python ciphersnake.py action -c CIPHER [-k KEY] [-i INPUT_FILE] [-o OUTPUT_FILE]
```

Where `action` can be: `encrypt`, `decrypt` and `crack` (now only for Caesar cipher)

If `INPUT_FILE` or `OUTPUT_FILE` isn't specified, `stdin`/`stdout` will be used

### Examples

#### Atbash

```
$ python ciphersnake.py encrypt -c atbash -i input.txt -o output.txt
```

#### Caesar

If you need to hide some information from others...

```
$ python ciphersnake.py encrypt -c caesar -k 42 -i book.txt -o encrypted_book.txt
```

And then restore it...

```
$ python ciphersnake.py decrypt -c caesar -k 42 -i encrypted_book.txt -o decrypted_book.txt
```

But don't forget, that someone can try to get your data!

```
$ python ciphersnake.py crack -c caesar -i encrypted_book.txt -o cracked_book.txt
```

#### Vigenere

```
$ python ciphersnake.py encrypt -c vigenere -k mywonderfulkeyword -o encrypted.txt
```

#### Vernam

```
$ python ciphersnake.py encrypt -c vernam -k supermegakeywordtomakemydatasafe -o message.txt
```

Note, that Vernam cipher need as long keyword as your message is.
Also it preferred not to use `stdout` as output, because it can cause some problems with appearance (due to service characters in output).