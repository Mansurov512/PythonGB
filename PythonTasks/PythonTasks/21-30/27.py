# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел


def minAndMaxInStr(strOfNum: str) -> tuple:
    listOfNum = strOfNum.split()
    li = [int(el) for el in listOfNum]
    return min(li), max(li)  # Сергей сказал что не стоит использовть функции min и max 
                             # если не знаешь как они работают - могут спросить на собеседовании.


print(minAndMaxInStr('234 34 78 349'))

