# 2. Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE,
# если не является — вывести FALSE. вариант 25

n = (input('введите целое число больше нуля '))
i = 1

while (type(n) != int): #запуская цикл while проверка типа данных переменных
    try:
        n = int(n) #преобразование переменной к целочисленному типу данных
        while True:
            if 3 ** i < n:
                i += 1
            else:
                print(3 ** i == n)
                break


    except ValueError:
        print('Вы ввели неверное значение!')      #если введено неверное значение задача пойдет заново
        n = (input('введите целое число больше нуля '))
