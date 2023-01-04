import os
import general_functions as gf
from get_stats import Stats
import numpy as np
from get_data import Game

class CompileStats:
    def __init__(self, path_to_games: str, main_team = 'sirius', N = 1000) -> None:
        self.path = path_to_games
        self.main_team = main_team
        self.teams = {self.main_team, 'opponent'}
        self.fill_games(N)
        self.all_stats = dict()
        self.stats_summary = dict()
        self.compile_all_stats()
        self.summarize_stats()

    def compile_all_stats(self) -> None:
        '''fills self.all_stats'''
        #self.all_stats['score'] = self.get_score()
        self.all_stats['possession'] = self.get_possession()
        self.all_stats['scrimmages'] = self.get_scrimmages()
        self.all_stats['duels'] = self.get_duels()
        self.all_stats['interceptions'] = self.get_interceptions()
        self.all_stats['lost balls'] = self.get_lost_balls()
        self.all_stats['shots on goal'] = self.get_shots_on_goal()
        self.all_stats['duel zones'] = self.get_duel_zones()
        self.all_stats['corners'] = self.get_corners()
        self.all_stats['corner goal sides'] = self.get_corner_goal_sides()
        self.all_stats['shot attempts'] = self.get_shot_attempts()
        self.all_stats['40'] = self.get_40_list()
        self.all_stats['shot types'] = self.get_shot_types()
        self.all_stats['goal types'] = self.get_goal_types()
        self.all_stats['score'] = self.get_state_of_goal()
        self.all_stats['slot passes'] = self.get_slot_passes()
        self.all_stats['long passes'] = self.get_long_passes()
        self.all_stats['before and after'] = self.get_before_and_after()
        self.all_stats['shot origins'] = self.get_shot_origins()
        self.all_stats['penalties'] = self.get_penalties()
        return
    
    def summarize_stats(self) -> None:
        '''returns a dict of the summarized stats of the object'''
        #self.stats_summary['score'] = self.summarize_score() 
        self.stats_summary['possession'] = self.summarize_possession()
        self.stats_summary['scrimmages'] = self.summarize_scrimmages()
        self.stats_summary['duels'] = self.summarize_duels()
        self.stats_summary['interceptions'] = self.summarize_interceptions()
        self.stats_summary['lost balls'] = self.summarize_lost_balls()
        self.stats_summary['shots on goal'] = self.summarize_shots_on_goal()
        self.stats_summary['duel zones'] = self.summarize_duel_zones()
        self.stats_summary['corners'] = self.summarize_corners()
        self.stats_summary['corner goal sides'] = self.summarize_corner_goal_sides()
        self.stats_summary['shot attempts'] = self.summarize_shot_attempts()
        self.stats_summary['40'] = self.summarize_40()
        self.stats_summary['shot types'] = self.summarize_shot_types()
        self.stats_summary['goal types'] = self.summarize_goal_types()
        self.stats_summary['score'] = self.summarize_state_of_goal()
        self.stats_summary['slot passes'] = self.summarize_slot_passes()
        self.stats_summary['long passes'] = self.summarize_long_passes()
        self.stats_summary['before and after'] = self.summarize_before_and_after()
        self.stats_summary['shot origins'] = self.summarize_shot_origins()
        self.stats_summary['penalties'] = self.summarize_penalties()
        return 

    def returns_stats_obj(self) -> Stats:
        '''returns a Stats object filled with data from self.stats_summary'''
        stats = Stats(filename= f'summary of {len(self.games)} files', dummy= True, main_team= self.main_team)
        stats.teams = self.teams
        stats.prints = self.stats_summary
        stats.number_of_games = len(self.games)
        return stats

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
    
    def get_penalties(self) -> dict:
        '''returns the penalties dict of the games in self.games'''
        penalties_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['penalties']:
                penalties_dict[self.return_team(team)].append(game.prints['penalties'][team])
        return penalties_dict

    def get_shot_attempts(self) -> dict:
        '''returns the shot attempts dict of the games in self.games'''
        shot_attempts_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['shot types']:
                shot_attempts_dict[self.return_team(team)].append(sum(game.prints['shot types'][team].values()))
        return shot_attempts_dict

    def get_corners(self) -> dict:
        '''returns the corners dict of the games in self.games'''
        corners_dict = {team: {side: list() for side in Stats.corner_sides} for team in self.teams}
        for game in self.games:
            for team in game.prints['corners']:
                for side in game.prints['corners'][team]:
                    corners_dict[self.return_team(team)][side].append(game.prints['corners'][team][side])
        return corners_dict

    def get_corner_goal_sides(self) -> dict:
        '''returns the corner goal sides dict of the games in self.games'''
        corners_dict = {team: {side: list() for side in Stats.corner_sides} for team in self.teams}
        for game in self.games:
            for team in game.prints['corner goal sides']:
                for side in game.prints['corner goal sides'][team]:
                    corners_dict[self.return_team(team)][side].append(game.prints['corner goal sides'][team][side])
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

    def get_slot_passes(self) -> dict:
        '''returns the slot passes (passning - straffområde) dict of the games in self.games'''
        sp_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['slot passes']:
                sp_dict[self.return_team(team)].append(game.prints['slot passes'][team])
        return sp_dict

    def get_long_passes(self) -> dict:
        '''returns the long passes (passning - lång, farlig) dict of the games in self.games'''
        lp_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['long passes']:
                lp_dict[self.return_team(team)].append(game.prints['long passes'][team])
        return lp_dict


    def get_before_and_after(self) -> dict:
        '''returns the before and after dict of the games in self.games'''
        baf_dict = {team: {t: list() for t in self.teams} for team in self.teams}
        for game in self.games:
            for team in game.prints['before and after']:
                for t in game.prints['before and after'][team]:
                    baf_dict[self.return_team(team)][self.return_team(t)].append(game.prints['before and after'][team][t])
        return baf_dict

    def summarize_before_and_after(self) -> dict:
        '''returns a dict of the combined before and after dict for the games in self.games'''
        baf_dict = {team: {t: 0 for t in self.teams} for team in self.teams}
        for team in self.all_stats['before and after']:
            for t in self.all_stats['before and after'][team]:
                baf_dict[team][t] = sum(self.all_stats['before and after'][team][t])
        return baf_dict

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
        shot_types_dict = {t: {st: list() for st in Game.events_and_their_subevents['skottyp']} for t in self.teams}
        for game in self.games:
            for team in game.prints['shot types']: 
                for st in Game.events_and_their_subevents['skottyp']: # fetching from here to include zeros
                    if st in game.prints['shot types'][team]:
                        shot_types_dict[self.return_team(team)][st].append(game.prints['shot types'][team][st])
                    else:
                        shot_types_dict[self.return_team(team)][st].append(0)
        return shot_types_dict

    def get_goal_types(self) -> dict:
        '''returns the goal types dict of the games in self.games'''
        gt_dict = {t: {st: [0]*len(self.games) for st in Game.events_and_their_subevents['skottyp']} for t in self.teams}
        for i, game in enumerate(self.games):
            for goal in game.goals_info_list:
                gt_dict[self.return_team(goal['team'])][goal['shot type']][i] += 1
        return gt_dict

    def get_state_of_goal(self) -> dict:
        '''returns the state of play for each goal of the games in self.games'''
        state_dict = {t: {st: [0]*len(self.games) for st in Game.events_and_their_subevents['mål']} for t in self.teams}
        for i, game in enumerate(self.games):
            for goal in game.goals_info_list:
                state_dict[self.return_team(goal['team'])][goal['subevent']][i] += 1
        return state_dict

    def get_duels(self) -> dict:
        '''returns a dictionary of the duels of the games in self.games'''
        duels_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['duels']:
                duels_dict[self.return_team(team)].append(game.prints['duels'][team])
        return duels_dict

    def get_interceptions(self) -> dict:
        '''returns a dictionary of the interceptions of the games in self.games'''
        interceptions_dict = {team: list() for team in self.teams}
        for game in self.games:
            for team in game.prints['interceptions']:
                interceptions_dict[self.return_team(team)].append(game.prints['interceptions'][team])
        return interceptions_dict    

    def get_shot_origins(self) -> dict:
        '''returns a dictionary of the shot origins of the games in self.games'''
        so_dict = {team: {so: [0]*len(self.games) for so in Game.events} for team in self.teams}
        for i, game in enumerate(self.games):
            for team in game.prints['shot origins']:
                for so in game.prints['shot origins'][team]:
                    so_dict[self.return_team(team)][so][i] = game.prints['shot origins'][team][so]
        # remove all zero values
        return {team: {k:v for k,v in so_dict[team].items() if v != [0]*len(self.games)} for team in so_dict}
    
    def summarize_shot_origins(self) -> dict:
        '''returns a dict of the combined shot origins of the object'''
        so_dict = {team: {so: 0 for so in Game.events} for team in self.teams}
        for team in self.all_stats['shot origins']:
            for so in self.all_stats['shot origins'][team]:
                so_dict[team][so] = sum(self.all_stats['shot origins'][team][so])
        # remove all zero values
        return {team: {k:v for k,v in so_dict[team].items() if v != 0} for team in so_dict}

    def summarize_duels(self) -> dict:
        '''returns a dict of the combined duels of the object'''
        d_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['duels']:
            d_dict[team] = sum(self.all_stats['duels'][team]) 
        return d_dict
    
    def summarize_penalties(self) -> dict:
        '''returns a dict of the combined penalties of the object'''
        p_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['penalties']:
            p_dict[team] = sum(self.all_stats['penalties'][team]) 
        return p_dict

    def summarize_interceptions(self) -> dict:
        '''returns a dict of the combined interceptions of the object'''
        i_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['interceptions']:
            i_dict[team] = sum(self.all_stats['interceptions'][team]) 
        return i_dict

    def summarize_possession(self) -> dict:
        '''returns a dict of the combined possession of the object'''
        score_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['possession']:
            score_dict[team] = sum(gf.readable_to_sec(x) for x in self.all_stats['possession'][team]) 
            score_dict[team] = gf.sec_to_readable(score_dict[team])
        return score_dict
    
    def summarize_scrimmages(self) -> dict:
        '''returns a dict of the combined scrimmages (närkamper) of the object'''
        s_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['scrimmages']:
            s_dict[team] = sum(self.all_stats['scrimmages'][team]) 
        return s_dict

    def summarize_lost_balls(self) -> dict:
        '''returns a dict of the combined lost balls of the object'''
        lb_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['lost balls']:
            lb_dict[team] = sum(self.all_stats['lost balls'][team]) 
        return lb_dict
    
    def summarize_shots_on_goal(self) -> dict:
        '''returns a dict of the combined shots on goal of the object'''
        sog_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['shots on goal']:
            sog_dict[team] = sum(self.all_stats['shots on goal'][team]) 
        return sog_dict

    def summarize_slot_passes(self) -> dict:
        '''returns a dict of the combined slot (passning - staffområde) passes of the object'''
        sp_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['slot passes']:
            sp_dict[team] = sum(self.all_stats['slot passes'][team]) 
        return sp_dict

    def summarize_long_passes(self) -> dict:
        '''returns a dict of the combined long passes (passning - lång, farlig) of the object'''
        lp_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['long passes']:
            lp_dict[team] = sum(self.all_stats['long passes'][team]) 
        return lp_dict
    
    def summarize_corners(self) -> dict:
        '''returns a dict of the combined corners of the object'''
        c_dict = {team: {side: 0 for side in Stats.corner_sides} for team in self.teams}
        for team in self.all_stats['corners']:
            for side in self.all_stats['corners'][team]:
                c_dict[team][side] = sum(self.all_stats['corners'][team][side]) 
        return c_dict

    def summarize_corner_goal_sides(self) -> dict:
        '''returns a dict of the combined corner goal sides of the object'''
        c_dict = {team: {side: 0 for side in Stats.corner_sides} for team in self.teams}
        for team in self.all_stats['corner goal sides']:
            for side in self.all_stats['corner goal sides'][team]:
                c_dict[team][side] = sum(self.all_stats['corner goal sides'][team][side]) 
        return c_dict
    
    def summarize_40(self) -> dict:
        '''returns the number of 40s of the object'''
        return sum(self.all_stats['40'])
        
    def summarize_shot_attempts(self) -> dict:
        '''returns a dict of the combined shot attempts of the object'''
        sa_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['shot attempts']:
            sa_dict[team] = sum(self.all_stats['shot attempts'][team]) 
        return sa_dict
    
    def summarize_score(self) -> dict:
        '''returns a dict of the combined score of the object'''
        score_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['score']:
            score_dict[team] = sum([sum(g.values()) for g in self.all_stats['score'][team]])  
        return score_dict

    def summarize_state_of_goal(self) -> dict:
        '''returns a dict of the combined states of play for the goals of the object'''
        state_dict = {t: {st: 0 for st in Game.events_and_their_subevents['mål']} for t in self.teams} 
        for team in self.all_stats['score']:
            for state in self.all_stats['score'][team]:
                state_dict[team][state] = sum(self.all_stats['score'][team][state])
        return state_dict

    def summarize_shot_attempts(self) -> dict:
        '''returns a dict of the combined shot attempts of the object'''
        sa_dict = {team : 0 for team in self.teams}
        for team in self.all_stats['shot attempts']:
            sa_dict[team] = sum(self.all_stats['shot attempts'][team]) 
        return sa_dict
    
    def summarize_duel_zones(self) -> dict:
        '''returns a dict of the combined duel zones of the object'''
        dz_dict = {z: {t : 0 for t in self.teams} for z in Game.zones} 
        for zone in self.all_stats['duel zones']:
            for team in self.all_stats['duel zones'][zone]:
                dz_dict[zone][team] = sum(self.all_stats['duel zones'][zone][team])
        return dz_dict

    def summarize_shot_types(self) -> dict:
        '''returns a dict of the combined shot types of the object'''
        st_dict = {t: {st: 0 for st in Game.events_and_their_subevents['skottyp']} for t in self.teams} 
        for team in self.all_stats['shot types']:
            for st in self.all_stats['shot types'][team]:
                st_dict[team][st] = sum(self.all_stats['shot types'][team][st])
        return st_dict
        
    def summarize_goal_types(self) -> dict:
        '''returns a dict of the combined goal types of the object'''
        gt_dict = {t: {gt: 0 for gt in Game.events_and_their_subevents['skottyp']} for t in self.teams}
        for team in self.all_stats['goal types']:
            for gt in self.all_stats['goal types'][team]:
                gt_dict[team][gt] = sum(self.all_stats['goal types'][team][gt])
        return gt_dict