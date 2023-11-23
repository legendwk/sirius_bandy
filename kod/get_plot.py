import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pptx.dml.color import ColorFormat, RGBColor

from get_stats import Stats
import constants
import general_functions as gf
import numpy as np
from datetime import timedelta


class Plot:
# class variables
    # relative link to where the images are put
    out_folder = "..\\..\\bilder\\autogen\\"

    # colors of the scale
    color_many = RGBColor(255, 0, 0)
    color_few = RGBColor(255, 255, 255)

    # these are all due to the dimensions of the pitch image
    pitch_image = "..\\..\\bilder\\pptx\\bandtplan_transparent_no_zones.png"
    # size: (266, 1071)
    transparent_bar_image = "..\\..\\bilder\\pptx\\transparent_bar.png"
    # top left of z1
    xy_zone1 = (186, 3165) #(338, 184) #(68, 33)
    dx = 700 # (893-186) 944 # (1282 - 338) #301
    dy = 944 # (3170-2226) # 705 # 894 - 184 #225
    xy_starting_zones = {'z1': (xy_zone1[0] + 0 * dx, xy_zone1[1] - 1 * dy), 'z2': (xy_zone1[0] + 1 * dx, xy_zone1[1] - 1 * dy), 'z3': (xy_zone1[0] + 2 * dx, xy_zone1[1] - 1 * dy), 
    'z4': (xy_zone1[0] + 0 * dx, xy_zone1[1] + - 2 * dy), 'z5': (xy_zone1[0] + 1 * dx, xy_zone1[1] - 2 * dy), 'z6': (xy_zone1[0] + 2 * dx, xy_zone1[1] - 2 * dy), 
    'z7': (xy_zone1[0] + 0 * dx, xy_zone1[1] - 3 * dy), 'z8': (xy_zone1[0] + 1 * dx, xy_zone1[1] - 3 * dy), 'z9': (xy_zone1[0] + 2 * dx, xy_zone1[1] - 3 * dy)}

# constructor 
    def __init__(self, stats: Stats, transparent = True, N: int = 1) -> None:
        self.stats = stats
        self.transparent = transparent
        # if we want plots (only implemented on duel locations yeu) on per-game basis
        self.N = N

# static methods
    # doooooon't know if we'll have any!

