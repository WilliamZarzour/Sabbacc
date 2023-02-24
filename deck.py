import pyCardDeck


class SabbaccCard:
    '''<SabbaccCard> An object card.'''

    def __init__(self,suit,value,name):
        self.suit = suit
        self.value = value
        self.name = name
        
    def __str__(self):
        '''<string> representation of the card. helps pythonically'''
        #Return the name of the card + the ability.
        return f"the selected card is {self.name}"

    def __repr__(self):
        '''<string> representation of the card. helps pythonically'''
        #representation of the card
        return f"Card suit: {self.suit} Card value:{self.value} Card Name: {self.name}"

class SabbaccDeck:
    '''<Deck> An object composed of <SabbaccCard>'''

    def __init__(self):
        self.cards = []
        self.build_sabbacc_deck()

    def build_sabbacc_deck(self):
        '''Creates the 76 card deck'''
        suit_list = ["Sabers","Flasks","Coins","Staves"]
        for suit in suit_list:
            for value in range(1,12):
                self.cards.append(SabbaccCard(suit,value,f"{value} of {suit}"))

        for suit in suit_list:
            self.cards.append(SabbaccCard(suit,12,f"Commander of {suit}"))
            self.cards.append(SabbaccCard(suit,13,f"Mistress of {suit}")) 
            self.cards.append(SabbaccCard(suit,14,f"Master of {suit}")) 
            self.cards.append(SabbaccCard(suit,15,f"Ace of {suit}"))

        face_card_list = [
            
            SabbaccCard(None,-17,"The Star"),
            SabbaccCard(None,-17,"The Star"),
            
            SabbaccCard(None,-15,"The Evil One"),
            SabbaccCard(None,-15,"The Evil One"),
            
            SabbaccCard(None,-14,"Moderation"),
            SabbaccCard(None,-14,"Moderation"),
            
            SabbaccCard(None,-13,"Demise"),
            SabbaccCard(None,-13,"Demise"),
            
            SabbaccCard(None,-11,"Balance"),
            SabbaccCard(None,-11,"Balance"),
            
            SabbaccCard(None,-8,"Endurance"),
            SabbaccCard(None,-8,"Endurance"),
            
            SabbaccCard(None,-2,"Queen of Air and Darkness"),
            SabbaccCard(None,-2,"Queen of Air and Darkness"),
            
            SabbaccCard(None,0,"Idiot"),
            SabbaccCard(None,0,"Idiot"),
            ]
            
        for card in face_card_list:
            self.cards.append(card)
        