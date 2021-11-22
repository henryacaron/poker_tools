from random import randrange

class Card:

    def __init__(self, rank = randrange(2,14), suit = randrange(3)):
        if(rank > 14 or rank < 2): raise Exception("Invalid Card Rank")
        self.suits = ["S", "H", "C", "D"]
        self.rank  = rank
        if isinstance(suit, str): self.suit = self.suits.index(suit)
        else: self.suit = suit

        
    def Rank(self):
        return self.rank
    
    def Suit(self):
        return self.suit
    
    def __str__(self):
        ret = self.rank
        if self.rank == 14: ret = "A"
        if self.rank == 13: ret = "K"
        if self.rank == 12: ret = "Q"
        if self.rank == 11: ret = "J"
        if self.rank == 10: ret = "T"
        return f"{ret}{self.suits[self.suit]}"
        
    def toString(self):
        return 
        
    def __eq__(self, other):
        if self.rank == other.Rank() and self.suit == other.Suit():
            return True
        return False