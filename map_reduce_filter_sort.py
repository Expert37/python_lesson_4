    # map - в переводе "отображение". На вход подается какая-то функция и список. Функция map к каждому элементу списка применяет функцию, которая подается на вход.
    # Схема: map(функция, список(элемент) к которому применяется функция)
# напишем функцию по переводу милей в км
def miles_to_km(miles): # определим функцию miles_to_km, на вход подаются мили (miles)
    return miles*1.6    # возвращаем значение мили*1,6

# теперь создадим список из значений:
miles_dist = [1, 1.6, 2.3]
# теперь применим функцию map:
km_dist = list(map(miles_to_km, miles_dist))    # на вход map подаем функцию (miles_to_km) и далее список (miles_dist)
print(km_dist)

# теперь перепишем этот пример с функцией lambda:
km_dist = list(map(lambda x: x*1.6, miles_dist))    # на вход map подаем функцию (lambda) и далее список (miles_dist) с которым работает функция lambda
print(km_dist)

# теперь подадим на вход 2 списка:
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = list(map(lambda x,y: x*y, list_1, list_2))
print(list_3)

    # reduce - функция производит какую-то операцию со всеми элементами списка
# сначала нужно сделать импорт функции reduce (начиная с питона 3)
from functools import reduce

# найдем с помощью функции reduce максимальный элемент
list_temp = [41,3,46,8,10,100,1,102]
max = reduce(lambda a,b: a if a>b else b,list_temp) # первый элемент это функция, второй элемент это массив (список)
        # lambda: берем два элемента (a и b) из list_temp и сравниваем между собой. Если a>b, то оставляем элемент a и сравниваем со следующим. Иначе берем b. И т.д.
        # таким образом reduce пройдет по всему листу и оставит максимальный элемент
print(max)

    # filter
# отсортируем предыдущий список и найдем элементы, которые больше 50:
list_4 = list(filter(lambda a: a>50,list_temp))
print(list_4)

    # sorted - это функция, которая на вход принимает список и возвращает список:
list_temp_sort = sorted(list_temp)
print(list_temp_sort)

# попробуем сортировку в обратном порядке:
list_temp_sort_reverse = sorted(list_temp, reverse=True)
print(list_temp_sort_reverse)

# сортировка по ключам
list_name = ['Kate', 'Sergey', 'Sofia', 'Ivan', 'Nastya']
list_name_sort = sorted(list_name)
print(list_name_sort)   # упорядочено будет в алфавитном порядке

# домустим мы хотим отсортировать данный список по 2-й букве:
list_name_sort_key = sorted(list_name, key = lambda x: x[1])    # x[1] - буква с индексом 1 (т.е. вторая буква)
print(list_name_sort_key)




