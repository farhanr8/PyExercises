import enum


class OrderedEnum(enum.Enum):
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class HandRank(OrderedEnum):
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


class CardRank(OrderedEnum):
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


class Result(enum.Enum):
    WIN = "Win"
    LOSS = "Loss"
    TIE = "Tie"


class PokerHand(object):

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

        cards = self.sorted_cards
        nums = self.sorted_values

        # Flush check
        for i in range(1, 5):
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
                    if cards[j].rank != CardRank.TWO.value + j:
                        special = 0
                        break
                    else:
                        special = 1
                if special is 1:
                    return HandRank.STRAIGHT_FLUSH
            ##########################################

            for i in range(5):

                if cards[0].rank - i != cards[i].rank:
                    sf = 0
                    break
                else:
                    sf = 1

            if sf is 1:

                # Straight starting with T, meaning royal flush

                if cards[0].rank == CardRank.TEN.value:
                    return HandRank.ROYAL_FLUSH

                # Straight flush starting at some other value
                else:
                    return HandRank.STRAIGHT_FLUSH

            else:
                return HandRank.FLUSH

        # Straight check

        ##########################################
        # Special Case: A 2 3 4 5
        if 'A' in nums:
            for j in range(4):
                if cards[j].rank != CardRank.TWO.value + j:
                    special = 0
                    break
                else:
                    special = 1
            if special is 1:
                return HandRank.STRAIGHT
        ##########################################

        for i in range(5):
            if cards[0].rank - i != cards[i].rank:
                s = 0
                break
            else:
                s = 1
        if s is 1:
            return HandRank.STRAIGHT

        # Kind check

        k3, k2 = 0, 0
        count = set()
        for elem in nums:
            if nums.count(elem) == 4:
                return HandRank.FOUR_OF_KIND
            if nums.count(elem) == 3:
                k3 = 1
            if nums.count(elem) == 2:
                k2 = 1
                count.add(elem)

        if k3 and k2:
            return HandRank.FULL_HOUSE
        elif k3:
            return HandRank.THREE_OF_KIND
        elif k2 and len(count) == 2:
            return HandRank.TWO_PAIR
        elif k2:
            return HandRank.PAIR

        # If all checks fail, return high card

        return HandRank.HIGH_CARD

    def compare_with(self, other):

        if self.myRank < other.myRank:
            return Result.WIN.value

        elif self.myRank > other.myRank:
            return Result.LOSS.value

        else:

            # Tie Cases #

            cards = self.sorted_cards
            nums = self.sorted_values
            other_cards = other.sorted_cards
            other_nums = other.sorted_values

            # Royal flush
            if self.myRank is HandRank.ROYAL_FLUSH:
                return Result.TIE.value

            # Straight flush or Straight
            elif self.myRank is HandRank.STRAIGHT_FLUSH or self.myRank is HandRank.STRAIGHT:

                # Starting value of straight determines winner
                if cards[0].rank < other_cards[0].rank:
                    return Result.WIN.value
                elif cards[0].rank > other_cards[0].rank:
                    return Result.LOSS.value
                else:
                    return Result.TIE.value

            # 4 of a kind
            elif self.myRank is HandRank.FOUR_OF_KIND:

                for c in cards:
                    if nums.count(c.value) == 4:
                        four_card = c
                    else:
                        one_card = c

                # Compare 4kind value than the remaining one card value

                for card in other_cards:
                    if other_nums.count(card.value) == 4:
                        if four_card.rank < card.rank:
                            return Result.WIN.value
                        elif four_card.rank > card.rank:
                            return Result.LOSS.value
                    else:
                        other_one = card

                if one_card.rank < other_one.rank:
                    return Result.WIN.value
                elif one_card.rank > other_one.rank:
                    return Result.LOSS.value
                else:
                    return Result.TIE.value

            # Full House
            elif self.myRank is HandRank.FULL_HOUSE:

                for c in cards:
                    if nums.count(c.value) == 3:
                        three_card = c
                    else:
                        two_card = c

                # Check 3kind value than 2kind value
                for card in other_cards:
                    if other_nums.count(card.value) == 3:
                        if three_card.rank < card.rank:
                            return Result.WIN.value
                        elif three_card.rank > card.rank:
                            return Result.LOSS.value
                    else:
                        other_two = card

                if two_card.rank < other_two.rank:
                    return Result.WIN.value
                elif two_card.rank > other_two.rank:
                    return Result.LOSS.value

                return Result.TIE.value

            # Flush or High Card
            elif self.myRank is HandRank.FLUSH or self.myRank is HandRank.HIGH_CARD:

                # Compare highest cards
                for i in range(4, -1, -1):
                    if cards[i].rank < other_cards[i].rank:
                        return Result.WIN.value
                    elif cards[i].rank > other_cards[i].rank:
                        return Result.LOSS.value

                return Result.TIE.value

            # 3 of a Kind
            elif self.myRank is HandRank.THREE_OF_KIND:

                remaining = []
                for c in cards:
                    if nums.count(c.value) == 3:
                        three_card = c
                    else:
                        remaining.append(c)

                # Compare 3kind value than remaining 2 values
                other_rem = []
                for card in other_cards:
                    if other_nums.count(card.value) == 3:
                        if three_card.rank < card.rank:
                            return Result.WIN.value
                        elif three_card.rank > card.rank:
                            return Result.LOSS.value
                    else:
                        other_rem.append(card)

                for i in range(1, -1, -1):
                    if remaining[i].rank < other_rem[i].rank:
                        return Result.WIN.value
                    elif remaining[i].rank > other_rem[i].rank:
                        return Result.LOSS.value
                    else:
                        return Result.TIE.value

            # Two pair
            elif self.myRank is HandRank.TWO_PAIR:

                # Push to a set the values of 2 pairs and compare the two hands
                pairs = []
                other_pairs = []

                for c in cards:
                    ignore = []
                    if nums.count(c.value) == 2:
                        if c.value not in ignore:
                            pairs.append(c)
                            ignore.append(c.value)
                    else:
                        rem = c

                for card in other_cards:
                    ignore = []
                    if other_nums.count(card.value) == 2:
                        if card.value not in ignore:
                            other_pairs.append(card)
                            ignore.append(card.value)
                    else:
                        other_rem = card

                for i in range(1, -1, -1):
                    if pairs[i].rank < other_pairs[i].rank:
                        return Result.WIN.value
                    elif pairs[i].rank > other_pairs[i].rank:
                        return Result.LOSS.value

                # Compare the remaining one card value if both pair values are a tie
                if rem.rank < other_rem.rank:
                    return Result.WIN.value
                elif rem.rank > other_rem.rank:
                    return Result.LOSS.value
                else:
                    return Result.TIE.value

            # One Pair
            elif self.myRank is HandRank.PAIR:

                rem = []
                for c in cards:
                    if nums.count(c.value) == 2:
                        two_card = c
                    else:
                        rem.append(c)

                # Check 2kind value than other value
                other_rem = []
                for card in other_cards:
                    if other_nums.count(card.value) == 2:
                        if two_card.rank < card.rank:
                            return Result.WIN.value
                        elif two_card.rank > card.rank:
                            return Result.LOSS.value
                    else:
                        other_rem.append(card)

                for i in range(2, -1, -1):
                    if rem[i].rank < other_rem[i].rank:
                        return Result.WIN.value
                    elif rem[i].rank > other_rem[i].rank:
                        return Result.LOSS.value

                return Result.TIE.value


    class Card:

        def __init__(self, val, suite):
            self.value = val
            self.suite = suite
            self.rank = self.CardRanking(val)

        def __lt__(self, other):
            # Low rank, high value
            if self.__class__ is other.__class__:
                return self.rank < other.rank
            return NotImplemented

        def CardRanking(self, val):
            if val == 'A':
                return CardRank.ACE.value
            elif val == 'K':
                return CardRank.KING.value
            elif val == 'Q':
                return CardRank.QUEEN.value
            elif val == 'J':
                return CardRank.JACK.value
            elif val == 'T':
                return CardRank.TEN.value
            elif val == '9':
                return CardRank.NINE.value
            elif val == '8':
                return CardRank.EIGHT.value
            elif val == '7':
                return CardRank.SEVEN.value
            elif val == '6':
                return CardRank.SIX.value
            elif val == '5':
                return CardRank.FIVE.value
            elif val == '4':
                return CardRank.FOUR.value
            elif val == '3':
                return CardRank.THREE.value
                #return CardRank.THREE
            elif val == '2':
                return CardRank.TWO.value
                # return CardRank.TWO


def runTest(msg, expected, hand, other):
    player, opponent = PokerHand(hand), PokerHand(other)

    print(player.compare_with(opponent), expected, "{}: '{}' against '{}'".format(msg, hand, other))

    # test.assert_equals(player.compare_with(opponent), expected, "{}: '{}' against '{}'".format(msg, hand, other))

def main():
    # runTest("Highest pair wins", "Loss", "KC 4H KS 2H 8D", "8C 4S KH JS 4D")
    # runTest("Highest straight flush wins", "Loss", "JC 7H JS JD JH", "JH 9H TH KH QH")
    runTest("I DONT KNOOOOW", "Loss", "JH AH TH KH QH", "JH AH TH KH QH")

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