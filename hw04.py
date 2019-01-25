import cProfile

# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

def with_recursion(n):
    def my_recursion4(i):
        if i == 1:
            return i
        else:
            return - my_recursion4(i-1)/2

    i, res = 1, 0
    while i <= n:
        res += my_recursion4(i)
        i += 1

    print('Сумма первых {} элементов посл-ти: {}'.format(n, res))

def without_recursion(n):
    i, s, res = 1, 0, 1
    while s <= n:
        i = -i/2
        res += i
        s += 1

    print('Сумма первых {} элементов посл-ти: {}'.format(n, res))

cProfile.run('with_recursion(100)')
cProfile.run('without_recursion(100)')

cProfile.run('with_recursion(800)')
cProfile.run('without_recursion(800)')

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность
# алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

def naive_search(n):
    prime_numbers = [2]
    i = prime_numbers[0]
    while len(prime_numbers) != n:
        i += 1
        for d in range(2, i):
            i_is_prime = True
            if i%d == 0:
                i_is_prime = False
                break
        if i_is_prime:
            prime_numbers.append(i)

    print(prime_numbers)

def eratosthenes_sieve2(m, mltplct=2):
    def eratosthenes_sieve(n):
        a = [0] * n
        for i in range(n):
            a[i] = i

        a[1] = 0

        m = 2
        while m < n:
            if a[m] != 0:
                j = m * 2
                while j < n:
                    a[j] = 0
                    j = j + m
            m += 1

        prime_numbers = []
        for i in a:
            if a[i] != 0:
                prime_numbers.append(a[i])

        return prime_numbers

    prime_numbers_count, n = 0, 100
    while prime_numbers_count <= m:
        prime_numbers = eratosthenes_sieve(n)
        prime_numbers_count = len(prime_numbers)
        n *= mltplct

    print(prime_numbers[0:m])


cProfile.run('naive_search(42)')
cProfile.run('eratosthenes_sieve2(42)')

cProfile.run('naive_search(180)')
cProfile.run('eratosthenes_sieve2(180)')

cProfile.run('naive_search(1800)')
cProfile.run('eratosthenes_sieve2(1800)')