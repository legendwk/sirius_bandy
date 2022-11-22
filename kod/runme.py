from get_data import Game
from get_stats import Stats
from get_plot import Plot
import os
from get_pp import PP
import general_functions as gf
import pandas as pd
from compile_stats import CompileStats
import time
# 37 matcher under 21/22 

# vi kör den här typ hela tiden så slipper vi bråk 
gf.clean_up()

# gör presentationer
os.chdir(r"data\2023\clean")

vsk1 = Stats('20221119 IK Sirius - Västerås SK halvlek 1 clean')
vsk20 = Stats('20221119 IK Sirius - Västerås SK halvlek 2 clean')
vsk25 = Stats('20221119 IK Sirius - Västerås SK halvlek 2.5 clean')
vsk2 = vsk20 + vsk25
vsk3 = Stats('20221119 IK Sirius - Västerås SK halvlek 3 clean')

os.chdir(r"..\..\..\powerpointer\matchrapporter")

PP(vsk1)
PP(vsk2)
PP(vsk3)


'''
# hämta data och gör presentation (avnänds typ live?)
filename = '20221119 IK Sirius - Västerås SK halvlek 3'
os.chdir(r"data\2023\raw")
teams = {'sirius', 'vsk'}

g = Game(teams)
g.collector_raw(filename)
g.clean_csv(filename)
os.chdir(r"..\\clean")


os.chdir(r"..\..\..\powerpointer\matchrapporter")






'''