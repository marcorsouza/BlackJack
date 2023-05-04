import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.player import Player
from game.dealer import Dealer  # importa a classe Dealer
from card.deck import Deck 
from game.round import Round # importa a classe Round

from abc import ABC, abstractmethod

class GameObserver(ABC):
    @abstractmethod
    def start_game(self):
        pass

class GameInputHandler(ABC):
    @abstractmethod
    def add_player(self, player: Player) -> Player:
        pass
    
class Game:
    #    def __init__(self, players: List[Player], dealer: Dealer, input_handler: GameInputHandler, observer: GameObserver) -> None:
    def __init__(self) -> None:
        self.__players = []
        self.__dealer = Dealer(Deck())    
        
    def reset_game(self):    
        print("Shuffled deck")
        self.__dealer.reset_deck()
        for player in self.__players:
            player.reset_cards()
        
    def add_player(self, player : Player) -> Player :
        self.__players.append(player)
        
    def start_game(self) :
        # Reinicia o jogo
        self.reset_game()
        
        # Verifica se há pelo menos um jogador no jogo
        if len(self.__players) == 0 :
            print("*Insufficient number of players*")
            return
        
        print("*Game started, Welcome!*")
        # Inicia a rodada
        self.play_round()
        
    
    def play_round(self):
        round = Round(self.__players, self.__dealer) # cria o objeto Round
        round.play() # chama o método play() da classe Round para iniciar a rodada

