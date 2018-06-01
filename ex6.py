'''
https://www.codewars.com/kata/55a2d7ebe362935a210000b2
'''


def find_smallest_int(arr):
    # Code here

    # return min(arr)

    min = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]

    return min


def main():
    print(find_smallest_int([34, 15, 88, 2]))

if __name__ == '__main__': main()