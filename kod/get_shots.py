import time
from get_data import Game

class Shots:

    # class variables
    offense_types = {'direkt', 'samlat', 'långt'}
    shot_types = {'friställande', 'inlägg', 'utifrån', 'dribbling', 'centralt', 'övrigt', 'fast'}
    outcomes = {'mål', 'hörna', 'annat'}

    # constructor
    def __init__(self, team1: str, team2: str) -> None:
        self.teams = {team1, team2}
        return
    # static methods


    # non-static methods
    def collect_shots(self, filename: str) -> None: 
        '''collects data on shots and exports into filenamne csv
            csv structure is events, time
            terminates when input is STOP
            change time by input clock: HH:MM:SS
        '''
        print(f'creating file {filename}')
        # variables 
        keys = ['event', 'time']
        values = [[], []]
        start_time = 0
        inp = ''

        # input
        while inp.lower() != 'stop':
            inp = input('next event: ')
            t = time.time()
            if start_time == 0:
                start_time = t
            # no double taps 
            if inp != '':
                # command for chaning time is 'clock HH:MM:SS'
                if inp.lower().split()[0] == 'clock':
                    start_time = Game.set_game_clock(inp.lower().split()[1], t)
                else:
                    values[0].append(inp)
                    values[1].append(Game.sec_to_readable(t-start_time))
                    Game.save_data_to_csv(filename, keys, values)
        return 
    
    def clean_shots(self, filename_in: str) -> None:
        '''cleans the raw shots csv
            asks user for help when it does not understand
        '''
        filename_out = Game.append_clean(filename_in)
        event_keys = ['time', 'team', 'offense_type', 'shot_type', 'outcome']
        event_values = [[] for i in range(len(event_keys))]
        
        df = Game.read_csv_as_df(filename_in)
        for index, row in df.iterrows():
            split_set = set(row['event'].lower().split())
            if 'stop' in split_set or index == 0:
                event_values[0].append(row['time'])
                for i in range(1, len(event_keys)):
                    event_values[i].append('0')
            # del is the 'undo' command
            elif 'del' not in split_set:
                # the or operator doesn't work with pandas (| also gives me errors)
                if 'del' not in set(str(df.iloc[[index + 1]]['event']).lower().split()):
                    # no 'del' -> POPULATE!
                    # fill everything with zeroes 
                    # time
                    event_values[0].append(row['time'])
                    event_values[1].append(self.find_team(split_set))
                    event_values[2].append(self.find_offense_type(split_set))
                    event_values[3].append(self.find_shot_type(split_set))
                    event_values[4].append(self.find_outcome(split_set))
                    
        Game.save_data_to_csv(filename_out, event_keys, event_values)
        return       

#event_keys = ['time', 'team', 'offense_type', 'shot_type', 'outcome', 'zone']

    def find_team(self, split_set: set) -> str:
        '''attempts to find team, if not successful asks user to do it manually'''
        for team in self.teams:
            if team in split_set:
                return team
        return self.ask_for_team(split_set)

    def ask_for_team(self, entry: set) -> str:
        '''asks the user to specify which team it is'''
        inp = ''
        while True:
            inp = input(f'{entry} \n {self.teams} \n what team are we looking for? ')
            if inp in self.teams or inp == '0':
                return inp
    
    def find_offense_type(self, split_set: set) -> str:
        '''attempts to find offense type, 
            if not successful asks user to do it manually'''
        for offense in Shots.offense_types:
            if offense in split_set:
                return offense
        return self.ask_for_offense_type(split_set)

    def ask_for_offense_type(self, entry: set) -> str:
        '''asks the user to specify which offense type it is'''
        inp = ''
        while True:
            inp = input(f'{entry} \n {Shots.offense_types} \n what offense type are we looking for? ')
            if inp in Shots.offense_types or inp == '0':
                return inp
    
    def find_shot_type(self, split_set: set) -> str:
        '''attempts to find shot type, 
            if not successful asks user to do it manually'''
        for shot in Shots.shot_types:
            if shot in split_set:
                return shot
        return self.ask_for_shot_type(split_set)

    def ask_for_shot_type(self, entry: set) -> str:
        '''asks the user to specify which shot type it is'''
        inp = ''
        while True:
            inp = input(f'{entry} \n {Shots.shot_types} \n what shot type are we looking for? ')
            if inp in Shots.shot_types or inp == '0':
                return inp

    def find_outcome(self, split_set: set) -> str:
        '''attempts to find outcome, 
            if not successful asks user to do it manually'''
        for outcome in Shots.outcomes:
            if outcome in split_set:
                return outcome
        return self.ask_for_outcome(split_set)

    def ask_for_outcome(self, entry: set) -> str:
        '''asks the user to specify which outcome it is'''
        inp = ''
        while True:
            inp = input(f'{entry} \n {Shots.outcomes} \n what outcome are we looking for? ')
            if inp in Shots.outcomes or inp == '0':
                return inp

