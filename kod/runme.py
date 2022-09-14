from get_data import Game

# 37 matcher under 21/22 

# match 6: 2022-02-23 sirius vetlanda

filename = '20220223 sirius vetlanda halvlek 2'
clean = '20220223 sirius vetlanda halvlek 2 clean'
g = Game('sirius', 'vetlanda')
#g.collector_raw(filename)

g.clean_csv(filename, clean)