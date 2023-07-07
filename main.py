# Define a list of card ranks
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Define a list of card suits
suits = ['hearts', 'diamonds', 'spades', 'clubs']

# Define a deck of cards as a list of tuples, where each tuple is a rank and a suit
deck = [(rank, suit) for rank in ranks for suit in suits]

# Define a function to evaluate a hand of 5 cards and return the hand's rank
def evaluate_hand(hand):
    # Check for an Ace-high straight flush (aka Royal Flush)
    royal_flush = False
    for suit in suits:
        if hand == [('10', suit), ('J', suit), ('Q', suit), ('K', suit), ('A', suit)]:
            royal_flush = True
    if royal_flush:
        return 'Ace-high Straight Flush (Royal Flush)'
        
    # Check for a straight flush
    straight = False
    flush = False
    for suit in suits:
        suit_count = 0
        for card in hand:
            if card[1] == suit:
                suit_count += 1
        if suit_count == 5:
            flush = True
    for i in range(len(ranks) - 4):
        if ranks[i:i+5] == [card[0] for card in hand]:
            straight = True
    if straight and flush:
        return 'Straight Flush'
    
    # Check for four of a kind
    for rank in ranks:
        count = 0
        for card in hand:
            if card[0] == rank:
                count += 1
        if count == 4:
            return 'Four of a Kind'
    
    # Check for a full house
    three_of_a_kind = False
    two_of_a_kind = False
    for rank in ranks:
        count = 0
        for card in hand:
            if card[0] == rank:
                count += 1
        if count == 3:
            three_of_a_kind = True
        if count == 2:
            two_of_a_kind = True
    if three_of_a_kind and two_of_a_kind:
        return 'Full House'
    
    # Check for a flush
    if flush:
        return 'Flush'
    
    # Check for a straight
    if straight:
        return 'Straight'
    
    # Check for three of a kind
    if three_of_a_kind:
        return 'Three of a Kind'
    
    # Check for two pairs
    pairs = 0
    for rank in ranks:
        count = 0
        for card in hand:
            if card[0] == rank:
                count += 1
        if count == 2:
            pairs += 1
    if pairs == 2:
        return 'Two Pairs'
    
    # Check for a pair
    if pairs == 1:
        return 'Pair'
    
    # Return high card
    return 'High Card'

# Get the user's 5 cards
hand = []
for i in range(5):
    while True:
        rank = input("Enter the rank of card {} (2-10, J, Q, K, A): ".format(i+1))
        if rank in ranks:
            break
        else:
            print("Invalid rank. Please enter a valid rank.")
    while True:
        suit = input("Enter the suit of card {} (hearts, diamonds, spades, clubs): ".format(i+1))
        if suit in suits:
            break
        else:
            print("Invalid suit. Please enter a valid suit.")
    hand.append((rank, suit))

print(hand)
print(evaluate_hand(hand))