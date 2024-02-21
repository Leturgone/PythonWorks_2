#Первый вариант

# def main(n):
#     if(n==0):
#         return -0.6
#     elif (n==1):
#         return 0.94
#     else:
#         return (0.17-(main(n-1))**2- main(n-2))

#Второй способ
# def main(n):
#     a, b = -0.6, 0.94
#     for _ in range(n):
#         a, b = b, 0.17 - (b ** 2) - a
#     return a

# Третий способ
# def main(n):
#     values = [-0.6, 0.94]

#     for i in range(2, n + 1):
#         values.append(0.17 - values[i - 1] ** 2  - values[i - 2])

#     return values[n]
   


    
    
#Другой споспоб
#def main(n):
#     if(n==0):
#         return -0.6
#     elif (n==1):
#         return 0.94
#     else:
#         a = (0.17-(main(n-1))**2- main(n-2))
#         return a
#def main(n):
#     x, y = -0.6, 0.94
#     while n > 0:
#         x, y = y, 0.17 - y**2 - x
#         n -= 1
#     return x if n == 0 else y
# def main(n):
#     if n == 0:
#         return -0.6
#     elif n == 1:
#         return 0.94
#     else:
#         a, b = -0.6, 0.94
#         i = 2
#         while i <= n:
#             a, b = b, 0.17 - b**2 - a
#             i += 1
#         return b

#Пятый способ
# def main(n):
#     return (
#         -0.6 if n == 0 else
#         0.94 if n == 1 else
#         (lambda x: 0.17 - x[0] ** 2 - x[1])([main(n-1),main(n-2)])
#     )


# Четвертый способ
import math


def main(n):
    sign = n
    match sign:
        case 0:
            return -0.6
        case 1:
            return 0.94
    return 0.17 - (main(n - 1))** 2 - main(n - 2)

print(main(9))