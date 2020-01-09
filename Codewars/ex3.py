'''
https://www.codewars.com/kata/558fc85d8fd1938afb000014

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

Hint: Do not modify the original array.

'''


def sum_two_smallest_numbers(numbers):
    # your code here

    min1 = min(numbers)
    numbers.remove(min1)
    min2 = min(numbers)
    return min1 + min2


def main():
    print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

if __name__ == '__main__': main()