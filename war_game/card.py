class Card:
    FIGURE_TO_VALUE = {
        **{str(i): i for i in range(2, 11)}, 'J': 11, 'Q': 12, 'K': 13, 'A': 15
    }

    def __init__(self, figure, colour):
        self.figure = figure
        self.colour = colour

    def __lt__(self, other):
        return self.FIGURE_TO_VALUE[self.figure] < self.FIGURE_TO_VALUE[other.figure]

    def __eq__(self, other):
        return self.FIGURE_TO_VALUE[self.figure] == self.FIGURE_TO_VALUE[other.figure]

    def __hash__(self):
        return hash(''.join((self.figure, self.colour)))

    def __repr__(self):
        return f"{self.figure}{self.colour}"

    @classmethod
    def create_card_from_string(cls, name):
        if len(name) == 2:
            return cls(name[0], name[-1])
        elif len(name) == 3:
            return cls(name[0:2], name[-1])


