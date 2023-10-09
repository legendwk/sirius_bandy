from tkinter import *   
from nicegui import ui
from get_data import Game
import general_functions as gf


class Visuals:
    # vi måste ange lag och outputfile name
    def __init__(self, path_to_write: str, game: Game, xdim = '1000', ydim = '700') -> None:
        self.game = game
        started = False
        output = path_to_write

        temp_dict = {}
        for team in self.game.teams:
            ui.button(team, on_click=lambda: ui.notify(f'tryckt på {team}'))
            # temp_dict['team'] = team

        for event in self.game.events:
            ui.button(event, on_click=lambda: ui.notify(f'tryckt på {event}'))

        ui.run()
        # self.root = Tk() 
        # self.root.geometry(f'{xdim}x{ydim}')

        # for team in teams:
        #     btn = Button(self.root, text = team, bd = str(int(ydim)//3),
        #                   command = self.root.destroy)
        #     btn.pack(side = 'top') 
        #     self.root.mainloop()
        # return


g = Game({'iks', 'bol'})

vis = Visuals(g)
