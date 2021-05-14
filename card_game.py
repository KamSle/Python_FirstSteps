# New class called Card
# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
from random import shuffle 
class Card:
    
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"	
#print(Card("Hearts","2"))		


# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".  shuffle should return the shuffled deck.
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.
class Deck:
    def __init__(self):
        suits=['Hearts','Diamonds','Clubs','Spades']
        values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        # self.cards=[]
        # for suit in suits:
        #  for value in values:
        #   self.cards.append(Card(value,suit))
        self.cards=[Card(value,suit) for value in values for suit in suits]
        # print(self.cards)
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"  

    # def __iter__(self):                  write it to see how the for loop works at the end of the code
    #     return iter(self.cards)    

    def count(self):
        return len(self.cards)

    def _deal(self,number):
        count = self.count()
        m=min([count,number])
        if count == 0:
            raise ValueError('All cards have been dealt')
        card_rem=self.cards[-m:]
        self.cards=self.cards[:-m]
        return card_rem     

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number):
        return self._deal(number)    

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
            shuffle(self.cards)
            return self
        
d = Deck()	
# print(d.deal_card())
# print(d.deal_hand(3))	
# print(d.count())
# print(d._deal(3))
d.shuffle()
print(d.cards)
print(d.deal_card())
print(d.deal_hand(5))	
						
# for c in d:
#     print(c)
                        