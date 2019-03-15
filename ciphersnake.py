import argparse
from cipherbook import book

parser = argparse.ArgumentParser()
parser.add_argument("action", help="Specify the action to perform with chosen cipher (encrypt, decrypt, analyse)")
parser.add_argument("-c", "--cipher", required=True, help="Choose cipher")
parser.add_argument("-k", "--key", default=None, help="Specify the key for cipher (if required)")
parser.add_argument("-i", "--input-file", default=None,
                    help="Choose the input file (if not chosen, text will be read from keyboard)")
parser.add_argument("-o", "--output-file", default=None,
                    help="Choose the output file (if not chosen, text will be written to screen")

if __name__ == "__main__":
    args = parser.parse_args()

    if args.cipher not in book:
        print("Sorry, but " + args.cipher + " is something I don't know")
        exit(0)

    if args.action not in book[args.cipher].actions:
        print("Sorry, but I can't " + args.action + " using " + args.cipher)
        exit(0)

    if book[args.cipher].need_key and args.key is None:
        print("Sorry, but " + args.cipher + " needs a key to " + args.action)
        exit(0)

    text = ""
    result = ""
    if args.input_file is None:
        text = input("Input text: ")
    else:
        text = open(args.input_file).read()

    if args.action == "encrypt":
        if book[args.cipher].need_key:
            result = book[args.cipher].encrypt(text, args.key)
        else:
            result = book[args.cipher].encrypt(text)

    if args.action == "decrypt":
        if book[args.cipher].need_key:
            result = book[args.cipher].decrypt(text, args.key)
        else:
            result = book[args.cipher].decrypt(text)

    if args.output_file is None:
        print("Output text:", result)
    else:
        open(args.output_file, "w").write(result)
