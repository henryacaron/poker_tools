import image_manip
import sys
sys.path.insert(1, './holdem-calc')

from poker_analysis import analyze_hand
import svm_model

estimator = svm_model.fit()

old_num = 0
while(True):
    new_num = image_manip.num_cards()
    if(new_num == 0):
            print("Waiting")
    else: 
        cards = image_manip.find_cards(estimator)
        pot_size = int(input("Pot size? "))
        analyze_hand(cards, pot_size)
    out = input("Press enter to run")
    if out == "q" : break
    