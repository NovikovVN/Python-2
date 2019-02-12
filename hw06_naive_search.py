from memory_profiler import profile
from sys import getsizeof

@profile
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

    print('Байт:', getsizeof(prime_numbers))


if __name__ == "__main__":
    naive_search(180)
    input()