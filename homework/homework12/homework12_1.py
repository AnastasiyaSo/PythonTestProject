"""Homework 12"""
# Task 1

import random


class Card:
    """Creating cards class"""
    number_list = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
                   "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    mast_list = ["Diamonds", "Clubs", "Hearts", "Spades"]

    def __init__(self, mast, number):
        self.mast = mast
        self.number = number


class CardsDeck:
    """Creating cards deck class"""
    def __init__(self):
        self.cards_list = []
        for i in Card.mast_list:
            for n in Card.number_list:
                self.cards_list.append(Card(i, n))
        self.cards_list.append(Card("Joker", "Red"))
        self.cards_list.append(Card("Joker", "Black"))

    def shuffle(self):
        """Shuffling cards deck"""
        random.shuffle(self.cards_list)
        return True

    def get(self, index):
        """Getting cards deck"""
        return self.cards_list[index - 1]


deck = CardsDeck()
deck.shuffle()
card_number = int(input("Выберите карту из колоды в 54 карты: "))
card = deck.get(card_number)
print(f"You card is: {card.mast} {card.number}")
