from get_data import Game
from get_stats import Stats
from get_plot import Plot
import constants
import os
from get_pp import PP
import general_functions as gf
import pandas as pd
from compile_stats import CompileStats
import time
import timedelta 

os.chdir(r'C:\Users\viking.nilsson\VSCode\Python\sirius_bandy')

# kör den här typ hela tiden så slipper vi bråk 
# gf.clean_up()

# hämta data
os.chdir('data\\2025\\raw')

# skapa vår match
filename = '20251029 IK Sirius - Broberg halvlek 1'
teams = {'iks', 'vet'}
g = Game(teams)

# samla och rensa data
g.collector_raw(filename)
g.clean_csv(filename)


'''
os.chdir(r'data\2024\clean')
v1 = Stats('20240226 Vetlanda - Sirius halvlek 1 clean') 
# v2 = Stats('20240221 Vetlanda - Sirius halvlek 2 clean')

# v_hel = v1 + v2

# gör presentation
os.chdir(r"..\..\..\powerpointer\matchrapporter")

pp = PP(v1)
pp.make_game_report()

'''