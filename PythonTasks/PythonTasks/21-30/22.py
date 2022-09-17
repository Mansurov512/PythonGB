﻿#22. Задайте список из нескольких чисел.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def ex22(listOfNums):
    result = 0
    for i in range(len(listOfNums) // 2):
        result += listOfNums[2 * i + 1]
    return result

print(ex22([222, 1, 555, 3, 111, 9, 122, 7])) #1+3+9+7=20
print(ex22([2, 3, 5, 9, 3])) #12