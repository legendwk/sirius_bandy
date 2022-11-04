from get_data import Game
from get_stats import Stats
from get_plot import Plot
import os
from get_pp import PP
import general_functions
import pandas as pd
# 37 matcher under 21/22 

# remeber to change directory to the correct season!
# remember to change to data\2023 for current season!


filename = '20220221 Vetlanda BK - IK Sirius'
os.chdir(r"data\2022\raw")
teams = {'sirius', 'vetlanda'}

#g = Game(teams)
#g.collector_raw(filename)
#g.clean_csv(filename)
os.chdir(r"..\\clean")
byn1 = Stats('20220225 Edsbyns IF - IK Sirius halvlek 1 clean')
byn2 = Stats('20220225 Edsbyns IF - IK Sirius halvlek 2 clean')
#vetlanda = Stats(filename + ' clean')
os.chdir(r"..\..\..\powerpointer\matchrapporter") 
#PP(vetlanda)
byn = byn1 + byn2
PP(byn)

'''
p = Plot(byn, transparent=False)

p.make_all_duels_locations_image()
p.make_duel_winners_per_locations_image()





os.chdir(r"data\2023\clean")
vsk1 = Stats('20221001 IK Sirius - Västerås SK halvlek 1 clean')
os.chdir(r"..\..\..\powerpointer\matchrapporter") 
# make a powerpoint 
PP(vsk1)


# hämta data och gör presentation (avnänds typ live?)
filename = '20221028 IFK Vänersborg - IK Sirius halvlek 1'
os.chdir(r"data\2023\raw")
teams = {'sirius', 'vänersborg'}

g = Game(teams)
g.collector_raw(filename)
g.clean_csv(filename)

os.chdir(r"..\\clean")
vnb1 = Stats('20221028 IFK Vänersborg - IK Sirius halvlek 1 clean')
#vnb2 = Stats('20221028 IFK Vänersborg - IK Sirius halvlek 2 clean')
os.chdir(r"..\..\..\powerpointer\matchrapporter") 
PP(vnb1)


'''

