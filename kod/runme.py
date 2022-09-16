from get_data import Game

# 37 matcher under 21/22 

# match 6: 2022-02-23 sirius vetlanda
# match 30: 2021-11-25 sirius aik
# match 5: 2022-02-21 sirius vetlanda

filename = '20220221 sirius vetlanda halvlek 2'
clean = '20220221 sirius vetlanda halvlek 2 clean'
g = Game('sirius', 'vetlanda')
#g.collector_raw(filename)

g.clean_csv(filename, clean)