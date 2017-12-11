# Практичское задание sort
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Задача sort
#
# ЧАСТЬ 1
#
# Реализуйте два алгоритма сортировки: методом пузырька и быструю сортировку,
# протестируйте их работу с использованием пакета hypothesis
# (возможно использовать код из лекции по тестированию) и проанализируйте время
# выполнения сортировки двумя методами с помощью модуля timeit (см. файл example_sort.py

# Практичское задание sort
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Задача sort
#
# ЧАСТЬ 1
#
# Реализуйте два алгоритма сортировки: методом пузырька и быструю сортировку,
# протестируйте их работу с использованием пакета hypothesis
# (возможно использовать код из лекции по тестированию) и проанализируйте время
# выполнения сортировки двумя методами с помощью модуля timeit (см. файл example_sort.py)

# Пузырьек

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr

# Быстрая сортировка
def quick_sort(arr):
    if arr:
        head, *tail = arr
        return quick_sort([x for x in tail if x <= head]) + \
               [head] + \
               quick_sort([x for x in tail if x > head])
    return []


if __name__ == "__main__":
    pass



import timeit

print("TIMEIT")
print("bubble_sort : ", end='')
print(timeit.timeit("bubble_sort([1,2,3,4,5,6,7,8,9])", setup="from __main__ import bubble_sort", number=10))
print("quick_sort : ", end='')
print(timeit.timeit("quick_sort([1,2,3,4,5,6,7,8,9])", setup="from __main__ import quick_sort", number=10))
