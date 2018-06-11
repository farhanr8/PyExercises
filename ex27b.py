import enum


class PokerHand(object):
    RESULT = ["Loss", "Tie", "Win"]

    TOP_HAND = {"rflush": 1, "sflush": 2, "4kind": 3, "fullhouse": 4, "flush": 5, "straight": 6, "3kind": 7, "2pair": 8,
               "pair": 9, "highcard": 10}

    RANKINGS = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12,
                "2": 13}

    def __init__(self, hand):

        cards = hand.split(" ")
        self.hand = []
        for c in cards:
            self.hand.append(self.Card(c[0], c[1]))

        self.sorted_cards = self.mySort(self.hand)
        self.sorted_values = []
        for c in self.sorted_cards:
            self.sorted_values.append(c.value)

        self.myRank = self.rank(self.hand)

    def mySort(self, card_list):

        card_list.sort(reverse=True)
        return card_list

    def rank(self, st):

        special_straight_index = 2

        cards = self.sorted_cards

        # Get only value of cards
        nums = self.sorted_values

        # Flush check
        for i in range(5):
            if cards[0].suite != cards[i].suite:
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
                    if self.RANKINGS.get(cards[j].value) != self.RANKINGS.get(str(special_straight_index + j)):
                        special = 0
                        break
                    else:
                        special = 1
                if special is 1:
                    return self.TOP_HAND.get("sflush")
            ##########################################

            for i in range(5):

                if self.RANKINGS.get(cards[0].value) - i != self.RANKINGS.get(cards[i].value):
                    sf = 0
                    break
                else:
                    sf = 1

            if sf is 1:

                # Straight starting with T, meaning royal flush
                if self.RANKINGS.get(cards[0].value) == self.Card.CardRank.TEN.value:
                    return self.TOP_HAND.get("rflush")

                # Straight flush starting at some other value
                else:
                    return self.TOP_HAND.get("sflush")

            else:
                return self.TOP_HAND.get("flush")

        # Straight check

        ##########################################
        # Special Case: A 2 3 4 5
        if 'A' in nums:
            for j in range(4):
                if self.RANKINGS.get(cards[j].value) != self.RANKINGS.get(str(special_straight_index + j)):
                    special = 0
                    break
                else:
                    special = 1
            if special is 1:
                return self.TOP_HAND.get("straight")
        ##########################################

        for i in range(5):
            if self.RANKINGS.get(cards[0].value) - i != self.RANKINGS.get(cards[i].value):
                s = 0
                break
            else:
                s = 1
        if s is 1:
            return self.TOP_HAND.get("straight")

        # Kind check

        k3, k2 = 0, 0
        count = set()
        for elem in nums:
            if nums.count(elem) == 4:
                return self.TOP_HAND.get("4kind")
            if nums.count(elem) == 3:
                k3 = 1
            if nums.count(elem) == 2:
                k2 = 1
                count.add(elem)

        if k3 and k2:
            return self.TOP_HAND.get("fullhouse")
        elif k3:
            return self.TOP_HAND.get("3kind")
        elif k2 and len(count) == 2:
            return self.TOP_HAND.get("2pair")
        elif k2:
            return self.TOP_HAND.get("pair")

        # If all checks fail, return high card
        return self.TOP_HAND.get("highcard")

    def compare_with(self, other):

        if self.myRank < other.myRank:
            return self.RESULT[2]
        elif self.myRank > other.myRank:
            return self.RESULT[0]
        else:

            # Tie Cases #

            # Royal flush
            if self.myRank is self.HandRank.ROYAL_FLUSH.value:
                return self.RESULT[1]

            # Straight flush
            elif self.myRank is self.HandRank.STRAIGHT_FLUSH.value:

                # Starting value of straight determines winner
                if self.sorted_cards[0].rank < other.sorted_cards[0].rank:
                    return self.RESULT[2]
                elif self.sorted_cards[0].rank > other.sorted_cards[0].rank:
                    return self.RESULT[0]
                else:
                    return self.RESULT[1]

            # 4 of a kind
            elif self.myRank is self.HandRank.FOUR_OF_KIND.value:

                nums = self.sorted_values
                for elem in nums:
                    if nums.count(elem) == 4:
                        four_card = elem
                    else:
                        one_card = elem

                # Compare 4kind value than the remaining one card value
                other_nums = other.sorted_values
                for elem in other_nums:
                    if other_nums.count(elem) == 4:
                        if self.RANKINGS.get(four_card) < self.RANKINGS.get(elem):
                            return self.RESULT[2]
                        elif self.RANKINGS.get(four_card) > self.RANKINGS.get(elem):
                            return self.RESULT[0]
                    else:
                        other_one = elem

                if self.RANKINGS.get(one_card) < self.RANKINGS.get(other_one):
                    return self.RESULT[2]
                elif self.RANKINGS.get(one_card) > self.RANKINGS.get(other_one):
                    return self.RESULT[0]
                else:
                    return self.RESULT[1]


            # Full House
            elif self.myRank is self.HandRank.FULL_HOUSE.value:

                nums = self.sorted_values
                for elem in nums:
                    if nums.count(elem) == 3:
                        three_card = elem
                    else:
                        two_card = elem

                # Check 3kind value than 2kind value
                other_nums = other.sorted_values
                for elem in other_nums:
                    if other_nums.count(elem) == 3:
                        if self.RANKINGS.get(three_card) < self.RANKINGS.get(elem):
                            return self.RESULT[2]
                        elif self.RANKINGS.get(three_card) > self.RANKINGS.get(elem):
                            return self.RESULT[0]
                    else:
                        other_two = elem

                if self.RANKINGS.get(two_card) < self.RANKINGS.get(other_two):
                    return self.RESULT[2]
                elif self.RANKINGS.get(two_card) > self.RANKINGS.get(other_two):
                    return self.RESULT[0]

                return self.RESULT[1]

            # Flush
            elif self.myRank is self.HandRank.FLUSH.value:

                # Compare highest cards
                nums = self.sorted_cards
                other_nums = other.sorted_cards
                for i in range(4, -1, -1):
                    if self.sorted_cards[i].rank < other.sorted_cards[i].rank:
                        return self.RESULT[2]
                    elif self.sorted_cards[i].rank < other.sorted_cards[i].rank:
                        return self.RESULT[0]

                return self.RESULT[1]

            # Straight
            elif self.myRank is self.HandRank.STRAIGHT.value:

                # Starting value of straight determines winner
                if self.sorted_cards[0].rank < other.sorted_cards[0].rank:
                    return self.RESULT[2]
                elif self.sorted_cards[0].rank > other.sorted_cards[0].rank:
                    return self.RESULT[0]
                else:
                    return self.RESULT[1]

            # 3 of a Kind
            elif self.myRank is self.HandRank.THREE_OF_KIND.value:

                remaining = []
                nums = self.sorted_cards
                for elem in nums:
                    if nums.count(elem) == 3:
                        three_card = elem
                    else:
                        remaining.append(elem)

                # Compare 3kind value than remaining 2 values
                other_nums = other.sorted_cards
                other_rem = []
                for elem in other_nums:
                    if other_nums.count(elem) == 3:
                        if self.RANKINGS.get(three_card) < self.RANKINGS.get(elem):
                            return self.RESULT[2]
                        elif self.RANKINGS.get(three_card) > self.RANKINGS.get(elem):
                            return self.RESULT[0]
                    else:
                        other_rem.append(elem)

                for i in range(1, -1, -1):
                    if self.RANKINGS.get(remaining[i]) < self.RANKINGS.get(other_rem[i]):
                        return self.RESULT[2]
                    elif self.RANKINGS.get(remaining[i]) > self.RANKINGS.get(other_rem[i]):
                        return self.RESULT[0]
                    else:
                        return self.RESULT[1]

            # Two pair
            elif self.myRank is self.HandRank.TWO_PAIR.value:

                # Push to a set the values of 2 pairs and compare the two hands
                pairs = set()
                other_pair = set()

                nums = self.sorted_values
                for elem in nums:
                    if nums.count(elem) == 2:
                        pairs.add(elem)
                    else:
                        rem = elem

                other_nums = other.sorted_values
                for elem in other_nums:
                    if other_nums.count(elem) == 2:
                        other_pair.add(elem)
                    else:
                        other_rem = elem

                for i in range(1, -1, -1):
                    p = pairs.pop()
                    op = other_pair.pop()
                    if self.RANKINGS.get(p) < self.RANKINGS.get(op):
                        return self.RESULT[2]
                    elif self.RANKINGS.get(p) > self.RANKINGS.get(op):
                        return self.RESULT[0]

                # Compare the remaining one card value if both pair values are a tie
                if self.RANKINGS.get(rem) < self.RANKINGS.get(other_rem):
                    return self.RESULT[2]
                elif self.RANKINGS.get(rem) > self.RANKINGS.get(other_rem):
                    return self.RESULT[0]
                else:
                    return self.RESULT[1]

            # One Pair
            elif self.myRank is self.HandRank.PAIR.value:

                rem = []
                nums = self.sorted_values
                for elem in nums:
                    if nums.count(elem) == 2:
                        two_card = elem
                    else:
                        rem.append(elem)

                # Check 2kind value than other value
                other_nums = other.sorted_values
                other_rem = []
                for elem in other_nums:
                    if other_nums.count(elem) == 2:
                        if self.RANKINGS.get(two_card) < self.RANKINGS.get(elem):
                            return self.RESULT[2]
                        elif self.RANKINGS.get(two_card) > self.RANKINGS.get(elem):
                            return self.RESULT[0]
                    else:
                        other_rem.append(elem)

                for i in range(2, -1, -1):
                    if self.RANKINGS.get(rem[i]) < self.RANKINGS.get(other_rem[i]):
                        return self.RESULT[2]
                    elif self.RANKINGS.get(rem[i]) > self.RANKINGS.get(other_rem[i]):
                        return self.RESULT[0]

                return self.RESULT[1]

            # High Card
            else:

                # Compare highest cards
                nums = self.sorted_cards
                other_nums = other.sorted_cards
                for i in range(4, -1, -1):
                    if nums[i].rank < other_nums[i].rank:
                        return self.RESULT[2]
                    elif nums[i].rank > other_nums[i].rank:
                        return self.RESULT[0]

                return self.RESULT[1]

    class HandRank(enum.Enum):
        ROYAL_FLUSH = 1
        STRAIGHT_FLUSH = 2
        FOUR_OF_KIND = 3
        FULL_HOUSE = 4
        FLUSH = 5
        STRAIGHT = 6
        THREE_OF_KIND = 7
        TWO_PAIR = 8
        PAIR = 9
        HIGH_CARD = 10

    class Card:

        def __init__(self, val, suite):
            self.value = val
            self.suite = suite
            self.rank = self.CardRanking(val)

        def __lt__(self, other):
            # Low rank, high value
            return self.rank > other.rank

        def CardRanking(self, val):
            if val == 'A':
                return self.CardRank.ACE.value
            elif val == 'K':
                return self.CardRank.KING.value
            elif val == 'Q':
                return self.CardRank.QUEEN.value
            elif val == 'J':
                return self.CardRank.JACK.value
            elif val == 'T':
                return self.CardRank.TEN.value
            elif val == '9':
                return self.CardRank.NINE.value
            elif val == '8':
                return self.CardRank.EIGHT.value
            elif val == '7':
                return self.CardRank.SEVEN.value
            elif val == '6':
                return self.CardRank.SIX.value
            elif val == '5':
                return self.CardRank.FIVE.value
            elif val == '4':
                return self.CardRank.FOUR.value
            elif val == '3':
                return self.CardRank.THREE.value
            elif val == '2':
                return self.CardRank.TWO.value


        class CardRank(enum.Enum):
            ACE = 1
            KING = 2
            QUEEN = 3
            JACK = 4
            TEN = 5
            NINE = 6
            EIGHT = 7
            SEVEN = 8
            SIX = 9
            FIVE = 10
            FOUR = 11
            THREE = 12
            TWO = 13

def runTest(msg, expected, hand, other):
    player, opponent = PokerHand(hand), PokerHand(other)

    print(player.compare_with(opponent), expected, "{}: '{}' against '{}'".format(msg, hand, other))

    # test.assert_equals(player.compare_with(opponent), expected, "{}: '{}' against '{}'".format(msg, hand, other))

def main():
    # runTest("Highest pair wins", "Loss", "KC 4H KS 2H 8D", "8C 4S KH JS 4D")
    # runTest("Highest straight flush wins", "Loss", "JC 7H JS JD JH", "JH 9H TH KH QH")
    runTest("I DONT KNOOOOW", "Loss", "3D 2H 3H 2C 2D", "2H 2C 3S 3H 3D")

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