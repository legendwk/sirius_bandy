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


# mapparna
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

# skapa objekt
cs = CompileStats(custom)
s = cs.returns_stats_obj()

# säsongsrapport
os.chdir('powerpointer\\säsongsrapporter')
pp = PP(s)
pp.make_season_report()

'''
# hämta data och gör presentation (avnänds typ live?)
filename = '20221230 IK Sirius - IFK Motala halvlek 2'
os.chdir(r"data\2023\raw")
teams = {'iks', 'mot'}

# samla data
g = Game(teams)
g.collector_raw(filename)
g.clean_csv(filename)

# skapa statsobjekt
os.chdir(r"..\\clean")
gripen1 = Stats(filename + ' clean')

# gör presentation
os.chdir(r"..\..\..\powerpointer\matchrapporter")
pp = PP(gripen1)
pp.make_game_report()






print('compile stats: stats summary')
for grabb in cs.stats_summary:
    print(grabb)
    print(cs.stats_summary[grabb])

print('\n\n\ncompile stats: all_stats')
for grabb in cs.all_stats:
    print(grabb)
    print(cs.all_stats[grabb])



print('\n\n\nstats: prints')
for grabb in stats.prints:
    print(grabb)
    print(stats.prints[grabb])






os.chdir(r"..\..\..\powerpointer\matchrapporter")


vsk1 = Stats('20221119 IK Sirius - Västerås SK halvlek 1 clean')
for grabb in vsk1.prints:
    print(f'{grabb}: {vsk1.prints[grabb]}')


cs = CompileStats('data\\compile\\45 min')
for grabb in cs.all_stats:
    print(grabb)
    print(cs.all_stats[grabb])





# hämta data och gör presentation (avnänds typ live?)
filename = '20221213 Vetlanda BK - IK Sirius halvlek 2'
os.chdir(r"data\2023\raw")
teams = {'iks', 'vtl'}

g = Game(teams)
g.collector_raw(filename)
g.clean_csv(filename)



# skapa statsobjekt
os.chdir(r"..\\clean")
vtl1 = Stats(filename + ' clean')
#bollnas2 = Stats('20221209 IK Sirius - Bollnäs GIF halvlek 2 clean')


# gör presentation
os.chdir(r"..\..\..\powerpointer\matchrapporter")
PP(vtl1)
#PP(bollnas2)



'''