import random
from war_game.card import Card
from war_game.hand import Hand
from itertools import product


def create_deck():
    figures = [*[str(i) for i in range(2, 11)], 'J', 'Q', 'K', 'A']
    colours = ['D', 'H', 'C', 'S']

    return [
        Card(figure, colour)
        for figure, colour in product(figures, colours)
    ]


def deal_to_player(deck, n_cards_in_hand, n_players, player_n):
    """The cards are dealt from the top of the stack
    The very left of output (top of players pile) are made of cards which were at the lower parts of the deck.
    The very last cards of the deck are never dealt unless 52 % n_players == 0"""
    return Hand(
        deck[i]
        for i in reversed(range(n_players * n_cards_in_hand))
        if i % n_players == player_n
    )


def deal_cards(n_players, n_cards_in_hand):
    """
    Deck is set from the top (left side of the list) to the bottom (to the right side)
    Cards are played from the top, one by one to the players to imitate the actual game.
    The spare cards from the very right of the list will not be dealt to players
    """

    deck = create_deck()
    random.shuffle(deck)

    return {
        i: deal_to_player(deck, n_cards_in_hand, n_players, i)
        for i in range(n_players)
    }


def set_table_from_given_two_cards_sets(set_1, set_2):
    return {
        0: set_1, 1: set_2
    }

# for well visible example turn off the cards shuffling to see an order

# example_table = deal_cards(n_players=2, n_cards_in_hand=5)
# print(example_table)
