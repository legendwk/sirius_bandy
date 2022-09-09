from get_data import Game


filename = 'träningsmatch u21'
clean = 'träningsmatch u21 clean'
g = Game('blå', 'gul')
g.collector_raw(filename)

#g.clean_csv(filename, clean)

