from memory_profiler import profile

@profile
def without_recursion(n):
    i, s, res = 1, 0, 1
    while s <= n:
        i = -i/2
        res += i
        s += 1

    print('Сумма первых {} элементов посл-ти: {}'.format(n, res))

if __name__ == "__main__":
    without_recursion(800)
    input()