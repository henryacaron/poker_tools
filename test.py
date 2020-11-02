from card import Card
from hand_strength import hand_strength

if __name__ == "__main__":
    a = Card(5, "H")
    cards = [Card(5, "H"), Card(6, "D"), Card(7, "S"),Card(7, "C"), Card(2, "C"), Card(3, "H"),Card(4, "D")]
    hand_strength(cards)