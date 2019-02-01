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
    def tang(self):
        return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.l12 = Line(p1, p2)
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

#---------------------------Задание 2------------------------------------------------------------------

class Equal_Barrel:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.l12 = Line(p1, p2)
        self.l23 = Line(p2, p3)
        self.l34 = Line(p3, p4)
        self.l14 = Line(p1, p4)
        self.l13 = Line(p1, p3)
        self.l24 = Line(p1, p4)
    def is_equal_barrel(self):
        if self.l12.length() == self.l34.length() and self.l23.tang() == self.l14.tang():
            a = 1234 #  а - переменная порядка вершин
        elif self.l23.length() == self.l14.length() and self.l12.tang() == self.l34.tang():
            a = 2314
        elif self.l13.length() == self.l24.length() and self.l23.tang() == self.l14.tang():
            a = 1324
        else:
            print("Не равнобокая трапеция")
            return False
        l1 = (a, "Равнобокая трапеция")
        return l1

    def per_bar(self):
        if self.is_equal_barrel()[0] == 1234:
            per = self.l12.length() * 2 + self.l23.length() + self.l14.length()
        elif self.is_equal_barrel()[0] == 2314:
            per = self.l23.length() * 2 + self.l12.length() + self.l34.length()
        elif self.is_equal_barrel()[0] == 2314:
            per = self.l13.length() * 2 + self.l23.length() + self.l14.length()
        else:
            return print("Фигура не равнобокая трапеция")
        return per
    def square_bar(self):
        if self.is_equal_barrel()[0] == 1234:
            sq = (self.l23.length() + self.l14.length()) / 2 * math.sqrt(
                self.l12.length() ** 2 - ((self.l23.length() - self.l14.length()) ** 2) / 4)
        elif self.is_equal_barrel()[0] == 2314:
            sq = (self.l12.length() + self.l34.length()) / 2 * math.sqrt(
                self.l23.length() ** 2 - ((self.l12.length() - self.l34.length()) ** 2) / 4)
        elif self.is_equal_barrel()[0] == 2314:
            sq = (self.l23.length() + self.l14.length()) / 2 * math.sqrt(
                self.l13.length() ** 2 - ((self.l23.length() - self.l14.length()) ** 2) / 4)
        else:
            return ("Фигура не равнобокая трапеция")
        return sq

#---------------Тестирование-----------------------------------
p1 = Point("0,0")
p2 = Point("1,2")
p3 = Point("3,2")
p4 = Point("4,0")

bar = Equal_Barrel(p1,p2,p3,p4)
print(bar.is_equal_barrel()[1])
print("Площадь: ",bar.square_bar())
print("Периметр: ",bar.per_bar())



