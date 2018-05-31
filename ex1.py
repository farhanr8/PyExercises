'''
https://www.codewars.com/kata/5626b561280a42ecc50000d1/solutions/python

The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the
title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (
inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.
'''


def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    # your code here
    retlist = []
    n = 0
    p = 1
    for num in range(a, b+1):
        for char in str(num):
            n = n + int(char) ** p
            p += 1
        if n == num:
            retlist.append(num)
            n = 0
            p = 1
        else:
            n = 0
            p = 1

    return retlist


def main():
    print(sum_dig_pow(10, 100))

if __name__ == '__main__': main()