'''
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word
and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
'''


def anagrams(word, wordlst):

    ret = []

    for w in wordlst:
        if len(w) == len(word):
            copy = word
            for c in w:
                if c in copy:
                    ind = copy.find(c)
                    copy = copy[:ind] + copy[ind + 1:]
            if len(copy) == 0:
                ret.append(w)

    return ret


def main():
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

if __name__ == '__main__': main()