from memory_profiler import profile
from numpy import array as np_array, arange as np_arange, append as np_append
from sys import getsizeof

@profile
def naive_search_with_np(n):
    prime_numbers = np_array([2])
    i = prime_numbers[0]
    while len(prime_numbers) != n:
        i += 1
        for d in np_arange(2, i):
            i_is_prime = True
            if i%d == 0:
                i_is_prime = False
                break
        if i_is_prime:
            prime_numbers = np_append(prime_numbers, i)

    print('Байт:', getsizeof(prime_numbers))


if __name__ == "__main__":
    naive_search_with_np(180)
    input()