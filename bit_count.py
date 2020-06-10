"""
Write a function that takes an integer as input, and returns the number of bits that are equal to
one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in
this case
"""

def countBits(n):
    # Convert the integer to a binary string
    binary_string = "{0:b}".format(n)
    count = 0

    # Count how many '1' characters there are in it
    for digit in binary_string:
        if digit == '1':
            count += 1

    return count

print(countBits(0))
print(countBits(4))
print(countBits(7))
print(countBits(9))
print(countBits(10))
