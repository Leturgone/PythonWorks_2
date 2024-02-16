#Первый вариант
from math import atan, acos

def main(x, y):
    x1 = 65 + (atan(x - y**3 - y**2)) ** 3
    x3 = x**12 + (((1 + y**2 + x**3) ** 7) / 40)
    x2 = acos((x**2) / 84 - x**3) + y**3
    x4 = 3 * y**6 - (x**2 - x**3) ** 3
    z = ((x1 / x3 - x2 / x4))
    return z
#Второй вариант
# import math

# def main(x, y):
#     a = (65 + (math.atan(x - y**3 - y**2))**3)
#     b = (x**12 + (((1 + y**2 + x**3)**7)/40))
#     c = (math.acos((x**2)/84 - x**3) + y**3)
#     d = (3*y**6 - (x**2 - x**3)**3)

#     return ((a/b - c/d))

#Третий вариант
#import math


# def a(x, y):
#     return 65 + pow(math.atan(x - pow(y, 3) - pow(y, 2)), 3)


# def b(x, y):
#     return pow(x, 12) + pow((1 + pow(y, 2) + pow(x, 3)), 7) / 40


# def c(x, y):
#     return math.acos(pow(x, 2) / 84 - pow(x, 3)) + pow(y, 3)


# def d(x, y):
#     return 3 * pow(y, 6) - pow((pow(x, 2) - pow(x, 3)), 3)


# def main(x, y):
#     return a(x, y) / b(x, y) - c(x, y) / d(x, y)

#Четвертый вариант
# from math import atan, acos


# def a(x, y):
#     return 65 + pow(atan(x - pow(y, 3) - pow(y, 2)), 3)


# def b(x, y):
#     return pow(x, 12) + pow((1 + pow(y, 2) + pow(x, 3)), 7) / 40


# def c(x, y):
#     return acos(pow(x, 2) / 84 - pow(x, 3)) + pow(y, 3)


# def d(x, y):
#     return 3 * pow(y, 6) - pow((pow(x, 2) - pow(x, 3)), 3)


# def main(x, y):
#     return a(x, y) / b(x, y) - c(x, y) / d(x, y)



print(main(0.03, 0.45))
print(main(0.53, 0.89))
