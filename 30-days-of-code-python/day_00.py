# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.

import sys

# Print a string literal saying "Hello, World." to stdout.

def print_out(input):
    return input

def main(args):
    statement="Hello, World!"
    print(print_out(statement))

if __name__ == '__main__':
    main(sys.argv)