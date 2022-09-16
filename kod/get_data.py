import pandas as pd 
import time
import datetime

class Game:
    
    # class variables
    events = {'skott', 'frislag', 'bolltapp', 'närkamp', 'hörna', 'inslag', 'utkast',
     'avslag', 'mål', 'utvisning', 'stop', 'passning', 'friläge', 'straff',
     'offside', 'rensning', 'timeout', 'boll', 'brytning'}
    events_and_their_subevents = {'skott' : {'utanför', 'räddning', 'täckt'}, 
                                    'bolltapp': {'tappad', 'passförsök'},
                                    'passning' : {'straffområde', 'lång'},
                                    'mål' : {'straffområde', 'lång', 'fast'},
                                    'utvisning' : {'5', '10'} 
                                    }
    zones = {'z' + str(i) for i in range(1, 10)}

    # constructor
    def __init__(self, team1: str, team2: str) -> None:
        self.teams = {team1.lower(), team2.lower()}
        return

    # static methods 
    def append_clean(filename: str) -> str:
        '''makes sure that the output ends in clean.csv'''
        if len(filename) <= 4 or filename[-4:] != '.csv':
            return filename + ' clean.csv'
        else:
            return filename[:-4] + ' clean.csv'

    def read_csv_as_df(filename: str) -> pd.core.frame.DataFrame:
        '''returns the csv as a df object'''
        try:
            return pd.read_csv(filename)
        except:
            return pd.read_csv(filename + '.csv')

    # non-static methods
    def save_data_to_csv(self, filename: str, keys: list, values: list) -> None:
        # makes sure path is good
        if len(filename) <= 4 or filename[-4:] != '.csv':
            filename += '.csv'
        dic = dict()
        for i, key in enumerate(keys):
            dic[key] = values[i]
        df = pd.DataFrame(dic)
        df.to_csv(filename, index=False) 
        return

    def collector_raw(self, filename: str) -> None:
        '''collects data and exports into filename csv
            csv structre is event, time
            terminates when input is STOP
            change time by input clock HH:MM:SS
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
            
            # we're not interested in double taps on enter!
            if inp != '':
                # command for chaning time is 'clock HH:MM:SS'
                if inp.lower().split()[0] == 'clock':
                    start_time = self.set_game_clock(inp.lower().split()[1], t)
                # event input
                else:
                    values[0].append(inp)
                    values[1].append(str(datetime.timedelta(seconds = (t-start_time)//1)))
                    self.save_data_to_csv(filename, keys, values)
        return 

    
    def clean_csv(self, filename_in: str) -> None:
        '''cleans raw csv file, creating a more easily worked one
            asks user when it does not understand, make sure to check if correct 
        '''
        # variables 
        filename_out = Game.append_clean(filename_in)
        event_keys = ['time', 'team', 'event', 'subevent', 'zone']
        event_values = [[] for i in range(len(event_keys))]

        df = Game.read_csv_as_df(filename_in)
        for index, row in df.iterrows():
            split_set = set(row['event'].lower().split())
            if 'stop' in split_set:
                self.set_stop(row['time'], event_values)
            # del is the 'undo' command
            elif 'del' not in split_set:
                # the or operator doesn't work with pandas (| also gives me errors)
                if 'del' not in set(str(df.iloc[[index + 1]]['event']).lower().split()):
                    # no 'del' -> POPULATE!
                    self.set_time(row['time'], event_values)
                    self.set_team(self.find_team(split_set), event_values)
                    event = self.find_event(split_set)
                    self.set_event(event, event_values)
                    self.set_subevent(event, split_set, event_values)
                    self.set_zone(self.find_zone(split_set), event_values)

        self.save_data_to_csv(filename_out, event_keys, event_values)
        return

    def set_game_clock(self, new_time: str, t: float) -> int:
        '''returns start_time to sync game clock to new_time at t'''
        return t - sum(int(x) * 60 ** i for i, x in enumerate(reversed(new_time.split(':'))))
 

    def set_subevent(self, event: str, split_set: set, event_values: list) -> None:
        '''sets subevent based on event'''
        # the event has a subevent
        if event in Game.events_and_their_subevents:
            event_values[3].append(self.find_subevent(split_set, event))
        # the event does not have a subevent
        else:
            event_values[3].append('0')

    def set_stop(self, time: str, event_values: list) -> None:
        '''populates event_values with data that indicates that the game is over'''
        event_values[0].append(time)
        event_values[1].append('0')
        event_values[2].append('stopp')
        event_values[3].append('0')
        event_values[4].append('0')
        return

    def set_time(self, time: str, event_values: list) -> None:
        '''sets time'''
        event_values[0].append(time)
        return

    def set_team(self, team: str, event_values: list) -> None:
        '''sets team'''
        event_values[1].append(team)
        return

    def set_event(self, event: str, event_values: list) -> None:
        '''sets event'''
        event_values[2].append(event)
        return
    
    def set_subevent1(self, subevent: str, event_values: list) -> None:
        '''sets event'''
        event_values[3].append(subevent)
        return

    def set_zone(self, zone: str, event_values: list) -> None:
        '''sets zone'''
        event_values[4].append(zone)
        return

    def ask_for_team(self, entry: set) -> str:
        '''asks the user to specify which team it is'''
        inp = ''
        while True:
            inp = input(f'{entry} \n what team are we looking for? ')
            if inp in self.teams or inp == '0':
                return inp

    def ask_for_event(self, entry: set) -> str:
        '''asks user to specify event'''
        while True:
            inp = input(f'{entry} \n {Game.events} \n what event are we looking for? ')
            if inp in Game.events or inp == '0':
                return inp

    def ask_for_subevent(self, entry: set, event: str) -> str:
        '''asks user to specify subevent'''
        while True:
            inp = input(f'{entry} \n {Game.events_and_their_subevents[event]} \n what subevent to {event} are we looking for? ')
            if inp in Game.events_and_their_subevents[event] or inp == '0':
                return inp

    def ask_for_zone(self, entry: set) -> str:
        '''asks user to specify zone'''
        while True:
            inp = input(f'{entry} \n {Game.zones} \n what zone are we looking for? ')
            if inp in Game.zones or inp == '0':
                return inp

    def find_team(self, split_set: set) -> str:
        '''attempts to find team, if not successful asks user to do it manually'''
        for team in self.teams:
            if team in split_set:
                return team
        return self.ask_for_team(split_set)
    
    def find_event(self, split_set: set) -> str:
        '''attempts to find event, if not successful asks user to do it manually'''
        for event in Game.events:
            if event in split_set:
                return event
        return self.ask_for_event(split_set)
    
    def find_subevent(self, split_set: set, event: str) -> str:
        '''attempts to find subevent for known event, if not successful asks user to do it manually'''
        for subevent in Game.events_and_their_subevents[event]:
            if subevent in split_set:
                return subevent
        return self.ask_for_subevent(split_set, event)

    def find_zone(self, split_set: set) -> str:
        '''attempts to find zone, if not successful asks user to do it manually'''
        for zone in Game.zones:
            if zone in split_set:
                return zone
        return self.ask_for_zone(split_set)


if __name__ == "__main__":
    print(f'hej')
    filename = '20220208 sirius edsbyn'
    print(f'filename {filename}')
    print(f'.append_clean(filename) {Game.append_clean(filename)}')
    filename = '20220208 sirius edsbyn.csv'
    print(f'filename {filename}')
    print(f'Game.append_clean(filename) {Game.append_clean(filename)}')

    '''
    TODO:

    '''
