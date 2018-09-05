# Проанализировать скорость и сложность алгоритмов в задаче:
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random
import time
import cProfile

# 1 вариант
def var_1():
    start = time.time()
    idx_min = 0
    idx_max = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    print(f"Min - {array[idx_min]} в ячейке {idx_min}; Max - {array[idx_max]} в ячейке {idx_max}")
    spam = array[idx_min]
    array[idx_min] = array[idx_max]
    array[idx_max] = spam
    print(array)
    print(time.time() - start)


# 2 вариант
def var_2():
    start = time.time()
    min_num = min(array)
    max_num = max(array)
    idx_min = array.index(min_num)
    idx_max = array.index(max_num)
    print(f"Min - {array[idx_min]} в ячейке {idx_min}; Max - {array[idx_max]} в ячейке {idx_max}")
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    print(array)
    print(time.time() - start)


SIZE = 10
array = [random.randint(-100,100) for _ in range(SIZE)]
print(array)
print
print("=" * 42)

var_1()
cProfile.run('var_1()')
print("=" * 42)

var_2()
cProfile.run('var_1()')