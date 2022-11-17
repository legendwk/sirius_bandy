import pandas as pd 
from get_data import Game
import general_functions as gf
from bisect import bisect_left


class Stats:
# class variables
    # used for possession data
    possession_gained = {'skott', 'frislag', 'närkamp', 'inslag', 'utkast', 'avslag', 
                        'friläge', 'boll', 'brytning', 'passning', '40'}    
    possession_lost = {'bolltapp', 'rensning', 'offside'}
    await_next = {'timeout', 'mål', 'stop', 'utvisning', 'hörna', 'straff'}#, 'skottyp'}
    # used for shot origins
    start_of_play = {'avslag', 'frislag', 'inslag', 'utkast', 'skott', 'hörna', 'straff'}
    # used for zone specific data, coverts zones 180 degrees
    zone_change = {'z1':'z9', 'z2':'z8', 'z3': 'z7', 'z4':'z4', 'z5':'z5', 'z6':'z6', 'z7':'z3', 'z8':'z2', 'z9':'z1'}

# constructor
    def __init__(self, filename: str, dummy = False, main_team = 'sirius', N = 3) -> None:
        '''makes and calculates the Stats object. 
        main_team is which team we highlight. N is how many parts the half is divided into for the per-part stats.
        Dummy is only used by dunder add'''
        # this is where we put everything we're printing
        self.prints = dict()
        self.possession_list = list()
        self.goal_origins_list = list()
        self.main_team = main_team
        self.N = N
        # dummy is only used if we are adding two ojects
        if not dummy: 
            self.big_df = gf.read_csv_as_df(filename)
            self.teams = {team for team in self.big_df['team'].tolist() if team != '0'}
            self.df_dict = dict()
            self.out = filename + '.txt'
            self.compile_stats()
        return

    def other_direction(zone: str) -> str:
        '''returns the zone in the other direction
            does not accept non-zone entry'''
        return Stats.zone_change[zone]

