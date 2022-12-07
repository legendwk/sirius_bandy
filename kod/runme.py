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
filename = '20221202 IK Sirius - Sandvikens AIK halvlek 2'
os.chdir(r"data\2023\raw")
teams = {'sirius', 'saik'}

g = Game(teams)
g.collector_raw(filename)
g.clean_csv(filename)


# skapa statsobjekt
os.chdir(r"..\\clean")
saik = Stats(filename + ' clean')


# gör presentation
os.chdir(r"..\..\..\powerpointer\matchrapporter")
PP(saik)


'''



os.chdir(r"..\..\..\powerpointer\matchrapporter")


vsk1 = Stats('20221119 IK Sirius - Västerås SK halvlek 1 clean')
for grabb in vsk1.prints:
    print(f'{grabb}: {vsk1.prints[grabb]}')


cs = CompileStats('data\\compile\\45 min')
for grabb in cs.all_stats:
    print(grabb)
    print(cs.all_stats[grabb])






'''