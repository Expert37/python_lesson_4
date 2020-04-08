    # создадим глобальную переменную:
global_var = 10
# напишем простую функцию, у которой будет 2 параметра на вход: local_var_1 и local_var_2
def function_example(local_var_1, local_var_2): # эта функция будет просто их печатать
    print(local_var_1, local_var_2)
# вызовем функцию и передадим ей какие-нибудь параметры
function_example(11,12)
#---> 11 12

# попробуем в этой функции напечатать глобальную переменную global_var:
def function_example(local_var_1, local_var_2):
    print(local_var_1, local_var_2, global_var)
function_example(11,12)
#---> 11 12 10
# т.е. глобальные переменные можно использовать в рамках функции

# теперь попробуем изменить внутри функции значение глобальной переменной global_var:
def function_example_1(local_var_1, local_var_2):
    global_var = 20
    print(local_var_1, local_var_2, global_var, id(global_var))
function_example_1(11,12)
#---> 11 12 20
# но вопрос вот в чем: изменилось ли реальное значение global_var? Проверим:
print(global_var, id(global_var))
#---> 10
# т.е. в рамках функции function_example_1 переменная global_var = 20 не имеет ничего общего с глобальной переменной global_var, инициализированной в самом начале
# чтобы в этом убедиться можно вывести id этих переменных. Они будут разные.
# т.е. все переменные, которые создаются в рамках функции являются локальными и не могут быть глобальными.

# НО все равно в рамках функции значение глобальных переменных можно менять. Для этого используется служебное слово global:
def function_example_2(local_var_1, local_var_2):
    global global_var   # объявление для функции, что следующая переменная (в данном случае global_var)  будет глобальной
    print(local_var_1, local_var_2, global_var, id(global_var))
function_example_1(11,12)

    # nonlocal - с помощью nonlocal можно добавлять переопределение области во внутренней области
# создадим функцию (counter) и в ней инициализируем какую-нибудь переменную (num):
def counter():
    num = 0
    # в ней мы также инициализируем какую-то функцию (plus_one) и в этой функции добавим 1 к переменной num:
    def plus_one():
        nonlocal num    # определим локальную переменную num внутри функции counter
        num+=1
        return num  # и вернем данную переменную
    return plus_one # пусть counter возвращает функцию plus_one
counter()   # вызовем функцию counter
count = counter()
print(count())
print(count())
#---> 1
#---> 2




