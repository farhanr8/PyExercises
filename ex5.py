'''
https://www.codewars.com/kata/5552101f47fc5178b1000050

'''


def dig_pow(n, p):
    # your code
    num = str(n)
    i = 0
    sum = 0
    for char in num:
        # print(char)
        sum = sum + int(char) ** (p + i)
        i += 1

    # print(sum)
    if sum % n == 0:
        return sum / n

    return -1


def main():
    print(dig_pow(89,1))

if __name__ == '__main__': main()