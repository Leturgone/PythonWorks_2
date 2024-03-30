# import math
# import time
# import tkinter as tk
# import random
# import numpy as np
# from scipy.ndimage import gaussian_filter

# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()


# # def shader(x, y):
# #     # центры:
# #     center_x=0.5
# #     center_y=0.5
# #     pacman_r=0.4
# #     distance = math.sqrt((x - center_x)**2+(y-center_y)**2)
# #     eye_x = 0.4
# #     eye_y = 0.3
# #     eye_r=0.1
# #     mouth_start_angle = math.pi / -4
# #     mouth_end_angle =5*math.pi / -4
# #     if(x-eye_x)**2+(y-eye_y)**2<=eye_r**2:
# #         return 0,0,0
# #     #Если пиксель внутри пакмана а не в его рту то цвет желтый
# #     elif distance<=pacman_r and not(
# #         mouth_start_angle<=math.atan2(y-center_y,x - center_x )<= mouth_end_angle
# #     ):
# #         return 1,1,0
# #     else:
# #         return 0,0,0
# #     return x, y, 0
# def shader(x, y):
#     t = time.time() * 1000  # текущее время в миллисекундах
#     r = math.cos(math.sqrt(y**x**(x**2 + y**2)) * t) * 0.5
#     g = math.tan(x ** y * t) * 0.5
#     b = math.tan((x ** 2 + y ** 2)* t) * 0.5
#      # создайте изображение с помощью шейдера
#     img = np.array([[shader(i/256, j/256) for i in range(256)] for j in range(256)])

#     # примените Гауссово размытие к изображению
#     blurred_img = gaussian_filter(img, sigma=5)
#     return (r, r, r)

# main(shader)


# import math
# import time
# import tkinter as tk
# import random
# import numpy as np
# from scipy.ndimage import gaussian_filter

# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()

    
# def shader(x, y):
#     center_x1, center_y1 = 0.3, 0.3  # координаты центра первого круга
#     radius1 = 0.2  # радиус первого круга

#     # Параметры для второго круга
#     center_x2, center_y2 = 0.2, 0.3  # координаты центра второго круга
#     radius2 = 0.2  # радиус второго круга

#     # Параметры для третьего круга
#     center_x3, center_y3 = 0.2, 0.2 # координаты для центра третьего круга
#     radius3 = 0.2
#     # расстояние от данной точки до центра первого круга
#     distance1 = math.sqrt((x - center_x1)**2 + (y - center_y1)**2)
#     # расстояние от данной точки до центра второго круга
#     distance2 = math.sqrt((x - center_x2)**2 + (y - center_y2)**2)
#     # расстояние от данной точки до центра третьего круга 
#     distance3 = math.sqrt((x - center_x3)**2 + (y - center_y3)**2)

#     # нормализуем расстояние к диапазону [0, 1]
#     normalized_distance1 = min(distance1 / radius1, 1.0)
#     normalized_distance2 = min(distance2 / radius2, 1.0)
#     normalized_distance3 = min(distance3 / radius3, 1.0)

#     # создаем градиент для первого и второго кругов
#     gradient1 = 1 - normalized_distance1  # значение градиента будет уменьшаться с увеличением расстояния
#     gradient2 = 1 - normalized_distance2  # значение градиента будет уменьшаться с увеличением расстояния
#     gradient3 = 1 - normalized_distance3
#     # возвращаем цвет для каждого круга
#     color1 = 0, gradient1, 0  # зеленый
#     color2 = gradient2, 0, 0  # красный
#     color3 = 0, 0, gradient3 
#     # Если точка находится внутри обоих кругов, возвращаем желтый цвет
#     if distance1 <= radius1 and distance2 <= radius2 and distance3 <= radius3:
#         return gradient2, gradient1, gradient3 

#     # Если точка находится внутри первого круга, возвращаем цвет первого круга
#     if distance1 <= radius1:
#         return color1

#     # Если точка находится внутри второго круга, возвращаем цвет второго круга
#     if distance2 <= radius2:
#         return color2
    
#     if distance3<= radius3:
#         return color3

#     # Если точка находится вне обоих кругов, возвращаем черный цвет
#     return (0, 0, 0)