# dunder add, for Stats() + Stats()
    def __add__(self, other) -> None:
        if not isinstance(other, Stats):
            return NotImplemented
        # new empty object
        obj = Stats(str(), dummy = True, main_team = self.main_team)
        obj.possession_list = self.possession_list + other.possession_list
        obj.goal_origins_list = self.goal_origins_list + other.goal_origins_list
        obj.goals_info_list = self.goals_info_list + other.goals_info_list
        obj.out = f'{self.out[:-4]} och {other.out}'
        obj.teams = self.teams
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
        obj.prints['per time lists'] = self.add_per_time_lists(other)
        obj.prints['40'] = self.add_40_list(other)

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
        self.make_per_time_lists()
        self.make_40_list()

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
    
    # TODO: GÖÖÖÖÖÖÖÖÖÖÖÖR, hur kan det vara så svårt??????
    def sustained_attacks(self, min_attack_length = 45, max_disruption_time = 10) -> dict:
        """returns a dict of each team's sustained attacks that are longer than min_attack_length s
            we accept that the opponent gets the ball if it is won back within max_disruption_time s"""
        attacks = {team : list() for team in self.teams}
        current_team, start_time = self.possession_list[0]
        for i in range(len(self.possession_list) - 1):
            team, time = self.possession_list[i]
            if team in self.teams:
                if team != current_team:
                    pass
    
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
    
    def add_40_list(self, other):
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
        times = [gf.readable_to_sec(df.iloc[-1]['time'])/self.N * i for i in range(self.N+1)]
        limits = [(times[i], times[i+1]) for i in range(self.N)]
        per_time_list = [{team: 0 for team in self.teams} for n in range(self.N)]
        for index, row in df.iterrows():
            for i, span in enumerate(limits):
                if gf.readable_to_sec(row['time']) > span[0] and gf.readable_to_sec(row['time']) <= span[1]:
                    per_time_list[i][row['team']] += 1
        return per_time_list

    def get_duel_zones_dict(self) -> dict:
        '''returns a dictionary of where the duels happened, and who won them
            will alter to make sure that self.main_team always scores in z8'''
        if 'duel zones' not in self.prints:
            duel_zones = {'z' + str(i): {team: 0 for team in self.teams} for i in range(1, 10)}
            change_dir = not self.team_attacks_up(team = self.main_team)
            duels_df = self.get_duels_df()
            for index, row in duels_df.iterrows():
                if row['zone'] != '0':
                    if change_dir:
                        z = Stats.zone_change[row['zone']]
                    else:
                        z = row['zone']
                    duel_zones[z][row['team']] += 1
            self.prints['duel zones'] = duel_zones
        return self.prints['duel zones']

    def add_duel_zones(self, other) -> dict:
        '''returns the duel zones of the added objects'''
        return_dict = {'z' + str(i): {team: 0 for team in self.teams} for i in range(1, 10)}
        for zone in self.prints['duel zones']:
            for team in self.prints['duel zones'][zone]:
                return_dict[zone][team] = self.prints['duel zones'][zone][team] + other.prints['duel zones'][zone][team]
        return return_dict

    def get_score_dict(self) -> dict:
        '''returns a dictionary of the score
            if need be it fills self.prints'''
        if 'score' not in self.prints:
            score_df = self.get_score_df()
            score_dict = {team: 0 for team in self.teams}
            for team in score_dict:
                score_dict[team] = len(score_df.loc[score_df['team'] == team].index)
            self.prints['score'] = score_dict
        return self.prints['score']

    def add_score(self, other) -> dict:
        '''returns the score of the added objects
            expects type to already have been checked'''
        return_dict = dict()
        for team in self.prints['score']:
            return_dict[team] = self.prints['score'][team] + other.prints['score'][team]
        return return_dict

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
    
    def add_before_and_after(self, other) -> dict:
        '''handels addition for the before and after stats'''
        return_dict = {team: dict() for team in self.teams} 
        for before in self.prints['before and after']:
            for after in self.prints['before and after'][before]:
                return_dict[before][after] = self.prints['before and after'][before][after] + other.prints['before and after'][before][after]
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

    def get_scrimmages_dict(self) -> dict:
        '''returns a dictionary of the scrimmages
            if need be it fills self.prints'''
        if 'scrimmages' not in self.prints:
            scrimmages_df = self.get_scrimmages_df()
            scrimmages_dict = {team: 0 for team in self.teams}
            for team in scrimmages_dict:
                scrimmages_dict[team] = len(scrimmages_df.loc[scrimmages_df['team'] == team].index)
            self.prints['scrimmages'] = scrimmages_dict
        return self.prints['scrimmages']
    
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
    
    def add_scrimmages(self, other) -> dict:
        '''returns the scrimmages of the added objects
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

    def get_possession_dict(self) -> dict:
        '''returns a dictionary of the possession
            if need be it fills self.prints'''
        if 'possession' not in self.prints:
            poss_dict = {team: 0 for team in self.teams}
            self.make_possession_list()
            self.make_per_time_lists()
            for d in self.prints['per time lists']['possession']:
                for team in d:
                    poss_dict[team] += gf.readable_to_sec(d[team]) 
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
        return goals_list        

    def get_goal_origins_list(self) -> list:
        '''returns a list of the goal events'''
        return self.get_goal_origins_df().values.tolist()
    
    def get_shot_origins_df(self) -> pd.core.frame.DataFrame:
        '''returns a df object of shot origins
            fills the df_dict if need be'''
        if 'shot origins' not in self.df_dict:
            keys = ['team', 'shot origin', 'attack time',  'shot time', 'goal']
            values = [[] for i in range(len(keys))]
            possession_team = None
            possession_gained = None
            time_gained = 0 

            for index, row in self.big_df.iterrows():
                # a shot is made; save shot origin info
                if row['event'] == 'skott' or row['event'] == 'mål':
                    values[0].append(possession_team)
                    values[1].append(possession_gained)
                    values[2].append(gf.readable_to_sec(row['time']) - time_gained)
                    values[3].append(row['time'])
                    values[4].append(row['event'] == 'mål')
                # new team gains possession OR new start of play
                elif (row['event'] in Stats.possession_gained and row['team'] != possession_team) or row['event'] in Stats.start_of_play:
                    possession_team = row['team']
                    possession_gained = row['event']
                    time_gained = gf.readable_to_sec(row['time'])
                # old team loses possession
                elif row['event'] in Stats.possession_lost and row['team'] == possession_team:
                    possession_team = self.opposite_team(row['team'])
                    possession_gained = row['event']
                    time_gained = gf.readable_to_sec(row['time'])
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

    def get_lost_balls_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the lost balls
            populates the df_dict if not already done'''
        if 'lost balls' not in self.df_dict:
            self.df_dict['lost balls'] = self.big_df.loc[self.big_df['event'] == 'bolltapp']
        return self.df_dict['lost balls'] 

    def get_scrimmages_df(self) -> pd.core.frame.DataFrame:
        '''returns a df with only the the scrimmages
            populates the df_dict if not already done'''
        if 'scrimmages' not in self.df_dict:
            self.df_dict['scrimmages'] = self.big_df.loc[self.big_df['event'] == 'närkamp']
        return self.df_dict['scrimmages'] 