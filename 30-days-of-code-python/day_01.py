#!/bin/python

import sys

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

VERBOSE=0

n = int(input())

# if n % 2:
#     print("Weird")
# elif n <= 5:
#     print("Not Weird")
# elif n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")

def conditional_test_odd_even(n):
    print(f"Processing {n}") if (VERBOSE == 1) else ""
    try:
        if (n % 2) == 0:
            return True
        else:
            return False
    except Exception as e: 
        print(f"An exception occurred during conditional_test_odd_even: {e}")

def conditional_test_range_2_5(n):
    try:
        if (2 <= n <= 5):
            print("Not Weird")
        elif (6 <= n <= 20):
            print("Weird")
        else:
            print("Not Weird")
    except Exception as e: 
        print(f"An exception occurred during conditional_test_range_2_5: {e}")

if conditional_test_odd_even(n):
    conditional_test_range_2_5(n)
else:
    print("Weird")


