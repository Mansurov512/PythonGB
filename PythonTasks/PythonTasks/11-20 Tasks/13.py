# 13 Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

first = "еще"
second = "ещещеще"
counter = 0

#print(len(first))
#print(len(second))

for i in range(len(second)):
    if i < len(second) - len(first):
        for j in range(len(first)):
                if second[i + j] == first[j]:
                    if j == len(first) - 1:
                        counter += 1
                    continue
                else:
                    break
    else:
        break

print(counter)