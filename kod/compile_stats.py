import os
import general_functions as gf
from get_stats import Stats


class CompileStats:
    # class variables
    # assumes we are standing in the 'sirius_bandy' folder
    current_season = r'data\2023\clean'
    last_season = r'data\2022\clean'

    # constructor seems to take ~5 seconds with N = 20
    def __init__(self, main_team = 'sirius', N = 20) -> None:
        self.main_team = main_team
        self.fill_games(N)

    def fill_games(self, N: int) -> None: 
        '''populates the self.games list with Stats objects of the last self.N games'''
        self.games = list()
        l = [CompileStats.current_season + '\\' + x for x in sorted(os.listdir(CompileStats.current_season), reverse=True)[: N]]
        if len(l) < N:
            l = l + [CompileStats.last_season + '\\' + x for x in sorted(os.listdir(CompileStats.last_season), reverse=True)[: N- len(l)]]
        for game_link in l:
            self.games.append(Stats(game_link))
        


