'''
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a
string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]

[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

    It can happen that a sum is 0 if some numbers are negative!

Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the
sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.
'''

import collections

map = {}

def isPrime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True;
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True


def findPrime(num):
    primes = []
    for n in range(1 ,abs(num)+1):
        if num % n == 0 and isPrime(n):
            if n in map:
                map[n] = map[n] + num
            else:
                map[n] = num

def sum_for_list(lst):

    ret = []

    for num in lst:
        findPrime(num)

    #Sort map by keys
    for key, v in collections.OrderedDict(sorted(map.items())).items():
        val = []
        val.append(key)
        val.append(v)
        ret.append(val)
    map.clear()
    return ret


def main():
    print(sum_for_list([15, 30, -45]))

if __name__ == '__main__': main()