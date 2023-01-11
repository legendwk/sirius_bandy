from get_data import Game
from get_stats import Stats
from get_plot import Plot
import os
from get_pp import PP
import general_functions as gf
import pandas as pd
from compile_stats import CompileStats
import time

# kör den här typ hela tiden så slipper vi bråk 
gf.clean_up()

# mappar med csvfiler
season2223 = 'data\\compile\\säsong 2223'
regular_season2223 = 'data\\compile\\grundserie 2223'
all_games = 'data\\compile\\alla'
cup2223 = 'data\\compile\\cupen 2223'
all_45_min = 'data\\compile\\45 min'
outdoors = 'data\\compile\\utomhus'
indoors = 'data\\compile\\inomhus'
bad_ice = 'data\\compile\\dålig is'
playoff2122 = 'data\\compile\\slutspel 2122'
playoff2223 = 'data\\compile\\slutspel 2223'
custom = 'data\\compile\\custom'
rapport_inne = 'data\\compile\\rapport inomhus'
rapport_ute = 'data\\compile\\rapport utomhus'
rapport_bad_ice = 'data\\compile\\rapport dålig is'
rapport_good_ice = 'data\\compile\\rapport bra is'
rapport_all = 'data\\compile\\rapport all'
broberg = 'data\\compile\\broberg'


os.chdir('data\\2023\\clean')
filename = '20230107 IK Sirius - IFK Vänersborg halvlek 2 clean'
van2 = Stats(filename)

os.chdir('..\\..\\..')

cs_rapport = CompileStats(rapport_all)

os.chdir('powerpointer\\säsongsrapporter')
pp_broberg = PP(cs_rapport.returns_stats_obj())
pp_broberg.make_season_report('säsongsrapport höst 2022')

os.chdir('..\\matchrapporter')
pp_van2 = PP(van2)
pp_van2.make_game_report()


'''
# hämta data och gör presentation (avnänds typ live?)
filename = '20230110 Edsbyns IF - IK Sirius halvlek 2'
os.chdir(r"data\2023\raw")
teams = {'iks', 'ed'}


# samla data
#g = Game(teams)
#g.collector_raw(filename)
#g.clean_csv(filename)

# skapa statsobjekt
os.chdir(r"..\\clean")
eds = Stats('20230110 Edsbyns IF - IK Sirius halvlek 2 clean')

# gör presentation
os.chdir(r"..\..\..\powerpointer\matchrapporter")
pp = PP(eds)
pp.make_game_report()


'''