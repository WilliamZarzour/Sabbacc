#File Name: main.py
#Description: main game loop
#Date: 2021-01-05
#Author: William
# game based on: http://sabacc.sourceforge.net/rules

from player import Player
from sabbacc import SabbaccGame
from deck import *
import pyCardDeck

player_list = [
    Player("Chewbacca"),
    Player("Lando Calrissian"),
    Player("Han Solo")]

'''
num_of_players = int(input(f"How many players are playing?\n>"))

for n in range(0,num_of_players+1): 
    player_name = input(f"Enter Player {n}'s name: ").strip()
    player_list.append(Player("player_name"))'''


build_sabbacc_deck= SabbaccDeck()

sabbacc_deck = pyCardDeck.Deck(build_sabbacc_deck.cards,True,"Sabbacc Deck")

sabbacc_deck.shuffle()


game = SabbaccGame(player_list,sabbacc_deck)
game.introduction()
initial_round_call = game.buy_in_phase()
game.play_sabbacc(initial_round_call)
