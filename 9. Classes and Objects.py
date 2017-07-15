import graphics
class Vector2D:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def xComponent(self):
        return self.x

    def yComponent(self):
        return self.y

    def magnitude(self):
        return (self.x**2 + self.y**2)**(1/2.0)

    def showVector(self):
        origin = Point(0,200)
        end = Point(self.x,200-self.y)
        l1 = Line(origin, end)
        w1 = GraphWin()
        l1.draw(w1)

v = Vector2D(3,4)
print v.xComponent()
print v.magnitude()

    
class Student:
    def __init__(self, name,stnumber,credit,point):
        self.name = name
        self.stnumber = stnumber
        self.credit = float(credit)
        self.points = float(points)

    def getName(self):
        return self.name

    def getStNumber(self):
        return self.stnumber

    def getCredit(self):
        return self.credit

    def getPoints(self):
        return self.points

    def gpa(self):
        return self.points/self.credit

