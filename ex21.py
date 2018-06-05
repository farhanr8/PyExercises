'''
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

'''


def snail(array):

    # Only works with array with all distinct elements

    ff = 1
    rev = 0

    ln = len(array)

    if len is 1: return array

    run = ln + 2

    row = 0
    rowUp = 0
    rowDown = ln - 1

    col = 0
    colLeft = 0
    colRight = ln - 1

    result = []

    for i in range(0, run):
        if ff > 0:
            if rev is 0:
                row = rowUp
                rowUp += 1

                for j in range(0, ln - 1):
                    if array[row][j] not in result:
                        result.append(array[row][j])
            else:
                row = rowDown
                rowDown -= 1

                for j in range(ln - 1, -1, -1):
                    if array[row][j] not in result:
                        result.append(array[row][j])

        if ff < 0:
            if rev is 1:
                col = colLeft
                colLeft += 1

                for j in range(ln - 1, -1, -1):
                    if array[j][col] not in result:
                        result.append(array[j][col])
                rev = 0


            else:
                col = colRight
                colRight -= 1

                for j in range(0, ln - 1):
                    if array[j][col] not in result:
                        result.append(array[j][col])

                rev = 1

        ff = ff * -1

    return result



def main():
    print(snail([1,2,3]))

if __name__ == '__main__': main()