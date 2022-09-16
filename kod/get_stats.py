import pandas as pd 
import matplotlib.pyplot as plt
from get_data import Game


class Stats:

    # probably won't need any class variables

    # constructor
    def __init__(self, teams: set, filename: str) -> None:
        self.team_dict = {x: 0 for x in teams}
        self.df = Game.read_csv_as_df(filename)

    # methods

    def get_score(self) -> dict:
        '''returns the score of the df'''
        score_dict = self.team_dict.copy()
        for index, row in self.df.iterrows():
            if row['event'] == 'mål':
                score_dict[row['team']] = 1
        return score_dict

    def get_shots(self, only_on_goal = False) -> dict:
        '''returns the shot counter from the given df
            only_on_goal will only return shots on goal'''
        shots_dict = self.team_dict.copy()
        for index, row in self.df.iterrows():
            if row['event'] == 'skott':
                if only_on_goal:
                    if row['subevent'] == 'räddning':
                        shots_dict[row['team']] += 1
                else:
                    shots_dict[row['team']] += 1
            elif row['event'] == 'mål':
                shots_dict[row['team']] += 1
        return shots_dict
    
    def get_corners(self) -> dict:
        '''returns the number of corners'''
        corners_dict = self.team_dict.copy()
        for index, row in self.df.iterrows():
            if row['event'] == 'hörna':
                corners_dict[row['team']] = 1
        return corners_dict
