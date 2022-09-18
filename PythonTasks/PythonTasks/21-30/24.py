#24. Задайте список из вещественных чисел.
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

def ex24(listOfFloats, quantityFractionalParts): #указываем список и округление количества знаков после запятой
    fractionalParts = []
    for num in listOfFloats:
        value = (round(math.modf(num)[0], quantityFractionalParts))#отделяем дробную часть кортежем и выбираем её индексом [0], а после округляем до указанного знака после запятой
        if value == 0:
            continue
        else:
            fractionalParts.append(value) 
    return round((max(fractionalParts) - min(fractionalParts)), quantityFractionalParts)
    
print(ex24([1.1, 1.2, 3.5, 5, 10.055673], 3))
print(ex24([1.1, 1.2, 3.1, 5, 10.01], 3))
