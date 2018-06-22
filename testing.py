
def evaluate(string):
    list = string.split()
    list = "".join(list)
    list = list.split('/')
    it = iter(list)
    n = next(it)
    i, j = 0, 0
    res_list = []

    while n:

        res = list[i[-1]] / list[j[0]]
        i += 1
        j += 1
        n = next(it)

        res_list.append(res)


    return list

def main():
    print(evaluate("2 / 2 + 3 * 4 - 6"))

if __name__ == '__main__':
    main()

    