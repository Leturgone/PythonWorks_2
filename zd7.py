# #Первый способ
# def el_zero(x, left, mid, right):
#     if x[0] == "OPAL":
#         return left
#     if x[0] == "ELM":
#         return mid
#     if x[0] == "ZIMPL":
#         return right


# def el_one(x, left, mid, right):
#     if x[1] == 1991:
#         return left
#     if x[1] == 1968:
#         return mid
#     if x[1] == 1989:
#         return right


# def el_two(x, left, mid, right):
#     if x[2] == "EAGLE":
#         return left
#     if x[2] == "SLASH":
#         return mid
#     if x[2] == "CSV":
#         return right


# def el_three(x, left, right):
#     if x[3] == 2007:
#         return left
#     if x[3] == 2019:
#         return right


# def el_four(x, left, right):
#     if x[4] == 1973:
#         return left
#     if x[4] == 1966:
#         return right


# def main(x):
#     result = el_two(
#         x,
#         el_zero(
#             x,
#             el_three(x,
#                      0,
#                      el_one(x,1,2,3)),
#             el_four(x,
#                     4,
#                     el_one(x,5,6,7)),
#             el_three(x,
#                      el_four(x,8,9),
#                      10)
#             ), 
#         11, 
#         12)
#     return result

#Второй способ

# x = (
#     {"EAGLE", "OPAL", 2007},
#     {"EAGLE", "OPAL", 2019, 1991},
#     {"EAGLE", "OPAL", 2019, 1968},
#     {"EAGLE", "OPAL", 2019, 1989},
#     {"EAGLE", "ELM", 1973},
#     {"EAGLE", "ELM", 1966, 1991},
#     {"EAGLE", "ELM", 1966, 1968},
#     {"EAGLE", "ELM", 1966, 1989},
#     {"EAGLE", "ZIMPL", 2007, 1973},
#     {"EAGLE", "ZIMPL", 2007, 1966},
#     {"EAGLE", "ZIMPL", 2019},
#     {"SLASH"},
#     {"CSV"}
# )


# def main(x1):
#     s1 = set(x1)
#     return [i for i in range(len(x)) if not (len(x[i] - s1))][0]




#Третий способ 
# def el_zero(x, left, mid, right):
#     match x[0]:
#         case "OPAL":
#             return left
#         case "ELM":
#             return mid
#         case "ZIMPL":
#             return right


# def el_one(x, left, mid, right):
#     match x[1]:
#         case 1991:
#             return left
#         case 1968:
#             return mid
#         case 1989:
#             return right


# def el_two(x, left, mid, right):
#     match x[2]:
#         case "EAGLE":
#             return left
#         case "SLASH":
#             return mid
#         case "CSV":
#             return right


# def el_three(x, left, right):
#     match x[3]:
#         case 2007:
#             return left
#         case 2019:
#             return right


# def el_four(x, left, right):
#     match x[4]:
#         case 1973:
#             return left
#         case 1966:
#             return right


# def main(x):
#     result = el_two(
#         x,
#         el_zero(
#             x,
#             el_three(x, 0, el_one(x, 1, 2, 3)),
#             el_four(x, 4, el_one(x, 5, 6, 7)),
#             el_three(x, el_four(x, 8, 9), 10),
#         ),
#         11,
#         12,
#     )
#     return result

#Четвертый способ
# x = [
#     {"EAGLE", "OPAL", 2007},
#     {"EAGLE", "OPAL", 2019, 1991},
#     {"EAGLE", "OPAL", 2019, 1968},
#     {"EAGLE", "OPAL", 2019, 1989},
#     {"EAGLE", "ELM", 1973},
#     {"EAGLE", "ELM", 1966, 1991},
#     {"EAGLE", "ELM", 1966, 1968},
#     {"EAGLE", "ELM", 1966, 1989},
#     {"EAGLE", "ZIMPL", 2007, 1973},
#     {"EAGLE", "ZIMPL", 2007, 1966},
#     {"EAGLE", "ZIMPL", 2019},
#     {"SLASH"},
#     {"CSV"}
# ]


# def main(x1):
#     s1 = set(x1)
#     for i, v in enumerate(x):
#         if not(len(v - s1)):
#             return i

#Пятый способ

class tree():

    def __init__(self, number, top, topcon, mid, midcon, down, downcon):
        self.number = number
        self.top = top
        self.mid = mid
        self.down = down
        self.topCon = topcon
        self.midCon = midcon
        self.downCon = downcon

    def find(self, mas: list, ):
        if self.top == mas[self.number]:
            if (type(self.topCon) == int):
                return self.topCon
            return self.topCon.find(mas)
        if self.mid == mas[self.number]:
            if (type(self.midCon) == int):
                return self.midCon
            return self.midCon.find(mas)
        if self.down == mas[self.number]:
            if (type(self.downCon) == int):
                return self.downCon
            return self.downCon.find(mas)


def main(mas):
    x1 = tree(1, 1991, 1, 1968, 2, 1989, 3)
    x41 = tree(1, 1991, 5, 1968, 6, 1989, 7)
    x34 = tree(4, 1973, 8, None, None, 1966, 9)
    x3 = tree(3, 2007, 0, None, None, 2019, x1)
    x4 = tree(4, 1973, 4, None, None, 1966, x41)
    x03 = tree(3, 2007, x34, None, None, 2019, 10)
    x0 = tree(0, "OPAL", x3, "ELM", x4, "ZIMPL",x03)
    x2 = tree(2, "EAGLE", x0,"SLASH", 11, "CSV", 12)
    return x2.find(mas)



print(main(['OPAL', 1991, 'SLASH', 2019, 1973]))
print(main(['OPAL', 1968, 'CSV', 2007, 1966]))
print(main(['OPAL', 1968, 'EAGLE', 2019, 1966])) 
print(main(['ELM', 1991, 'EAGLE', 2007, 1966])) 
print(main(['ZIMPL', 1968, 'EAGLE', 2019, 1966]))
