from get_data import Game
from get_stats import Stats
import os
from get_pp import PP




# 37 matcher under 21/22 

# match 6: 2022-02-23 sirius vetlanda
# match 30: 2021-11-25 sirius aik
# match 5: 2022-02-21 sirius vetlanda
# match 10: 2022-02-08 sirius edsbyn
# match 31: 2021-11-21 IK Sirius - IFK Rättvik

filename = '20211121 sirius rättvik halvlek 1'

# collect data 
g = Game('sirius', 'rättvik')


# remember to change to data\2023 for current season!
os.chdir(r"data\2022\raw")
g.collector_raw(filename)
g.clean_csv(filename)


'''
# get stats
s = Stats(g.teams, filename)
s.populate_individual_stats()
s.populate_big_stats()


os.chdir(r"..\..\..\powerpointer") 
# make something nice looking 
pp = PP('test', s)
pp.make_pres()
'''