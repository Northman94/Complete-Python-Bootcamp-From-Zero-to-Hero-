
# Fill in the Line class methods to accept coordinates as
# a pair of tuples and return the slope and distance of the line.

import math

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor2[1] - self.coor1[1]) ** 2 + (self.coor2[0] - self.coor1[0]) ** 2)

    def slope(self):
        return ((self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]))

# OR
class Line2:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        # Tuple unpacking:
        # Can't be initialized elsewhere:
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        # Tuple unpacking:
        # Can't be initialized elsewhere:
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return (y2 - y1) / (x2 - x1)
# - = - = - = - = - = - = - = - = - = - = -


coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)

li.distance()
# 9.433981132056603
li.slope()
# 1.6


# - = - = - = - = - = - = - = - = - = - = -

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * self.radius ** 2 * self.height

    def surface_area(self):
        return (2 * 3.14 * self.radius * self.height) + (2 * 3.14 * self.radius ** 2)


c = Cylinder(2,3)

# V = Pi * r^2 * h
c.volume()
# 56.52

# S = (2Pi*r*h) + 2Pi*r^2
c.surface_area()
# 94.2

