n = int(input("Введите целое число:")) # Просим пользователя ввести число
x = n % 2 # Находим остаток от деления
if x == 1: # Используем оператор ветвления if и задаем условие
    print("Число", n, "является нечетным") # Выведется, если условие будет истинно
else: # Оператор else будет выполнен, если условие будет ложно
    print("Число", n, "является четным") # Выведется, если условие будет ложно