# main(shader)



# import math
# import time
# import tkinter as tk
# import random
# import numpy as np
# from scipy.ndimage import gaussian_filter

# def draw(shader, width, height):
#     image = bytearray((0, 0, 0) * width * height)
#     for y in range(height):
#         for x in range(width):
#             pos = (width * y + x) * 3
#             color = shader(x / width, y / height)
#             normalized = [max(min(int(c * 255), 255), 0) for c in color]
#             image[pos:pos + 3] = normalized
#     header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
#     return header + image


# def main(shader):
#     label = tk.Label()
#     img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
#     label.pack()
#     label.config(image=img)
#     tk.mainloop()

    
# def shader(x, y):
#     center_x1, center_y1 = 0.3, 0.3  # координаты центра первого круга
#     radius1 = 0.2  # радиус первого круга

#     # Параметры для второго круга
#     center_x2, center_y2 = 0.2, 0.3  # координаты центра второго круга
#     radius2 = 0.2  # радиус второго круга

#     # Параметры для третьего круга
#     center_x3, center_y3 = 0.2, 0.2 # координаты для центра третьего круга
#     radius3 = 0.2
#     # расстояние от данной точки до центра первого круга
#     distance1 = math.sqrt((x - center_x1)**2 + (y - center_y1)**2)
#     # расстояние от данной точки до центра второго круга
#     distance2 = math.sqrt((x - center_x2)**2 + (y - center_y2)**2)
#     # расстояние от данной точки до центра третьего круга 
#     distance3 = math.sqrt((x - center_x3)**2 + (y - center_y3)**2)

#     # нормализуем расстояние к диапазону [0, 1]
#     normalized_distance1 = min(distance1 / radius1, 1.0)
#     normalized_distance2 = min(distance2 / radius2, 1.0)
#     normalized_distance3 = min(distance3 / radius3, 1.0)

#     # создаем градиент для первого и второго кругов
#     gradient1 = 1 - normalized_distance1  # значение градиента будет уменьшаться с увеличением расстояния
#     gradient2 = 1 - normalized_distance2  # значение градиента будет уменьшаться с увеличением расстояния
#     gradient3 = 1 - normalized_distance3
#     # возвращаем цвет для каждого круга
#     color1 = 0, gradient1, 0  # зеленый
#     color2 = gradient2, 0, 0  # красный
#     color3 = 0, 0, gradient3 
#     # Если точка находится внутри обоих кругов, возвращаем желтый цвет
#     if distance1 <= radius1 and distance2 <= radius2 and distance3 <= radius3:
#         return gradient2, gradient1, gradient3 

#     # Если точка находится внутри первого круга, возвращаем цвет первого круга
#     if distance1 <= radius1:
#         return color1

#     # Если точка находится внутри второго круга, возвращаем цвет второго круга
#     if distance2 <= radius2:
#         return color2
    
#     if distance3<= radius3:
#         return color3

#     # Если точка находится вне обоих кругов, возвращаем черный цвет
#     return (0, 0, 0)

# main(shader)

# def shader(x, y):
#     # центры:
#     center_x=0.5
#     center_y=0.5
#     pacman_r=0.4
#     distance = math.sqrt((x - center_x)**2+(y-center_y)**2)
#     eye_x = 0.4
#     eye_y = 0.3
#     eye_r=0.1
#     mouth_start_angle = math.pi / -4
#     mouth_end_angle =5*math.pi / -4
#     if(x-eye_x)**2+(y-eye_y)**2<=eye_r**2:
#         return 0,0,0
#     #Если пиксель внутри пакмана а не в его рту то цвет желтый
#     elif distance<=pacman_r and not(
#         mouth_start_angle<=math.atan2(y-center_y,x - center_x )<= mouth_end_angle
#     ):
#         return 1,1,0
#     else:
#         return 0,0,0
#     return x, y, 0

# def F(x):
#     res=0
#     for i in range(x):
#         res+=16
#     return res

# print(F(2))


