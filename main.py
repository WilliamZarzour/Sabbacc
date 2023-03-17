from player import Player
from sabbacc import SabbaccGame
from deck import *
import pyCardDeck

player_list = [
    Player("Chewbacca"),
    Player("Lando Calrissian"),
    Player("Han Solo")]

build_sabbacc_deck= SabbaccDeck()

sabbacc_deck = pyCardDeck.Deck(build_sabbacc_deck.cards,True,"Sabbacc Deck")

sabbacc_deck.shuffle()


game = SabbaccGame(player_list,sabbacc_deck)
game.introduction()
initial_round_call = game.buy_in_phase()
game.play_sabbacc(initial_round_call)


