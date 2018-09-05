# Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

import math
import time
import cProfile

# 1 вариант (решето Эратосфена)


def get_primes(n):
  m = n+1
  numbers = [True for i in range(m)]
  for i in range(2, int(math.sqrt(n))):
    if numbers[i]:
      for j in range(i*i, m, i):
        numbers[j] = False
  primes = []
  for i in range(2, m):
    if numbers[i]:
      primes.append(i)
  return primes

start = time.time()
primes = get_primes(10000)
print(time.time() - start)
print(get_primes(100))
array = get_primes(100)
print(array[10])
cProfile.run('get_primes(10000)')



# 2 вариант

def sundaram(n):
  b = list()
  a = [0] * n
  i = k = j = 0
  while 3 * i + 1 < n:
    while k < n and j <= i:
      a[k] = 1
      j += 1
      k = i + j + 2 * i * j
    i += 1
    k = j = 0

  for i in range(1, n):
    if a[i] == 0:
      b.append(2 * i + 1)
  return b


start = time.time()
b = sundaram(10000)
print(time.time() - start)
print(sundaram(50))
array_ = sundaram(100)
print(array_[9])
cProfile.run('sundaram(10000)')

