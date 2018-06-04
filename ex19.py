'''
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of
the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed
in the same manner as in the drawing:

alternative text

#Hint: See Fibonacci sequence


The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n)
and returns the total perimeter of all the squares.
'''



def perimeter(n):
    # your code

    fib = []
    fib.append(1)

    if n > 0:
        fib.append(1)
        for i in range(2,n+1):
            fib.append(fib[i-1] + fib[i-2])

    sum = 0
    for num in fib:
        sum = sum + num

    return 4 * sum


def main():
    print(perimeter(1))

if __name__ == '__main__': main()