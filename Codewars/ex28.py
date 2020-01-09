'''

https://www.codewars.com/kata/calculator

Not working on python 2
'''

def operate(op):
    operand1 = op[0]
    operation = op[1]
    operand2 = op[2]

    if (operation == '+'):
        result = int(operand1) + int(operand2)

    elif (operation == '-'):
        result = int(operand1) - int(operand2)

    elif (operation == '*'):
        result = int(operand1) * int(operand2)

    elif (operation == '/'):
        result = int(operand1) / int(operand2)

    elif (operation == '**'):
        result = int(operand1) ** int(operand2)

    return int(result)

def evaluate(string):
    '''

    In the first pass of the string, complete all divisions and multiplication. In the second pass,
    complete add and sub.

    Each time an operation is completed a new string is created with the result taking the place
    of the operands. Parsing begins from the start again.

    '''

    list = string.split()
    list2 = []
    op = []
    parse_count = 0

    while len(list) != 1:

        for i in range(0, len(list)):

            # Handle numbers

            # char = list[i]
            if list[i].isdigit():
                op.append(int(list[i]))

                if len(op) != 3:
                    list2.append(list[i])

            # Handle operators
            else:
                if parse_count == 0:
                    if list[i] == '/' or list[i] == '*':
                        list2 = list2[:-1]
                        op.append(list[i])
                    else:
                        op = op[:-1]
                        list2.append(list[i])
                else:
                    list2 = list2[:-1]
                    op.append(list[i])

            if len(op) == 3:
                val = operate(op)
                list2.append(str(val))
                op.clear()

                list2 = list2 + list[i+1:len(list)]
                list = list2[:]

                break

            if i == len(list) - 1:
                parse_count += 1
                op.clear()

        list2.clear()

    return list[0]

def main():
    print(evaluate("6 * 9 / 84 + 3 * 6 * 6"))

if __name__ == '__main__': main()

'''
IN PYTHON 2

import __future__

class Calculator(object):

  def isfloat(self, value):
      try:
        float(value)
        return True
      except ValueError:
        return False
    
  def operate(self, op):
    operand1 = op[0]
    operation = op[1]
    operand2 = op[2]

    if (operation == '+'):
        result = float(operand1) + float(operand2)

    elif (operation == '-'):
        result = float(operand1) - float(operand2)

    elif (operation == '*'):
        result = float(operand1) * float(operand2)

    elif (operation == '/'):
        result = float(operand1) / float(operand2)

    elif (operation == '**'):
        result = float(operand1) ** float(operand2)
        
    print operation
    print operand1
    print operand2

    return float(result)
    
  def evaluate(self, string):
    print string
    list = string.split()
    list2 = []
    op = []
    parse_count = 0
    result = 0

    while len(list) != 1:

        for i in range(0, len(list)):
            
            if list[i].isdigit() or self.isfloat(list[i]):
                op.append(float(list[i]))

                if len(op) != 3:
                    list2.append(list[i])

            else:
                if parse_count == 0:
                    if list[i] == '/' or list[i] == '*':
                        list2 = list2[:-1]
                        op.append(list[i])
                    else:
                        op = op[:-1]
                        list2.append(list[i])
                else:
                    list2 = list2[:-1]
                    op.append(list[i])

            if len(op) == 3:
                val = self.operate(op)
                list2.append(str(val))
                #op.clear()
                del op[:]

                list2 = list2 + list[i+1:len(list)]
                list = list2[:]
                
                print list

                break

            if i == len(list) - 1:
                parse_count += 1
                #op.clear()
                del op[:]

        #list2.clear()
        del list2[:]

    return float(list[0])
'''