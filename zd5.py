# Решение 1
# from math import sqrt

# def main(x,y):
#     n = len(x)
#     res = 0
#     for i in range(1, n+1):
#         index = n + 1 - i - 1
#         res += 14 * (sqrt(x[index - 1] ** 3 + 55 * y[index - 1])) ** 4
    
#     return 89 * res

#Решение 2
# from math import sqrt


# def main(x, y):
#     return 89 * sum(
#         14
#         * (
#             (
#                 sqrt(
#                     x[len(x) - i - 1 ] ** 3 + 55 * y[len(x) - i - 1]
#                     )
#                 ) ** 4
#             )
#         for i in range(1, len(x) + 1)
#     )



#Решение 3 
# from math import sqrt


# def main(x,y):
#     n = len(x)
#     res = 0
#     i = 1
#     while i<n+1:
#         index = n + 1 - i - 1
#         res += 14 * (sqrt(x[index - 1] ** 3 + 55 * y[index - 1])) ** 4
#         i+=1
    
#     return 89 * res
#решение 4
from math import sqrt
def fun(x,y,i,res):
    if(i > 0 ):
        a = 55 * y[len(x) - i - 1]
        res += 14 * (sqrt(x[len(x) - i - 1] ** 3 + a)) ** 4
        return fun(x,y,i - 1,res)
    return res
    
def main(x,y):
    return 89 * fun(x,y,len(x),0)
    
print(main([-0.62, 0.48, -0.66],[0.5, 0.08, 0.65]))

print(main([-0.14, 0.26, 0.2],[0.36, 0.06, 0.94]))
print(main([-0.46, 0.54, -0.7],[0.94, 0.4, 0.46]))

# 2518332.204408576
# 3833512.029878058
# 4705693.429793007