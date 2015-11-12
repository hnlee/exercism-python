
class PokerHand:
    POKER_HANDS = ["nothing",
                   "one pair",
                   "two pairs",
                   "three of a kind",
                   "straight",
                   "flush",
                   "full house",
                   "four of a kind",
                   "straight flush"]
    FACE_CARDS = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    def __init__(self, card_list):
        self.cards = card_list
        if len(card_list) != 5:
            raise ValueError("Poker hands have five cards.")
        numbers, suits = zip(*self.cards)
        self.numbers = sorted(self.FACE_CARDS[n] if n in self.FACE_CARDS 
                              else int(n)
                              for n in numbers)
        if self.numbers == [2, 3, 4, 5, 14]:
            # ace-low straights or straight flushes
            self.numbers = [1, 2, 3, 4, 5]
        self.suits = set(suits)
    def rank_hand(self):
        self.frequency = dict((n, self.numbers.count(n))
                              for n in set(self.numbers))
        if self.numbers == range(self.numbers[0], self.numbers[0] + 5):
            self.kickers = [max(self.numbers)]
            if len(self.suits) == 1:
                self.rank = self.POKER_HANDS.index("straight flush")
            else:
                self.rank = self.POKER_HANDS.index("straight")
        elif len(self.suits) == 1:
            self.kickers = self.numbers[::-1]
            self.rank = self.POKER_HANDS.index("flush")
        elif max(self.frequency.values()) == 4:
            self.kickers = [i for i, j in self.frequency.items()
                            if j == 4] + \
                           [i for i, j in self.frequency.items()
                            if j == 1]
            self.rank = self.POKER_HANDS.index("four of a kind")
        elif max(self.frequency.values()) == 3:
            self.kickers = [i for i, j in self.frequency.items()
                            if j == 3]
            if sorted(self.frequency.values()) == [2, 3]:
                self.kickers += [i for i, j in self.frequency.items()
                                 if j == 2]
                self.rank = self.POKER_HANDS.index("full house")
            else:
                self.kickers += sorted([i for i, j in self.frequency.items()
                                        if j == 1], reverse = True)
                self.rank = self.POKER_HANDS.index("three of a kind")
        elif max(self.frequency.values()) == 2:
            if sorted(self.frequency.values()) == [1, 2, 2]:
                self.kickers = sorted([i for i, j in self.frequency.items()
                                       if j == 2], reverse = True) + \
                               [i for i, j in self.frequency.items()
                                if j == 1]
                self.rank = self.POKER_HANDS.index("two pairs")
            else:
                self.kickers = [i for i, j in self.frequency.items()
                                if j == 2] + \
                               sorted([i for i, j in self.frequency.items()
                                       if j == 1], reverse = True)
                self.rank = self.POKER_HANDS.index("one pair")
        else:
            self.kickers = self.numbers[::-1]
            self.rank = self.POKER_HANDS.index("nothing")
        return self.rank
    def __str__(self):
        return ' '.join(self.cards)

def poker(hands_list):
    hands = [PokerHand(hand) for hand in hands_list]
    ranks = [hand.rank_hand() for hand in hands]
    highest_hands = [hands[i] for i, j in enumerate(ranks)
                     if j == max(ranks)]
    if len(highest_hands) > 1:
        kickers = zip(*[hand.kickers for hand in highest_hands])
        k = 0
        while k < len(kickers) - 1 and len(set(kickers[k])) == 1:
            k += 1
        if len(set(kickers[k])) > 1:
            highest_hands = [highest_hands[i]
                             for i, j in enumerate(kickers[k])
                             if j == max(kickers[k])]
    return [hand.cards for hand in highest_hands]