# a = '12222345'
# print(len(set(a)))
# a='123456'
# s = a[::-1]
# print(s)
# import ctypes
# import numpy as np
# def decrypt(v):
#     k = np.array([0, 4, 5, 1], dtype = np.uint32)
#     v0, v1 = v[0], v[1]
#     v0  = np.uint32(v0)
#     v1 = np.uint32(v1)
#     s1um = np.uint32(0xC6EF3720)
#     delta = np.uint32(0x9E3779B9)
#     k0, k1, k2, k3 = (k[0]), (k[1]), (k[2]), (k[3])
#     for i in range(32):
#         v1 = (v1 - (((v0 << 4) + k2) ^ (v0 + s1um) ^ ((v0 >> 5) + k3))) & 0xFFFFFFFF
#         v0 = (v0 - (((v1 << 4) + k0) ^ (v1 + s1um) ^ ((v1 >> 5) + k1))) & 0xFFFFFFFF
#         s1um = (s1um - delta) & 0xFFFFFFFF 
#     v[0], v[1] = v0, v1

# a = np.array([0xE3238557, 0x6204A1F8, 0xE6537611, 0x174E5747,
#                    0x5D954DA8, 0x8C2DFE97, 0x2911CB4C, 0x2CB7C66B,
#                    0xE7F185A0, 0xC7E3FA40, 0x42419867, 0x374044DF,
#                    0x2519F07D, 0x5A0C24D4, 0xF4A960C5, 0x31159418,
#                    0xF2768EC7, 0xAEAF14CF, 0x071B2C95, 0xC9F22699,
#                    0xFFB06F41, 0x2AC90051, 0xA53F035D, 0x830601A7,
#                    0xEB475702, 0x183BAA6F, 0x12626744, 0x9B75A72F,
#                    0x8DBFBFEC, 0x73C1A46E, 0xFFB06F41, 0x2AC90051,
#                    0x97C5E4E9, 0xB1C26A21, 0xDD4A3463, 0x6B71162F,
#                    0x8C075668, 0x7975D565, 0x6D95A700, 0x7272E637],dtype= np.uint32)
# # Расшифровка данных
# for i in range(0, len(a), 2):
#     decrypt(a[i:i+2])
# decoded_text = ''.join([chr(val) if 0 <= val < 0x110000 and val != 0xFFFD else '?' for val in a])
# print(decoded_text)

# def ham_dist(x,y):
#     a = bin(x ^ y)
#     c = 0 
#     for i in a:
#         if i == '1':
#             c= c+1
#     print(c)       

# ham_dist(0b1100, 0b0011)

# words = [["Коллеги,", "В то же время,", "Однако,", "Тем не менее,", 
#           "Следовательно,","Соответственно,","Вместе с тем,", "С другой стороны, "],
         
#          ["парадигма цифровой экономики","контекст цифровой трансформации",
#           "диджитализация бизнес-процессов", "прагматичный подход к цифровым платформам",
#           "совокупность сквозных технологий", "программа прорывных исследований",
#           "ускорение блокчейн-транзакций","экспоненциальный рост Big Data"],
#          ["открывает новые возможности для","выдвигает новые требования", 
#           "несёт в себе риски","расширяет горизонты", "заставляет искать варианты",
#           "не оставляет шанса для", "повышает вероятность","обостряет проблему"],
#          ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта",
#           "компрометации конфиденциальных", "универсальной коммодитизации", 
#           "несанкционированной кастомизации", "нормативного регулирования", "практического применения"],
#          ["знаний и компетенций.","непроверенных гипотез.","волатильных активов.",
#           "опасных экспериментов.","государственно-частных партнёрств.",
#           "цифровых следов граждан.", "нежелательных последствий.","внезапных открытий." ]]

# doc = ''
# for i in range(8):
#     sentence = ''
#     pr_word = ''
#     for j in range(5):
#         word = words[j][i]
#         if word != pr_word:
#             sentence += " " +word
#             pr_word = word
#     doc+= sentence.strip() + '.\n'  
# print(doc)

# import random

# def learn_model(text, prefix_length):
#     slovar_model = {}
#     for i in range(len(text) - prefix_length):
#         #подсчет количества символов
#         prefix = text[i:i + prefix_length]
#         next_char = text[i + prefix_length]
#         if prefix not in slovar_model:
#             slovar_model[prefix] = {}
#         if next_char not in slovar_model[prefix]:
#             slovar_model[prefix][next_char] = 1
#         else:
#             slovar_model[prefix][next_char] += 1
#     return slovar_model

