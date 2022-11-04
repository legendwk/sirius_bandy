import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from random import random as r
import constants
import general_functions as gf
from pptx.dml.color import ColorFormat, RGBColor



image_link = "..\\..\\bilder\\pptx\\bandyplan_transparent1.png"

dx = 301
dy = 225
beginning_zone1 = (68, 33)

d = {'z1': {'edsbyn': 0, 'sirius': 2}, 'z2': {'edsbyn': 1, 'sirius': 10}, 'z3': {'edsbyn': 3, 'sirius': 2}, 'z4': {'edsbyn': 6, 'sirius': 4},
 'z5': {'edsbyn': 13, 'sirius': 11}, 'z6': {'edsbyn': 7, 'sirius': 9}, 'z7': {'edsbyn': 3, 'sirius': 2},
  'z8': {'edsbyn': 11, 'sirius': 3}, 'z9': {'edsbyn': 3, 'sirius': 0}}

starting_zones = {'z1': (68 + 0 * dx, 33 + 0 * dy), 'z2': (68 + 0 * dx, 33 + 1 * dy), 'z3': (68 + 0 * dx, 33 + 2 * dy), 
'z4': (68 + 1 * dx, 33 + 0 * dy), 'z5': (68 + 1 * dx, 33 + 1 * dy), 'z6': (68 + 1 * dx, 33 + 2 * dy), 
'z7': (68 + 2 * dx, 33 + 0 * dy), 'z8': (68 + 2 * dx, 33 + 1 * dy), 'z9': (68 + 2 * dx, 33 + 2 * dy)}


constants
c_many = RGBColor(0, 0, 255)
c_few = RGBColor(255, 0, 0)

save_location = r''

max_duels = max([sum(d[x].values()) for x in d])

fig = plt.figure()
ax = fig.add_subplot(111)
for zone in d:
    frac = sum(d[zone].values())/max_duels
    # plt tar RGB i [0, 1] istället för [1, 255]
    c = [x/255 for x in gf.faded_rgb_color(c_many, frac, c_few)]
    ax.add_patch(Rectangle(starting_zones[zone], dx, dy, color = c))# [r() for i in range(3)])) 
 
# color palette placement
cp0 = 0
dcp = 50
for i in range(6):
    c = [x/255 for x in gf.faded_rgb_color(c_many, 1-i/5, c_few)]
    ax.add_patch(Rectangle([cp0, cp0 + dcp * i], dcp, dcp, color =c))
    print(type(ax))

plt.title('Närkamper och brytningar på planen')
im = plt.imread(image_link)
implot = plt.imshow(im, alpha=1.0, zorder=1)

ax.axis('off')
plt.savefig('hejhej.png', transparent=True)
plt.show()