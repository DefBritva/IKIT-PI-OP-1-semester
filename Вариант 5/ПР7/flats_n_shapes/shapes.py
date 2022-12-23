from polygon import Polygon
from shape import Shape
import math


class Triangle(Polygon):
    def __init__(self, color, flat_ind, vertices):
        super().__init__("triangle", color, flat_ind, vertices)

    def get_area(self):
        ver1, ver2, ver3 = self.vertices
        a, b, c = (ver2[0] - ver1[0], ver2[1] - ver1[1]), \
            (ver3[0] - ver2[0], ver3[1] - ver2[1]), \
            (ver1[0] - ver3[0], ver1[1] - ver3[1])
        len_a, len_b, len_c = math.sqrt(a[0] ** 2 + a[1] ** 2), \
            math.sqrt(b[0] ** 2 + b[1] ** 2), \
            math.sqrt(c[0] ** 2 + c[1] ** 2)
        p = (len_a + len_b + len_c) / 2
        return math.sqrt(p * (p - len_a) * (p - len_b) * (p - len_c))
        # rad_ang = math.acos((len_b ** 2 + len_c ** 2 - len_a ** 2) /
        #                     (2 * len_b * len_c))
        # area = round(math.sin(rad_ang) * len_b * len_c, 3)

    def __str__(self):
        return "Класс треугольника. Наследован от класса фигуры."


class Square(Polygon):
    def __init__(self, color, flat_ind, vertices):
        super().__init__("square", color, flat_ind, vertices)

    def get_area(self):
        return abs(self.vertices[0][0] - self.vertices[1][0]) ** 2

    def __str__(self):
        return "Класс квадрата. Наследован от класса многоугольника."


class Rectangle(Polygon):
    def __init__(self, color, flat_ind, vertices):
        super().__init__("rectangle", color, flat_ind, vertices)

    def get_area(self):
        return abs(self.vertices[0][0] - self.vertices[1][0]) * abs(self.vertices[0][1] - self.vertices[3][1])

    def __str__(self):
        return "Класс прямоугольника. Наследован от класса многоугольника."


class Circle(Shape):
    def __init__(self, color, flat_ind, center, rad):
        super().__init__("circle", color, flat_ind)
        self.center = center
        self.rad = rad

    def get_area(self):
        return math.pi * self.rad ** 2

    def __str__(self):
        return "Класс круга. Наследован от класса фигуры. " \
               "Свойства (помимо родительских):\n" \
               "Радиус (rad) int, Координаты центра (center) int(x, y)"