# def generate_text(model, length):
#     prefix = random.choice(list(model.keys()))
#     result = prefix

#     for _ in range(length - len(prefix)):
#         if prefix not in model:
#             break
#         next_char = random.choices(
#             list(model[prefix].keys()),
#             weights=model[prefix].values()
#         )[0]
#         result += next_char
#         prefix = prefix[1:] + next_char

#     return result

# text = """Не жалею, не зову, не плачу,
# Все пройдет, как с белых яблонь дым.
# Увяданья золотом охваченный,
# Я не буду больше молодым.

# Ты теперь не так уж будешь биться,
# Сердце, тронутое холодком,
# И страна березового ситца
# Не заманит шляться босиком.

# Дух бродяжий! ты все реже, реже
# Расшевеливаешь пламень уст
# О, моя утраченная свежесть,
# Буйство глаз и половодье чувств!"""

# prefix_l = 6
# generated_l = 300
# model = learn_model(text, prefix_l)
# generated_text = generate_text(model, generated_l)
# print(generated_text)

# rooms = {
#     "комната1": {
#         "название": "Начало лабиринта",
#         "описание": "Вы в начале лабиринта. Сможете ли из него выбраться?",
#         "действия": {
#             "Проход на запад": "комната2"
#         }
#     },
#     "комната2": {
#         "название": "Комната №2",
#         "описание": "Вы находитесь в комнате №2.",
#         "действия": {
#             "Проход на запад": "комната3",
#             "Проход на восток": "комната1"
#         }
#     },
#     "комната3": {
#         "название": "Комната №3",
#         "описание": "Вы находитесь в комнате №3.",
#         "действия": {
#             "Проход на север": "комната2",
#             "Проход на восток": "комната4"
#         }
#     }
# }

# def game():
    

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# import random

# # Функция для генерации случайного симметричного спрайта
# def generate_random_symmetric_sprite(size=5):
#     sprite = np.random.randint(0, 2, size=(size, size // 2))
#     sprite = np.hstack((sprite, sprite[:, ::-1]))
#     return sprite

# # Функция для отображения спрайтов
# def display_sprites(sprites, cmaps):
#     fig, axs = plt.subplots(10, 20, figsize=(20, 10))
#     for i, sprite in enumerate(sprites):
#         r, c = i // 20, i % 20
#         axs[r, c].imshow(sprite, cmap=cmaps[i], interpolation='nearest')
#         axs[r, c].axis('off')
#     plt.show()

# # Создаем список цветовых карт
# color_lists = [
#     ['#1D2B53', '#7E2553'],
#     ['#008751', '#AB5236'],
#     ['#5F574F', '#C2C3C7'],
#     ['#FFF1E8', '#FF004D'],
#     ['#FFA300', '#FFEC27'],
# ]
# cmaps = [ListedColormap(colors) for colors in color_lists]

# # Задаем количество спрайтов, которые хотим сгенерировать
# num_sprites = 200

# # Генерируем спрайты и случайные цветовые карты
# sprites = [generate_random_symmetric_sprite() for _ in range(num_sprites)]
# random_cmaps = random.choices(cmaps, k=num_sprites)

# # Отображаем спрайты
# display_sprites(sprites, random_cmaps)

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('lego_sets.csv')
# #добавляем столбец
# df['contains_house'] = df['name'].str.contains('house')

# house_count = df['contains_house'].sum()

# print(f'Количество наборов с "дом" в названии: {house_count}')

# df['decade'] = (df['year']//10)*10
# dec = df['decade'].value_counts()
# print(dec)
# print(f'Среднее количество наборов в год: {round(dec.mean())}')

# thematic_count = df['theme'].value_counts()
# sub_thematic_count = df['subtheme'].value_counts()

# df = df.loc[df['theme'] == 'Bionicle']
# x = df['year']
# y = df['name']

# #df['bionicle'] = df['theme'].str.contains('Bionicle') + " " + df['name']


