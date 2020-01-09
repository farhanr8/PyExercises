'''

Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

'''

def move_zeros(array):
    # Generate a new array without 0's.
    # Count number of 0 in original and append to new list

    out = []
    count = 0

    for elem in array:
        if elem == 0 and not(elem is False):
            if elem == 0:
                count += 1
        else:
            out.append(elem)
    for i in range(0,count):
        out.append(0)

    return out

def main():
    print(move_zeros([0,1,0.0,None,2,False,1,0]))

if __name__ == '__main__': main()