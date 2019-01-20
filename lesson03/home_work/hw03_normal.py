# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# def fibonacci(n, m):
#     nFirst = 1
#     nSecond = 1
#     i = 2
#     while i <= m:
#         if i >= n:
#             fibList.append(nFib)
#         nFib = nFirst + nSecond
#         nFirst = nSecond
#         nSecond = nFib
#         i += 1
#     return fibList
#
# fibList = []
# n = int(input("Введите с какого порядкового номера хотите получить последовательность Фибоначчи: "))
# m = int(input("И до какого порядкового номера: "))
# fibList = fibonacci(n,m)
# print(fibList)
#    pass

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# def sort_to_max(origin_list):
#     i = 0
#     while i < len(origin_list) - 1:
#         a = origin_list[i]
#         b = origin_list[i+1]
#         if a > b:
#             origin_list[i] = b
#             origin_list[i+1] = a
#             i = -1
#         i += 1
#     return origin_list
#
# oList = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
# print(oList)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def func(a):
    if int(a) >= 0:
        return 1
    else:
        return 0
def filt(func,a):
    b = []
    for i in a:
        while func(i) == True:
            b.append(i)
            break
    return b
a = [1, -3, 5, 9]
print("Отфильтрованная последовательность: ", filt(func,a))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