# plt.plot(x, y)
# plt.xlabel('Ось х') #Подпись для оси х
# plt.ylabel('Ось y') #Подпись для оси y
# plt.title('График') #Название
# plt.show()
# print(f'Cамая популярная тематика и подтематика: {thematic_count.idxmax()} {sub_thematic_count.idxmax()}')

# print()

# import matplotlib.pyplot as plt
# import numpy as np

# plt.clf()

# #ветвь дерева

# class branch():
#     def __init__(self, x, x2, y, y2):
#         self.x = x
#         self.y = y
#         self.x2 = x2
#         self.y2 = y2
#         self.grow_count = 0#количество разветвлений 
#         self.grow_x = 0
#         self.grow_y = 0
#         self.width = 1#ширина
#         self.child = []

#     def updateWidth(self):
#         #Рекурсивно обновляет ширину ветви на основе суммарной ширины всех ее дочерних ветвей.
#         width = 0
#         for i in range(len(self.child)):
#             width += self.child[i].updateWidth()
#         if width > 0:
#             self.width = width
#         return self.width

#     def plot(self):
#         #Рисует ветвь как линию с заданной шириной и цветом.
#         plt.plot([self.x, self.x2], [self.y, self.y2], linewidth=np.sqrt(self.width), color='black')

# branches = [branch(30, 30, -3, 0)]

# branches[0].plot()

# maxdist = 10
# mindist = 1

# x = np.random.random(300) * 70
# y = np.random.random(300) * 70

# for h in range(100):
#     for i in range(len(x) - 1, 0, -1):
#         #Для каждой точки в x и y находит ближайшую ветвь.
#         closest_branch = 0
#         dist = 1000
#         for j in range(len(branches)):
#             temp_dist = np.sqrt((x[i] - branches[j].x2)**2 + (y[i] - branches[j].y2)**2)
#             if temp_dist < dist:
#                 dist = temp_dist
#                 closest_branch = j
#         #Если точка находится слишком близко к ветви (меньше mindist), она удаляется из массивов.
#         if dist < mindist:
#             x = np.delete(x, i)
#             y = np.delete(y, i)
#         #Если точка находится достаточно близко к ветви (меньше maxdist), она заставляет ветвь расти в направлении точки.    
#         elif dist < maxdist:
#             branches[closest_branch].grow_count += 1
#             branches[closest_branch].grow_x += (x[i] - branches[closest_branch].x2) / dist
#             branches[closest_branch].grow_y += (y[i] - branches[closest_branch].y2) / dist
#         #Для каждой ветви, которая росла в течение этой итерации, создается новая дочерняя ветвь, которая становится частью дерева.
#     for i in range(len(branches)):
#         if branches[i].grow_count > 0:
#             newBranch = branch(branches[i].x2, branches[i].x2 + branches[i].grow_x / branches[i].grow_count,
#                                branches[i].y2, branches[i].y2 + branches[i].grow_y / branches[i].grow_count)
#             branches.append(newBranch)
#             branches[i].child.append(newBranch)
#             branches[i].grow_count = 0
#             branches[i].grow_x = 0
#             branches[i].grow_y = 0

# plt.clf()
# branches[0].updateWidth()

# for i in range(len(branches)):
#     branches[i].plot()

# plt.axis('equal')
# plt.show()

# class TAG:
#     def __init__(self, name):
#         self.name = name
#         self.tags = []

#     def __enter__(self):#когда входим в with
#         print(f"<{self.name}>")
#         return self

#     def __exit__(self, type, value, traceback):
#         print(f"</{self.name}>")#когда выходим из with

#     def __call__(self, *tags):#чтобы можно было использовать как функцию
#         if tags:
#             for tag in tags:
#                 print(tag)


# class HTML:
#     def __init__(self):
#         self.body = TAG('body')
#         self.div = TAG('div')
#         self.p = TAG('p')

#     def get_code(self):
#         pass


# html = HTML()
# with html.body:
#     with html.div:
#         with html.div:
#             html.p('Первая строка.')
#             html.p('Вторая строка.')
#         with html.div:
#             html.p('Третья строка.')




# import matplotlib.pyplot as plt
# import networkx as nx

# class Tree:
#     def __init__(self, val, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

