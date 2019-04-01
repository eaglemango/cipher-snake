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


def encrypt_action():
    if book[args.cipher].need_key and args.key is None:
        print("Sorry, but {0} needs a key to {1}".format(args.cipher, args.action))
        exit(0)

    if book[args.cipher].need_key:
        temp_result = book[args.cipher].encrypt(text, args.key)
    else:
        temp_result = book[args.cipher].encrypt(text)

    return temp_result


def decrypt_action():
    if book[args.cipher].need_key and args.key is None:
        print("Sorry, but {0} needs a key to {1}".format(args.cipher, args.action))
        exit(0)

    if book[args.cipher].need_key:
        temp_result = book[args.cipher].decrypt(text, args.key)
    else:
        temp_result = book[args.cipher].decrypt(text)

    return temp_result


def crack_action():
    temp_result = book[args.cipher].crack(text)
    return temp_result


actions = {
    "encrypt": encrypt_action,
    "decrypt": decrypt_action,
    "crack": crack_action
}

if __name__ == "__main__":
    args = parser.parse_args()

    if args.cipher not in book:
        print("Sorry, but {0} is something I don't know".format(args.cipher))
        exit(0)

    text = ""
    result = ""
    if args.input_file is None:
        text = input("Input text: ")
    else:
        with open(args.inout_file) as input_:
            text = input_.read()

    try:
        result = actions[args.action]()
    except KeyError:
        print("Sorry, but I can't {0} {1}".format(args.action, args.cipher))
        exit(0)

    if args.output_file is None:
        print("Output text:", result)
    else:
        with open(args.output_file, "w") as output:
            output.write(result)
