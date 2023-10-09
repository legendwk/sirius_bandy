from nicegui import ui
import general_functions as gf

def write_time(time, event_values):
    event_values[0].append(time)

def write_team(team, event_values):
    event_values[1].append(team)
    ui.notify(f'tryckt på {team}')

def write_event(event, event_values):
    event_values[2].append(event)
    ui.notify(f'tryckt på {event}')

def write_subevent(subevent, event_values):
    event_values[3].append(subevent)
    ui.notify(f'tryckt på {subevent}')

def write_zone(zone, event_values):
    event_values[4].append(zone)
    ui.notify(f'tryckt på {zone}')

def write_player(player, event_values):
    event_values[5].append(player)
    ui.notify(f'tryckt på {player}')

def disable_buttons(li):
    for b in li:
        b.disable()

def create_dashboard():
    '''creates the dashboard'''
    teams = {'iks', 'bol'}
    events = {'skott', 'frislag', 'bolltapp', 'närkamp', 'hörna', 'inslag', 'utkast',
        'avslag', 'mål', 'utvisning', 'stop', 'passning', 'friläge', 'straff',
        'offside', 'rensning', 'timeout', 'boll', 'brytning', 'skottyp', '40', 'kontring'}
    events_and_their_subevents = {'skott': {'utanför', 'räddning', 'täckt'}, 
                                        'skottyp': {'friställande', 'inlägg', 'utifrån', 'dribbling', 'centralt', 'fast', 'retur'},
                                        'bolltapp': {'tappad', 'passförsök'},
                                        'passning' : {'straffområde', 'lång', 'farlig'},
                                        'mål': {'spelmål', 'hörnmål', 'straffmål', 'frislagsmål'},
                                        'utvisning': {'5', '10'}
                                        }
        
    zones = {'z' + str(i) for i in range(1, 10)}
    players = {1, 2, 4, 5, 7}
    event_keys = ['time', 'team', 'event', 'subevent', 'zone', 'player']
    event_values = [[] for i in range(len(event_keys))]

    temp_buttons = []
    for team in teams:
        button = ui.button(team, on_click=lambda team=team: write_team(team, event_values))
        temp_buttons.append(button)
    #disable_buttons(temp_buttons)
    
    temp_buttons = []
    for event in events:
        button = ui.button(event, on_click=lambda event=event: write_event(event, event_values))
        temp_buttons.append(button)
    
    
    ui.run()

create_dashboard()
