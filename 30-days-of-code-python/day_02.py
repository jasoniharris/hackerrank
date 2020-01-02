import sys

# Read two integers from STDIN and print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

def sum(x, y):
    return x + y

def difference(x, y):
    return x - y

def product(x, y):
    return x * y

def main(args):
    n1 = int(args[1])
    n2 = int(args[2])

    print(sum(n1, n2))
    print(difference(n1, n2))
    print(product(n1, n2))

if __name__ == '__main__':
    main(sys.argv)