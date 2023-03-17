#File Name: main.py
#Description: Sabbacc
#Date: 2021-01-05
#Author: William
# game based on: http://sabacc.sourceforge.net/rules

import pyCardDeck
from player import Player
import random as rand
import math

class SabbaccGame:
    def __init__(self,players,deck):
        self.deck= deck
        self.players = players
        self.participating_players = []
        self.scores = 0
        self.round_pot = 0
        self.sabbacc_pot = 0
        self.current_round_call = 0
        #self.blind = 10
          
    def introduction(self):
        print(f'''
Welcome to the Sabbacc Table.
Sabbacc is a gambling game played in Star Wars.
The goal of the game is to get a score of 23 or -23. Using combinations of of cards from the 76 Card deck.
This can be done by mathematically using the card combinations to reach the goal. OR by getting an "Idiots Array"
See the "Card combinations" under help for more information.
The game is similar to the earth game, Blackjack.
Players will be forced to play minimum 5 rounds as the first 4 rounds are for pot building (aka Gambling)
Players can buy into a round by placing a minimum amount of $$ into the pot. (this minimum increases over time)
If a with a hand outside of the constraints of the game (-23:23) bombs out and must pay the value of the main pot to the sabbacc pot.
Use the Sabbacc Help CMD for info on the rules / deck / or Cards
''')

    def play_sabbacc(self,initial_round_call):
        '''The main game sequence.'''
        print("The game is about to begin...\n")
        self.deal()
        self.current_round_call = initial_round_call
        self.betting_phase(self.current_round_call)
        self.players_turns()
        self.sabbacc_shift()
        #self.players play
        self.determine_winner()
        # Play another round? 

        
    def deal(self):
        '''Dealing 2 cards per player'''
        for n in range(2):
            for player in self.players:
                newcard = self.deck.draw()
                player.hand.append(newcard)
                print(f"Dealt the {newcard.name} card to {player.name}.")

    def find_round_winner(self):
        '''Determines the winner of the round.'''
        round_winners = []
        return round_winners

    def hit(self, player):
        '''Adds a card to the player's hand and prints the drawn card.'''
        drawn_card = self.deck.draw()
        player.hand.append(drawn_card)
        print(f"Drew the {drawn_card}.")
    

    def buy_in_phase(self):
        '''Initiates the pot building phase for those who want to bet money'''
        #This function works but will likely need to write a minimum bet before player buyins and player raises to ensure people dont just keep raising 1$
        player_buyins = []
        for player in self.players:
            initial_player_buyin = float(input(f"{player.name} Please enter the amount of money you wish to place into the Sabbacc pot for your initial buy-in:"))
            player_buyins.append(initial_player_buyin)
        minimum_round_bet = sum(player_buyins)/len(player_buyins)
        self.sabbacc_pot = minimum_round_bet*len(self.players)
        print(f"Each player's initial buy-in values were: {player_buyins}. Resulting in an average minimum buy-in of: {minimum_round_bet}. The total Sabbacc pot is now: {self.sabbacc_pot}")
        for player in self.players:
            player.bank_balance - minimum_round_bet 
        return minimum_round_bet

    def betting_phase(self,current_round_call):
        print(f"A new betting phase has begun, please make your bets...")
        for player in self.players:
            self.gambling_decision(player,current_round_call)
            print(f"The total Sabbacc pot is: {self.sabbacc_pot}\nThe total main pot is: {self.round_pot}\n")
        print(f"Checking to see if the bets are balanced. ")
        self.check_bet_balance(current_round_call)

    def increase_blind_bet():
        '''Increases the minimum raise/bet to accelerate gameplay'''
        #function not required but good update
        pass
    
    def determine_winner(self):
        '''Determine winner'''
        winners = []
        smallest_target_delta = 99
        for player in self.players:
            player.sum_hand()
            player_delta = player.get_target_delta()
            if player_delta < smallest_target_delta:
                winners=[player]
                smallest_target_delta = player_delta
            elif player_delta == smallest_target_delta:
                winners.append(player)

        if len(winners)>1:
            winners=self.tiebreaker(winners)
        
        winner = winners[0]

        winner.rounds_won += 1
        print(f"{winner.name} has won this round!")

    def check_burn_status(self, player):
        '''check if the player has burned
        Returns True if a player has burned and False if they are not Burned
        '''
        hand_value = player.sum_hand()
        if hand_value>23:
            print(f"Burned.")#pay $ into main pot
            return True
        print(f"Not burned") #pay $ into main pot
        return False
    
    def tiebreaker(self,tied_players):
        '''Tiebreaker game function. Conducts a 1v1 
       # war 1v1 (negative cards)
        '''
        num_tied_players = len(tied_players)
        winning_number = rand.randint(1,num_tied_players)
        print(f"Rolling dice with {num_tied_players} sides")
        return [tied_players[winning_number-1]]

        #each player tied draws 1 extra card
        #player with the best modified hand wins
        #players that bombout do not pay but also do not win. 
        #game rules says mainpot goes to the next player who didn't bomb out
    

    def gambling_decision(self,player,current_round_call):
        '''A function that provides the players with the corresponding gambling action. These actions are: All-in, Fold, Call, Raise'''
        if player.bank_balance < current_round_call:
            print(f"{player.name} you do not have the bank balance to call the round. You fold")
            self.players.remove(player)
            self.folded_players(player)
        else:
            valid_inputs = ["1","2","3"]
            player_choice = input(f"""
{player.name} Select an action by inputting the corresponding integer :
1. Fold
2. Call
3. Raise
            
Enter corresponding integer here: """).strip()

            #catch all
            while player_choice not in valid_inputs:
                player_choice = input("Invalid entry. Player must enter an integer from 1 to 3:\n1. Fold\n2. Call\n3. Raise\n").strip()
            #fold
            if player_choice == "1":
                #player.fold(self,player) a player doesnt need to fold if beyond this point only participating players is being used
                print(f"{player.name} has folded.")
            #call
            elif player_choice == "2":
                player.call(self.current_round_call,self)
                self.participating_players.append(player)
            #raise
            elif player_choice == "3":
                player.raise_the_stakes(self.current_round_call, self)
                self.participating_players.append(player)

    def check_bet_balance(self,current_round_call):
        '''A function that checks to see if all players meet the call amount. If they don't it prompts them to balance. Returns True when balanced'''
        flag = False
        while flag == False:
            for player in self.participating_players:
                if player.player_round_bet < self.current_round_call:
                    player_choice = input(f"{player.name}To play in this round you must increase your call by {self.current_round_call - player.player_round_bet}\nWould you like to:\n1. Fold \n2. Match Call\n").strip()
                    while player_choice not in ["1","2"]:
                        player_choice = input("Invalid entry. Player must enter an integers 1 (For fold) or 2 (to match call):\n1. Fold\n2. Match Call").strip()
                    if player_choice == "1":
                        player.fold(player)
                        flag = True
                    elif player_choice == "2":
                        player.match_call(self.current_round_call,self,player.player_round_bet)
                        self.participating_players.append(player)
                        flag = True
                else:
                    print(f"All bets are balanced.")
                    flag = True

    def sabbacc_shift(self):#prob need to pass the deck into the shift
        '''A function that rolls dice to see if a Sabbacc Shift Occurs Trade in Cards'''
        dice_1 = 2#random.randint(1,6)
        dice_2 = 2#random.randint(1,6)
        if dice_1 == dice_2:
            print(f"A Sabbacc Shift has ocurred. All cards not placed in the static zone will be replaced with cards from the deck.")
            for player in self.participating_players:
                for card in player.hand:
                    player.trade_into_deck(self.deck,card)
                player.remove_static_card
        else:
            print(f"A Sabbacc Shift has not ocurred, the cards in the static zone have returned to your hand.")

    def players_turns(self):
        '''A Function that initiates the player's turn. Each player can decide to draw a card. Trade a card or Stand.'''
        for player in self.participating_players:
            print(f"{player.name} your turn has begun.")
            player.make_card_static()
            player_choice = input(f"{player.name} your turn has begun. What would you like to do:\n1. Hit/Draw \n2. Trade a Card \n3. Stand\n").strip()
            while player_choice not in ["1","2","3"]:
                player_choice = input(f"Invalid Entry. {player.name} you must enter an integer that corresponds to one of the options. Integer's: 1, 2, 3 \nWhat would you like to do:\n1. Hit/Draw \n2. Trade a Card \n3. Stand").strip()
            if player_choice == "1":
                self.hit(player)
                self.check_player_status(player)
            if player_choice == "2": 
                card_traded = player.select_card_from_hand()
                player.trade_into_deck(card_traded)
                self.check_player_status(player)
            if player_choice == "3": 
                print(f"{player.name} you have decided to Stand.")
            print("Your turn is over")
