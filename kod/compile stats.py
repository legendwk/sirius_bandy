import os
import general_functions as gf
import constants
from get_stats import Stats
from get_pp import PP
import pandas as pd


os.chdir(r"data\2022\clean")
list_of_games = os.listdir()
list_of_games.sort()
main_team = 'sirius'

number_of_games = 2 #len(number_of_games)

# read as Stats objects

all_stats = {ht: dict() for ht in list_of_games[: number_of_games]}

for i, ht in enumerate(list_of_games[: number_of_games]):
    s = Stats(ht)
    # save the stats in some manner
    all_stats[ht] = s.prints
    if i == number_of_games:
        break
        

print(pd.DataFrame.from_dict(all_stats))





'''
print(df)

        score possession  duels                                         shot types  ... scrimmages  shots on goal             before and after                  duel zones
sirius    2.0    0:16:01   21.0  {'fast': 5, 'retur': 1, 'utifrån': 4, 'central...  ...       18.0            5.0  {'sirius': 6, 'edsbyn': 12}                         NaN
edsbyn    2.0    0:21:52   15.0  {'fast': 6, 'retur': 2, 'dribbling': 1, 'utifr...  ...       12.0           10.0  {'sirius': 15, 'edsbyn': 3}                         NaN
z1        NaN        NaN    NaN                                                NaN  ...        NaN            NaN                          NaN  {'sirius': 2, 'edsbyn': 0}
z2        NaN        NaN    NaN                                                NaN  ...        NaN            NaN                          NaN  {'sirius': 3, 'edsbyn': 1}
z3        NaN        NaN    NaN                                                NaN  ...        NaN            NaN                          NaN  {'sirius': 1, 'edsbyn': 1}
z4        NaN        NaN    NaN                                                NaN  ...        NaN            NaN                          NaN  {'sirius': 3, 'edsbyn': 3}
z5        NaN        NaN    NaN                                                NaN  ...        NaN            NaN                          NaN  {'sirius': 4, 'edsbyn': 3}
z6        NaN        NaN    NaN                                                NaN  ...        NaN            NaN                          NaN  {'sirius': 5, 'edsbyn': 1}
z7        NaN        NaN    NaN                                                NaN  ...        NaN            NaN                          NaN  {'sirius': 1, 'edsbyn': 0}
z8        NaN        NaN    NaN                                                NaN  ...        NaN            NaN                          NaN  {'sirius': 2, 'edsbyn': 4}
z9        NaN        NaN    NaN                                                NaN  ...        NaN            NaN                          NaN  {'sirius': 0, 'edsbyn': 2}

[11 rows x 11 columns]

'''