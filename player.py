#File Name: player.py
#Description: file for player functions
#Date: 2021-01-05
#Author: William
# game based on: http://sabacc.sourceforge.net/rules



class Player:
    def __init__(self, name):
        self.hand = []
        self.hand_value = 0
        self.static_zone = []
        self.name = name
        self.bank_balance = 1000
        self.player_round_bet = 0
        self.rounds_won = 0
        
    def __str__(self):
        return self.name
    
    def bet_round_pot(self,game):
        '''Player makes, calls, or raises a bet'''
        player_bet = float(input(f"{self.name} How much would you like to bet on the round pot: ").strip())
        self.player_round_bet = player_bet
        game.round_pot += player_bet
    
    def bet_sabbacc_pot(self,game):
        '''Player makes, calls, or raises a bet'''
        player_bet = float(input(f"{self.name} How much would you place into the Sabbacc pot?: "))
        self.current_sabbacc_bet = player_bet
        game.sabbacc_pot += player_bet

    def call(self,current_round_call,game):
        player_bet = current_round_call
        game.round_pot += player_bet
        self.player_round_bet = player_bet

    def match_call(self,current_round_call,game,player_bet):
        call_diff = current_round_call-player_bet
        game.round_pot += call_diff
        player_bet = current_round_call
        self.player_round_bet = player_bet

    def raise_the_stakes(self,current_round_call, game):
        player_bet = float(input(f"Please enter the full raise amount:"))
        while player_bet <= current_round_call:
            player_bet = float(input(f"Invalid entry. Please enter the an amount larger than {current_round_call}:"))
        game.round_pot += player_bet 
        game.current_round_call = player_bet
        self.player_round_bet = player_bet

    def fold(self,game,player):
        if player in game.participating_players:
            game.participating_players.remove(player)
            print(f"{player.name} has folded the hand")
        else:
            print(f"{player.name} has folded the hand")

    def see_hand(self):
        '''creates a list of str that contain the names of cards in your hand'''
        list_of_card_names = [card.name for card in self.hand]
        print(f"These are the cards in {self.name}'s hand:{list_of_card_names}")
        return list_of_card_names
    
    def sum_hand(self):
        hand_value = sum(card.value for card in self.hand)
        self.hand_value = hand_value
        print(f"{self.name}'s hand value is {hand_value}")
        return hand_value
    
    def get_target_delta(self):
        hand_value_target = 23
        return hand_value_target - abs(self.sum_hand())
        
    def select_card_from_hand(self):
        '''A function that allows a player to select a single card from their hand'''
        list_of_card_names= self.see_hand()
        list_of_card_names = [card_name.lower() for card_name in list_of_card_names]
        selected_card_name = input(f"Please type the name of the card you wish to select: ").strip().lower()
        while selected_card_name not in list_of_card_names:
            selected_card_name = input("You have not made a valid selection. Please type the name of the card you wish to select: ").strip().lower()
        
        for card in self.hand:
            if card.name.strip().lower()==selected_card_name:
                print(f"You have selected {card.name} from your hand")
                break
        return card

    def make_card_static(self): 
        '''A function that allows a player to protect 1 card from being swapped (randomly changed) by placing it inside the static field'''
        player_choice = input("Do you want to place a card inside the static field? Type yes or no:\n").strip().lower()
        while player_choice != "yes" and player_choice != "no":
            player_choice = input("Invalid Entry. Do you want to place a card inside the static field? Type [yes] or [no]:\n").strip().lower()
        
        if player_choice == "no":
            print(f"{self.name} chose not to place any cards inside the static field")
        else:
            card_selection = self.select_card_from_hand()
            self.static_zone.append(card_selection)
    
    def remove_static_card(self):
        '''A function that removes 1 card from the static field. Allowing the card to be swapped during a sabbacc Shift'''
        self.static_zone = []
        print(f"Static Zone has been cleared.")

    def trade_into_deck(self,deck,card):
        '''A function that takes 1 card and trades it for a card in the deck'''
        index = self.hand.index(card)
        self.hand.remove(card)
        self.hand.insert(index,deck.draw_random())
    
    def check_bank_balance(self):
        print(f"{self.name} has a bank balance of {self.bank_balance}")



