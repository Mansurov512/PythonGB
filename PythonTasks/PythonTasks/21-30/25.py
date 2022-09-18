#25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

def ex25(number):
     result = ''
     while number != 0:
         result += str(number % 2)
         number //= 2
     return result

print(ex25(45))
print(ex25(3))
print(ex25(2))