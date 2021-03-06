# Hello World program in Python

import __future__


class Calculator(object):

    def operate(self, op):
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

    def evaluate(self, string):
        list = string.split()
        list2 = []
        op = []
        parse_count = 0
        result = 0

        while len(list) != 1:

            for i in range(0, len(list)):
                char = list[i]
                if list[i].isdigit():
                    op.append(int(list[i]))

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
                    # op.clear()
                    del op[:]

                    list2 = list2 + list[i + 1:len(list)]
                    list = list2[:]

                    break

                if i == len(list) - 1:
                    parse_count += 1
                    # op.clear()
                    del op[:]

            # list2.clear()
            del list2[:]

            if parse_count == 2:
                result = list2[0]

        # return result
        return list[0]


def main():
    obj = Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8")
    print(obj)


if __name__ == '__main__': main()