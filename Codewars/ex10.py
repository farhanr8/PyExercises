'''
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
'''


def duplicate_count(text):
    # Your code goes here

    text = text.lower()
    list = set()
    for c in text:
        if text.count(c) > 1:
             list.add(c)
    return len(list)


def main():
    print(duplicate_count("test text"))

if __name__ == '__main__': main()