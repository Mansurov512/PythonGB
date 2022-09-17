#23. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def ex23(listOfNums):
    result = []
    lengthOfList = len(listOfNums)
    for i in range(lengthOfList // 2 + lengthOfList % 2):
        result.append(listOfNums[i] * listOfNums[lengthOfList - 1 - i])
    return result

print(ex23([2, 3, 4, 5, 6]))
print(ex23([2, 3, 5, 6]))
print(ex23([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))