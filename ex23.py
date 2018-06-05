'''
Task

Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South. The Clojure version returns nil when the path is reduced to nothing. The Rust version takes a slice of enum Direction {NORTH, SOUTH, EAST, WEST}.
Examples

dirReduc(@[@"NORTH", @"SOUTH", @"SOUTH", @"EAST", @"WEST", @"NORTH", @"WEST"]); // => @[@"WEST"]
dirReduc(@[@"NORTH", @"SOUTH", @"SOUTH", @"EAST", @"WEST", @"NORTH"]); // => @[]

'''


def dirReduc(arr):
    ret = []
    for dir in arr:
        if len(ret) == 0:
            ret.append(dir)
        elif (ret[len(ret)-1] == "SOUTH" and dir == "NORTH") or (ret[len(ret)-1] == "NORTH" and dir == "SOUTH") or (ret[len(ret) - 1] == "EAST" and dir == "WEST") or (ret[len(ret) - 1] == "WEST" and dir == "EAST"):
            del ret[len(ret)-1]
        else:
            ret.append(dir)

    return ret


def main():
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

    print(dirReduc(a))

if __name__ == '__main__': main()