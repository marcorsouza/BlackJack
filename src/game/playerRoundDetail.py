from ast import List
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.base_class import BaseClass
from player.hand import Hand

class PlayerRoundDetail(BaseClass):
    def __init__(self, player_name, bet):
        self.player_name = player_name
        self.bet = bet
        self.hand_details = []

    def add_hand_detail(self, hand_detail):
        self.hand_details.append(hand_detail)
        
    def get_hands(self):
        return self.hand_details