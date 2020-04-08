    # Рекурсивные функции - это те функции, которые вызывают сами себя, но с разными параметрами
    # factorial
def fact(num):      # одно число на вход (num)
    if num == 0:     # если num равно 0, то
        return 1    # мы возвращаем значение 1
    else:
        return num*fact(num-1)  # иначе мы возващаем num умноженной на вызов той же самой функции fact но с параметром num-1

print(fact(10))

# сделаем то же самое с цикле (для сравнения)
factorial = 1
for i in range(1,11):
    factorial = factorial * i   # можно сократить так: factorial*=i
print(factorial)

    # напишем функцию для возведения в степень:
def degree(a,b):
    if b==0:
        return 1
    else:
        return a*degree(a,b-1)  # т.е. а умножаем на параметр (b-1). Т.е. мы каждый раз уменьшаем параметр b
print(degree(2,10))

# сделаем то же самое с цикле (для сравнения)
deg = 1
for i in range(1,11):
    deg = deg * 2
print(deg)


