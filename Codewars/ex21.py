'''
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element,
traveling clockwise.

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

    if ln < 2:
        return array[ln-1]

    i = ln - 2
    run = 3 + (2 * i)

    row = 0
    row_top = 0
    row_bot = ln - 1

    col = 0
    colLeft = 0
    colRight = ln - 1

    result = []

    for i in range(0, run):
        if ff > 0:
            if rev is 0:
                row = row_top
                row_top += 1

                for j in range(0, ln - 1):
                    if array[row][j] not in result:
                        result.append(array[row][j])
            else:
                row = row_bot
                row_bot -= 1

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
    array = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]]
    print(snail(array))

if __name__ == '__main__': main()