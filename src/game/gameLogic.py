import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player.participant import Participant
from object_value.level import Level
from object_value.handChoice import HandChoice 
from player.hand import Hand
from player.dealer import Dealer
from utils.base_class import BaseClass

class GameLogic(BaseClass):
    def __init__(self, players: List[Participant], dealer: Dealer):
        self.players = players
        self.dealer = dealer  
    
    def get_winners(self):
        winners = []
        dealer_value = self.dealer.get_player().hand.get_value()
        hands_won = 0
        for player in self.players:
            
            if(player.get_hand_choice() == HandChoice.HAND1):
                if self.has_winner(dealer_value, player.hand):
                    hands_won += 1
                    player.hand.win = True
            
            if(player.get_hand_choice() == HandChoice.BOTH):
                for i in range(0, 2):                    
                    player.switch_hand(i)
                    if self.has_winner(dealer_value, player.hand):
                        hands_won += 1
                        player.hand.win = True                  
                player.switch_hand(0)
            if hands_won > 0:
                winners.append((player, hands_won))
                
            hands_won = 0
        return winners
    
    def has_winner(self, dealer_value, hand:Hand) -> bool:        
            player_value = hand.get_value()
            """
            Returns a list of players who won the round.

            For a player to win, the following conditions must be met:
            - The total value of the player's hand must not exceed 21 points.
            - If the total value of the dealer's hand exceeds 21 points or the total value of the player's hand is greater than the dealer's, the player wins.
            - If the player has exactly two cards in the hand and the total value is 21, then they have a blackjack and win, unless the dealer also has a blackjack.
            """
            is_blackjack = hand.is_blackjack() and len(hand) == 2
            return player_value <= 21 and (dealer_value > 21 or player_value > dealer_value or is_blackjack and dealer_value != 21)
                