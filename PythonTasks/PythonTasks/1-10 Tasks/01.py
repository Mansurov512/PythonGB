 #1) По двум заданным числам проверить является ли одно квадратом второго 

a = int(input('Введите a = '))
b = int(input('Введите b = '))

if a**2 == b:
    print("b это квадрат a")
elif b**2 == a:
     print("a это квадрат b")
else:
     print("Числа не являются квадратами друг друга")
