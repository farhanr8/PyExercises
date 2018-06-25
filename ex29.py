'''
https://www.codewars.com/kata/calculating-with-functions/
'''

def operate(x, func):
    operation = func[0][0]
    if operation == '+':
        result = x + int(func[0][1])

    elif operation == '-':
        result = x - int(func[0][1])

    elif operation == '*':
        result = x * int(func[0][1])

    elif operation == '/':
        result = x // int(func[0][1])

    return result

def zero(*func): #your code here

    if func:
        return operate(0, func)

    else:
        return 0

def one(*func): #your code here
    if func:
        return operate(1, func)

    else:
        return 1

def two(*func): #your code here
    if func:
        return operate(2, func)

    else:
        return 2

def three(*func): #your code here
    if func:
        return operate(3, func)

    else:
        return 3

def four(*func): #your code here
    if func:
        return operate(4, func)

    else:
        return 4

def five(*func): #your code here
    if func:
        return operate(5, func)

    else:
        return 5


def six(*func): #your code here
    if func:
        return operate(6, func)

    else:
        return 6


def seven(*func): #your code here

    if func:
        return operate(7, func)

    else:
        return 7


def eight(*func): #your code here
    if func:
        return operate(8, func)

    else:
        return 8

def nine(*func): #your code here
    if func:
        return operate(9, func)

    else:
        return 9

def plus(num): #your code here
    op = '+' + str(num)
    return op

def minus(num): #your code here
    op = '-' + str(num)
    return op

def times(num): #your code here
    op = '*' + str(num)
    return op


def divided_by(num): #your code here
    op = '/' + str(num)
    return op


def main():
    print(seven(times(five())))

if __name__ == '__main__': main()