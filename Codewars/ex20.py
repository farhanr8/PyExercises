'''
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral
representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
any digit with a value of zero.
In Roman numerals 1990 is rendered:

1000=M, 900=CM, 90=XC; resulting in MCMXC.

2008 is written as 2000=MM, 8=VIII; or MMVIII.

1666 uses each Roman symbol in descending order: MDCLXVI.

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

'''

def roman(num):
    th = ["", "M", "MM", "MMM"]
    hun = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    one = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    thousands = th[int(num / 1000)]
    hundereds = hun[int((num % 1000) / 100)]
    tens = ten[int((num % 100) / 10)]
    ones = one[int(num % 10)]

    out = thousands + hundereds + tens + ones

    return out


def main():
    print(roman(34))

if __name__ == '__main__': main()