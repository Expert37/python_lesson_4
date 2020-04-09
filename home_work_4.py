import random
print('1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);')
n = 100
list_name = ['Sergey', 'Kate', 'Sofia', 'Ivan', 'Nastya', 'Sveta', 'Mari', 'Dima', 'Olga', 'Oleg', 'Mike', 'Den', 'Alex', 'Vasya', 'Nik', 'Tom', 'Lena', 'Ulya', 'Sasha', 'Dasha']
# используем модуль random.choice для случайного выбора элементов непустой последовательности list_name
sampling = random.choices(list_name, k=n)

def func_name(n, list_name):
    return sampling
print(sampling)
print(len(sampling))
print()

print('2. Напишите функцию вывода самого частого имени из списка на выходе функции F;')
def pop_name(sampling):
    temp_dict = {i: sampling.count(i) for i in sampling}
    a = list(temp_dict.items())
    a.sort(key=lambda i: i[1], reverse=True)
    for i in a[0:1]:
        print(i[0], ':', i[1])
pop_name(sampling)
print()

print('3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.')
def red_name(sampling):
    first_letters = [i[0] for i in sampling]    # список из первых букв имен списка sampling
    temp_dict = {i: first_letters.count(i) for i in first_letters}  # словарь (буква:количество)
    a = list(temp_dict.items()) # приводим к формату list
    a.sort(key=lambda i: i[1])
    for i in a[0:1]:
        print(i[0], ':', i[1])
red_name(sampling)

