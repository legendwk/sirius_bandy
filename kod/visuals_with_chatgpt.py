import nicegui as ng

teams = {'iks', 'bol'}
events = {'skott', 'frislag', 'bolltapp', 'närkamp', 'hörna', 'inslag', 'utkast',
          'avslag', 'mål', 'utvisning', 'stop', 'passning', 'friläge', 'straff',
          'offside', 'rensning', 'timeout', 'boll', 'brytning', 'skottyp'}
events_and_their_subevents = {
    'skott': {'utanför', 'räddning', 'täckt'},
    'skottyp': {'friställande', 'inlägg', 'utifrån', 'dribbling', 'centralt', 'fast', 'retur'},
    'bolltapp': {'tappad', 'passförsök'},
    'passning': {'straffområde', 'lång', 'farlig'},
    'mål': {'spelmål', 'hörnmål', 'straffmål', 'frislagsmål'},
    'utvisning': {'5', '10'}
}
players = {1, 2, 5, 6, 7, 10, 13, 23, 89}

# Backend functions
def select_team(t):
    # Your implementation here
    print(f"Selected team: {t}")

def select_event(e):
    # Your implementation here
    print(f"Selected event: {e}")

def select_subevent(e, se):
    # Your implementation here
    print(f"Selected event: {e}, Subevent: {se}")

def select_coordinates(x, y):
    # Your implementation here
    print(f"Selected coordinates: ({x}, {y})")

def select_player(n):
    # Your implementation here
    print(f"Selected player: {n}")

def generate_team_buttons():
    buttons = [ng.ui.button(team, on_click=lambda t=team: select_team(t)) for team in teams]
    return buttons

def generate_event_buttons():
    buttons = [ng.ui.button(event, on_click=lambda e=event: select_event(e)) for event in events]
    return buttons

def generate_subevent_buttons(event):
    if event in events_and_their_subevents:
        buttons = [ng.ui.button(subevent, on_click=lambda se=subevent: select_subevent(event, se))
                   for subevent in events_and_their_subevents[event]]
        return buttons
    return []

def generate_player_buttons():
    buttons = [ng.ui.button(str(player), on_click=lambda n=player: select_player(n)) for player in players]
    return buttons

def main_window():
    team_buttons = generate_team_buttons()
    
    while True:
        #ng.app(title="Sports App", width=800, height=600, header=False)
        
        with ng.ui.row():
            for button in team_buttons:
                ng.ui.box(width="50%")(button)
        
        selected_team = ng.await_selection()
        team_buttons = []

        event_buttons = generate_event_buttons()
        
        with ng.ui.row():
            for button in event_buttons:
                ng.ui.box(width="50%")(button)
        
        selected_event = ng.await_selection()
        event_buttons = []

        subevent_buttons = generate_subevent_buttons(selected_event)
        
        with ng.ui.row():
            for button in subevent_buttons:
                pass
                #ng.ui.box(width="50%")(button)
        
        ng.ui.button("Field Image", on_click=lambda: select_coordinates(0, 0))
        
        player_buttons = generate_player_buttons()
        
        with ng.ui.row():
            for button in player_buttons:
                pass#ng.ui.box(width="50%")(button)
        
        selected_coordinates = ng.await_selection()
        player_buttons = []

if __name__ == "__main__":
    main_window()
