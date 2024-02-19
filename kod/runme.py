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

os.chdir(r'C:/Users/viking.nilsson/VSCode/Python/sirius_bandy/data/compile/2024/vetlanda hemma')
v1 = Stats('Vetlanda hemma halvlek 1 första 15') 
v2 = Stats('Vetlanda hemma halvlek 2 första 15') 
v3 = Stats('Vetlanda hemma halvlek 1 15-30') 
v4 = Stats('Vetlanda hemma halvlek 2 15-30') 
v5 = Stats('Vetlanda hemma halvlek 1 30-45') 
v6 = Stats('Vetlanda hemma halvlek 2 30-45') 
v7 = Stats('Vetlanda hemma halvlek 1 15-45') 
v8 = Stats('Vetlanda hemma halvlek 2 15-45') 

os.chdir(r'C:/Users/viking.nilsson/VSCode/Python/sirius_bandy/powerpointer/matchrapporter')
pp = PP(v1)
pp.make_game_report()
pp = PP(v2)
pp.make_game_report()
pp = PP(v3)
pp.make_game_report()
pp = PP(v4)
pp.make_game_report()
pp = PP(v5)
pp.make_game_report()
pp = PP(v6)
pp.make_game_report()
pp = PP(v7)
pp.make_game_report()
pp = PP(v8)
pp.make_game_report()


'''
# hämta data
os.chdir('data\\2024\\raw')

# skapa vår match
# filename = '20240206 IFK Rättvik - IK Sirius halvlek 2'
# teams = {'iks', 'rät'}
# g = Game(teams)

# samla och rensa data
# g.collector_raw(filename)
# g.clean_csv(filename)

os.chdir(r"..\\clean")
# gf.control_time('20240206 IFK Rättvik - IK Sirius halvlek 2 clean')
# gf.control_time('20240113 Edsbyns IF - IK Sirius halvlek 2 clean')



# v1 = Stats('20240206 IFK Rättvik - IK Sirius halvlek 1 clean') 
# v2 = Stats('20240206 IFK Rättvik - IK Sirius halvlek 2 clean')

# v_hel = v1 + v2

# gör presentation
os.chdir(r"..\..\..\powerpointer\matchrapporter")

# pp = PP(v1)
# pp.make_game_report()

# pp = PP(v2)
# pp.make_game_report()

# pp = PP(v_hel)
# pp.make_game_report()


# mappar med csvfiler
# måste lägga till undermapp för att dessa ska funka 
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
del1 = 'data\\compile\\2024\\del 1'
del2 = 'data\\compile\\2024\\del 2'
spelare = 'data\\compile\\2024\\spelare'
uddamal = 'data\\compile\\2024\\jämna'
senastefem = 'data\\compile\\2024\\senaste fem'
senastefemejratt = 'data\\compile\\2024\\senaste fem ej rättvik'


# spelarrapporter
# cs = CompileStats(spelare)
# s = cs.returns_stats_obj()
# print(s.get_player_stats_dict('97'))
# os.chdir('powerpointer\\spelarrapporter')
# pp = PP(s)
# p = sorted((k for k in constants.players if k != 'placeholder'), key=lambda x: int(x))
# pp.make_player_report(players = p) 

# säsongsrapporter
d1 = CompileStats(senastefem)
d2 = CompileStats(senastefemejratt)
d1 = PP(d1.returns_stats_obj())
d2 = PP(d2.returns_stats_obj())


os.chdir('powerpointer\\säsongsrapporter')

d1.make_season_report('senaste fem')
d2.make_season_report('ej rättvik senaste fem')
# # s1.make_season_report('säsongsrapport grundserie 2024')


'''
# os.chdir('data\\2024\\clean')
# v2 = Stats('20231031 Västerås - Sirius halvlek 2 clean')

# print(v2.get_player_stats_dict('97'))

# gör presentation
# os.chdir(r"..\..\..\powerpointer\spelarrapporter")
