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
left = 'data\\compile\\left'
right = 'data\\compile\\right'

cs = CompileStats(regular_season2223)


after = cs.stats_summary['after long shots events']
print('offensivt lag: motståndare   ')
print(after['sirius']['opponent'])

print('defensivt lag: sirius')
print(after['opponent']['sirius'])

#print(gf.combine_dictionaries(after['sirius']['sirius'], after['opponent']['opponent']))

os.chdir('powerpointer\\säsongsrapporter')

rapport = PP(cs.returns_stats_obj())
rapport.make_season_report('säsongsrapport grundserie')

'''

cs_left = CompileStats(left)
cs_right = CompileStats(right)

os.chdir('powerpointer\\säsongsrapporter')

pp_right = PP(cs_right.returns_stats_obj())
pp_right.make_season_report('säsongsrapport stå höger')

pp_left = PP(cs_left.returns_stats_obj())
pp_left.make_season_report('säsongsrapport stå vänster')





os.chdir('..\\matchrapporter')
pp_van2 = PP(van2)
pp_van2.make_game_report()




cs = CompileStats(rapport_all)
res = {'sirius': {'sirius': 0, 'opp': 0}, 'opp': {'sirius': 0, 'opp': 0}}
si = cs.all_stats['goals']['sirius']
op = cs.all_stats['goals']['opponent']
x_si = cs.all_stats['possession']['sirius']
x_op = cs.all_stats['possession']['opponent']

print(len(si))
barrier = 0.55
print(barrier)
for i in range(len(si)):
    if gf.readable_to_sec(x_si[i]) /(gf.readable_to_sec(x_si[i]) + gf.readable_to_sec(x_op[i])) < barrier:
        if si[i] > op[i]:
            res['sirius']['sirius'] += 1
        elif op[i] > si[i]:
            res['sirius']['opp'] += 1
    elif gf.readable_to_sec(x_op[i]) /(gf.readable_to_sec(x_si[i]) + gf.readable_to_sec(x_op[i])) < barrier:
        if si[i] > op[i]:
            res['opp']['sirius'] += 1
        elif op[i] > si[i]:
            res['opp']['opp'] += 1
print(res)


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


# hämta data och gör presentation (avnänds typ live?)
filename = '20230131 IK Sirius - Vetlanda BK halvlek 2'
os.chdir(r"data\2023\raw")
teams = {'iks', 'vet'}

# samla data
#g = Game(teams)
#g.collector_raw(filename)
#g.clean_csv(filename)


# skapa statsobjekt
os.chdir(r"..\\clean")
vet = Stats(filename + ' clean')

# gör presentation
os.chdir(r"..\..\..\powerpointer\matchrapporter")
pp = PP(vet)
pp.make_game_report()

'''