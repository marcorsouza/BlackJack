import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.base_class import BaseClass

class HandPlayerRoundDetail(BaseClass):
    def __init__(self):
        self.cards = []
        self.value = 0
        self.result = None

    def add_card(self, card):
        self.cards.append(card)

    def set_value(self, value):
        self.value = value

    def set_result(self, result):
        self.result = result