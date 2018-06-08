def highC(str):
    str = str.split(" ")
    nums = []
    for c in str:
        nums.append(c[0])

    for i in range(4, -1, -1):
        print(i)

    nums.sort()
    while 'T' in nums:
        ind = nums.index('T')
        nums[ind] = 'B'
        nums.sort()

    while 'A' in nums:
        ind = nums.index('A')
        nums[ind] = 'Z'
        nums.sort()

    while 'K' in nums:
        ind = nums.index('K')
        nums[ind] = 'Y'
        nums.sort()

    while 'B' in nums:
        ind = nums.index('B')
        nums[ind] = 'T'

    while 'Y' in nums:
        ind = nums.index('Y')
        nums[ind] = 'K'

    while 'Z' in nums:
        ind = nums.index('Z')
        nums[ind] = 'A'

    return nums


def main():
    print(highC("KC TH JS TH QD"))

if __name__ == '__main__': main()