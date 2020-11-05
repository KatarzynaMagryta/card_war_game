from collections import deque, defaultdict
from war_game.prepare_game import *


def war_game(hand_p1, hand_p2):
    hand_p1 = Hand.form_hand_from_list_of_strings(hand_p1)
    hand_p2 = Hand.form_hand_from_list_of_strings(hand_p2)

    table = set_table_from_given_two_cards_sets(hand_p1, hand_p2)

    nrounds = 0
    while (len(hand_p1.cards) > 0 and len(hand_p2.cards) > 0):
        winner = play_round(table, all_players=True)
        nrounds += 1
        if winner == "PAT":
            return f"{winner} {nrounds}"

        if len(hand_p1.cards) == 0:
            winner = 2

        elif len(hand_p2.cards) == 0:
            winner = 1

    return f"{winner} {nrounds}"


def play_round(table, active_players=None, all_players=False):
    print(f"init table: {table}")
    len_1 = len(table[0].cards)
    len_2 = len(table[1].cards)

    if all_players:
        active_players = set(range(len(table)))

    # jeżeli jest wojna, wskazani gracze dokładają karty na stos:
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

        # utwórz stos kart wygranych zaczynając od gracza zwycięzcy
        prize = deque()
        players_piles = [
            add_pile_to_prize(table, i, prize)
            for i in range(len(table))
        ]

        # stos kart wygranych dołóż na spód kart gracza zwycięzcy tej rundy
        table[winner].add_to_cards(prize)
        for player in table:
            table[player].give_up_cards()

    else:
        winner = play_round(table, active_players=war_pointer)

    return winner


def add_pile_to_prize(table, i, prize):
    prize.extend(table[i].pile)
    return prize


def declare_round_winner(cards):
    return max(cards, key=cards.get)


def check_for_war(played_cards):
    counter = defaultdict(set)

    for player in played_cards:
        counter[played_cards[player].figure].add(player)

    war_pointer = {
        player
        for figure in counter
        for player in counter[figure]
        if len(counter[figure]) > 1
    }

    return war_pointer
