'''
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"

'''


def spin_words(sentence):
    # Your code goes here

    return " ".join(word[::-1] if len(word) > 4 else word for word in sentence.split())

'''
    out = []
    list = sentence.split()
    for word in list:
        if len(word) > 4:
            out.append(word[::-1])
        else:
            out.append(word)
    return " ".join(out)
'''
def main():
    print(spin_words( "Hey fellow warriors" ))

if __name__ == '__main__': main()