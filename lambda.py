def ident(x):
    return(x)
print(ident(10))

# перепишем тоже самое в терминах lambda функции
print((lambda x: x) (10)) # синтаксис: (lambda x: x) - в функцию х подаем на вход х(т.е. ничего не делаем), затем вместо х подставляем (10)

# с помощью lambda функции мы можем определить функцию
ident_lambda = lambda x: x
print(ident_lambda(10))

# сделаем lambda функцию от 3 переменных
car = lambda brend, engine_volume, price: f'Car: {brend.title()}, Engine_volume: {engine_volume}, Price:{price}'
# f' - форматирование строки. После форматирования то, что в фигурных скобках будет заменено на свои переменные
print(car('volvo',1.5,1300000))


