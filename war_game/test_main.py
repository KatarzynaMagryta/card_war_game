import pytest
from war_game.main import war_game


@pytest.mark.parametrize(
    ('hand_player_1', 'hand_player_2', 'expected_winner'), (
            (
                ['AD', 'KC', 'QC'], ['KH', 'QS', 'JC'], "1 3"
            ),
            (
                ['5C', '3D', '2C', '7D', '8C', '7S', '5D', '5H', '6D', '5S', '4D', '6H', '6S', '3C', '3S', '7C',
                '4S', '4H', '7H', '4C', '2H', '6C', '8D', '3H', '2D', '2S'],
                ['AC', '9H', 'KH', 'KC', 'KD', 'KS', '10S', '10D', '9S', 'QD', 'JS', '10H', '8S', 'QH', 'JD', 'AD',
                'JC', 'AS', 'QS', 'AH', 'JH', '10C', '9C', '8H', 'QC', '9D'],
                "2 26"
            ),
            (
                ['6H', '7H', '6C', 'QS', '7S', '8D', '6D', '5S', '6S', 'QH', '4D', '3S', '7C', '3C', '4S', '5H',
                 'QD', '5C', '3H', '3D', '8C', '4H', '4C', 'QC', '5D', '7D'],
                ['JH', 'AH', 'KD', 'AD', '9C', '2D', '2H', 'JC', '10C', 'KC', '10D', 'JS', 'JD', '9D', '9S', 'KS',
                 'AS', 'KH', '10S', '8S', '2S', '10H', '8H', 'AC', '2C', '9H'],
                "2 56"
            ),
            (
                ['8C', 'KD', 'AH', 'QH', '2S'], ['8D', '2D', '3H', '4D', '3S'], "2 1"
            ),
            (
                ['10H', 'KD', '6C', '10S', '8S', 'AD', 'QS', '3D', '7H', 'KH', '9D', '2D', 'JC', 'KS', '3S', '2S', 'QC',
                 'AC', 'JH', '7D', 'KC', '10D', '4C', 'AS', '5D', '5S'],
                ['2H', '9C', '8C', '4S', '5C', 'AH', 'JD', 'QH', '7C', '5H', '4H', '6H', '6S', 'QD', '9H', '10C', '4D',
                 'JS', '6D', '3H', '8H', '3C', '7S', '9S', '8D', '2C'],
                "1 52"
            ),
            (
                ['5S', '8D', '10H', '9S', '4S', '6H', 'QC', '6C', '6D', '9H', '2C', '7S', 'AC', '5C', '7D', '9D', 'QS',
                 '4D', '3C', 'JS', '2D', 'KD', '10S', 'QD', '3H', '8H'],
                ['4C', 'JC', '8S', '10C', '5H', '7H', '3D', 'AH', 'KS', '10D', 'JH', '6S', '2S', 'KC', '8C', '9C', 'KH',
                 '3S', 'AD', 'JD', '4H', '7C', '2H', 'QH', '5D', 'AS'],
                'PAT'
            )
    )
)
def test_war_game(hand_player_1, hand_player_2, expected_winner):
    winner = war_game(hand_player_1, hand_player_2)
    assert winner == expected_winner

