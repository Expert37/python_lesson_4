import random
print('1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);')
n = 100
list_name = ['Sergey', 'Kate', 'Sifia', 'Ivan', 'Nastya', 'Sveta', 'Mari', 'Dima', 'Olga', 'Oleg', 'Mike', 'Den', 'Alex', 'Vasya', 'Nik', 'Tom', 'Lena', 'Ulya', 'Sasha', 'Dasha']
# используем модуль random.choice для случайного выбора элементов непустой последовательности list_name
sampling = random.choices(list_name, k=n)

def func_name(n, list_name):
    return sampling
print(sampling)
print(len(sampling))
print()

print('2. Напишите функцию вывода самого частого имени из списка на выходе функции F;')
print(max(set(sampling), key=lambda x: sampling.count(x)),':')
'''
def pop_name(sampling):
    print(max(set(sampling), key=lambda x: sampling.count(x)))
    return sampling
print(list(max))
'''





