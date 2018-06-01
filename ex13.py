'''
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/solutions/python

Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''


def solution(s):

    retlist = []

    if len(s) % 2 != 0:
        s += '_'

    for c in range(0, len(s), 2):
        retlist.append(s[c:c+2])

    return retlist


def main():
    print(solution("asdfadsfs"))

if __name__ == '__main__': main()