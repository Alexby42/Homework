"""REQUESTS"""
'''Запрос данных с ресурсов (сервисов и сайтов)'''
import requests as rq
var = rq.get('https://jsonplaceholder.typicode.com/posts/3').json()
print(var)
# С помощью библиотеки можно получать различные данные с интренет-ресурсов без использования браузера

"""PANDAS"""
'''Обработка и анализ структурированных табличных данных'''
import pandas as pd
df = pd.read_csv('csvfile.csv')
print(df)                                                   #Вывод таблицы
print(df.head(2))                                           #Вывод первых двух строк таблицы
grouped_data = df.groupby('Country').agg({'Units Sold': 'mean'})
print(grouped_data)                                         #Вывод сгруппированных данных
# Одна из самых популярных библиотек осуществляющая группировку, интеграцию, итерацию, повторное индексирование
# и представление данных с минимальным количеством команд

"""NUMPY"""
'''Различные математические расчеты при работе с многомерными массивами данных'''
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
c = a * b
print(c)
d = np.sin(c*np.pi/180)
print(d)
print(np.degrees(d))
# Быстрые вычисления с экономией памяти

"""MATPLOTLIB"""
'''Используется для визуализации данных в форме диаграмм и графиков, в том числе 3D'''
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.title("Пример линейного графика")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.plot(x, y, color='green', marker='o', markersize=7)
plt.show()
# Популярная библиотека позволяющая наиболее полно понять различные данные в виде создания не сложных графиков

"""PILLOW"""
'''Используется для обработки изображений и анимации'''
from PIL import Image, ImageEnhance, ImageFilter
with Image.open('kremlin.jpg') as img:
    img.load()
img.show()
enh = ImageEnhance.Contrast(img)
enh.enhance(1.8).show("30% more contrast")      #Добавление контраста
cropped_img = img.crop((130, 50, 250, 550))     #Обрезка
cropped_img.show()
blur_img = cropped_img.filter(ImageFilter.BLUR) #Размытие
blur_img.show()
cropped_img.save('sample_cropped.png')          #Конвертация
# Библиотека предоставляет широкие возможности обработки изображений различных форматов