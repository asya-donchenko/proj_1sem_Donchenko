# 2. Даны координаты поля шахматной доски х, у (целые числа, лежащие в диапазоне 1-
# 8). Учитывая, что левое нижнее поле доски (1,1) является черным, проверить
# истинность высказывания: «Данное поле является белым»  вариант 25

x = input('введите первое целое число от 1 до 9 ')  #вводим значения для переменных с клавиатуры
y = input('введите второе целое число 1 до 9 ')
c = 0

while (type(x) != int) & (type(y) != int): #запуская цикл while проверка типа данных переменных
    try:
        x = int(x) #Перобразовываем наши введённые значения с целое число
        y = int(y)

        if (1<=x<=9) and (1<=y<=9): #проверяем входит ли число в заданный задачей диапазон
            c = (x + 2) % 2
            print(x, y)
            print("Данное поле является белым:", (c == 1))
        else:
            print('число больше девяти или меньше одного')


    except ValueError:
        print('Вы ввели не подходящее значение!')      #если введено неверное значение задача пойдет заново
        x = input('введите первое целое число от 1 до 9 ')
        y = input('введите второе целое число 1 до 9 ')