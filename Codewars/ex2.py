'''
https://www.codewars.com/kata/5656b6906de340bd1b0000ac

Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

    each taken only once - coming from s1 or s2. #Examples: ``` a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ```

'''


def longest(s1, s2):
    # your code
    str = ''
    for char in s1:
        if char not in str:
            str = str + char

    for char in s2:
        if char not in str:
            str = str + char

    return ''.join(sorted(str))


def main():
    print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))

if __name__ == '__main__': main()