
# Первый способ
def main(m,a,y,b):
    z=0;
    e=0;
    for c in range(1,a+1):
        for j in range(1,m+1):
            z=z+((41*j**3-89*y-1)**5+(1+c/55)**7)
    for i in range(1,b+1):
        e=e+(91*i**4-56*i-i**3)
    
    return z-e

#Второй способ
# def main(m,a,y,b):
#     z=0;
#     e=0;
#     c=1;
#     i=1;
#     while(c<a+1):
#         j=1
#         while(j<m+1):
#              z=z+((41*j**3-89*y-1)**5+(1+c/55)**7)
#              j=j+1
#         c=c+1
#     while(i<b+1):
#         e=e+(91*i**4-56*i-i**3)
#         i=i+1
        
#     return z-e

#Третий способ

# def main(m, a, y, b):
#     z = sum(
#         [
#             (41 * j**3 - 89 * y - 1) ** 5 + (1 + c / 55) ** 7
#             for c in range(1, a + 1)
#             for j in range(1, m + 1)
#         ]
#     )
#     e = sum([91 * i**4 - 56 * i - i**3 for i in range(1, b + 1)])

#     return z - e
#Четвертый способ
# def main(m,a,y,b):
#     res1 = sum(((41*j**3-89*y-1)**5+(1+c/55)**7)
#               for c in range(1,a+1) for j in range(1,m+1))
#     res2 = sum((91*i**4-56*i-i**3)
#                for i in range(1,b+1))
#     return res1-res2

#Пятый спосб
# def main(m,a,y,b):
#     def cal_s(c,s,a):
#         if c>a:
#             return s
#         else:
#             s+=cal_z(c,1,0,m,a,y)
#             return cal_s(c+1,s,a)
    
#     def cal_z(c,j,z,m,a,y):
#         if j > m:
#             return z
#         else:
#             z += ((41*j**3-89*y-1)**5+(1+c/55)**7)
#             return cal_z(c,j+1,z,m,a,y)
    
#     def cal_e(i,e,b):
#         if i > b:
#             return e
#         else:
#             e += (91*i**4-56*i-i**3)
#             return cal_e(i+1,e,b)
    
#     s = cal_s(1,0,a)
#     e = cal_e(1,0,b)
    
#     return s - e
#Шестой способ
def cal_z(m, a, y, b, c=1, j=1, z=0):
    if c > a:
        return z
    elif j > m:
        return cal_z(m, a, y, b, c + 1, 1, z)
    else:
        z = z + ((41 * j**3 - 89 * y - 1)**5 + (1 + c / 55)**7)
        return cal_z(m, a, y, b, c, j + 1, z)

def cal_e(b, i=1, e=0):
    if i > b:
        return e
    else:
        e = e + (91 * i**4 - 56 * i - i**3)
        return cal_e(b, i + 1, e)

def main(m, a, y, b):
    z = cal_z(m, a, y, b)
    e = cal_e(b)
    return z - e

print(main(8,8,0.98,8))
