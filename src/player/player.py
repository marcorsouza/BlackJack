import os
import sys
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant

class Player(Participant):
    def __init__(self, user) -> None:
        super().__init__(user)      

    def __get_user_input(self, prompt: str, valid_responses: list) -> str:
        while True:
            response = input(prompt).lower()
            if response in valid_responses:
                return response
            else:
                self.logger.log("Invalid input. Please try again.")

    def wants_to_hit(self) -> bool:
        while True:
            self.logger.log(f"{self.get_user().name}: {[card.name + ' ' + card.suit.symbol for card in self.hand.get_cards()]} - Points: {self.hand.get_value()}")

            response = self.__get_user_input(f"{self.get_user().name}, do you want to hit or stand or surrender? ", ['hit', 'stand', 'h', 's', 'surrender', 'sur'])

            if response in ['hit', 'h']:
                self.logger.log(f"{self.get_user().name} says: {random.choice(super().HITS)}") 
                return True
            elif response in ['stand', 's']:
                self.logger.log(f"{self.get_user().name} says: {random.choice(super().STANDS)}") 
                return False
            elif response in ['surrender', 'sur']:
                has_surrender = self.wants_to_surrender()
                if(has_surrender):
                    self.logger.log(f"{self.get_user().name} says: {random.choice(super().SURRENDERS)}") 
                return has_surrender
