import math
class Line():
    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2
    def slope(self):
        x1, y1 = self.cord1
        x2, y2 = self.cord2
        return (y2 - y1) / (x2 - x1)
    def length(self):
        x1, y1 = self.cord1
        x2, y2 = self.cord2
        return math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
cord1 = (3, 5)
cord2 = (1, 8)
line = Line(cord1, cord2) 
print(line.slope())
print(line.length())
