#Первое по популярности решение
def main(s):
    symbols = ["do", "let", "ne;", "<: ", " :>", "::=", ".", "\\n"]
    input_string = s
    for symbol in symbols:
        input_string = input_string.replace(symbol, " ")
    input_list = input_string.split()
    list_of_tuples = [(input_list[i], int(input_list[i + 1])) for i in range(0, len(input_list) - 1, 2)]
    return list_of_tuples


##Второе по популярности решение
# def main(s):
#     k = ["do", "let", "ne;", "<: ", " :>", "::=", ".", "\n"]
#     list_of_tuples = []
#     input_string = s
#     input_string = input_string.replace(k[0], " ").replace(k[1], " ")
#     input_string = input_string.replace(k[2], " ").replace(k[3], " ")
#     input_string = input_string.replace(k[4], " ").replace(k[5], " ")
#     input_string = input_string.replace(k[6], " ").replace(k[7], " ")
#     input_string = input_string.split(" ")
#     new_list = []
#     for i in input_string:
#         if i != "":
#             new_list.append(i)
#     for i in range(0, len(new_list) - 1, 2):
#         list_of_tuples.append((new_list[i], int(new_list[i + 1])))
#     return list_of_tuples






input_string = "<: do let soat ::= 5521. done;do let isorge ::= 1596. done;do let gearxe_947 ::=-1944. done; :>"
input_string2 = "<: do let ente::= 496. done; do let gequ ::= -5474. done; :>"
input_string3 = '<: do let soat ::= 5521. done;do let isorge ::= 1596. done;do let\ngearxe_947 ::=-1944. done; :>'
input_string4 = '<: do let cesoin ::= -8045. done; do let enus ::= 5595. done; :>'
input_string5 = '<: do let gear_736 ::= -3814. done; do let anbe ::=5132. done; do let\nerinza_449 ::= 500. done;do let riri_876::=1021. done;:>'
input_string6 = '<:do let marabe_7 ::=-1644. done; do let eren_319 ::=6806. done; do\nlet zaleza ::= 6167. done;:>'
print(main(input_string))
print(main(input_string2))
print(main(input_string3))
print(main(input_string4))
print(main(input_string5))
print(main(input_string6))
