from get_data import Game
from get_stats import Stats
import os
from get_pp import PP
import general_functions


# 37 matcher under 21/22 

# match 6: 2022-02-23 sirius vetlanda
# match 30: 2021-11-25 sirius aik
# match 5: 2022-02-21 sirius vetlanda
# match 10: 2022-02-08 sirius edsbyn
# match 15: 2022-01-23 IK Sirius - IK Tellus
# match 11: 2022-02-04 IK Sirius - IFK Vänersborg

# let's try adding objects
os.chdir(r"data\2023\clean")
teams = {'sirius', 'villa'}
s1 = Stats(teams, '20220930 IK Sirius - Villa Lidköping halvlek 1 clean.csv')
s2 = Stats(teams, '20220930 IK Sirius - Villa Lidköping halvlek 2 clean.csv')
os.chdir(r"..\..\..\txt") 
s1.write_stats()
s2.write_stats()
#print(s1.prints)
s = s1 + s2
#print(s.prints)


'''
os.chdir(r"data\2023\clean")
filename = '20220930 IK Sirius - Villa Lidköping halvlek 1 clean.csv'
teams = {'sirius', 'villa'}
s = Stats(teams, filename)
os.chdir(r"..\..\..\txt") 
s.write_stats()
print(s.prints)




g = Game('a', 'b')
# remember to change to data\2023 for current season!
os.chdir(r"data\2023\raw")
g.collector_raw(filename)
g.clean_csv(filename)



# get stats

filename = '20220930 IK Sirius - Villa Lidköping halvlek 1 clean.csv'
os.chdir(r"data\2023\clean")
s = Stats({'sirius', 'villa'}, filename)
s.populate_individual_stats()
s.populate_big_stats()
print(s.stats_dict)


# collect data 
filename = '20220930 IK Sirius - Villa Lidköping halvlek 2'
g = Game('sirius', 'villa')
# remember to change to data\2023 for current season!
os.chdir(r"data\2023\raw")
g.collector_raw(filename)
g.clean_csv(filename)


os.chdir(r"..\..\..\powerpointer") 
# make something nice looking 
pp = PP('test', s)
pp.make_pres()
'''