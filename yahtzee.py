import pytest

from numpy import random, unique, max


def roll(n_dice):
    return random.randint(1, 7, size=n_dice)


def score_numbers(rolls, num):
    numbers, counts = unique(rolls, return_counts=True)
    if num in numbers:
        return counts[numbers == num] * num
    return 0


def multiples_score(rolls, multiplicity):
    numbers, counts = unique(rolls, return_counts=True)
    if multiplicity in counts:
        return numbers[counts == multiplicity] * multiplicity
    return 0


def straight_score(rolls):
    numbers, counts = unique(rolls, return_counts=True)
    if all(counts == 1):
        return sum(rolls)
    return 0


def full_house_score(rolls):
    numbers, counts = unique(rolls, return_counts=True)
    if 3 in counts and 2 in counts:
        return sum(rolls)
    return 0


def yahtzee_score(rolls):
    numbers, counts = unique(rolls, return_counts=True)
    if len(numbers) == 1:
        return 50
    return 0


def score(rolls, category):
    categories = {'Yahtzee': yahtzee_score,
                  "Full House": full_house_score,
                  }
    return categories[category](rolls)
