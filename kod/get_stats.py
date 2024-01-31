import pandas as pd 
from get_data import Game
import general_functions as gf
import constants
from bisect import bisect_left
import numpy as np


class Stats:
# class variables
    # used for possession data
    possession_gained = {'skott', 'frislag', 'närkamp', 'inslag', 'utkast', 'avslag', 
                        'friläge', 'boll', 'brytning', 'passning', '40'}    
    possession_lost = {'bolltapp', 'rensning', 'offside'}
    await_next = {'timeout', 'mål', 'stop', 'utvisning', 'hörna', 'straff'}#, 'skottyp'}
    # used for shot origins
    start_of_play = {'avslag', 'frislag', 'inslag', 'utkast', 'skott', 'hörna', 'straff', 'boll'} # varför hade jag inte boll? för att den kommer med för ofta????
    # used for zone specific data, coverts zones 180 degrees
    zone_change = {'z1':'z9', 'z2':'z8', 'z3': 'z7', 'z4':'z6', 'z5':'z5', 'z6':'z4', 'z7':'z3', 'z8':'z2', 'z9':'z1', '0': '0'}
    # used for corners
    corner_sides = {'right': ['z1', 'z9'], 'left': ['z3', 'z7']}
    corner_zone_to_name = {'z1': 'right', 'z9': 'right', 'z3': 'left', 'z7': 'left'}
    # used for possession after shot
    positive_events = {'mål', 'hörna', 'straff'}
# constructor
    def __init__(self, filename: str, dummy = False, main_team = 'iks', N = 3) -> None:
        '''makes and calculates the Stats object. 
        main_team is which team we highlight. N is how many parts the half is divided into for the per-part stats.
        Dummy is only used when we are creating a custom object for example by dunder add'''
        self.prints = dict()
        self.possession_list = list()
        self.goal_origins_list = list()
        self.main_team = main_team
        self.out = filename
        # mainly used for number of halves  
        self.number_of_games = 1
        # number of parts the game will be split into
        self.N = N
        # dummy is only used when creating a custom object such as when adding two ojects  
        if not dummy: 
            self.big_df = gf.read_csv_as_df(filename)
            self.teams = {team for team in self.big_df['team'].tolist() if team != '0'}
            # ensures that main_team always scores in z8
            self.flip_zones()

            self.df_dict = dict()
            self.compile_stats()
        return

# static methods
    def other_direction(zone: str) -> str:
        '''returns the zone in the other direction
            does not accept non-zone entry'''
        return Stats.zone_change[zone]
    
    def corner_names(zone: str) -> str:
        '''returns the corner side from zone name
            does not accept non-zone entry'''
        return Stats.corner_zone_to_name[zone]


# dunder add, for Stats() + Stats()
    def __add__(self, other) -> None:
        if not isinstance(other, Stats):
            return NotImplemented
        # new empty object
        obj = Stats(str(), dummy = True, main_team = self.main_team)
        obj.possession_list = self.possession_list + other.possession_list
        obj.goal_origins_list = self.goal_origins_list + other.goal_origins_list
        obj.goals_info_list = self.goals_info_list + other.goals_info_list
        obj.out = f'{self.out} och {other.out}'
        obj.teams = self.teams
        obj.number_of_games = self.number_of_games + other.number_of_games
        
        obj.prints['score'] = self.add_score(other)
        obj.prints['possession'] = self.add_possession(other)
        obj.prints['duels'] = self.add_duels(other)
        obj.prints['shot types'] = self.add_shottypes(other)
        obj.prints['shot origins'] = self.add_shot_origins(other)
        obj.prints['interceptions'] = self.add_interceptions(other)
        obj.prints['lost balls'] = self.add_lost_balls(other)
        obj.prints['scrimmages'] = self.add_scrimmages(other)
        obj.prints['before and after'] = self.add_before_and_after(other)
        obj.prints['shots on goal'] = self.add_sog(other)
        obj.prints['duel zones'] = self.add_duel_zones(other)
        obj.prints['freeshot zones'] = self.add_freeshot_zones(other)
        obj.prints['per time lists'] = self.add_per_time_lists(other)
        obj.prints['40'] = self.add_40_list(other)
        obj.prints['sustained attacks'] = self.add_sustained_attacks(other)
        obj.prints['corners'] = self.add_corners(other)
        obj.prints['corner goal sides'] = self.add_corner_goal_sides(other)
        obj.prints['slot passes'] = self.add_slot_passes(other)
        obj.prints['long passes'] = self.add_long_passes(other)
        obj.prints['penalties'] = self.add_penalties(other)
        obj.prints['goal types'] = self.add_goal_types(other)
        obj.prints['expected goals'] = self.add_expected_goals(other)
        obj.prints['expected goals list'] = self.add_expected_goals_lists(other)
        obj.prints['goals lists'] = self.add_goals_list(other)
        obj.prints['penalty shots'] = self.add_penalty_shots(other)
        obj.prints['duel zones per team'] = self.add_duel_zones_per_team(other)
        obj.prints['duel winners per zone and team'] = self.add_duel_winners_per_zone_and_team(other)
        
        return obj

