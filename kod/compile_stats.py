import os
import general_functions as gf
from get_stats import Stats
import numpy as np
from get_data import Game

class CompileStats:
    # constructor seems to take ~5 seconds with N = 20
    def __init__(self, path_to_games: str, main_team = 'sirius', N = 20) -> None:
        self.path = path_to_games
        self.main_team = main_team
        self.teams = {self.main_team, 'opponent'}
        self.fill_games(N)
        self.all_stats = dict()
        self.compile_all_stats()

    def compile_all_stats(self) -> None:
        '''fills self.all_stats'''
        self.all_stats['score'] = self.get_score()
        self.all_stats['possession'] = self.get_possession()
        self.all_stats['scrimmages'] = self.get_scrimmages()
        self.all_stats['lost balls'] = self.get_lost_balls()
        self.all_stats['shots on goal'] = self.get_shots_on_goal()
        self.all_stats['duel zones'] = self.get_duel_zones()
        self.all_stats['corners'] = self.get_corners()
        self.all_stats['shot attempts'] = self.get_shot_attempts()
        self.all_stats['40'] = self.get_40_list()
        self.all_stats['shot types'] = self.get_shot_types()
        return

    def return_team(self, team: str) -> str:
        '''returns main_team if team == main team, else opponent'''
        return team if team == self.main_team else 'opponent'

    def fill_games(self, N: int) -> None: 
        '''populates the self.games list with Stats objects of the last self.N games'''
        self.games = list()
        l = [f'{self.path}\\{x}' for x in sorted(os.listdir(self.path), reverse=True)[: N]]
        for game_link in l:
            self.games.append(Stats(game_link))
    
    def get_score(self) -> dict:
        '''returns the score dict of the games in self.games'''
        score_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['score']:
                score_dict[self.return_team(team)].append(game.prints['score'][team])
        return score_dict

    def get_shot_attempts(self) -> dict:
        '''returns the shot attempts dict of the games in self.games'''
        shot_attempts_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['shot types']:
                shot_attempts_dict[self.return_team(team)].append(sum(game.prints['shot types'][team].values()))
        return shot_attempts_dict

    def get_corners(self) -> dict:
        '''returns the corners dict of the games in self.games'''
        corners_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['corners']:
                corners_dict[self.return_team(team)].append(game.prints['corners'][team])
        return corners_dict

    def get_40_list(self) -> list:
        '''returns the 40 dict of the games in self.games'''
        fourty_list = list()
        for game in self.games:
            fourty_list.append(sum(game.prints['40']))
        return fourty_list

    def get_possession(self) -> dict:
        '''returns the possession dict of the games in self.games'''
        poss_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['possession']:
                poss_dict[self.return_team(team)].append(game.prints['possession'][team])
        return poss_dict

    def get_interceptions(self) -> dict:
        '''returns the interceptions dict of the games in self.games'''
        interceptions_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['interceptions']:
                interceptions_dict[self.return_team(team)].append(game.prints['interceptions'][team])
        return interceptions_dict
    
    def get_scrimmages(self) -> dict:
        '''returns the scrimmages (närkamper) dict of the games in self.games'''
        scrimmages_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['scrimmages']:
                scrimmages_dict[self.return_team(team)].append(game.prints['scrimmages'][team])
        return scrimmages_dict

    def get_lost_balls(self) -> dict:
        '''returns the lost balls dict of the games in self.games'''
        lost_balls_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['lost balls']:
                lost_balls_dict[self.return_team(team)].append(game.prints['lost balls'][team])
        return lost_balls_dict

    def get_shots_on_goal(self) -> dict:
        '''returns the shots on goal dict of the games in self.games'''
        sog_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['shots on goal']:
                sog_dict[self.return_team(team)].append(game.prints['shots on goal'][team])
        return sog_dict
    
    def get_duel_zones(self) -> dict:
        '''returns the duel zones dict of the games in self.games'''
        duel_zones_dict = {z: {t : list() for t in self.teams} for z in Game.zones} 
        for game in self.games:
            for zone in game.prints['duel zones']:
                for team in game.prints['duel zones'][zone]:
                    duel_zones_dict[zone][self.return_team(team)].append(game.prints['duel zones'][zone][team])
        return duel_zones_dict            

    def get_shot_types(self) -> dict:
        '''returns the shot types dict of the games in self.games'''
        shot_types_dict = {st: {t: list() for t in self.teams} for st in Game.events_and_their_subevents['skottyp']}
        for game in self.games:
            for team in game.prints['shot types']: 
                for st in Game.events_and_their_subevents['skottyp']: # fetching from here to include zeros
                    if st in game.prints['shot types'][team]:
                        shot_types_dict[st][self.return_team(team)].append(game.prints['shot types'][team][st])
                    else:
                        shot_types_dict[st][self.return_team(team)].append(0)
        return shot_types_dict
                
        