from typing import List, Tuple
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from card.suit import Suit
from card.card import Card

from card.card import Card
from card.suit import Suit
from utils.base_class import BaseClass

import random

class Deck(BaseClass):
        
    def __init__(self):
        self.__cards = self.__create_deck()
        self.__card_iterator = iter(self.__cards)        
    def __create_suits(self):
        suits: Tuple[Tuple[str, str]] = (("spade", "♠"), ("heart", "♥"), ("diamond", "♦"), ("clubs", "♣"))
        return tuple(Suit(name, symbol) for name, symbol in suits)

    def __create_deck(self):
        deck: List[Card] = []
        for suit in self.__create_suits():
            deck.append(Card("Ace", 1, suit))
            for i in range(2, 11):
                deck.append(Card(str(i), i, suit))
            deck.append(Card("Jack", 10, suit))
            deck.append(Card("Queen", 10, suit))
            deck.append(Card("King", 10, suit))
        
        return deck
    
    def shuffle_deck(self): 
        self.__cards = random.sample(self.__cards, len(self.__cards))
        self.__card_iterator = iter(self.__cards)

    def get_next_card(self):
        if len(self.__cards) == 0:
            raise ValueError("No cards available in the deck.")
        return next(self.__card_iterator)

    def reset_deck(self):
        self.__cards = self.__create_deck()
        self.shuffle_deck()
        self.__card_iterator = iter(self.__cards)

    def get_cards(self)-> List[Card]:
        return self.__cards
