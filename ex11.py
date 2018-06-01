'''
https://www.codewars.com/kata/54e6533c92449cc251001667
'''


def unique_in_order(iterable):
    list = []
    for c in range(0, len(iterable)):
        if c == 0:
            list.append(iterable[c])
        elif iterable[c] == iterable[c - 1]:
            continue
        else:
            list.append(iterable[c])

    return list


def main():
    print(unique_in_order('AAAABBBCCDAABBB'))

if __name__ == '__main__': main()