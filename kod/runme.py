from get_data import Game
from get_stats import Stats
import os
from get_pp import PP
import general_functions
import pandas as pd
# 37 matcher under 21/22 

# match 6: 2022-02-23 sirius vetlanda
# match 30: 2021-11-25 sirius aik
# match 5: 2022-02-21 sirius vetlanda
# match 10: 2022-02-08 sirius edsbyn
# match 15: 2022-01-23 IK Sirius - IK Tellus
# match 11: 2022-02-04 IK Sirius - IFK Vänersborg

# collect data 
# remeber to change to the correct season!

os.chdir(r"data\2023\clean")
vsk1 = Stats('20221001 IK Sirius - Västerås SK halvlek 1 clean')
vsk2 = Stats('20221001 IK Sirius - Västerås SK halvlek 2 clean')
villa1 = Stats('20220930 IK Sirius - Villa Lidköping halvlek 1 clean')
villa2 = Stats('20220930 IK Sirius - Villa Lidköping halvlek 2 clean')
os.chdir(r"..\..\..\powerpointer\matchrapporter") 
# make a powerpoint 
PP(villa1)
PP(villa1 + villa2)


'''
# collect data
filename = '20221001 IK Sirius - Västerås SK halvlek 2'
# remember to change to data\2023 for current season!
os.chdir(r"data\2023\raw")
g = Game('sirius', 'vsk')
g.collector_raw(filename)
g.clean_csv(filename)
'''