#     def knut_visual_tree(self, TREE, parent = None, pos = None, x = 0, y = 0, level = 0, vert = 1.0, hor=1.0):
#         if pos is None:
#             pos = {self.val: (x, y)}  
#         else:
#             pos[self.val] = (x, y)

#         if parent is not None:
#             TREE.add_edge(parent, self.val)

#         if self.left:
#             pos = self.left.knut_visual_tree(TREE, self.val, pos, x - hor, y - vert, level + 1, vert, hor/2)
#         if self.right:
#             pos = self.right.knut_visual_tree(TREE, self.val, pos, x + hor, y - vert, level + 1, vert, hor/2)

#         return pos


# tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, None, Tree(7)))
# tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
# tree = Tree(1, tree_2, tree_8)

# TREE = nx.DiGraph()
# pos = tree.knut_visual_tree(TREE)
# plt.figure(figsize=(12, 8))
# nx.draw(TREE, pos, with_labels=True, arrows=True, node_color ='none')
# plt.show()

# import math
# from random import randint
# from tkinter import Tk, Canvas, Button

# CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600

# NODE_R = 15

# C1, C2, C3, C4 = 2, 50, 20000, 0.1

# DELAY = 10

# class Vec:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Node:
#     def __init__(self, text):
#         self.text = text
#         self.targets = []
#         self.vec = Vec(0, 0)

#     def to(self, *nodes):
#         for n in nodes:
#             self.targets.append(n)
#             n.targets.append(self)
#         return self

# class Graph:
#     def __init__(self):
#         self.nodes = []

#     def add(self, text):
#         self.nodes.append(Node(text))
#         return self.nodes[-1]

# def random_layout(nodes):
#     for n in nodes:
#         n.vec.x = randint(NODE_R * 4, CANVAS_WIDTH - NODE_R * 4 - 1)
#         n.vec.y = randint(NODE_R * 4, CANVAS_HEIGHT - NODE_R * 4 - 1)

# class GUI:
#     def __init__(self, root):
#         self.canvas = Canvas(root, width=CANVAS_WIDTH,
#                              height=CANVAS_HEIGHT, bg="white")
#         self.draw_button = Button(root, text="Draw", command=self.draw_graph)
#         self.canvas.pack()
#         self.draw_button.pack()
#         self.nodes = None

#     def draw_node(self, x, y, text, r=NODE_R):
#         self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="MistyRose2")
#         self.canvas.create_text(x, y, text=text)

#     def draw_graph(self):
#         self.canvas.delete("all")
#         random_layout(self.nodes)
#         self.force_layout()
#         self.draw_graph_items()

#     def draw_graph_items(self):
#         for n in self.nodes:
#             for t in n.targets:
#                 self.canvas.create_line(n.vec.x, n.vec.y, t.vec.x, t.vec.y)
#         for n in self.nodes:
#             self.draw_node(n.vec.x, n.vec.y, n.text)
    

#     def f_ball(self, u, v):
#         dx = v.vec.x - u.vec.x
#         dy = v.vec.y - u.vec.y
#         r = math.sqrt(dx**2 + dy**2)
#         force = C3 / (r**2)
#         return Vec(force * dx / r, force * dy / r)
    
    
#     def f_spring(self, u, v):
#         dx = v.vec.x - u.vec.x
#         dy = v.vec.y - u.vec.y
#         r = math.sqrt(dx**2 + dy**2)
#         force = C1 * (r - C2)
#         return Vec(force * dx / r, force * dy / r)

    
    
#     def force_layout(self):
#         forces = {node: Vec(0, 0) for node in self.nodes}

#         for node in self.nodes:
#             for target in node.targets:
#                 spring_force = self.f_spring(node, target)
#                 forces[node].x += spring_force.x
#                 forces[node].y += spring_force.y

#         for i, node in enumerate(self.nodes):
#             for other_node in self.nodes[i+1:]:
#                 ball_force = self.f_ball(node, other_node)
#                 forces[node].x += ball_force.x
#                 forces[node].y += ball_force.y
#                 forces[other_node].x -= ball_force.x
#                 forces[other_node].y -= ball_force.y

#         for node in self.nodes:
#             node.vec.x += C4 * forces[node].x
#             node.vec.y += C4 * forces[node].y

# root = Tk()
# gui = GUI(root)

