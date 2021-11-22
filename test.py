from card import Card
from hand_strength import hand_strength
from itertools import combinations 
import statistics 

def print_hand(c):
    print("[", end = '')
    for i in c:
        print(i,  " ", end = '')
    print("]") 

    
def comm_cards():
    card1 = Card(3, "C")
    card2 = Card(14,"H")
    card3 = Card(4, "S")
    card4 = Card(5, "D")
    card5 = Card(9, "D")
    return [card1, card2, card3, card4, card5]
def my_cards():
    card1 = Card(14, "S")
    card2 = Card(14, "D")
    return [card1, card2]
def make_deck():
    ranks = list(range(2, 15))
    print(ranks)
    suits = ["S", "H", "C", "D"]
    deck = list()
    for i in ranks:
        for j in suits:
            deck.append(Card(i, j))
    return deck

def remove_card(deck, card):
    for i in deck:
        if card == i:
            deck.remove(i)
    return deck
    
if __name__ == "__main__":
    comm = comm_cards()
    deck = make_deck()
    my_cards = my_cards()
    better, worse, my_hand_strength, best = list(), list(), list(), list()

    for i in comm: remove_card(deck, i)
    for i in my_cards: remove_card(deck, i)
    
    if len(comm) == 4:
        comb = list(combinations(deck, 3))
        for i in deck:
            my_hand_strength, best = hand_strength(comm + my_cards + i)
        for i in comb:
            i = list(i)
            value, best = hand_strength(comm + i)
            for j in my_hand_strength:
                if value > j:
                    better.append([i, best])
                else: worse.append([i, best])
            
    # my_hand_strength, best = hand_strength(comm + my_cards)
    # print_hand(best)
    # comb = list(combinations(deck, 2)) 
    # better, worse = list(), list()
    
    # for i in comb:         
    #     i = list(i)
    #     # print_hand(comm + i)
    #     value, best = hand_strength(comm + i)
    #     if value > my_hand_strength:
    #         better.append([i, best])
    #     else: worse.append([i, best])
    
    # for i in worse:
    #     print_hand(i[0])
    #     print_hand(i[1])
    print(len(worse)/(len(better) + len(worse)))