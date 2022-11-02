import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


import constants


image_link = r'C:\Users\vikin\Documents\Sirius Bandy\sirius_bandy\bilder\pptx\bandyplan_transparent1.png'
# coords in (x, y)




dx = 301
dy = 225
beginning_zone1 = (68, 33)
end_zone1 = (369, 257)
end_zone5 = (672, 480)
end_zone9 = (974, 708)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.add_patch(Rectangle(beginning_zone1, dx, dy)) #, color = constants.colors['sirius'][1])
ax.axis('off')

im = plt.imread(image_link)
implot = plt.imshow(im)
plt.show()

'''
fig = plt.figure()
ax = fig.add_subplot(111)
# put a blue dot (10,20)
#plt.scatter([10], [20])
# put a red dot, size 40, at 2 locations:
# vi försöker oss på en rektangel
ax.add_patch(Rectangle(beginning_zone1, dx, dy)) #, color = constants.colors['sirius'][1])
im = plt.imread(image_link)
implot = plt.imshow(im)
ax.axis('off')

'''


plt.show()