# non-static methods
    def compile_stats(self) -> None:
        '''calls all methods needed to compile all the stats'''
        self.get_score_dict()
        self.get_possession_dict()
        self.get_duels_dict()
        self.get_shottypes_dict()
        self.get_shot_origins_dict()
        self.get_interceptions_dict()
        self.get_lost_balls_dict()
        self.get_scrimmages_dict()
        self.get_sog_dict()
        self.get_before_and_after_dict()
        self.get_duel_zones_dict()
        self.get_freeshot_zones_dict()
        self.make_per_time_lists()
        self.make_40_list()
        self.make_sustained_attacks()
        self.get_corners_dict()
        self.get_corner_goal_sides()
        self.get_slot_passes_dict()
        self.get_long_passes_dict()
        self.get_penalties_dict()
        self.get_goal_types()
        self.get_expected_goals()
        self.get_penalty_shots_dict()
        self.get_expected_goals_lists()
        self.get_goals_lists()
        self.get_duel_zones_per_team()
        self.get_duel_winners_per_zone_and_team()

        # gör något åt detta, det ser förjävligt ut 
        self.goal_origins_list = self.get_goal_origins_list()
        self.goals_info_list = self.get_goals_info_list()

    def team_attacks_up(self, team: str) -> bool:
        '''does team score in z8? 
            None if team does not play'''
        if team not in self.teams:
            return None
        attacking_zone = {t: {'up': 0, 'down': 0} for t in self.teams}
        up = {'z7', 'z8', 'z9'}
        down = {'z1', 'z2', 'z3'}
        events = self.big_df.loc[self.big_df['event'].isin(['hörna', 'mål', 'skott'])]
        for index, row in events.iterrows():
            if row['zone'] in up:
                attacking_zone[row['team']]['up'] += 1
            elif row['zone'] in down:
                attacking_zone[row['team']]['down'] += 1
        # does team attack up and opposite down?
        return max(attacking_zone[team], key=attacking_zone[team].get) == 'up' and max(attacking_zone[self.opposite_team(team)], key=attacking_zone[self.opposite_team(team)].get) == 'down'
    
    def get_player_stats_dict(self, player: str) -> dict:
        '''calculates a dictionary of the player in question's stats'''
        player_df = self.big_df.loc[self.big_df['player'] == int(player)]
        stats_dict = dict()
        stats_dict['mål'] = len(player_df.loc[player_df['event'] == 'mål'])
        stats_dict['skott'] = len(player_df.loc[player_df['event'] == 'skottyp'])
        stats_dict['målformer'] = player_df.loc[player_df['event'] == 'mål', 'subevent'].value_counts().to_dict()
        stats_dict['skottyp'] = player_df.loc[player_df['event'] == 'skottyp', 'subevent'].value_counts().to_dict()
        stats_dict['passning'] = player_df.loc[player_df['event'] == 'passning', 'subevent'].value_counts().to_dict()
        stats_dict['hörna'] = len(player_df.loc[player_df['event'] == 'hörna'])

        # skottyper för varje mål
        goal_indices = player_df[player_df['event'] == 'mål'].index
        next_indices = goal_indices + 1
        stats_dict['målskottyper'] = player_df.loc[next_indices, 'subevent'].value_counts().to_dict()

        stats_dict['xg'] = sum([constants.expected_goals[st] * stats_dict['skottyp'][st] for st in stats_dict['skottyp']])
        return stats_dict

    
    def flip_zones(self) -> None:
        '''ensures that main_team scores into z8, if not calls other_direction on all zones so it does'''
        if not self.team_attacks_up(self.main_team):
            for index, row in self.big_df.iterrows():
                try:
                    self.big_df.at[index, 'zone'] = Stats.other_direction(self.big_df.at[index, 'zone'])
                except:
                    print(f'fel på rad {index}, \n{row}')
    
    def make_per_time_lists(self) -> None:
        '''populates the prints["per time lists"]'''
        self.prints['per time lists'] = dict()
        self.prints['per time lists']['duels'] = self.get_per_time_list(self.get_duels_df())
        self.prints['per time lists']['shots'] = self.get_per_time_list(self.get_shots_df())
        self.prints['per time lists']['goals'] = self.get_per_time_list(self.get_score_df())
        self.prints['per time lists']['possession'] = self.get_possession_per_time_list()
        return 

    def add_per_time_lists(self, other) -> dict:
        '''returns a dict containing the added per time lists'''
        per_time_dict = dict()
        for event_type in self.prints['per time lists']:
            per_time_dict[event_type] = self.prints['per time lists'][event_type] + other.prints['per time lists'][event_type]
        return per_time_dict
    
    def add_sustained_attacks(self, other):
        '''handles the addition of the sustained attacks'''
        sa_dict = {team: list() for team in self.teams}
        for team in sa_dict:
            sa_dict[team] = self.prints['sustained attacks'][team] + other.prints['sustained attacks'][team]
        return sa_dict

    def make_sustained_attacks(self, min_length = 60, disruption_length = 10) -> dict:
        ''''returns a dict with a list of each game minute, 
        if a team had ball possession for longer than min_length starting that minute the list index is the possession time, else 0
        a possession is if a team has the ball, if it loses it wins back possession within disruption_length, and the other team does not get a stoppage in play'''
        if 'sustained attacks' not in self.prints:
            sustained_attacks_dict = {team : [0 for i in range(gf.readable_to_sec(self.possession_list[-1][1])//60 + 1)] for team in self.teams}
            i = 0 
            while i < len(self.possession_list) - 1:
                current_team, current_time = self.possession_list[i]
                attack_time = 0 
                for j in range(i, len(self.possession_list)):
                    following_team, following_time  = self.possession_list[j]
                    # team has the ball
                    if following_team == current_team:
                        attack_time += gf.readable_to_sec(self.possession_list[j+1][1])-gf.readable_to_sec(following_time)
                    # other team has the ball
                    elif following_team == self.opposite_team(current_team):
                        # they have the ball long enough or get a break in play
                        if gf.readable_to_sec(self.possession_list[j+1][1])-gf.readable_to_sec(following_time) > disruption_length or self.possession_list[j+1][0] == None:
                            break
                    else:
                        pass
                if attack_time >= min_length:
                    sustained_attacks_dict[current_team][gf.readable_to_sec(current_time)//60] = attack_time
                i = j
                self.prints['sustained attacks'] = sustained_attacks_dict
            return self.prints['sustained attacks']
    
    def get_expected_goals(self) -> dict:
        '''calculates the XG for both teams and places it in prints'''
        if 'expected goals' not in self.prints:
            xg_dict = {team : sum([constants.expected_goals[st] * self.prints['shot types'][team][st] for st in self.prints['shot types'][team]]) for team in self.teams}
            for team in xg_dict:
                xg_dict[team] = xg_dict[team] - self.get_penalty_shots_dict()[team] * constants.expected_goals['fast'] + self.get_penalty_shots_dict()[team] * constants.expected_goals['straff']
            self.prints['expected goals'] = xg_dict
        return self.prints['expected goals']

    def get_expected_goals_lists(self) -> dict:
        '''calculates the expected goals change over time'''
        if 'expected goals list' not in self.prints:
            xgl_dict = {'x': [0], self.main_team: [0], self.opposite_team(self.main_team): [0]}
            st_df = self.get_shottypes_df()
            for index, row in st_df.iterrows():
                xgl_dict['x'].append(gf.readable_to_sec(row['time']))
                delta_xg = constants.expected_goals[row['subevent']]
                # specialfall eftersom straff har skottyp fast, vi skriver över osv
                if row['subevent'] == 'fast' and index > 2: # se till att vi inte råkar hamna i bråk med index
                    if self.big_df.loc[index - 2]['event'] == 'straff' or self.big_df.loc[index - 3]['event'] == 'straff':
                        delta_xg = constants.expected_goals['straff']
                shooting_team_xg = xgl_dict[row['team']][-1] + delta_xg
                xgl_dict[row['team']].append(shooting_team_xg)
                xgl_dict[self.opposite_team(row['team'])].append(xgl_dict[self.opposite_team(row['team'])][-1])
            self.prints['expected goals list'] = xgl_dict
        return self.prints['expected goals list']
    
    def get_goals_lists(self) -> dict:
        '''calculates the scored goals lists that are used with expected goals lists'''
        if 'goals lists' not in self.prints:
            g_df = {self.main_team: [0], self.opposite_team(self.main_team): [0]}
            st_df = self.get_shottypes_df()
            for index, row in st_df.iterrows():
                goal_scored = self.big_df.loc[index - 1]['event'] == 'mål'
                shooting_team_goals = g_df[row['team']][-1] + int(goal_scored)
                g_df[row['team']].append(shooting_team_goals)
                g_df[self.opposite_team(row['team'])].append(g_df[self.opposite_team(row['team'])][-1])
            self.prints['goals lists'] = g_df
        return self.prints['goals lists']

    def add_expected_goals_lists(self, other) -> dict:
        '''handels the addition of the expected goals lists'''
        xgl_dict = dict()
        for list_type in self.prints['expected goals list']:
            max_value = self.prints['expected goals list'][list_type][-1]
            second_list = [i + max_value for i in other.prints['expected goals list'][list_type]]
            xgl_dict[list_type] = self.prints['expected goals list'][list_type] + second_list
        return xgl_dict
    
    def add_goals_list(self, other) -> dict:
        '''handels the addition of the goals lists'''
        xgl_dict = dict()
        for list_type in self.prints['goals lists']:
            max_value = self.prints['goals lists'][list_type][-1]
            second_list = [i + max_value for i in other.prints['goals lists'][list_type]]
            xgl_dict[list_type] = self.prints['goals lists'][list_type] + second_list
        return xgl_dict

    def add_expected_goals(self, other) -> dict:
        '''handels the addition of the expected goals'''
        xg_dict = {}
        for team in self.prints['expected goals']:
            xg_dict[team] = self.prints['expected goals'][team] + other.prints['expected goals'][team]
        return xg_dict

    def make_40_list(self) -> list:
        '''makes the list of 40 situations for main_team''' 
        if '40' not in self.prints:
            fourty_list = [0 * i for i in range(gf.readable_to_sec(self.big_df.iloc[-1]['time']) // 60 + 1)]
            df_40 = self.get_40_df()
            for index, row in df_40.iterrows():
                if row['team'] == self.main_team:
                    fourty_list[gf.readable_to_sec(row['time']) // 60] += 1
            self.prints['40'] = fourty_list
        return self.prints['40']
    
    def add_40_list(self, other) -> list:
        '''handels the addition of the 40 lists'''
        return self.prints['40'] + other.prints['40']

    def add_sustained_attack(self, other) -> dict:
        '''returns a dict contianind the added sustained attack dicts'''
        d = {team : list() for team in self.teams}
        for team in self.prints['sustained attack']:
            d[team] = self.prints['sustained attack'][team] + other.prints['sustained attack'][team] 
        return d

    def get_possession_per_time_list(self) -> list:
        '''returns the possession per time list'''
        parts = [gf.readable_to_sec(self.big_df.iloc[-1]['time'])/self.N * i for i in range(self.N+1)][1:]
        per_time_list = [{team: 0 for team in self.teams} for n in range(self.N)]
        current_part = 0
        for i in range(len(self.possession_list) -1):
            team, time = self.possession_list[i]
            if team in self.teams:
                next_time = self.possession_list[i+1][1]
                # we are still within our part, only including the equals for edge case last index.
                if gf.readable_to_sec(next_time) <= parts[current_part]:
                    per_time_list[current_part][team] += gf.readable_to_sec(next_time) - gf.readable_to_sec(time)
                # we are entering the next part
                else:
                    # handling of the possession within this part
                    per_time_list[current_part][team] += parts[current_part] - gf.readable_to_sec(time)
                    per_time_list[current_part + 1][team] += gf.readable_to_sec(next_time) - parts[current_part]
                    current_part += 1
        for i, part in enumerate(per_time_list):
            for team in part:
                part[team] = gf.sec_to_readable(per_time_list[i][team])
        return per_time_list
        
    def get_per_time_list(self, df: pd.core.frame.DataFrame) -> list:
        '''returns a list of the occurrence of the events in the df'''
        times = [gf.readable_to_sec(self.big_df.iloc[-1]['time'])/self.N * i for i in range(self.N+1)]
        limits = [(times[i], times[i+1]) for i in range(self.N)]
        per_time_list = [{team: 0 for team in self.teams} for n in range(self.N)]
        for index, row in df.iterrows():
            for i, span in enumerate(limits):
                if gf.readable_to_sec(row['time']) > span[0] and gf.readable_to_sec(row['time']) <= span[1]:
                    per_time_list[i][row['team']] += 1
        return per_time_list

    def get_duel_zones_dict(self) -> dict:
        '''returns a dictionary of where the duels happened, and who won them'''
        if 'duel zones' not in self.prints:
            duel_zones = {'z' + str(i): {team: 0 for team in self.teams} for i in range(1, 10)}
            duels_df = self.get_duels_df()
            for index, row in duels_df.iterrows():
                if row['zone'] != '0':
                    duel_zones[row['zone']][row['team']] += 1
            self.prints['duel zones'] = duel_zones
        return self.prints['duel zones']

    def get_freeshot_zones_dict(self) -> dict:
        '''returns a dictionary of where the freeshots (frislag) happened, and by whom'''
        if 'freeshot zones' not in self.prints:
            freeshot_zones = {'z' + str(i): {team: 0 for team in self.teams} for i in range(1, 10)}
            freeshots_df = self.get_freeshots_df()
            for index, row in freeshots_df.iterrows():
                if row['zone'] != '0':
                    freeshot_zones[row['zone']][row['team']] += 1
            self.prints['freeshot zones'] = freeshot_zones
        return self.prints['freeshot zones']

    def get_goal_types(self) -> dict:
        '''returns the goal types dict of the object and populates prints'''
        if 'goal types' not in self.prints:
            gt_dict = {t: {st: 0 for st in Game.events_and_their_subevents['skottyp']} for t in self.teams}
            for goal in self.get_goals_info_list():
                gt_dict[goal['team']][goal['shot type']] += 1
        self.prints['goal types'] = gt_dict
        return self.prints['goal types']

    def add_goal_types(self, other) -> dict:
        '''returns the goal types for the added objects'''
        return gf.combine_dictionaries(self.prints['goal types'], other.prints['goal types'])

    def add_duel_zones(self, other) -> dict:
        '''returns the duel zones of the added objects'''
        return_dict = {'z' + str(i): {team: 0 for team in self.teams} for i in range(1, 10)}
        for zone in self.prints['duel zones']:
            for team in self.prints['duel zones'][zone]:
                return_dict[zone][team] = self.prints['duel zones'][zone][team] + other.prints['duel zones'][zone][team]
        return return_dict

    def add_freeshot_zones(self, other) -> dict:
        '''returns the freeshot zones of the added objects'''
        return_dict = {'z' + str(i): {team: 0 for team in self.teams} for i in range(1, 10)}
        for zone in self.prints['freeshot zones']:
            for team in self.prints['freeshot zones'][zone]:
                return_dict[zone][team] = self.prints['freeshot zones'][zone][team] + other.prints['freeshot zones'][zone][team]
        return return_dict

    def get_score_dict(self) -> dict:
        '''returns a dictionary of the score types, get raw score by sum(d[team].values())
            if need be it fills self.prints'''
        if 'score' not in self.prints:
            score_df = self.get_score_df()
            subevents = score_df["subevent"].unique()
            score_dict = {team: {subevent: 0 for subevent in subevents} for team in self.teams}
            for index, row in score_df.iterrows():
                score_dict[row['team']][row['subevent']] += 1
            self.prints['score'] = score_dict
        return self.prints['score']

    def add_score(self, other) -> dict:
        '''returns the score of the added objects
            expects type to already have been checked'''
        return gf.combine_dictionaries(self.prints['score'], other.prints['score'])
        
    def get_before_and_after_dict(self) -> dict:
        '''returns a dictionary of the before and after possession from each duel
            if not already done, it'll fill self.prints'''
        if 'before and after' not in self.prints:
            duels_df = self.get_duels_df()
            before_after_dict = {team : {t : 0 for t in self.teams} for team in self.teams}   
            #team_list = [x[0] for x in self.possession_list]
            time_list = [x[1] for x in self.possession_list]
            for index, row in duels_df.iterrows():
                # binary search is O(logn)
                i = bisect_left(time_list, row['time'])
                # we find a possession change from duel
                if time_list[i] == row['time']:
                    # other team used to have possession, now we do
                    before_after_dict[self.opposite_team(row['team'])][row['team']] += 1
                # the duel didn't result in possession change
                else:
                    before_after_dict[row['team']][row['team']] += 1
            self.prints['before and after'] = before_after_dict
        return self.prints['before and after']
    
    def get_duel_zones_per_team(self) -> dict:
        '''returns a dictionary of the zones of all duels based on each team's possession before 
            if not already done, it'll fill self.prints'''
        if 'duel zones per team' not in self.prints:
            duels_df = self.get_duels_df()
            duel_zones = {team : {z: 0 for z in Game.zones} for team in self.teams}   
            time_list = [x[1] for x in self.possession_list]
            for index, row in duels_df.iterrows():
                if row['zone'] != '0':
                    # binary search is O(logn)
                    i = bisect_left(time_list, row['time'])
                    # we find a possession change from duel
                    if time_list[i] == row['time']:
                        # other team used to have possession, now we do
                        duel_zones[self.opposite_team(row['team'])][row['zone']] += 1
                    # the duel didn't result in possession change
                    else:
                        duel_zones[row['team']][row['zone']] += 1
            self.prints['duel zones per team'] = duel_zones
        return self.prints['duel zones per team']
    
    def get_duel_winners_per_zone_and_team(self) -> dict:
        '''returns a dictionary of the winner in each zone based on each team's possession before 
            if not already done, it'll fill self.prints
            dictionary of format d[team_before][zone][team_after]'''
        if 'duel winners per zone and team' not in self.prints:
            duels_df = self.get_duels_df()
            duel_zones = {team :  {z: {t: 0 for t in self.teams} for z in Game.zones} for team in self.teams}
            time_list = [x[1] for x in self.possession_list]
            for index, row in duels_df.iterrows():
                if row['zone'] != '0':
                    # binary search is O(logn)
                    i = bisect_left(time_list, row['time'])
                    # we find a possession change from duel
                    if time_list[i] == row['time']:
                        # other team used to have possession, now we do
                        duel_zones[self.opposite_team(row['team'])][row['zone']][row['team']] += 1
                    # the duel didn't result in possession change
                    else:
                        duel_zones[row['team']][row['zone']][row['team']] += 1
            self.prints['duel winners per zone and team'] = duel_zones
        return self.prints['duel winners per zone and team']
    
    def add_before_and_after(self, other) -> dict:
        '''handels addition for the before and after stats'''
        return_dict = {team: dict() for team in self.teams} 
        for before in self.prints['before and after']:
            for after in self.prints['before and after'][before]:
                return_dict[before][after] = self.prints['before and after'][before][after] + other.prints['before and after'][before][after]
        return return_dict
    
    def add_duel_winners_per_zone_and_team(self, other) -> dict:
        '''handles the addition for the duel winners per zone and team'''
        return_dict = {team: {z : {t: 0 for t in self.teams} for z in Game.zones} for team in self.teams}
        for team in self.prints['duel winners per zone and team']:
            for zone in self.prints['duel winners per zone and team'][team]:
                for t in self.prints['duel winners per zone and team'][team][zone]:
                    return_dict[team][zone][t] = self.prints['duel winners per zone and team'][team][zone][t] + other.prints['duel winners per zone and team'][team][zone][t]
        return return_dict
    
    def add_duel_zones_per_team(self, other) -> dict:
        '''handles the addition for the duel zones per teams'''
        return_dict = {team: dict() for team in self.teams}
        for team in self.prints['duel zones per team']:
            for zone in self.prints['duel zones per team'][team]:
                return_dict[team][zone] = self.prints['duel zones per team'][team][zone] + other.prints['duel zones per team'][team][zone]
        return return_dict
    
    def get_duels_dict(self) -> dict:
        '''returns a dictionary of the duels
            if need be it fills self.prints'''
        if 'duels' not in self.prints:
            duels_df = self.get_duels_df()
            duels_dict = {team: 0 for team in self.teams}
            for team in duels_dict:
                duels_dict[team] = len(duels_df.loc[duels_df['team'] == team].index)
            self.prints['duels'] = duels_dict
        return self.prints['duels']

    def get_slot_passes_dict(self) -> dict:
        '''returns a dictionary of the slot passes
            if need be it fills self.prints'''
        if 'slot passes' not in self.prints:
            sp_df = self.get_slot_passes_df()
            sp_dict = {team: 0 for team in self.teams}
            for team in sp_dict:
                sp_dict[team] = len(sp_df.loc[sp_df['team'] == team].index)
            self.prints['slot passes'] = sp_dict
        return self.prints['slot passes']
    
    def get_long_passes_dict(self) -> dict:
        '''returns a dictionary of the long passes (passning - lång, farlig)
            if need be it fills self.prints'''
        if 'long passes' not in self.prints:
            lp_df = self.get_long_passes_df()
            lp_dict = {team: 0 for team in self.teams}
            for team in lp_dict:
                lp_dict[team] = len(lp_df.loc[lp_df['team'] == team].index)
            self.prints['long passes'] = lp_dict
        return self.prints['long passes']


    def get_interceptions_dict(self) -> dict:
        '''returns a dictionary of the interceptions
            if need be it fills self.prints'''
        if 'interceptions' not in self.prints:
            interceptions_df = self.get_interceptions_df()
            interceptions_dict = {team: 0 for team in self.teams}
            for team in interceptions_dict:
                interceptions_dict[team] = len(interceptions_df.loc[interceptions_df['team'] == team].index)
            self.prints['interceptions'] = interceptions_dict
        return self.prints['interceptions']

    def get_lost_balls_dict(self) -> dict:
        '''returns a dictionary of the lost balls
            if need be it fills self.prints'''
        if 'lost balls' not in self.prints:
            lost_balls_df = self.get_lost_balls_df()
            lost_balls_dict = {team: 0 for team in self.teams}
            for team in lost_balls_dict:
                lost_balls_dict[team] = len(lost_balls_df.loc[lost_balls_df['team'] == team].index)
            self.prints['lost balls'] = lost_balls_dict
        return self.prints['lost balls']
    
    def get_penalties_dict(self) -> dict:
        '''returns a dictionary of the penalties
            if need be it fills self.prints'''
        if 'penalties' not in self.prints:
            penalties_df = self.get_penalties_df()
            penalties_dict = {team: 0 for team in self.teams}
            for team in penalties_dict:
                penalties_dict[team] = len(penalties_df.loc[penalties_df['team'] == team].index)
            self.prints['penalties'] = penalties_dict
        return self.prints['penalties']

    def get_scrimmages_dict(self) -> dict:
        '''returns a dictionary of the scrimmages (närkamper)
            if need be it fills self.prints'''
        if 'scrimmages' not in self.prints:
            scrimmages_df = self.get_scrimmages_df()
            scrimmages_dict = {team: 0 for team in self.teams}
            for team in scrimmages_dict:
                scrimmages_dict[team] = len(scrimmages_df.loc[scrimmages_df['team'] == team].index)
            self.prints['scrimmages'] = scrimmages_dict
        return self.prints['scrimmages']

    def get_corners_dict(self) -> dict: 
        '''returns a dictionary of the corners and based on left right then team
            if need be it fills self.prints'''
        if 'corners' not in self.prints:
            corners_df = self.get_corners_df()
            corners_dict = {team: {side: 0 for side in Stats.corner_sides} for team in self.teams}
            for team in corners_dict:
                for side in corners_dict[team]: # self.big_df['event'].isin(['skott', 'mål'])
                    corners_dict[team][side] = len(corners_df.loc[(corners_df['team'] == team) & (corners_df['zone'].isin(Stats.corner_sides[side]))].index)
            self.prints['corners'] = corners_dict
        return self.prints['corners']
    
    def get_corner_goal_sides(self) -> dict:
        '''returns a dictionary of what side the corner goals are scored from'''
        if 'corner goal sides' not in self.prints:
            corners_dict = {team: {side: 0 for side in Stats.corner_sides} for team in self.teams}
            for goal in self.get_goals_info_list():
                if goal['subevent'] == 'hörnmål' and goal['origin zone'] != '0': # 'origin zone'
                    corners_dict[goal['team']][Stats.corner_names(goal['origin zone'])] += 1
            self.prints['corner goal sides'] = corners_dict
        return self.prints['corner goal sides']

    def add_corner_goal_sides(self, other):
        '''handles the addition of the corner goal sides'''
        return gf.combine_dictionaries(self.get_corner_goal_sides(), other.get_corner_goal_sides())

    def get_sog_dict(self) -> dict:
        '''returns a dictionary of the shots on goal
            if need be it fills self.prints'''
        if 'shots on goal' not in self.prints:
            sog_df = self.get_sog_df()
            sog_dict = {team: 0 for team in self.teams}
            for team in sog_dict:
                sog_dict[team] = len(sog_df.loc[sog_df['team'] == team].index)
            self.prints['shots on goal'] = sog_dict
        return self.prints['shots on goal']

    def add_duels(self, other) -> dict:
        '''returns the duels of the added objects
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['duels']:
            return_dict[team] = self.prints['duels'][team] + other.prints['duels'][team]
        return return_dict

    def add_interceptions(self, other) -> dict:
        '''returns the interceptions of the added objects
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['interceptions']:
            return_dict[team] = self.prints['interceptions'][team] + other.prints['interceptions'][team]
        return return_dict

    def add_lost_balls(self, other) -> dict:
        '''returns the lost balls of the added objects
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['lost balls']:
            return_dict[team] = self.prints['lost balls'][team] + other.prints['lost balls'][team]
        return return_dict
    
    def add_penalties(self, other) -> dict:
        '''returns the penalties of the added objects
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['penalties']:
            return_dict[team] = self.prints['penalties'][team] + other.prints['penalties'][team]
        return return_dict
    
    def add_scrimmages(self, other) -> dict:
        '''returns the scrimmages (närkamper) of the added objects
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['scrimmages']:
            return_dict[team] = self.prints['scrimmages'][team] + other.prints['scrimmages'][team]
        return return_dict

    def add_sog(self, other) -> dict:
        '''returns the shots on goal of the added objects
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['shots on goal']:
            return_dict[team] = self.prints['shots on goal'][team] + other.prints['shots on goal'][team]
        return return_dict 
    
    def add_slot_passes(self, other) -> dict:
        '''returns the slot passes (passning - straffområde) of the added objects
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['slot passes']:
            return_dict[team] = self.prints['slot passes'][team] + other.prints['slot passes'][team]
        return return_dict 
    
    def add_long_passes(self, other) -> dict:
        '''returns the long passes (passning - lång, farlig) of the added objects
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['long passes']:
            return_dict[team] = self.prints['long passes'][team] + other.prints['long passes'][team]
        return return_dict 

    def add_corners(self, other) -> dict:
        '''returns the corners for the added objects
            expects type to already have been checked'''   
        return gf.combine_dictionaries(self.prints['corners'], other.prints['corners']) 

    def get_possession_dict(self) -> dict:
        '''returns a dictionary of the possession
            if need be it fills self.prints'''
        if 'possession' not in self.prints:
            poss_dict = {team: 0 for team in self.teams}
            self.make_possession_list()
            self.make_per_time_lists()
            for d in self.prints['per time lists']['possession']:
                for team in d:
                    try:
                        poss_dict[team] += gf.readable_to_sec(d[team]) 
                    except:
                        pass
            for team in poss_dict:
                poss_dict[team] = gf.sec_to_readable(poss_dict[team])
            self.prints['possession'] = poss_dict
        return self.prints['possession']

    def add_possession(self, other) -> dict:
        '''returns the possession of the two added objects
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['possession']:
            return_dict[team] = gf.sec_to_readable(gf.readable_to_sec(self.prints['possession'][team]) + gf.readable_to_sec(other.prints['possession'][team]))
        return return_dict

    def get_penalty_shots_dict(self) -> dict:
        '''returns a dictionary of the penalty shots (straff) for each team
            if need be if fills self.prints'''
        if 'penalty shots' not in self.prints:
            ps_dict = {team: 0 for team in self.teams}
            ps_df = self.get_penalty_shot_df()
            for team in ps_dict:
                ps_dict[team] = len(ps_df.loc[ps_df['team'] == team].index)
            self.prints['penalty shots'] = ps_dict
        return self.prints['penalty shots']
    
    def add_penalty_shots(self, other) -> dict:
        '''handels the addition of the penalty shots (straff)
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['penalty shots']:
            return_dict[team] = self.prints['penalty shots'][team] + other.prints['penalty shots'][team]
        return return_dict

    def get_shottypes_dict(self) -> dict:
        '''returns a dictionary of the shot types
            if need be it fills self.prints'''
        if 'shot types' not in self.prints:
            st_dict = {team: dict() for team in self.teams}
            for team in self.teams:
                st_df = self.get_shottypes_df().loc[self.get_shottypes_df()['team'] == team]
                for shottype in Game.events_and_their_subevents['skottyp']:
                    if len(st_df.loc[st_df['subevent'] == shottype].index) > 0:
                        st_dict[team][shottype] = len(st_df.loc[st_df['subevent'] == shottype].index)
            self.prints['shot types'] = st_dict
        return self.prints['shot types']

    def add_shottypes(self, other) -> dict:
        '''returns the shot types of the added objects
            expects type to already have been checked'''
        return_dict = {team: dict() for team in self.teams}
        for team in self.prints['shot types']:
            for shottype in self.prints['shot types'][team]:
                if shottype in other.prints['shot types'][team]:
                    return_dict[team][shottype] = self.prints['shot types'][team][shottype] + other.prints['shot types'][team][shottype]
                else:
                    return_dict[team][shottype] = self.prints['shot types'][team][shottype] 
            for shottype in other.prints['shot types'][team]:
                if shottype not in return_dict[team]:
                    return_dict[team][shottype] = other.prints['shot types'][team][shottype]
        return return_dict

    def get_goal_origins_df(self) -> pd.core.frame.DataFrame:
        '''returns a df object of only goals and their origins
            fils df_dict if need be'''
        if 'goal origins' not in self.df_dict:
            goals_df = self.get_shot_origins_df().loc[self.get_shot_origins_df()['goal'] == True].drop('goal', axis=1)
            self.df_dict['goal origins'] = goals_df
        return self.df_dict['goal origins']

    def get_goals_info_list(self) -> list:
        '''returns a list with the info for all goals'''
        goals_list = list()
        df = self.big_df.loc[self.big_df['event'] == 'mål']
        for index, row in df.iterrows():
            d = dict()
            d['time'] = row['time']
            d['team'] = row['team']
            d['subevent'] = row['subevent']
            d['zone'] = row['zone']
            d['shot type'] = self.big_df.loc[index + 1]['subevent']
            goals_list.append(d)
        for i, d in enumerate(goals_list):
            d['origin'] = self.get_goal_origins_list()[i][1]
            d['attack time'] = self.get_goal_origins_list()[i][2]
            d['origin zone'] = self.get_goal_origins_list()[i][4]
        return goals_list        

    def get_goal_origins_list(self) -> list:
        '''returns a list of the goal events'''
        return self.get_goal_origins_df().values.tolist()
    
    def get_shot_origins_df(self) -> pd.core.frame.DataFrame:
        '''returns a df object of shot origins
            fills the df_dict if need be'''
        if 'shot origins' not in self.df_dict:
            keys = ['team', 'shot origin', 'attack time',  'shot time', 'goal', 'origin zone']
            values = [[] for i in range(len(keys))]
            possession_team = None
            possession_gained = None
            time_gained = 0 
            origin_zone = None

            for index, row in self.big_df.iterrows():
                # a shot is made; save shot origin info
                if row['event'] == 'skott' or row['event'] == 'mål':
                    values[0].append(possession_team)
                    values[1].append(possession_gained)
                    values[2].append(gf.readable_to_sec(row['time']) - time_gained)
                    values[3].append(row['time'])
                    values[4].append(row['event'] == 'mål')
                    values[5].append(origin_zone)
                # new team gains possession OR new start of play
                elif (row['event'] in Stats.possession_gained and row['team'] != possession_team) or row['event'] in Stats.start_of_play:
                    possession_team = row['team']
                    possession_gained = row['event']
                    time_gained = gf.readable_to_sec(row['time'])
                    origin_zone = row['zone']
                # old team loses possession
                elif row['event'] in Stats.possession_lost and row['team'] == possession_team:
                    possession_team = self.opposite_team(row['team'])
                    possession_gained = row['event']
                    time_gained = gf.readable_to_sec(row['time'])
                    origin_zone = row['zone']
            self.df_dict['shot origins'] = gf.make_df(keys, values)
        return self.df_dict['shot origins']

    def get_shot_origins_dict(self) -> dict:
        '''returns a dictionary of the shot origins
            if need be it fills self.prints'''
        if 'shot origins' not in self.prints:
            so_df = self.get_shot_origins_df()
            so_dict = {team: dict() for team in self.teams}
            for index, row in so_df.iterrows():
                if row['shot origin'] in so_dict[row['team']]:
                    so_dict[row['team']][row['shot origin']] += 1
                else:
                    so_dict[row['team']][row['shot origin']] = 1
            self.prints['shot origins'] = so_dict
        return self.prints['shot origins']

    def add_shot_origins(self, other) -> dict:
        '''returns the shot origins of the added objects
            expects type to already have been checked'''
        return_dict = {team: dict() for team in self.teams}
        for team in self.prints['shot origins']:
            for shotorigin in self.prints['shot origins'][team]:
                if shotorigin in other.prints['shot origins'][team]:
                    return_dict[team][shotorigin] = self.prints['shot origins'][team][shotorigin] + other.prints['shot origins'][team][shotorigin]
                else:
                    return_dict[team][shotorigin] = self.prints['shot origins'][team][shotorigin] 
            for shotorigin in other.prints['shot origins'][team]:
                if shotorigin not in return_dict[team]:
                    return_dict[team][shotorigin] = other.prints['shot origins'][team][shotorigin]
        return return_dict

    def note_possession(self, row: pd.core.series.Series, index: int) -> None:
        '''updates the possession list based on row'''
        if row['event'] in Stats.possession_gained:
            if index == 0 or row['team'] != self.possession_list[-1][0]:
                self.possession_list.append((row['team'], row['time']))
        elif row['event'] in Stats.possession_lost:
            if index == 0 or self.opposite_team(row['team']) != self.possession_list[-1][0]:
                self.possession_list.append((self.opposite_team(row['team']), row['time']))
        elif row['event'] in Stats.await_next:
            if index != 0 and self.possession_list[-1][0] != None:
                self.possession_list.append((None, row['time']))
        return     
    
    def make_possession_list(self) -> None:
        '''makes the possession list'''
        if len(self.possession_list) == 0:
            for index, row in self.big_df.iterrows():
                self.note_possession(row, index)
        return 
        
    def get_shots_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the outcome events from shots
            populates the df_dict if not already done'''
        if 'shots' not in self.df_dict:
            self.df_dict['shots'] = self.big_df.loc[self.big_df['event'].isin(['skott', 'mål'])]
        return self.df_dict['shots'] 

    def get_40_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the 40 events
            populates the df_dict if not already done'''
        if '40' not in self.df_dict:
            self.df_dict['40'] = self.big_df.loc[(self.big_df['event'] == '40')]
        return self.df_dict['40'] 

    def get_sog_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with the shots on goal
            populates the df_dict if not already done'''
        if 'shots on goal' not in self.df_dict:
            # bitwise comparison
            self.df_dict['shots on goal'] = self.big_df.loc[(self.big_df['subevent'] == 'räddning') | (self.big_df['event'] == 'mål')]
        return self.df_dict['shots on goal'] 
             
    def get_shottypes_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the shot types
            populates the df_dict if not already done'''
        if 'shot types' not in self.df_dict:
            self.df_dict['shot types'] = self.big_df.loc[self.big_df['event'] == 'skottyp']
        return self.df_dict['shot types'] 
    
    def get_score_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the goals
            populates the df_dict if not already done'''
        if 'goals' not in self.df_dict:
            self.df_dict['goals'] = self.big_df.loc[self.big_df['event'] == 'mål']
        return self.df_dict['goals'] 

    def get_duels_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the duels
            populates the df_dict if not already done'''
        if 'duels' not in self.df_dict:
            self.df_dict['duels'] = self.big_df.loc[self.big_df['event'].isin(['närkamp', 'brytning'])]
        return self.df_dict['duels'] 

    def opposite_team(self, team: str) -> str:
        '''returns the opposite team of input
            only works if input is correct'''
        return self.teams.difference({team}).pop()

    def get_interceptions_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the interceptions
            populates the df_dict if not already done'''
        if 'interceptions' not in self.df_dict:
            self.df_dict['interceptions'] = self.big_df.loc[self.big_df['event'] == 'brytning']
        return self.df_dict['interceptions'] 
    
    def get_freeshots_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the freeshots (frislag)
            populates the df_dict if not already done'''
        if 'freeshots' not in self.df_dict:
            self.df_dict['freeshots'] = self.big_df.loc[self.big_df['event'] == 'frislag']
        return self.df_dict['freeshots'] 

    def get_lost_balls_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the lost balls
            populates the df_dict if not already done'''
        if 'lost balls' not in self.df_dict:
            self.df_dict['lost balls'] = self.big_df.loc[self.big_df['event'] == 'bolltapp']
        return self.df_dict['lost balls'] 

    def get_scrimmages_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the scrimmages (närkamper)
            populates the df_dict if not already done'''
        if 'scrimmages' not in self.df_dict:
            self.df_dict['scrimmages'] = self.big_df.loc[self.big_df['event'] == 'närkamp']
        return self.df_dict['scrimmages'] 

    def get_corners_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the corners
            populates the df_dict if not already done'''
        if 'corners' not in self.df_dict:
            self.df_dict['corners'] = self.big_df.loc[self.big_df['event'] == 'hörna']
        return self.df_dict['corners'] 

    def get_slot_passes_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the slot passes (passning - straffområde)
            populates the df_dict if not already done'''
        if 'slot passes' not in self.df_dict:
            self.df_dict['slot passes'] = self.big_df.loc[self.big_df['subevent'] == 'straffområde']
        return self.df_dict['slot passes'] 

    def get_long_passes_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the long passes (passning - lång, farlig)
            populates the df_dict if not already done'''
        if 'long passes' not in self.df_dict:
            self.df_dict['long passes'] = self.big_df.loc[self.big_df['subevent'].isin(['lång', 'farlig'])]
        return self.df_dict['long passes'] 

    def get_penalties_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the penaties
            populates the df_dict if not already done'''
        if 'penalties' not in self.df_dict:
            self.df_dict['penalties'] = self.big_df.loc[self.big_df['event'] == 'utvisning']
        return self.df_dict['penalties'] 

    def get_long_shots_df(self) -> pd.core.frame.DataFrame:
        '''returns a ff with only the long shots (skottyp: utifrån)
            populates the df_dict if not already done'''
        if 'long shots' not in self.df_dict:
            self.df_dict['long shots'] = self.big_df.loc[self.big_df['subevent'] == 'utifrån']
        return self.df_dict['long shots'] 
    
    def get_penalty_shot_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the penalty shots (straff)
            populates the df_dict if not already done'''
        if 'penalty shot' not in self.df_dict:
            self.df_dict['penalty shot'] = self.big_df.loc[self.big_df['event'] == 'straff']
        return self.df_dict['penalty shot'] 