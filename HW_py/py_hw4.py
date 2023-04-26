#!/user/bin/env python3

'''Используйте модуль времени, чтобы сравнить производительность «эффективного» метода
поиска простых чисел с простой реализацией (без перерывов, тестирования по всем числам и т.д.).
Проверьте несколько диапазонов поиска простых чисел (например, до 100, до 1000 и т. д.)'''

import time


def simple_prime(n):
    
    ''' Фунукція пошуку простих чисел, звичайний алгоритм  '''
    
    primes = []
    for num in range(2, n):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes


def efficient_prime(n):                 #решето Ератосфена
    
    ''' Фнукція пошуку простих чисел, алгортм решето Ератосфена'''
    
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i in range(n+1) if primes[i]]

ranges = [100, 1000, 10000]#, 100000]          # діапазони з завдання + добавив 100 000 для ще кращого порівняння. 30 на 0,01 це суттєво )


for n in ranges:                             # прогонка в циклі
    start_time = time.time()
    simple_prime(n)
    end_time = time.time()
    print(f"Простий метод для діапазону {n} з часом виконання {end_time - start_time:.4} секунд.")

    start_time = time.time()
    efficient_prime(n)
    end_time = time.time()
    print(f"Ефективний метод (Ератосфена) для діапазону {n} з часом виконання {(end_time - start_time):.4} секунд.\n")
    