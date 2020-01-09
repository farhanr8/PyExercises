'''
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
'''


def duplicate_encode(word):
    # your code here
    out = ""
    word = word.lower()
    for c in word:
        if word.count(c) > 1:
            out += ")"
        else:
            out += "("

    return out


def main():
    print(duplicate_encode("word text"))

if __name__ == '__main__': main()