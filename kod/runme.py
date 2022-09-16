from get_data import Game

# 37 matcher under 21/22 

# match 6: 2022-02-23 sirius vetlanda
# match 30: 2021-11-25 sirius aik
# match 5: 2022-02-21 sirius vetlanda
# match 10: 2022-02-08 sirius edsbyn

filename = 'testtesthej'
g = Game('a', 'b')
g.collector_raw(filename)

g.clean_csv(filename)