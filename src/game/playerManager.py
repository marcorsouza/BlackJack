import os
import sys


from utils.base_class import BaseClass

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from object_value.result import Result
from player.participant import Participant
from game.roundDetail import RoundDetail
from game.playerRoundDetail import PlayerRoundDetail
from game.handPlayerRoundDetail import HandPlayerRoundDetail
from player.dealer import Dealer
from player.hand import Hand


class PlayerManager(BaseClass):
    def __init__(self, bet: float):
        self.__bet = bet
    
    def update_balances(self, players: list[Participant], dealer: Dealer, winners: list[Participant]) -> RoundDetail:
        round_detail = RoundDetail()

        self.logger.result_log(f"Dealer's cards: {[card.name + ' ' + card.suit.symbol for card in dealer.get_player().hand]} - Balance: {dealer.get_player().get_user().balance}")
        
        if len(winners) == 0:
            self.logger.log("\nDealer wins! All players lost.")
            self.logger.result_log("\nDealer wins! All players lost.")

            for player in players:
                player_round_detail = PlayerRoundDetail(player.get_user().name, self.__bet)
                
                for hand in player.get_hands():
                    hand_player_detail = self.process_hand(player, hand, dealer)
                    player_round_detail.add_hand_detail(hand_player_detail)
                
                round_detail.add_player_detail(player_round_detail)
        else:
            for player in players:
                player_round_detail = PlayerRoundDetail(player.get_user().name, self.__bet)
                
                for hand in player.get_hands():
                    hand_player_detail = self.process_hand(player, hand, dealer)
                    player_round_detail.add_hand_detail(hand_player_detail)
                
                round_detail.add_player_detail(player_round_detail)
                
        for player_detail  in round_detail.player_details:
            for hand in player_detail.get_hands():
                self.logger.log(f"testando - {player_detail.player_name} - {hand} - {type(hand)}")
                self.logger.log(f"{[str(card) for card in hand.cards]}")

        self.logger.result_log(f"Dealer's cards: {[card.name + ' ' + card.suit.symbol for card in dealer.get_player().hand]} - Balance: {dealer.get_player().get_user().balance}")
        
        return round_detail

    def process_hand(self, player: Participant, hand: Hand, dealer: Dealer) -> HandPlayerRoundDetail:
        hand_player_detail = HandPlayerRoundDetail()

        if hand.get_value() > 0:
            if hand.win:
                player.get_user().update_balance(Result.WIN, self.__bet)
                dealer.get_player().get_user().update_balance(Result.LOSS, self.__bet)
                hand_player_detail.set_result(Result.WIN)
                self.logger.result_log(f"{player.get_user().name} win! {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")
            else:
                if hand.surrender:
                    player.get_user().update_balance(Result.LOSS, self.__bet/2)
                    dealer.get_player().get_user().update_balance(Result.WIN, self.__bet/2)
                    hand_player_detail.set_result(Result.SURRENDER)
                    self.logger.result_log(f"{player.get_user().name} surrender. {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")
                else:
                    player.get_user().update_balance(Result.LOSS, self.__bet)
                    dealer.get_player().get_user().update_balance(Result.WIN, self.__bet)
                    hand_player_detail.set_result(Result.LOSS)
                    self.logger.result_log(f"{player.get_user().name} loses. {[str(card) for card in hand]} - Points: {hand.get_value()} - Balance: {player.get_user().balance}")

            [hand_player_detail.add_card(card) for card in hand]
            hand_player_detail.set_value(hand.get_value())
        
        return hand_player_detail
