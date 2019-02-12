from memory_profiler import profile

@profile
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


if __name__ == "__main__":
    eratosthenes_sieve2(180)
    input()