from get_data import Game
from get_stats import Stats
from get_shots import Shots
import os
from get_pp import PP




# 37 matcher under 21/22 

# match 6: 2022-02-23 sirius vetlanda
# match 30: 2021-11-25 sirius aik
# match 5: 2022-02-21 sirius vetlanda
# match 10: 2022-02-08 sirius edsbyn
# match 15: 2022-01-23 IK Sirius - IK Tellus
# match 11: 2022-02-04 IK Sirius - IFK Vänersborg


# collect data 
filename = '20220204 IK Sirius - IFK Vänersborg halvlek 2'
g = Game('sirius', 'vänersborg')
# remember to change to data\2023 for current season!
os.chdir(r"data\2022\raw")
g.collector_raw(filename)
g.clean_csv(filename)


'''
# get stats
s = Stats(g.teams, filename)
s.populate_individual_stats()
s.populate_big_stats()
print(s.stats_dict)

os.chdir(r"..\..\..\powerpointer") 
# make something nice looking 
pp = PP('test', s)
pp.make_pres()
'''