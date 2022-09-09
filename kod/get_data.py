import pandas as pd 
import time
import datetime

class Game:
    
    # class variables
    events = {'skott', 'frislag', 'vunnenboll', 'hörna', 'inslag', 'utkast',
     'avslag', 'mål', 'utvisning', 'lagvarning', 'stopp', 'farligpassning', 'friläge'}
    events_and_their_subevents = {'skott' : {'utanför', 'räddning', 'täckt'}, 
                                    'vunnenboll': {'närkamp', 'tappadboll', 'dåligpassning'},
                                    'farligpassning' : {'straffområde', 'lång'}}
    zones = {'z' + str(i) for i in range(1, 10)}

    # constructor
    def __init__(self, team1: str, team2: str) -> None:
        self.team1 = team1.lower()
        self.team2 = team2.lower()
        return

    # methods
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
                values[0].append(inp)
                values[1].append(str(datetime.timedelta(seconds = (t-start_time)//1)))
                self.save_data_to_csv(filename, keys, values)
        return 


    # this method can probably be split into smaller and more general methods,
    def clean_csv(self, filename_in: str, filename_out: str) -> None:
        '''cleans raw csv file, creating a more easily worked one
            asks user when it does not understand, make sure to check if correct 
        '''
        # variables 
        event_keys = ['time', 'team', 'event', 'subevent', 'zone']
        event_values = [[] for i in range(len(event_keys))]
        
        # open the raw csv, maybe shouldn't be done like this but whatever
        try:
            df = pd.read_csv(filename_in)
        except:
            df = pd.read_csv(filename_in + '.csv')

        for index, row in df.iterrows():
            if row['event'] == 'stop': # done!
                event_values[0].append(row['time'])
                event_values[1].append('0')
                event_values[2].append('stopp')
                event_values[3].append('0')
                event_values[4].append('0')
                break

            # del is the 'undo' command
            else:
                # the or operator doesn't work with pandas (| also gives me errors)
                if str(df.iloc[[index + 1]]['event']) != 'del':
                    #print('inne i första if ')
                    if row['event'] != 'del': 
                        #print('inne i andra if ')
                    # each data type
                        event_values[0].append(row['time'])
                        split_set = set(row['event'].lower().split())
                        event_values[1].append(self.find_team(split_set))
                        event_values[2].append(self.find_event(split_set)) 
                        if event_values[2][-1] in Game.events_and_their_subevents:
                            event_values[3].append(self.find_subevent(split_set, event_values[2][-1]))
                        else:
                            event_values[3].append('0')
                        event_values[4].append(self.find_zone(split_set))

        self.save_data_to_csv(filename_out, event_keys, event_values)
        return

    def ask_for_team(self, entry: set) -> str:
        '''asks the user to specify which team it is'''
        inp = ''
        while True:
            inp = input(f'{entry} \n what team are we looking for? ')
            if inp == self.team1 or inp == self.team2 or inp == 0:
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
        if self.team1 in split_set:
            return self.team1
        elif self.team2 in split_set:
            return self.team2
        else: 
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


# TODO:
    def compile_stats(self):
        '''makes some sort of big stats page'''
        pass


if __name__ == "__main__":
    print('print från get_data')
    print(f'{__name__}')


    '''
    TODO:
        * spara data efter n = 1 input 
            * DONE
        * discard tomma entries 
            * DONE
        * hur haterar vi "del"?
            * ska vi skriva över föregående tid med nästa input? 
            * ska vi bara ta bort föregående input? 



    FÖRSLAG
        * var på isen saker händer? ex zoner?
        * spara data för passar "in i boxen"
            * det här tror jag på!
        * sida hörnor slås från? 

    * filnamn:
        * lag lag halvlek raw
    * ta bort förra:
        * del

    '''
