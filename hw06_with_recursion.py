from memory_profiler import profile

@profile
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


if __name__ == "__main__":
    with_recursion(800)
    input()