#14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# (Подсчитать сумму цифр в вещественном числе.)
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

def ex1 (x):
    number = str(x)
    numbers=[]
    for char in number:
        if char == "." or char == ",":
            continue
        numbers.append(int(char))

    return sum(numbers)

print(ex1("12,34")) #если число вводим через запятую, то обязательны кавычки
print(ex1(1234))
print(ex1(12.34))