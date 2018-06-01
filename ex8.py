'''
https://www.codewars.com/kata/554e4a2f232cdd87d9000038
'''


def DNA_strand(dna):
    # code here
    out = ""
    for c in dna:
        if c.lower() == 'a':
            out = out + 'T'
        elif c.lower() == 't':
            out = out + 'A'
        elif c.lower() == 'g':
            out = out + 'C'
        elif c.lower() == 'c':
            out = out + 'G'

    return out


def main():
    print(DNA_strand("ATTG"))

if __name__ == '__main__': main()