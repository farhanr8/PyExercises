'''
A famous casino is suddenly faced with a sharp decline of their revenues.
They decide to offer Texas hold'em also online. Can you help them by writing an
 algorithm that can rank poker hands?

Task:

    Create a poker hand that has a method to compare itself to another poker hand:

        compare_with(self, other_hand)

    A poker hand has a constructor that accepts a string containing 5 cards:

        PokerHand(hand)

    The characteristics of the string of cards are:
        A space is used as card seperator
        Each card consists of two characters
        The first character is the value of the card, valid characters are:
            2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
        The second character represents the suit, valid characters are:
            S(pades), H(earts), D(iamonds), C(lubs)

    The result of your poker hand compare can be one of these 3 options:

        RESULT = ["Loss", "Tie", "Win"]

    Apply the Texas Hold'em rules for ranking the cards.

    There is no ranking for the suits.

'''

from collections import Counter


class PokerHand(object):
    RESULT = ["Loss", "Tie", "Win"]

    topHand = {"rflush": 1, "sflush": 2, "4kind": 3, "fullhouse": 4, "flush": 5, "straight": 6, "3kind": 7, "2pair": 8, "pair": 9, "highcard": 10}

    #rankings = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}

    rankings = {"A": 5, "K": 3, "Q": 2, "J": 4, "T": 1, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}

    def __init__(self, hand):
        #Constructor sets the current hand, rank, and its highcards
        self.hand = hand
        self.myRank = self.rank(hand)
        self.highCard = self.highC(hand)

    def compare_with(self, other):
        try:
            if self.myRank < other.myRank:
                return self.RESULT[2]
            elif self.myRank > other.myRank:
                return self.RESULT[0]

            # Tie Cases

            else:
                #Case: 4 of a kind
                for i in range(5):
                    self.rankings.get
                    if self.rankings.get(self.highCard[i]) > self.rankings.get(other.highCard[i]):
                        return self.RESULT[2]

                return self.RESULT[1]

        except (RuntimeError, TypeError, NameError):
            pass

    def rank(self, str):

        lst = str.split(" ")
        lst.sort()

        #Flush check
        for i in range(5):
            if lst[0][1] != lst[i][1]:
                f = 0
                break
            else: f = 1

        if f is 1:
            # Straight/Royal Flush check
            for i in range(5):

                if self.rankings.get(lst[0][0]) - i != self.rankings.get(lst[i][0]):
                    sf = 0
                    break
                else:
                    sf = 1

            if sf is 1:
                if self.rankings.get(lst[0][0]) == 5:
                    return self.topHand.get("rflush")
                else:
                    return self.topHand.get("sflush")

            else: return self.topHand.get("flush")

        # Straight check
        for i in range(5):
            if self.rankings.get(lst[0][0]) - i != self.rankings.get(lst[i][0]):
                s = 0
                break
            else:
                s = 1
        if s is 1: return self.topHand.get("straight")

        # Kind check
        nums = []
        for c in lst:
            nums.append(c[0])

        rep = Counter(nums).items()
        count, k3, k2 = 0, 0, 0
        for k in rep.items():
            if rep.get(k) == 4:
                return self.topHand.get("4kind")
            if rep.get(k) == 3:
                k3 = 1
            if rep.get(k) == 2:
                k2 = 1
                count += 1

        if k3 and k2:
            return self.topHand.get("fullhouse")
        elif k3:
            return self.topHand.get("3kind")
        elif k2 and count == 2:
            return self.topHand.get("2pair")
        elif k2:
            return self.topHand.get("pair")

        return self.topHand.get("highcard")


    def highC(self, str):
        str = str.split(" ")
        nums = []
        for c in str:
            nums.append(c[0])

        return nums.sort()


def runTest(msg, expected, hand, other):
    player, opponent = PokerHand(hand), PokerHand(other)
    print(player.compare_with(opponent), expected, "{}: '{}' against '{}'".format(msg, hand, other))
    #test.assert_equals(player.compare_with(opponent), expected, "{}: '{}' against '{}'".format(msg, hand, other))


def main():
    runTest("Highest straight flush wins", "Loss", "2H 3H 4H 5H 6H", "KS AS TS QS JS")
    runTest("Straight flush wins of 4 of a kind", "Win", "2H 3H 4H 5H 6H", "AS AD AC AH JD")
    runTest("Highest 4 of a kind wins", "Win", "AS AH 2H AD AC", "JS JD JC JH 3D")
    runTest("4 Of a kind wins of full house", "Loss", "2S AH 2H AS AC", "JS JD JC JH AD")
    runTest("Full house wins of flush", "Win", "2S AH 2H AS AC", "2H 3H 5H 6H 7H")
    runTest("Highest flush wins", "Win", "AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H")
    runTest("Flush wins of straight", "Win", "2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C")
    runTest("Equal straight is tie", "Tie", "2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S")
    runTest("Straight wins of three of a kind", "Win", "2S 3H 4H 5S 6C", "AH AC 5H 6H AS")
    runTest("3 Of a kind wins of two pair", "Loss", "2S 2H 4H 5S 4C", "AH AC 5H 6H AS")
    runTest("2 Pair wins of pair", "Win", "2S 2H 4H 5S 4C", "AH AC 5H 6H 7S")
    runTest("Highest pair wins", "Loss", "6S AD 7H 4S AS", "AH AC 5H 6H 7S")
    runTest("Pair wins of nothing", "Loss", "2S AH 4H 5S KC", "AH AC 5H 6H 7S")
    runTest("Highest card loses", "Loss", "2S 3H 6H 7S 9C", "7H 3C TH 6H 9S")
    runTest("Highest card wins", "Win", "4S 5H 6H TS AC", "3S 5H 6H TS AC")
    runTest("Equal cards is tie", "Tie", "2S AH 4H 5S 6C", "AD 4C 5H 6H 2C")


if __name__ == '__main__': main()