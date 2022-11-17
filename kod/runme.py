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

# hämta data och gör presentation (avnänds typ live?)
filename = '20221115 Frillesås BK - IK Sirius halvlek 2'
os.chdir(r"data\2023\raw")
teams = {'sirius', 'frillesås'}

os.chdir(r"..\\clean")
frille1 = Stats('20221115 Frillesås BK - IK Sirius halvlek 1 clean', N=3)
frille2 = Stats('20221115 Frillesås BK - IK Sirius halvlek 2 clean', N=3)

os.chdir(r"..\..\..\powerpointer\matchrapporter") 
PP(frille1)
PP(frille2)
'''

# hämta data och gör presentation (avnänds typ live?)
filename = '20221115 Frillesås BK - IK Sirius halvlek 2'
os.chdir(r"data\2023\raw")
teams = {'sirius', 'frillesås'}

g = Game(teams)
g.collector_raw(filename)
g.clean_csv(filename)




'''