import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from object_value.level import Level
from player.botPlayer import BotPlayer
from player.participant import Participant
from game.user import User

class Dealer:
    def __init__(self, deck = []):
        self.__player = BotPlayer(User("Dealer", Level.ADVANCED, 100000))
        self.__deck = deck
        
    def get_player(self):
        return self.__player
    
    def reset_deck(self):
        self.__deck.reset_deck()
        self.__player.reset_cards()
    
    def deal_card(self, player : Participant):
        # Distribui uma carta para o jogador
        player.add_card(self.__deck.get_next_card())
        
    def remaining_cards(self):
        return self.__deck.get_cards()
