import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2*math.pi*self.__radius
    def get_area(self):
        return math.pi*self.__radius**2
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        if value >= 0:
            self.__radius = value

def main():
    circle = Circle(10)
    print(circle.get_circumference())
    print(circle.get_area())
    # print(circle.__radius)
    print(circle.get_radius())

if __name__ == '__main__':
    main()