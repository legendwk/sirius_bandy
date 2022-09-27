import pandas as pd 
from get_data import Game


class Stats:
    # class variables
    possession_gained = {'skott', 'frislag', 'närkamp', 'inslag', 'utkast', 'avslag', 
                        'friläge', 'boll', 'brytning', 'passning', 'brytning'}    
    possession_lost = {'bolltapp', 'rensning'}
    await_next = {'timeout', 'mål', 'stop', 'offside', 'utvisning', 'hörna', 'straff'}

    # constructor
    def __init__(self, teams: set, filename: str) -> None:
        self.teams = teams
        self.team_dict = {x: 0 for x in teams}
        self.df = Game.read_csv_as_df(filename)
        self.create_instance_variables()


        # individual stats dictionaries 
    def create_instance_variables(self) -> None:
        '''creates instance variables for the object'''
        self.shots = {'saves': {x: list() for x in self.teams}, 'blocks': {x: list() for x in self.teams}, 'misses': {x: list() for x in self.teams}}
        self.goals = {'set': {x: list() for x in self.teams}, 'box': {x: list() for x in self.teams}, 'far': {x: list() for x in self.teams}}
        self.corners = {x: list() for x in self.teams}
        self.scrimmages = {x: list() for x in self.teams}
        self.lost_balls = {'lost': {x: list() for x in self.teams}, 'pass': {x: list() for x in self.teams}}
        self.interceptions = {x: list() for x in self.teams}
        self.misc = {x: list() for x in self.teams}

        # this is a list as we need it to be ordered with both teams 
        self.possession_list = list()

        # big stats dictionary
        self.stats_dict = {'goals': {x: 0 for x in self.teams}, 'shots_on_goal': {x: 0 for x in self.teams}, 'shot_attempts': {x: 0 for x in self.teams}, 
                            'corners': {x: 0 for x in self.teams}, 'scrimmages': {x: 0 for x in self.teams}, 'lost_balls': {x: 0 for x in self.teams},
                            'interceptions': {x: 0 for x in self.teams}, 'possession': {x: 0 for x in self.teams}}
        return

    # methods
    # pandas.core.series.Series
    # you can probably do everything on the df directly.......... but it's easier with for loops :---)

    def populate_individual_stats(self) -> None:
        '''loops over the df collecting stats'''
        for index, row in self.df.iterrows():
            self.note_possession(row, index)
            self.note_shots(row)
            self.note_corners(row)
            self.note_goals(row)
            self.note_shots(row)
            self.note_duels(row)
        return

    def populate_big_stats(self) -> None:
        '''populates the big stats dictionary based on individual dicts'''
        for team in self.teams:
            self.get_goals(team)
            self.get_corners(team)
            self.get_shots(team)
            self.get_duels(team)
            # vi har tappat bort metoden för att sammanfställa innehvaet : -)))))
        self.get_possession()
        return


    def get_duels(self, team: str) -> None:
        '''populates the stats_dict with info concerning duels'''
        self.stats_dict['scrimmages'][team] = len(self.scrimmages[team])
        self.stats_dict['lost_balls'][team] = len(self.lost_balls['lost'][team]) + len(self.lost_balls['pass'][team])
        self.stats_dict['interceptions'][team] = len(self.interceptions[team])
        return


    def get_shots(self, team: str) -> None:
        '''populates the stats_dict with shots info'''
        self.stats_dict['shots_on_goal'][team] = self.stats_dict['goals'][team] + len(self.shots['saves'][team])
        self.stats_dict['shot_attempts'][team] = len(self.shots['saves'][team]) + len(self.shots['blocks'][team]) + len(self.shots['misses'][team])
        return

    def get_goals(self, team: str) -> None:
        '''populates the stats_dict with goals info'''
        self.stats_dict['goals'][team] = len(self.goals['set'][team]) + len(self.goals['box'][team]) + len(self.goals['far'][team])  
        return

    def get_corners(self, team: str) -> None:
        '''populates the stats_dict with corners info'''
        self.stats_dict['corners'][team] = len(self.corners[team]) 
        return

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
        else: # we should never get here?
            print(f"error in get_possession_list, event: {row['event']} not recognized by Stats")
            self.possession_list.append((None, None))
        return 

    def get_possession(self) -> None:
        '''populates the stats_dict with possesion 
            possession_list looks like [[team, time], [team, time] ... ]'''
        for i in range(len(self.possession_list) - 1):
            if self.possession_list[i][0] in self.teams: # this is the current team
                self.stats_dict['possession'][self.possession_list[i][0]] += Game.readable_to_sec(self.possession_list[i+1][1]) - Game.readable_to_sec(self.possession_list[i][1])
        for team in self.stats_dict['possession']:
            self.stats_dict['possession'][team] = Game.sec_to_readable(self.stats_dict['possession'][team])
        return


    def note_duels(self, row: pd.core.series.Series) -> None:
        '''checks all types of duels and updates the appropriate dictionaries'''
        if row['event'] == 'närkamp':
            self.scrimmages[row['team']].append(row['time'])
        elif row['event'] == 'bolltapp':
            if row['subevent'] == 'tappad':
                self.lost_balls['lost'][row['team']].append(row['time'])
            elif row['subevent'] == 'passförsök':
                self.lost_balls['pass'][row['team']].append(row['time'])
            else: # no subevent
                self.note_misc(row)
        elif row['event'] == 'brytning':
            self.interceptions[row['team']].append(row['time'])
        return 

    def note_corners(self, row: pd.core.series.Series) -> None:
        '''checks row for corners and updates the appropriate dictionaries'''
        if row['event'] == 'hörna':
            self.corners[row['team']].append(row['time'])
        return 

    def note_goals(self, row: pd.core.series.Series) -> None:
        '''checks row for goals and updates the appropriate dictionaries'''
        if row['event'] == 'mål':
            if row['subevent'] == 'fast':
                self.goals['set'][row['team']].append(row['time'])
            elif row['subevent'] == 'straffområde':
                self.goals['box'][row['team']].append(row['time'])
            elif row['subevent'] == 'lång':
                self.goals['far'][row['team']].append(row['time'])
            else: # this is only if the subshot type isn't noted
                self.note_misc(row)
        return 

    def note_misc(self, row: pd.core.series.Series) -> None:
        '''should be used when data is missing'''
        self.misc[row['team']].append((row['event'], row['time']))
        return 

    def note_shots(self, row: pd.core.series.Series) -> None:
        '''checks row for shots and updates the appropriate dictionaries'''
        if row['event'] == 'skott':
            if row['subevent'] == 'räddning':
                self.shots['saves'][row['team']].append(row['time'])
            elif row['subevent'] == 'täckt':
                self.shots['blocks'][row['team']].append(row['time'])
            elif row['subevent'] == 'utanför':
                self.shots['misses'][row['team']].append(row['time'])
            else: # this is only if the subshot type isn't noted
                self.note_misc(row)
        return 

    def opposite_team(self, team: str) -> str:
        '''returns the opposite team of input
            only works if input is correct'''
        return self.teams.difference(team).pop()
