# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
import math
class Point:
    def __init__(self, string2=""):
        if string2 == "":
            self.x = 0
            self.y = 0
            return
        self.x = float(string2.split(',')[0])
        self.y = float(string2.split(',')[1])
    def fromCoords(self, x, y):
        self.x = x
        self.y = y
        return self
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def length(self):
        # pc = self.p1.y
        return math.sqrt((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2)
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.l12 = Line(p1,p2)
        self.l23 = Line(p2, p3)
        self.l31 = Line(p3, p1)
    def perimeter(self):
        return self.l12.length() + self.l23.length() + self.l31.length()
    def square(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.l12.length()) * (p - self.l23.length()) * (p - self.l31.length()))
    def height(self, pointNum):
        if pointNum == 1:
            return 2 * self.square() / self.l23.length()
        if pointNum == 2:
            return 2 * self.square() / self.l31.length()
        if pointNum == 3:
            return 2 * self.square() / self.l12.length()

p1 = Point("1,4")
p2 = Point("-5,3")
p3 = Point("4,-3")

t1 = Triangle(p1,p2,p3)
print("Площадь: ", t1.square())
print("Высоты: ", t1.height(1), t1.height(2), t1.height(3))
print("Периметр: ", t1.perimeter())






# class Triangle:
#     def __init__(self, dot1, dot2, dot3):

# p1 = Dot(input(print("Enter p1")))
p1 = Point().fromCoords(1, 2)
p2 = Point("4, 2")

line1 = Line(p1,p2)
line1.length()

#
# x1y1 = input(print("Введите координаты первой точки: "))
# x2y2 = input(print("Введите координаты второй точки: "))
# x3y3 = input(print("Введите координаты третьей точки: "))

