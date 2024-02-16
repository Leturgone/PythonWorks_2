
#Первый вариант

# import math as m
# def main(x):
#     if x < -23:
#         return x / 35
#     elif x >= -23 and x < 39:
#         return 81 * x**5 - 50
#     elif x >= 39 and x < 133:
#         return (74 * x**2) ** 2 - (m.atan(51 + 93 * x**2 + x**3)) ** 5
#     elif x >= 133:
#         return 51 * (m.log10(x)) ** 4

#Второй вариант
# from math import atan,log10
# def a(x):
#     return x / 35
# def b(x)->float:
#     return 81 * x**5 - 50
# def c(x)->float:
#     return (74 * x**2) ** 2 - (atan(51 + 93 * x**2 + x**3)) ** 5
# def d(x)->float:
#     return 51 * (log10(x)) ** 4
# def main(x):
#     if x < -23:
#         return a(x)
#     elif x >= -23 and x < 39:
#         return b(x)
#     elif x >= 39 and x < 133:
#         return c(x)
#     elif x >= 133:
#         return d(x)




#Третий способ

# import math


# def main(x):
#     return (
#         x / 35
#         if x < -23
#         else (
#             81 * x**5 - 50
#             if -23 <= x < 39
#             else (
#                 (74 * x**2) ** 2 - (math.atan(51 + 93 * x**2 + x**3)) ** 5
#                 if 39 <= x < 133
#                 else 51 * (math.log10(x)) ** 4
#             )
#         )
#     )


#Четвертый способ
# from math import atan, log10


# def main(x):
#     result = {
#         x < -23: x / 35,
#         -23 <= x < 39: 81 * x**5 - 50,
#         39 <= x < 133: (74 * x**2) ** 2 - (atan(51 + 93 * x**2 + x**3)) ** 5,
#     }.get(True, 51 * (log10(x)) ** 4 if x > 0 else float("-inf"))
#     return result

#Пятый способ
# import math 
# def func1(x):
#     return x / 35

# def func2(x):
#     return 81 * x ** 5 - 50

# def func3(x):
#     return (74 * x ** 2) ** 2 - (math.atan(51 + 93 * x ** 2 + x ** 3)) ** 5

# def func4(x):
#     return 51 * (math.log10(x)) ** 4
# def main(x):
#     range_funcs = {range(-1000000000,-23): func1,
#                 range(-23, 39): func2,
#                 range(39, 133): func3,
#                 range(133, 1000000000): func4}

#     for r, func in range_funcs.items():
#         if x in r:
#             return func(x)
#Шестой способ
from math import atan, log10
def main(x):
    num = {x < -23: lambda: x /35,
           -23 <= x < 39: lambda: 81 * x ** 5 - 50,
           39 <= x < 133: lambda: (74 * x**2) ** 2 - (atan(51 + 93 * x**2 + x**3)) ** 5,
           x >= 133: lambda: 51 * (log10(x)) ** 4}
    return num[True]()
print(main(-3))
print(main(101))