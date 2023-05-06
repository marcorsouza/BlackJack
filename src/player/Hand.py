import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from card.card import Card

class Hand:
    def __init__(self, cards: list[Card] = None):
        
        if cards is None:
            cards = []
        self.__cards = cards
        self.__win= False
        
    @property
    def win(self):
        return self.__win
    
    @win.setter
    def win(self, win: bool):
        self.__win = win

    def add_card(self, card: Card):
        self.__cards.append(card)

    def pop_card(self, index: int) -> Card:
        return self.__cards.pop(index)

    def clear_cards(self):
        self.__cards.clear()
        self.__win= False

    def get_cards(self) -> list[Card]:
        return self.__cards
    
    def has_cards(self) -> list[Card]:
        return len(self.__cards) > 0

    def get_value(self) -> int:
        hand_value = 0
        aces_count = 0
        for card in self.__cards:
            if card.name != 'Ace':
                hand_value += card.value
            else:
                aces_count += 1

        for i in range(aces_count):
            if hand_value + 11 <= 21:
                hand_value += 11
            else:
                hand_value += 1
        return hand_value

    def is_bust(self) -> bool:
        return self.get_value() > 21

    def is_blackjack(self) -> bool:
        return len(self.__cards)