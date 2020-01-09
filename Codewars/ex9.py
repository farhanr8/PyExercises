'''
https://www.codewars.com/kata/520b9d2ad5c005041100000f
'''


def pig_it(text):
    # your code here

    list = text.split()
    retlist = []

    print(list)
    for val in list:
        if val[0].isalpha():
            val = val[1:] + val[0] + "ay"

            print(val)
            retlist.append(val)

        else:
            retlist.append(val)

    str1 = " ".join(retlist)
    return str1


def main():
    print(pig_it("Hello world"))

if __name__ == '__main__': main()