# g = Graph()
# n1 = g.add("1")
# n2 = g.add("2")
# n3 = g.add("3")
# n4 = g.add("4")
# n5 = g.add("5")
# n6 = g.add("6")
# n7 = g.add("7")
# n1.to(n2, n3, n4, n5)
# n2.to(n5)
# n3.to(n2, n4)
# n6.to(n4, n1, n7)
# n7.to(n5, n1)

# gui.nodes = g.nodes

# root.mainloop()

import operator

# OP_NAMES = {0: 'push', 1: 'op', 2: 'call', 3: 'is', 4: 'to', 5: 'exit'}

# def not_implemented(vm):
#     raise RuntimeError('Not implemented!')

# LIB = { # Для быстрого задания большинства операций полезен модуль operator
#     '+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.floordiv, # Целочисленный вариант деления
#     '%': operator.mod,
#     '&':  operator.and_,
#     '|': operator.or_,
#     '^': operator.xor,
#     '<': operator.lt,
#     '>': operator.gt,
#     '=': operator.eq,
#     '<<': operator.lshift,
#     '>>': operator.rshift,
#     'if': not_implemented,
#     'for': not_implemented,
#     '.': lambda vm: print(vm.stack.pop()),
#     'emit': not_implemented,
#     '?': not_implemented,
#     'array': not_implemented,
#     '@': not_implemented,
#     '!': not_implemented
# }



# class VM:
#     def __init__(self, code):
#         self.stack = []
#         self.code = code
#         self.pc = 0
#     def run(self):
#         while self.pc < len(self.code):
#             op = self.code[self.pc]
#             self.pc += 1
#             if op in LIB:
#                 LIB[op]()
#             else:
#                 print("Invalid opcode:", op)

# def test_VM():
#     bytecode = [0, 2, 0, 2, 1, 2] 
#     vm = VM(bytecode)
#     vm.run()

# test_VM()

LIB = [
    '+', '-', '*', '/', '%', '&', '|', '^', '<', '>', '=', '<<', '>>', 'if',
    'for', '.', 'emit', '?', 'array', '@', '!'
]

class VM:
    def __init__(self, code):
        self.stack = []
        self.code = code
        self.pc = 0
        self.scope = {} 
        self.call_stack = []

    def run(self):
        while self.pc < len(self.code):
            instruction = self.code[self.pc]
            op_code = instruction & 0b111
            arg = instruction >> 3
            
            if op_code == 0:
                self.stack.append(arg)
                self.pc += 1
            elif op_code == 1:
                if arg < len(LIB):
                    operation = LIB[arg]
                    if operation == '+':
                        a = self.stack.pop()
                        b = self.stack.pop()
                        self.stack.append(a + b)
                    elif operation == '.':
                        print(self.stack.pop())
                    elif operation == 'emit':
                        print(chr(self.stack.pop()), end='')
                    elif operation == 'to':
                        var_name = self.stack.pop()
                        var_value = self.stack.pop()
                        self.local_scope[-1][var_name] = var_value
                    elif operation == 'from':
                        var_name = self.stack.pop()
                        for scope in reversed(self.local_scope):
                            if var_name in scope:
                                self.stack.append(scope[var_name])
                                break
                self.pc += 1
            elif op_code == 2:
                function_address = self.scope.get(arg, (0,0))[1]
                if function_address:
                    self.call_stack.append(self.pc)
                    self.pc = function_address
                else:
                    print("Function not found")
                    break
            elif op_code == 3:
                self.scope[arg] = ('function', self.pc + 1)
                self.pc += 1
            
        
            elif op_code == 4:
                if self.call_stack:
                    self.pc = self.call_stack.pop() + 1
                else:
                    break
            else:
                print("Unknown operation")
                break

LIB.extend(['+', '.', 'emit','to','from'])

bytecode = [31, 256, 129, 5, 8, 4, 16, 12, 24, 20, 2, 121, 26, 10, 121, 26, 18, 121, 26, 5,
 32, 4, 40, 12, 34, 2, 121, 26, 10, 121, 26, 5, 0, 27, 48, 4, 24, 35, 152, 43,
 42, 2, 121, 26, 5]

vm = VM(bytecode)
vm.run()