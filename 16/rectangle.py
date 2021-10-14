class Rectangle:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getArea(self):
        return self.a * self.b
class Square:
    def __init__(self,a):
        self.a=a
    def getA(self):
        return self.a
    def getAreaSquare(self):
        return self.a ** 2

class Circle:
    def __init__(self,r):
        self.r=r
    def getR(self):
        return self.r
    def getS(self):
        return 3.14*self.r**2

