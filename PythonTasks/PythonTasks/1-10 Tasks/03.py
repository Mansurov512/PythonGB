# 3) Вывести на экран числа от -N до N

N = int(input('Введите N = '))

for i in range(-N,  N+1): #последнее число не включается в перечень, потому +1
    print(i, end=" ")# так в сторку выводит