# non-static methods
    def make_all_duels_locations_image(self, number_text: bool = True) -> str:
        '''creates an image of all the duels at out_folder
            returns the relative link to the image'''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        d = self.stats.prints['duel zones']
        max_duels = max([sum(d[x].values()) for x in d])
        for zone in d:
            frac = sum(d[zone].values())/max_duels
            c = gf.rgb255_to_rgb1(gf.faded_rgb_color(Plot.color_many, frac, Plot.color_few))
            ax.add_patch(Rectangle(Plot.xy_starting_zones[zone], Plot.dx, Plot.dy, color = c))
            if number_text:
                text = str(round(sum(d[zone].values())/self.N))
                plt.text(Plot.xy_starting_zones[zone][0] + Plot.dx/3, Plot.xy_starting_zones[zone][1] + Plot.dy/2, text, fontsize=20)
        self.make_color_palette(ax)
        #plt.title('Närkamper och brytningar per zon')
        # paint the transparent pitch image on top
        im = plt.imread(Plot.pitch_image)
        plt.imshow(im, alpha=1.0, zorder=1)
        ax.axis('off')
        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]} all duel locations.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        #plt.show()
        # done to save memory
        plt.close(fig)
        return output_image_link
    
    def make_duel_zones_per_team_image(self, team_in_possession: str, number_text: bool = True) -> str:
        '''creates an image of the duel zones per team at out_folder
            returns the relative link to the image'''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        d = self.stats.prints['duel zones per team'][team_in_possession]
        max_duels = max([d[x] for x in d])
        for zone in d:
            frac = d[zone]/max_duels
            c = gf.rgb255_to_rgb1(gf.faded_rgb_color(Plot.color_many, frac, Plot.color_few))
            ax.add_patch(Rectangle(Plot.xy_starting_zones[zone], Plot.dx, Plot.dy, color = c))
            if number_text:
                text = str(round(d[zone]/self.N))
                plt.text(Plot.xy_starting_zones[zone][0] + Plot.dx/3, Plot.xy_starting_zones[zone][1] + Plot.dy/2, text, fontsize=20)
        self.make_color_palette(ax)
        #plt.title('Närkamper och brytningar per zon')
        # paint the transparent pitch image on top
        im = plt.imread(Plot.pitch_image)
        plt.imshow(im, alpha=1.0, zorder=1)
        ax.axis('off')
        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]} {team_in_possession} duel zones per team.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        #plt.show()
        # done to save memory
        plt.close(fig)
        return output_image_link
    
    def make_all_freeshot_locations_image(self, number_text = True) -> str:
        '''creates an image of all the freeshots (frislag) at out_folder
            returns the relative link to the image'''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        d = self.stats.prints['freeshot zones']
        max_duels = max([sum(d[x].values()) for x in d])
        for zone in d:
            frac = sum(d[zone].values())/max_duels
            c = gf.rgb255_to_rgb1(gf.faded_rgb_color(Plot.color_many, frac, Plot.color_few))
            ax.add_patch(Rectangle(Plot.xy_starting_zones[zone], Plot.dx, Plot.dy, color = c))
            if number_text:
                text = str(round(sum(d[zone].values())/self.N))
                plt.text(Plot.xy_starting_zones[zone][0] + Plot.dx/3, Plot.xy_starting_zones[zone][1] + Plot.dy/2, text, fontsize=20)
        self.make_color_palette(ax)
        #plt.title('Närkamper och brytningar per zon')
        # paint the transparent pitch image on top
        im = plt.imread(Plot.pitch_image)
        plt.imshow(im, alpha=1.0, zorder=1)
        ax.axis('off')
        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]} all freeshot locations.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        #plt.show()
        # done to save memory
        plt.close(fig)
        return output_image_link

    def make_duel_winners_per_locations_image(self, text_type: str) -> str:
        '''creates an image of all the duel winners at out_folder
            returns the relative link to the image
            text_type is frac, procent or anything else'''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        d = self.stats.prints['duel zones']
        for zone in d:
            if sum(d[zone].values()) != 0:
                frac = d[zone][self.stats.main_team]/sum(d[zone].values())
            else:
                frac = 0 
            c = gf.rgb255_to_rgb1(gf.faded_rgb_color(Plot.color_many, frac, Plot.color_few))
            ax.add_patch(Rectangle(Plot.xy_starting_zones[zone], Plot.dx, Plot.dy, color = c))
            if text_type == 'frac':
                text = f'{d[zone][self.stats.main_team]}/{sum(d[zone].values())}'
            elif text_type == 'procent':
                text = f'{round(frac * 100)} %' 
            else:
                text = ''
            plt.text(Plot.xy_starting_zones[zone][0] + Plot.dx/5, Plot.xy_starting_zones[zone][1] + Plot.dy * 1/2, text, fontsize=15)

        self.make_color_palette(ax)
        # paint the transparent pitch image on top
        im = plt.imread(Plot.pitch_image)
        plt.imshow(im, alpha=1.0, zorder=1)
        ax.axis('off')
        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]} team won duel locations.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        # done to save memory
        plt.close(fig)
        return output_image_link

    def make_duel_winners_per_zone_and_team_image(self, team_in_possession: str, text_type: str) -> str:
        '''creates an image of the duel winners per team at out_folder
            returns the relative link to the image
            text_type is frac, procent or anything else'''
        # HÄR
        fig = plt.figure()
        ax = fig.add_subplot(111)
        d = self.stats.prints['duel winners per zone and team'][team_in_possession]
        for zone in d:
            if sum(d[zone].values()) != 0:
                frac = d[zone][self.stats.main_team]/sum(d[zone].values())
            else:
                frac = 0 
            c = gf.rgb255_to_rgb1(gf.faded_rgb_color(Plot.color_many, frac, Plot.color_few))
            ax.add_patch(Rectangle(Plot.xy_starting_zones[zone], Plot.dx, Plot.dy, color = c))
            if text_type == 'frac':
                text = f'{d[zone][self.stats.main_team]}/{sum(d[zone].values())}'
            elif text_type == 'procent':
                text = f'{round(frac * 100)} %' 
            else:
                text = ''
            plt.text(Plot.xy_starting_zones[zone][0] + Plot.dx/5, Plot.xy_starting_zones[zone][1] + Plot.dy * 1/2, text, fontsize=15)

        self.make_color_palette(ax)
        # paint the transparent pitch image on top
        im = plt.imread(Plot.pitch_image)
        plt.imshow(im, alpha=1.0, zorder=1)
        ax.axis('off')
        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]}{team_in_possession} duel winners per zone and team.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        # done to save memory
        plt.close(fig)
        return output_image_link
    
    def make_freeshots_made_per_locations_image(self, text_type: str) -> str:
        '''creates an image of all the freeshot shooters at out_folder
            returns the relative link to the image
            text_type is frac, procent or anything else'''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        d = self.stats.prints['freeshot zones']
        for zone in d:
            if sum(d[zone].values()) != 0:
                frac = d[zone][self.stats.main_team]/sum(d[zone].values())
            else:
                frac = 0 
            c = gf.rgb255_to_rgb1(gf.faded_rgb_color(Plot.color_many, frac, Plot.color_few))
            ax.add_patch(Rectangle(Plot.xy_starting_zones[zone], Plot.dx, Plot.dy, color = c))
            if text_type == 'frac':
                text = f'{d[zone][self.stats.main_team]}/{sum(d[zone].values())}'
            elif text_type == 'procent':
                text = f'{round(frac * 100)} %' 
            else:
                text = ''
            plt.text(Plot.xy_starting_zones[zone][0] + Plot.dx/5, Plot.xy_starting_zones[zone][1] + Plot.dy * 1/2, text, fontsize=15)

        self.make_color_palette(ax)
        # paint the transparent pitch image on top
        im = plt.imread(Plot.pitch_image)
        plt.imshow(im, alpha=1.0, zorder=1)
        ax.axis('off')
        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]} team won duel locations.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        # done to save memory
        plt.close(fig)
        return output_image_link


    def make_color_palette(self, ax, xy0 = 0, dxy = 170, steps = 5) -> None:
        '''draws the color palette on the figure'''
        for i in range(steps):
            c = gf.rgb255_to_rgb1(gf.faded_rgb_color(Plot.color_many, 1-i/steps, Plot.color_few))
            ax.add_patch(Rectangle([xy0, xy0 + dxy * i], dxy, dxy, color =c))


    def make_team_minute_bars(self, values : dict, title = '', ylabel = '', main_team_color = 'k', other_team_color = 'r', minute_step = 3) -> str:
        '''makes value bars every minute'''
        mtv = values[self.stats.main_team]
        otv = values[self.stats.opposite_team(self.stats.main_team)]
        x = np.array([i for i in range(len(mtv))])
        x_labels = [str(i) if i%minute_step == 0 else '' for i in range(len(mtv))]
        width = 0.25
        fig, ax = plt.subplots()
        
        ax.bar(x - width/2, mtv, width = width, color= main_team_color, label=constants.nicknames[self.stats.main_team]['full'])
        ax.bar(x + width/2, otv, width = width, color= other_team_color, label=constants.nicknames[self.stats.opposite_team(self.stats.main_team)]['full'])
        ax.set_xlabel('matchminut')
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        plt.xticks(x, x_labels)
        ax.legend()

        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]}{title}.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        # done to save memory
        plt.close(fig)
        return output_image_link

    def make_time_vertical_bars(self, values: list, title = '', xlabel = '', ylabel = '',
    main_team_color = 'k', other_team_color = 'r') -> str:
        '''makes a time plot with vertical bars, will mostly be used for parts of game stats 
            returns link to image'''
        main_team_values = [gf.readable_to_sec(x[self.stats.main_team]) for x in values]
        other_team_values = [gf.readable_to_sec(x[self.stats.opposite_team(self.stats.main_team)]) for x in values]
        width = 0.25
        x = np.arange(len(values))
        x_labels = [f'{i+1}/{len(values)}' for i in range(len(values))]

        fig, ax = plt.subplots()
        ax.bar(x - width/2, main_team_values, color = main_team_color, width = width, label=constants.nicknames[self.stats.main_team]['full'])
        ax.bar(x + width/2, other_team_values, color = other_team_color, width = width, label=constants.nicknames[self.stats.opposite_team(self.stats.main_team)]['full'])
        y = [0, max(main_team_values + other_team_values) + 60]
        y = [i * 60 for i in range(max(main_team_values + other_team_values)//60 + 2)]
        y_timedelta = [gf.sec_to_readable(s) for s in y]
        plt.yticks(y, y_timedelta)
        plt.xticks(x, x_labels)
        
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend()
        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]}{title}.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        # done to save memory
        plt.close(fig)
        return output_image_link

    def make_per_minute_bars(self, values: list, title = '', ylabel = '', color = 'k') -> str:
        '''makes a plot of the action each minute
            returns a link the the image'''
        labels = [str(i) if i%3 == 0 else '' for i in range(len(values))]
        plt.bar(labels, values, color = color)
        plt.ylabel(ylabel)
        plt.yticks([i for i in range(max(values) + 1)])
        #plt.xlabel('matchminut')
        plt.title(title)
        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]}{title}.png'
        plt.savefig(output_image_link, transparent=self.transparent) # , dpi=400)
        # done to save memory
        plt.close()
        return output_image_link  

    def make_value_vertical_bars(self, values: list, title = '', xlabel = '', ylabel = '',
     main_team_color = 'k', other_team_color = 'r', x_labels = None) -> str:
        '''makes a value plot with vertical bars, will mostly be used for parts of game stats 
        if x_labels = None we expect the x-axis to be parts of the game, else specify
            returns link to image'''
        main_team_values = [x[self.stats.main_team] for x in values]
        other_team_values = [x[self.stats.opposite_team(self.stats.main_team)] for x in values]
        width = 0.25
        x = np.arange(len(values))
        if x_labels == None:
            x_labels = [f'{i+1}/{len(values)}' for i in range(len(values))]

        fig, ax = plt.subplots()
        ax.bar(x - width/2, main_team_values, color = main_team_color, width = width, label=constants.nicknames[self.stats.main_team]['full'])
        ax.bar(x + width/2, other_team_values, color = other_team_color, width = width, label=constants.nicknames[self.stats.opposite_team(self.stats.main_team)]['full'])
        #y = [0, max(main_team_values + other_team_values) + 60]
        m = max(main_team_values + other_team_values)
        if m < 50: # this is probably a game report
            y = [i for i in range(m + 3)]
        else: # this is a season report most likely 
            y = [i for i in range(0, m + m//10 , m//10)]  
        #y_labels = [gf.sec_to_readable(s) for s in y]
        plt.yticks(y)
        plt.xticks(x, x_labels)
        
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend()
        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]}{title}.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        # done to save memory
        plt.close(fig)
        return output_image_link

    def make_expected_goals_over_time_image(self, title = 'xg over time', 
    main_team_color = 'k', other_team_color = 'r') -> str:
        '''makes a plot of the xg change over time
            returns link to image'''
        x = self.stats.prints['expected goals list']['x']
        main_team_values = self.stats.prints['expected goals list'][self.stats.main_team]
        other_team_values = self.stats.prints['expected goals list'][self.stats.opposite_team(self.stats.main_team)]
        main_team_goals = self.stats.prints['goals lists'][self.stats.main_team]
        other_team_goals = self.stats.prints['goals lists'][self.stats.opposite_team(self.stats.main_team)]
        
        
        x_axis = [i//60 + 1 for i in x]
    
        fig, ax = plt.subplots()
        plt.plot(x_axis,main_team_values, color = main_team_color, linewidth=2, label = f"{constants.nicknames[self.stats.main_team]['abbreviation']} XG")
        plt.plot(x_axis,main_team_goals, '--', color = main_team_color, linewidth=2, label = f"{constants.nicknames[self.stats.main_team]['abbreviation']} mål")
        plt.plot(x_axis,other_team_values, color = other_team_color, linewidth=2, label = f"{constants.nicknames[self.stats.opposite_team(self.stats.main_team)]['abbreviation']} XG")
        plt.plot(x_axis,other_team_goals, '--', color = other_team_color, linewidth=2, label = f"{constants.nicknames[self.stats.opposite_team(self.stats.main_team)]['abbreviation']} mål")
        plt.legend()
        plt.xlabel('Minuter')
        plt.ylabel('Mål')
        output_image_link = f'{Plot.out_folder}{self.stats.out[:-9]}{title}.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        # done to save memory
        plt.close(fig)

        return output_image_link

