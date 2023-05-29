import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.base_class import BaseClass

class RoundDetail(BaseClass):
    def __init__(self):
        self.player_details = []

    def add_player_detail(self, player_detail):
        self.player_details.append(player_detail)



