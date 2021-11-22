from poker import Range
from poker.hand import Combo

import holdem_calc
import holdem_functions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display import display, HTML
from pprint import pprint

def analyze_hand(cards, pot_size):
    hero_odds = []
    hero_range_odds = []
    
    # my hand = King of spades and Jack of clubs
    if len(cards) < 5:
        preflop_calc(cards)
        print("preflop")
        return
    else:
        hero_hand = Combo(cards[0]+ cards[1])
        print("My hand: ", hero_hand)
        
        board = cards[2:]
        print(board)
        villan_hand = None # no prior knowledge about the villan
        exact_calculation = True if len(board) > 3 else False #  calculates exactly by simulating the set of all possible hands
        verbose = True # returns odds of making a certain poker hand, e.g., quads, set, straight
        num_sims = 1 # ignored by exact_calculation = True
        read_from_file = False # we are not reading hands from file

        villan_range = Range('66+, T9s, J9s, JTs, A8+, Q9+, KJ+')
        # display((villan_range.to_ascii()))
        
        # pprint("#combo combinations:" + str(len(villan_range.combos)))
        
        items = [holdem_calc.calculate_odds_villan(board, exact_calculation, 
                            num_sims, read_from_file , 
                            hero_hand, villan_hand, 
                            verbose, print_elapsed_time = False) for villan_hand in villan_range.combos]

        odds = {}
        [odds.update({odd_type: np.mean([res[0][odd_type] for res in items if res])}) for odd_type in ["tie", "win", "lose"]]

        
        # print("My Odds")
        # for hand_ranking in holdem_functions.hand_rankings:
        #     print(hand_ranking +": " + str(np.mean([res[1][0][hand_ranking] for res in items if res])))

        # print("\nVillain's Odds")
        # for hand_ranking in holdem_functions.hand_rankings:
        #     print(hand_ranking +": " + str(np.mean([res[1][1][hand_ranking] for res in items if res])))
        print("\nPrice to call:", odds["win"] * 0.8 * pot_size, )
        pprint(odds)


# def his_code(cards):
    
def make_range(agg = "default", pos = 0):
    range = Range('77+, AT+, KJ+')

    return range
    

def preflop_calc(cards): return

if __name__ == "__main__":
    analyze_hand(["Ah", "Ac", "2d", "3c", "5s"], 800)