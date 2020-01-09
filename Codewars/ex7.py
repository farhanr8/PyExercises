'''
https://www.codewars.com/kata/546e2562b03326a88e000020

'''


def square_digits(num):
    convert = str(num)
    out = ''
    for char in convert:
        out = out + str(int(char) ** 2)

    return int(out)


def main():
    print(square_digits(34))

if __name__ == '__main__': main()