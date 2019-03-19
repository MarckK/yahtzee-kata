from yahtzee import *


def test_six_dice_rolled():
    rolls = roll(6)
    assert len(rolls) == 6


def test_pair_score():
    rolls = [3, 3, 3, 4, 4]
    assert multiples_score(rolls, 2) == 8


def test_score_numbers():
    rolls = [1, 1, 2, 4, 4]
    num = 4
    assert score_numbers(rolls, num) == 8


def test_triples_score():
    rolls = [3, 3, 3, 4, 5]
    assert multiples_score(rolls, 3) == 9


def test_four_kind_score():
    rolls = [2, 2, 2, 2, 5]
    assert multiples_score(rolls, 4) == 8


def test_straight_score():
    rolls = [1, 2, 3, 4, 5]
    assert straight_score(rolls) == 15


def test_full_house_score():
    rolls = [1, 1, 2, 2, 2]
    assert full_house_score(rolls) == 8


def test_yahtzee_score():
    rolls = [1, 1, 1, 1, 1]
    assert yahtzee_score(rolls) == 50


@pytest.mark.parametrize("rolls, category", [([1, 1, 1, 1, 1], "Yahtzee")])
def test_score(rolls, category):
    assert score(rolls, category) == 50
