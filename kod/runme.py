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


# kör den här typ hela tiden så slipper vi bråk 
gf.clean_up()


'''
# hämta data
os.chdir('data\\2024\\raw')

# # skapa vår match
# filename = '20231220 IK Sirius - Gripen Trollhättan halvlek 2.csv'
# teams = {'iks', 'gri'}
# g = Game(teams)

# # samla och rensa data
# # g.collector_raw(filename)
# g.clean_csv(filename)

os.chdir(r"..\\clean")
gf.control_time('20231230 IK Sirius - IFK Vänersborg halvlek 1 clean')
# gf.control_time('20231230 IK Sirius - IFK Vänersborg halvlek 2 clean')


v1 = Stats('20231230 IK Sirius - IFK Vänersborg halvlek 1 clean') 
v2 = Stats('20231230 IK Sirius - IFK Vänersborg halvlek 2 clean')

v_hel = v1 + v2

# gör presentation
os.chdir(r"..\..\..\powerpointer\matchrapporter")

pp = PP(v1)
pp.make_game_report()

pp = PP(v2)
pp.make_game_report()

pp = PP(v_hel)
pp.make_game_report()



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
left = 'data\\compile\\left'
right = 'data\\compile\\right'
villa = 'data\\compile\\villa'
saikvilla = 'data\\compile\saik villa'
halva1 = 'data\\compile\halva 1'
halva2 = 'data\\compile\halva 2'
grundserie2024 = 'data\\compile\\grundserie2324'

# v = CompileStats(left)
# h = CompileStats(right)
cs = CompileStats(grundserie2024)
s = cs.returns_stats_obj()
print(s.get_player_stats_dict('97'))
os.chdir('powerpointer\\spelarrapporter')
pp = PP(s)
p = sorted((k for k in constants.players if k != 'placeholder'), key=lambda x: int(x))
pp.make_player_report(players = p) 

# v1 = PP(v.returns_stats_obj())
# h1 = PP(h.returns_stats_obj())


# os.chdir('powerpointer\\säsongsrapporter')

# v1.make_season_report('säsongsrapport stå vänster')
# h1.make_season_report('säsongsrapport stå höger')
# s1.make_season_report('säsongsrapport grundserie 2024')



# os.chdir('data\\2024\\clean')
# v2 = Stats('20231031 Västerås - Sirius halvlek 2 clean')

# print(v2.get_player_stats_dict('97'))

# gör presentation
# os.chdir(r"..\..\..\powerpointer\spelarrapporter")
'''