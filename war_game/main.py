from collections import deque, defaultdict
from war_game.prepare_game import *


# def war_game(n_players, n_cards_in_hand=5):
#     """table - dict with players (as keys) and their cards (class Hand)
#     Hand class has attributes:
#     - cards (deque),
#     - combat_card = card which is played in a round. This pole is empty between rounds
#     - pile (deque) = a stock in where played cards are being thrown"""
#
#     table = deal_cards(n_players, n_cards_in_hand)
#     play_round(table, all_players=True)

def war_game(hand_p1, hand_p2):
    """hand_p1, hand_p2 - lists of strings"""
    hand_p1 = Hand.form_hand_from_list_of_strings(hand_p1)
    hand_p2 = Hand.form_hand_from_list_of_strings(hand_p2)

    table = set_table_from_given_two_cards_sets(hand_p1, hand_p2)

    nrounds = 0
    while(len(hand_p1.cards) > 0 and len(hand_p2.cards) > 0):
        winner = play_round(table, all_players=True)
        nrounds += 1
        if winner == "PAT":
            return f"{winner} {nrounds}"

        if len(hand_p1.cards) == 0:
            winner = 2

        elif len(hand_p2.cards) == 0:
            winner = 1

        # if nrounds == 35:
        #     return f"{winner} {nrounds}"
        if nrounds == 215:
            x=1

    return f"{winner} {nrounds}"


def play_round(table, active_players=None, all_players=False):
    print(f"init table: {table}")
    len_1 = len(table[0].cards)
    len_2 = len(table[1].cards)

    if all_players:
        active_players = set(range(len(table)))

    # for player in table:
    #     if len(table[player].cards) == 0:
    #         return "game over"

    #jeżeli jest wojna, wskazani gracze dokładają karty na stos:
    if all_players == False:
        for player in active_players:
            if len(table[player].cards) < 4:
                return "PAT"
            table[player].play_three_cards_face_down()


    # wskazani gracze zagrywają karty
    for player in table:
        if player in active_players:
            table[player].play_card()

    # tworzy się słownik z rzuconymi kartami
    combat_cards = {
        player: table[player].combat_card
        for player in table
    }

    war_pointer = check_for_war(combat_cards)

    winner = None
    if len(war_pointer) == 0:
        winner = declare_round_winner(combat_cards)
        # print(f"winner {winner}")

        # utwórz stos kart wygranych zaczynając od gracza zwycięzcy
        prize = deque()
        players_piles = [
            add_pile_to_prize(table, i, prize)
            for i in range(len(table))
        ]  # popraw na petle

        # print(f"prize {prize}")

        # stos kart wygranych dołóż na spód kart gracza zwycięzcy tej rundy
        table[winner].add_to_cards(prize)
        for player in table:
            table[player].give_up_cards()
        # print(table[winner])
        # print(f"winner: {winner}")



    else:
        winner = play_round(table, active_players=war_pointer)

    return winner

def add_pile_to_prize(table, i, prize):
    prize.extend(table[i].pile)
    return prize


def declare_round_winner(cards):
    return max(cards, key=cards.get)


def check_for_war(played_cards):
    """played_cards to słownik, gdzie kluczami są numery graczy, a wartściami - instancje klasy Card
    zwraca zbiór graczy, który muszą wyłożyć natępną kartę
    """
    counter = defaultdict(set)

    for player in played_cards:
        # v 3 kasia
        # if played_cards[player].figure not in counter:
        #     counter[played_cards[player].figure] = set()
        # counter[played_cards[player].figure].add(player)

        # v2 counter.setdefault(played_cards[player].figure, set()).add(player)

        counter[played_cards[player].figure].add(player)

    war_pointer = {
        player
        for figure in counter
        for player in counter[figure]
        if len(counter[figure]) > 1
    }

    return war_pointer

print(war_game(
['5S', '8D', '10H', '9S', '4S', '6H', 'QC', '6C', '6D', '9H', '2C', '7S', 'AC', '5C', '7D', '9D', 'QS',
'4D', '3C', 'JS', '2D', 'KD', '10S', 'QD', '3H', '8H'],
['4C', 'JC', '8S', '10C', '5H', '7H', '3D', 'AH', 'KS', '10D', 'JH', '6S', '2S', 'KC', '8C', '9C', 'KH',
'3S', 'AD', 'JD', '4H', '7C', '2H', 'QH', '5D', 'AS']
))



# cards1 = {0: Hand.form_hand_from_list_of_strings(['AS', '2D', '6D']),
#           1: Hand.form_hand_from_list_of_strings(['QS', 'AD', 'AD']),
#           2: Hand.form_hand_from_list_of_strings(['QS', 'KD', 'QD'])}

# play_round(cards1)

