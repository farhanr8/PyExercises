'''
A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

    The first smallest Hamming number is 1 = 203050
    The second smallest Hamming number is 2 = 213050
    The third smallest Hamming number is 3 = 203150
    The fourth smallest Hamming number is 4 = 223050
    The fifth smallest Hamming number is 5 = 203051

'''

# Times out in codewars :(

# Function divides a by greatest divisible power of b
def maxDivide( a, b ):
    while a % b == 0:
        a = a / b
    return a

# Function checks numbers has only prime factors 2, 3 or 5.
def numCheck(num):
    num = maxDivide(num, 2)
    num = maxDivide(num, 3)
    num = maxDivide(num, 5)
    return 1 if num == 1 else 0

def hamming(n):
    i = 1
    count = 1

    # Che1ck all integers if its hamming until count becomes n
    while n > count:
        i += 1
        if numCheck(i):
            count += 1
    return i


def main():
    print(hamming(34))

if __name__ == '__main__': main()