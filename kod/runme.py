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
filename = '20220221 Vetlanda BK - IK Sirius halvlek 2'
os.chdir(r"data\2022\raw")
teams = {'sirius', 'vetlanda'}

g = Game(teams)
g.collector_raw(filename)
g.clean_csv(filename)

os.chdir(r"..\\clean")
vetlanda = Stats('20220221 Vetlanda BK - IK Sirius halvlek 2 clean', N=3)
os.chdir(r"..\..\..\powerpointer\matchrapporter") 
PP(vetlanda)
'''



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