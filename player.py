class Player:
    def __init__(self, name):
        self.hand = []
        self.static_zone = []
        self.name = name
        self.bank_balance = 1000
        self.player_round_bet = 0
        
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
        print(f"These are the cards in your hand:{list_of_card_names}")
        return list_of_card_names
    
    def select_card_from_hand(self):
        '''A function that allows a player to select a single card from their hand'''
        
        list_of_cards_in_hand = self.see_hand()
        selected_card = input(f"Select a Card from your hand:").strip().lower()
        while selected_card not in list_of_cards_in_hand:
            selected_card = input(f"You have not made a valid selection. Please type the name of the card you wish to select: ").strip()#.lower()
        
        print(f"You have selected {selected_card} from your hand")
        return selected_card


    def make_card_static(self): #only works for 2 card hands need to loop through hand inside the print statement and if statements for multi sized hands
        '''A function that allows a player to protect 1 card from being swapped (randomly changed) by placing it inside the static field'''
        player_choice = input("Do you want to place a card inside the static field? Type yes or no:\n").strip().lower()
        while player_choice != "yes" or player_choice != "no":
            player_choice = input("Invalid Entry. Do you want to place a card inside the static field? Type [yes] or [no]:\n").strip().lower()
        
        if player_choice == "no":
            print(f"{self.name} chose not to place any cards inside the static field")
        else:
            card_selection = float(input(f"Which card? 1.{self.hand[0]} \n2. {self.hand[1]}\n Enter the corresponding integer: \n"))

            while player_choice != 1 or player_choice != 2:
                player_choice = input(f"Invalid Entry. Which card? 1.{self.hand[0]} \n2. {self.hand[1]}\n Numerically enter the corresponding integers 1 or 2: \n").strip()
            
            if card_selection == 1:
                self.static_zone.append(self.hand[0])

            if card_selection == 2:
                self.static_zone.append(self.hand[1])
    
    def remove_static_card(self):
        '''A function that removes 1 card from the static field. Allowing the card to be swapped during a sabbacc Shift'''
        for card in self.static_zone:
            self.hand.append(card)
            self.static_zone.remove(card)
        print("Static Zone has been cleared. Card has been returned to hand.")

    def trade_into_deck(self,deck,card):
        '''A function that takes 1 card and trades it for a card in the deck'''
        #self.hand.add_to_deck
        self.hand.remove(card)
        self.hand.append(deck.draw_random())
        pass
