'''
You need to return a string that displays a diamond shape on the screen using asterisk ("*")
characters. Please see provided test cases for exact output format.

The shape that will be returned from print method resembles a diamond, where the number
provided as input represents the number of *’s printed on the middle line. The line above
and below will be centered and will have 2 less *’s than the middle line. This reduction by
2 *’s for each line continues until a line with a single * is printed at the top and bottom
of the figure.


Return null if input is even number or negative (as it is not possible to print diamond
with even number or negative number).

Please see provided test case(s) for examples.
Python Note

Since print is a reserved word in Python, Python students must implement the diamond(n)
method instead, and return None for invalid input.
JS Note

JS students, like Python ones, must implement the diamond(n) method, and return null for
invalid input.

expected =  " *\n"
expected += "***\n"
expected += " *\n"
test.assert_equals(diamond(3), expected)




def diamond(n):

    if n % 2 == 0 or n < 0:
        return None
    else:

        ln = 1
        lev = int( n / 2)
        mid = lev + 1
        for i in range(0, (lev * 2) + 1):

            if ln == lev + 1:
                for j in range(0,n):
                    print("*",end='')
                print("")
                ln += 1

            elif ln == 1 or ln == (lev * 2) + 1:
                for j in range(0, lev):
                    print(" ", end='')
                print("*")
                ln += 1

            else:

                diff = abs(mid - ln)


                for j in range(0,diff):
                    print(" ", end='')

                for j in range(0, n - (diff*2)):
                    print("*", end='')

                print("")
                ln += 1

'''


def diamond(n):
    out = ''

    # Invalid inputs
    if n % 2 == 0 or n < 0:
        return None

    # Valid input
    else:
        ln = 1
        mid = int(n / 2) + 1

        for i in range(0, n):

            # Case 1: Center row
            if ln == mid:

                for j in range(0, n):
                    print("*", end='')
                    out += '*'

                print("")
                out += '\n'
                ln += 1

            # Case 2: Top/Bottom row
            elif ln == 1 or ln == n + 1:

                for j in range(0, int(n / 2)):
                    print(" ", end='')
                    out += ' '

                print("*")
                out += '*\n'
                ln += 1

            # Case 3: Other rows
            else:

                diff = abs(mid - ln)

                for j in range(0, diff):
                    print(" ", end='')
                    out += ' '

                for j in range(0, n - (diff * 2)):
                    print("*", end='')
                    out += '*'

                print("")
                out += '\n'
                ln += 1

    return out

def main():
    print(diamond(9))

if __name__ == '__main__': main()