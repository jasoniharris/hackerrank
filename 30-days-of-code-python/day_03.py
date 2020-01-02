import sys

# Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .

# You don't need to perform any rounding or formatting operations.

def division_float(x, y):
    return x / y

def division(x, y):
    return x // y

def main(args):
    n1 = int(input())
    n2 = int(input())

    print(division(n1, n2))
    print(division_float(n1, n2))

if __name__ == '__main__':
    main(sys.argv)