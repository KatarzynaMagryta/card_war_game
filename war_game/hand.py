from war_game.card import Card
from collections import deque


class Hand:
    def __init__(self, cards):
        self._cards = deque(cards)
        self._combat_card = None
        self._pile = deque()

    @property
    def combat_card(self):
        return self._combat_card

    @property
    def cards(self):
        return self._cards

    @property
    def pile(self):
        return self._pile


    def play_card(self):
        self._combat_card = self._cards.popleft()
        self.add_to_pile(self._combat_card)
        return self._combat_card

    def play_three_cards_face_down(self):
        for i in range(3):
            card = self._cards.popleft()
            self.add_to_pile(card)

    def add_to_pile(self, thrown_card):
        self._pile.append(thrown_card)

    def add_to_cards(self, prize):
        for card in prize:
            self._cards.append(card)

    def give_up_cards(self):
        self._combat_card = None
        self._pile.clear()

    def __repr__(self):
        return str(self._cards)

    @classmethod
    def form_hand_from_list_of_strings(cls, input_list):
        return Hand(
            Card.create_card_from_string(card)
            for card in input_list
        )
        # przyjmuje wyr generujące obiektów typu card, a potem ją ubiera w klasę deck



