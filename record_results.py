import time
import pandas as pd


time = time.time()
game_type = int(input("Game type: \n 1 - $3 Triple Up \n 2 - $7 Triple Up 3 - $5 Double Up \n 4 - Cash Game"))

if game_type == 4:
    buyin = int(input("Buyin?"))
    net = int(input("Amount taken out?"))
    profit = buyin - net
    output = pd.DataFrame([game_type, profit])
else: 
    place = int(input("place?"))
    output = pd.DataFrame([game_type, place])

with pd.ExcelWriter('ignition.xlsx',
                    mode='a') as writer:  
    output.to_excel(writer, sheet_name='Data')