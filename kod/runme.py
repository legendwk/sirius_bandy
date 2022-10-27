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

# remeber to change directory to the correct season!
# collect data
# remember to change to data\2023 for current season!

filename = '20220930 Broberg Söderhamn IF - IK Sirius halvlek 2'
os.chdir(r"data\2023\clean")
broberg1 = Stats('20220930 Broberg Söderhamn IF - IK Sirius halvlek 1 clean')
broberg2 = Stats('20220930 Broberg Söderhamn IF - IK Sirius halvlek 2 clean')
os.chdir(r"..\..\..\powerpointer\matchrapporter") 
# make a powerpoint 
PP(broberg1)
PP(broberg1 + broberg2)


'''
os.chdir(r"data\2023\clean")
vsk1 = Stats('20221001 IK Sirius - Västerås SK halvlek 1 clean')
vsk2 = Stats('20221001 IK Sirius - Västerås SK halvlek 2 clean')
villa1 = Stats('20220930 IK Sirius - Villa Lidköping halvlek 1 clean')
villa2 = Stats('20220930 IK Sirius - Villa Lidköping halvlek 2 clean')
os.chdir(r"..\..\..\powerpointer\matchrapporter") 
# make a powerpoint 
PP(vsk1)
PP(villa1 + villa2)


os.chdir(r"data\2023\raw")

filename = '20220930 Broberg Söderhamn IF - IK Sirius halvlek 2'
teams = {'sirius', 'broberg'}

g = Game(teams)
g.collector_raw(filename)
g.clean_csv(filename)


'''