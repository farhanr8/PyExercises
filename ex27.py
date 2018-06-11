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

class PokerHand(object):
    RESULT = ["Loss", "Tie", "Win"]

    topHand = {"rflush": 1, "sflush": 2, "4kind": 3, "fullhouse": 4, "flush": 5, "straight": 6, "3kind": 7, "2pair": 8, "pair": 9, "highcard": 10}

    rankings = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}

    def __init__(self, hand):

        # Constructor sets the current hand, rank, and highcards of a particular instance of PokerHand
        self.hand = hand
        self.myRank = self.rank(hand)
        self.highCard = self.highC(hand)

    def compare_with(self, other):

        if self.myRank < other.myRank:
            return self.RESULT[2]
        elif self.myRank > other.myRank:
            return self.RESULT[0]
        else:

            # Tie Cases #

            # Royal flush
            if self.myRank and other.myRank is 1:
                return self.RESULT[1]

            # Straight flush
            elif self.myRank and other.myRank is 2:

                # Starting value of straight determines winner
                if self.rankings.get(self.highCard[0]) < self.rankings.get(other.highCard[0]):
                    return self.RESULT[2]
                elif self.rankings.get(self.highCard[0]) > self.rankings.get(other.highCard[0]):
                    return self.RESULT[0]
                else:
                    return self.RESULT[1]

            # 4 of a kind
            elif self.myRank and other.myRank is 3:

                nums = self.highCard
                for elem in nums:
                    if nums.count(elem) == 4:
                        four_card = elem
                    else:
                        one_card = elem

                # Compare 4kind value than the remaining one card value
                other_nums = other.highCard
                for elem in other_nums:
                    if other_nums.count(elem) == 4:
                        if self.rankings.get(four_card) < self.rankings.get(elem):
                            return self.RESULT[2]
                        elif self.rankings.get(four_card) > self.rankings.get(elem):
                            return self.RESULT[0]
                    else:
                        other_one = elem

                if self.rankings.get(one_card) < self.rankings.get(other_one):
                    return self.RESULT[2]
                elif self.rankings.get(one_card) > self.rankings.get(other_one):
                    return self.RESULT[0]
                else:
                    return self.RESULT[1]


            # Full House
            elif self.myRank and other.myRank is 4:

                nums = self.highCard
                for elem in nums:
                    if nums.count(elem) == 3:
                        three_card = elem
                    else:
                        two_card = elem

                # Check 3kind value than 2kind value
                other_nums = other.highCard
                for elem in other_nums:
                    if other_nums.count(elem) == 3:
                        if self.rankings.get(three_card) < self.rankings.get(elem):
                            return self.RESULT[2]
                        elif self.rankings.get(three_card) > self.rankings.get(elem):
                            return self.RESULT[0]
                    else:
                        other_two = elem

                if self.rankings.get(two_card) < self.rankings.get(other_two):
                    return self.RESULT[2]
                elif self.rankings.get(two_card) > self.rankings.get(other_two):
                    return self.RESULT[0]

                return self.RESULT[1]

            # Flush
            elif self.myRank and other.myRank is 5:

                # Compare highest cards
                nums = self.highCard
                other_nums = other.highCard
                for i in range(4, -1, -1):
                    if self.rankings.get(nums[i]) < self.rankings.get(other_nums[i]):
                        return self.RESULT[2]
                    elif self.rankings.get(nums[i]) > self.rankings.get(other_nums[i]):
                        return self.RESULT[0]

                return self.RESULT[1]

            # Straight
            elif self.myRank and other.myRank is 6:

                # Starting value of straight determines winner
                if self.rankings.get(self.highCard[0]) < self.rankings.get(other.highCard[0]):
                    return self.RESULT[2]
                elif self.rankings.get(self.highCard[0]) > self.rankings.get(other.highCard[0]):
                    return self.RESULT[0]
                else:
                    return self.RESULT[1]

            # 3 of a Kind
            elif self.myRank and other.myRank is 7:

                remaining = []
                nums = self.highCard
                for elem in nums:
                    if nums.count(elem) == 3:
                        three_card = elem
                    else:
                        remaining.append(elem)

                # Compare 3kind value than remaining 2 values
                other_nums = other.highCard
                other_rem = []
                for elem in other_nums:
                    if other_nums.count(elem) == 3:
                        if self.rankings.get(three_card) < self.rankings.get(elem):
                            return self.RESULT[2]
                        elif self.rankings.get(three_card) > self.rankings.get(elem):
                            return self.RESULT[0]
                    else:
                        other_rem.append(elem)

                for i in range(1, -1, -1):
                    if self.rankings.get(remaining[i]) < self.rankings.get(other_rem[i]):
                        return self.RESULT[2]
                    elif self.rankings.get(remaining[i]) > self.rankings.get(other_rem[i]):
                        return self.RESULT[0]
                    else:
                        return self.RESULT[1]

            # Two pair
            elif self.myRank and other.myRank is 8:

                # Push to a set the values of 2 pairs and compare the two hands
                pairs = set()
                other_pair = set()

                nums = self.highCard
                for elem in nums:
                    if nums.count(elem) == 2:
                        pairs.add(elem)
                    else:
                        rem = elem

                other_nums = other.highCard
                for elem in other_nums:
                    if other_nums.count(elem) == 2:
                        other_pair.add(elem)
                    else:
                        other_rem = elem

                for i in range(1, -1, -1):
                    p = pairs.pop()
                    op = other_pair.pop()
                    if self.rankings.get(p) < self.rankings.get(op):
                        return self.RESULT[2]
                    elif self.rankings.get(p) > self.rankings.get(op):
                        return self.RESULT[0]

                # Compare the remaining one card value if both pair values are a tie
                if self.rankings.get(rem) < self.rankings.get(other_rem):
                    return self.RESULT[2]
                elif self.rankings.get(rem) > self.rankings.get(other_rem):
                    return self.RESULT[0]
                else:
                    return self.RESULT[1]

            # One Pair
            elif self.myRank and other.myRank is 9:

                rem = []
                nums = self.highCard
                for elem in nums:
                    if nums.count(elem) == 2:
                        two_card = elem
                    else:
                        rem.append(elem)

                # Check 2kind value than other value
                other_nums = other.highCard
                other_rem = []
                for elem in other_nums:
                    if other_nums.count(elem) == 2:
                        if self.rankings.get(two_card) < self.rankings.get(elem):
                            return self.RESULT[2]
                        elif self.rankings.get(two_card) > self.rankings.get(elem):
                            return self.RESULT[0]
                    else:
                        other_rem.append(elem)

                for i in range(2, -1, -1):
                    if self.rankings.get(rem[i]) < self.rankings.get(other_rem[i]):
                        return self.RESULT[2]
                    elif self.rankings.get(rem[i]) > self.rankings.get(other_rem[i]):
                        return self.RESULT[0]

                return self.RESULT[1]

            # High Card
            else:

                # Compare highest cards
                nums = self.highCard
                other_nums = other.highCard
                for i in range(4, -1, -1):
                    if self.rankings.get(nums[i]) < self.rankings.get(other_nums[i]):
                        return self.RESULT[2]
                    elif self.rankings.get(nums[i]) > self.rankings.get(other_nums[i]):
                        return self.RESULT[0]

                return self.RESULT[1]

    def rank(self, st):

        lst = st.split(" ")
        lst.sort()

        # Get only value of cards
        nums = []
        for c in lst:
            nums.append(c[0])
        nums.sort()

        # Custom sorting to get Ace, King and Tens in the right place
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

        # Flush check
        for i in range(5):
            if lst[0][1] != lst[i][1]:
                f = 0
                break
            else:
                f = 1

        if f is 1:

            # Straight/Royal Flush check

            ##########################################
            # Special Case: A 2 3 4 5
            if 'A' in nums:
                for j in range(4):
                    if self.rankings.get(nums[0]) - j != self.rankings.get(str(2 + j)):
                        special = 0
                        break
                    else:
                        special = 1
                if special is 1:
                    return self.topHand.get("sflush")
            ##########################################

            for i in range(5):

                if self.rankings.get(nums[0]) - i != self.rankings.get(nums[i]):
                    sf = 0
                    break
                else:
                    sf = 1

            if sf is 1:

                # Straight starting with T, meaning royal flush
                if self.rankings.get(nums[0]) == 5:
                    return self.topHand.get("rflush")

                # Straight flush starting at some other value
                else:
                    return self.topHand.get("sflush")

            else:
                return self.topHand.get("flush")

        # Straight check

        ##########################################
        # Special Case: A 2 3 4 5
        if 'A' in nums:
            for j in range(4):
                if self.rankings.get(nums[j]) != self.rankings.get(str(2 + j)):
                    special = 0
                    break
                else:
                    special = 1
            if special is 1:
                return self.topHand.get("straight")
        ##########################################

        for i in range(5):
            if self.rankings.get(nums[0]) - i != self.rankings.get(nums[i]):
                s = 0
                break
            else:
                s = 1
        if s is 1:
            return self.topHand.get("straight")

        # Kind check

        k3, k2 = 0, 0
        count = set()
        for elem in nums:
            if nums.count(elem) == 4:
                return self.topHand.get("4kind")
            if nums.count(elem) == 3:
                k3 = 1
            if nums.count(elem) == 2:
                k2 = 1
                count.add(elem)

        if k3 and k2:
            return self.topHand.get("fullhouse")
        elif k3:
            return self.topHand.get("3kind")
        elif k2 and len(count) == 2:
            return self.topHand.get("2pair")
        elif k2:
            return self.topHand.get("pair")

        # If all checks fail, return high card
        return self.topHand.get("highcard")

    def highC(self, st):

        # Grab card values and return custom sorting

        st = st.split(" ")
        nums = []
        for c in st:
            nums.append(c[0])

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


def runTest(msg, expected, hand, other):
    player, opponent = PokerHand(hand), PokerHand(other)

    print(player.compare_with(opponent), expected, "{}: '{}' against '{}'".format(msg, hand, other))

    #test.assert_equals(player.compare_with(opponent), expected, "{}: '{}' against '{}'".format(msg, hand, other))


def main():
    #runTest("Highest pair wins", "Loss", "KC 4H KS 2H 8D", "8C 4S KH JS 4D")
    #runTest("Highest straight flush wins", "Loss", "JC 7H JS JD JH", "JH 9H TH KH QH")
    runTest("I DONT KNOOOOW", "Loss", "AD 2H 3H 4C 5D", "2H 2C 3S 3H 3D")

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