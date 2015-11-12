POKER_HANDS = ["nothing",
               "one pair",
               "two pair",
               "three of a kind",
               "straight",
               "flush",
               "full house",
               "four of a kind",
               "straight flush"]
FACE_CARDS = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def parse_hand(hand):
    numbers, suits = zip(*hand)
    numbers = sorted(FACE_CARDS[n] if n in FACE_CARDS else int(n)
                     for n in numbers)
    if numbers == [2, 3, 4, 5, 14]:
        numbers = [1, 2, 3, 4, 5]
    return (numbers, suits)

def rank_hand(hand):
    numbers, suits = parse_hand(hand)
    if numbers == range(numbers[0], numbers[-1] + 1):
        if len(set(suits)) == 1:
            return POKER_HANDS.index("straight flush")
        else:
            return POKER_HANDS.index("straight")
    if len(set(numbers)) == 2:
        if len(set(suits)) == 4:
            return POKER_HANDS.index("four of a kind")
        else:
            return POKER_HANDS.index("full house")
    if len(set(suits)) == 1:
        return POKER_HANDS.index("flush")
    if len(set(numbers)) == 3:
        if sorted(numbers.count(n) for n in set(numbers)) == [1, 1, 3]:
            return POKER_HANDS.index("three of a kind")
        else:
            return POKER_HANDS.index("two pair")
    if len(set(numbers)) == 4:
        return POKER_HANDS.index("one pair")
    return POKER_HANDS.index("nothing")

def poker(hands_list):
    ranks = [rank_hand(hand) for hand in hands_list]
    max_rank = max(ranks)
    max_hands = [j for i, j in enumerate(hands_list)
                 if ranks[i] == max_rank]
    if len(max_hands) == 1:
        return max_hands
    if max_rank in [0, 4, 5, 8]:
        kickers = [parse_hand(hand)[0][-1] for hand in hands_list]
        return [j for i, j in enumerate(hands_list)
                if kickers[i] == max(kickers)]
    if max_rank in [7, 6, 3]:
        
    if max_rank in [1, 2]:

