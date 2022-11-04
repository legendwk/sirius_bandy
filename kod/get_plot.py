import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pptx.dml.color import ColorFormat, RGBColor

from get_stats import Stats
import constants
import general_functions as gf

class Plot:
# class variables
    # relative link to where the images are put
    out_folder = "..\\..\\bilder\\autogen\\"

    # colors of the scale
    color_many = RGBColor(255, 0, 0)
    color_few = RGBColor(255, 255, 255)

    # these are all due to the dimensions of the pitch image
    pitch_image = "..\\..\\bilder\\pptx\\bandtplan_transparent_no_zones.png"
    xy_zone1 = (338, 184) #(68, 33)
    dx = 944 # 1282 - 338 #301
    dy = 705 # 894 - 184 #225
    xy_starting_zones = {'z1': (xy_zone1[0] + 0 * dx, xy_zone1[1] + 0 * dy), 'z2': (xy_zone1[0] + 0 * dx, xy_zone1[1] + 1 * dy), 'z3': (xy_zone1[0] + 0 * dx, xy_zone1[1] + 2 * dy), 
    'z4': (xy_zone1[0] + 1 * dx, xy_zone1[1] + 0 * dy), 'z5': (xy_zone1[0] + 1 * dx, xy_zone1[1] + 1 * dy), 'z6': (xy_zone1[0] + 1 * dx, xy_zone1[1] + 2 * dy), 
    'z7': (xy_zone1[0] + 2 * dx, xy_zone1[1] + 0 * dy), 'z8': (xy_zone1[0] + 2 * dx, xy_zone1[1] + 1 * dy), 'z9': (xy_zone1[0] + 2 * dx, xy_zone1[1] + 2 * dy)}

# constructor 
    def __init__(self, stats: Stats, transparent = True) -> None:
        self.stats = stats
        self.transparent = transparent

# static methods
    # doooooon't know if we'll have any!

# non-static methods
    def make_all_duels_locations_image(self, number_text = True) -> str:
        '''creates an image of all the duels at out_folder
            returns the relative link to the image'''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        d = self.stats.prints['duel zones']
        max_duels = max([sum(d[x].values()) for x in d])
        for zone in d:
            frac = sum(d[zone].values())/max_duels
            # plt colors are in RGB [0, 1] instead of [1, 255]
            c = [x/255 for x in gf.faded_rgb_color(Plot.color_many, frac, Plot.color_few)]
            ax.add_patch(Rectangle(Plot.xy_starting_zones[zone], Plot.dx, Plot.dy, color = c))
            if number_text:
                text = str(sum(d[zone].values()))
                plt.text(Plot.xy_starting_zones[zone][0] + Plot.dx/3, Plot.xy_starting_zones[zone][1] + Plot.dy/2, text, fontsize=20)
        self.make_color_palette(ax)
        #plt.title('Närkamper och brytningar per zon')
        # paint the transparent pitch image on top
        im = plt.imread(Plot.pitch_image)
        plt.imshow(im, alpha=1.0, zorder=1)
        ax.axis('off')
        output_image_link = Plot.out_folder + self.stats.out[:-9] + ' all duel locations.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        return output_image_link

    def make_duel_winners_per_locations_image(self, text_type: str) -> str:
        '''creates an image of all the duel winners at out_folder
            returns the relative link to the image
            text_type is frac, procent or anything else'''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        d = self.stats.prints['duel zones']
        for zone in d:
            frac = d[zone][self.stats.main_team]/sum(d[zone].values())
            # plt colors are in RGB [0, 1] instead of [1, 255]
            c = [x/255 for x in gf.faded_rgb_color(Plot.color_many, frac, Plot.color_few)]
            ax.add_patch(Rectangle(Plot.xy_starting_zones[zone], Plot.dx, Plot.dy, color = c))
            if text_type == 'frac':
                text = f'{d[zone][self.stats.main_team]}/{sum(d[zone].values())}'
            elif text_type == 'procent':
                text = f'{round(frac * 100)} %' 
            else:
                text = ''
            plt.text(Plot.xy_starting_zones[zone][0] + Plot.dx/3, Plot.xy_starting_zones[zone][1] + Plot.dy/2, text, fontsize=15)

        self.make_color_palette(ax)
        #plt.title(f"{constants.nicknames[self.stats.main_team]['full']} vunna närkamper per zon")
        # paint the transparent pitch image on top
        im = plt.imread(Plot.pitch_image)
        plt.imshow(im, alpha=1.0, zorder=1)
        ax.axis('off')
        output_image_link = Plot.out_folder + self.stats.out[:-9] + ' team won duel locations.png'
        plt.savefig(output_image_link, transparent=self.transparent)
        return output_image_link


    def make_color_palette(self, ax, xy0 = 150, dxy = 170, steps = 5) -> None:
        '''draws the color palette on the figure'''
        for i in range(steps):
            c = [x/255 for x in gf.faded_rgb_color(Plot.color_many, 1-i/steps, Plot.color_few)]
            ax.add_patch(Rectangle([xy0, xy0 + dxy * i], dxy, dxy, color =c))
            
