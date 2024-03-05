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


print(main(['OPAL', 1991, 'SLASH', 2019, 1973]))
print(main(['OPAL', 1968, 'CSV', 2007, 1966]))
print(main(['OPAL', 1968, 'EAGLE', 2019, 1966]))