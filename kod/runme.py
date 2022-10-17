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

os.chdir(r"data\2022\clean")
teams = {'sirius', 'vänersborg'}
s1 = Stats(teams, '20220204 IK Sirius - IFK Vänersborg halvlek 1 clean.csv')
s2 = Stats(teams, '20220204 IK Sirius - IFK Vänersborg halvlek 1 clean.csv')
os.chdir(r"..\..\..\txt") 
s = s1 + s2

os.chdir(r"..\powerpointer") 
# make something nice looking 
pp = PP(s)



'''
os.chdir(r"data\2023\clean")
teams = {'sirius', 'villa'}
s1 = Stats(teams, '20220930 IK Sirius - Villa Lidköping halvlek 1 clean.csv')
s2 = Stats(teams, '20220930 IK Sirius - Villa Lidköping halvlek 2 clean.csv')
os.chdir(r"..\..\..\txt") 
s = s1 + s2

os.chdir(r"..\powerpointer") 
# make something nice looking 
pp = PP(s1)



# collect data 
filename = '20220930 IK Sirius - Villa Lidköping halvlek 2'
g = Game('sirius', 'villa')
# remember to change to data\2023 for current season!
os.chdir(r"data\2023\raw")
g.collector_raw(filename)
g.clean_csv(filename)


'''