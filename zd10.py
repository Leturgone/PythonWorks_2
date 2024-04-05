
#Над входной таблицей провести ряд преобразований:

# Удалить пустые столбцы.
#  Удалить пустые строки.
#   Преобразовать содержимое ячеек по примерам.
#    Транспонировать таблицу.
#




#----------------- Лирическое отступление -----------------

# Если бы вы знали как меня бесит когнетивная сложность, вы бы расплакались
# Я битый час уже сижу над тем чтобы найти первое рещение (700 человек, жестко полюбили вонючку жпт наверняка)
# Но я не могу, это ужас какой то, ну реально там когнетивные функции у МОЗГА ЧЕЛОВЕЧЕСКОГО, 
# ты машина, у тебя памяти 16 мегабайт, тебе надо код запускать, а не думать 
# ОЙ, А ЧТО ЕСЛИ ЧЕЛОВЕЧЕКУ БУДЕТ СЛОЖНО ПОНЯТЬ МОЙ КОД БЛИН
# КОМУ СЛОЖНО ПОНЯТЬ КОД, ГДЕ СИМВОЛЫ ЗАМЕНЯЮТСЯ, ПОКАЖИТЕ МНЕ ЭТОГО ЧЕЛОВЕКА, НУ ЧТО ЗА ЧУШЬ. 

# Когнитивная сложность кода превышена (11 > 10).

# Сложность функции "transform_content" составляет 11:

# ну поплачь об этом я не знаю, я поплакал теперь твоя очерель, придурок серверный

# Тильт, обажаю ЦАП ням ням

#УПД
# Отлично, я исправил сложность, и знаете что? ОН ЗАСЧИТАЛ ЭТО КАК ВТОРОЕ РЕШЕНИЕ, МДА, ПОТРАЧЕНОГО ВРЕМЕНИ ЖАЛЬ

#УПД2
# Я устал и хочу спать, опять сложность, если тут пандасом надо, я не знаю что я сделаю

#------------------------------------------------------





#Второй вариант решения
# def remove_empty_columns_and_rows(table):
#     # Удаление пустых столбцов
#     table = [list(filter(None, row)) for row in table]

#     # Удаление пустых строк
#     table = list(
#         filter(
#             lambda row: any(cell is not None for cell in row), table
#         )
#     )
#     return table

# def transform_cell_content(table):
#     # Преобразование содержимого ячеек
#     for i in range(len(table)):
#         for j in range(len(table[i])):
#             table[i][j] = str(table[i][j])
#             match j:
#                 case 0:
#                     table[i][j] = table[i][j].replace(",", "")
#                     table[i][j] = table[i][j].split()
#                     table[i][j] = (
#                         " ".join(
#                             [table[i][j][0], table[i][j][1][0]]
#                             ) + "."
#                         )
#                 case 1:
#                     year, month, day = table[i][j].split(
#                         "-"
#                     )
#                     table[i][j] = "/".join(
#                         [day, month, year[2:]]
#                         )  # Соединить день, месяц и две последние цифры года
#                 case 2:
#                     table[i][j] = table[i][j].replace("@", " ")
#                     table[i][j] = table[i][j].split()
#                     table[i][j] = table[i][j][0]
#                 case 3:
#                     table[i][j] = table[i][j].replace(" ", "")
#                     table[i][j] = table[i][j].replace("(", "")
#                     table[i][j] = table[i][j].replace(")", "-")
#                     table[i][j] = table[i][j].replace("-", " ").split()
#                     table[i][j] = "-".join(
#                         [table[i][j][0], table[i][j][1], table[i][j][2]]
#                         ) + table[i][j][3]
#     return table

# def transpose_table(table):
#     # Транспонирование таблицы
#     table = list(map(list, zip(*table)))
#     return table

# def main(table):
#     table = remove_empty_columns_and_rows(table)
#     table = transform_cell_content(table)
#     table = transpose_table(table)
#     return table


table = [
    [None,"Нумберг, А.Ч.", "2003-09-26", "numberg91@yandex.ru", "(466) 780-61-27"],
    [None,"Мелич, Н.Т.", "2000-09-26", "melic15@gmail.com", "(367) 085-68-88"],
    [None,"Занодий, И.Ч.","2000-08-13", "zanodij15@yandex.ru", "(938) 945-95-11"],
    [None,"Зимашяк, Е.Л.", "1999-03-25", "zimasak51@rambler.ru", "(427) 142-80-18"]
]

table1 = [[None, 'Нумберг, А.Ч.', '2003-09-26', 'numberg91@yandex.ru', '(466) 780-61-27'], 
          [None, None, None, None, None], 
          [None, 'Мелич, Н.Т.', '2000-09-26', 'melic15@gmail.com', '(367) 085-68-88'], 
          [None, 'Занодий, И.Ч.', '2000-08-13', 'zanodij15@yandex.ru', '(938) 945-95-11'], 
          [None, 'Зимашяк, Е.Л.', '1999-03-25', 'zimasak51@rambler.ru', '(427) 142-80-18']]
print(main(table1))