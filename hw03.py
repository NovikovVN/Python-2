# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# любому из чисел в диапазоне от 2 до 9.

# делаем срезы исходного массива с шагом в каждый из делителей, начиная с
# первого кратного, и ищем длины получаемых срезов.

numbers = list(range(2, 100))
for i in range(2, 10):
    print('{} кратно {} элементов'.format(i, len(numbers[(i - 2) : 100 : i])))

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
# надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят
# четные числа.

numbers_2 = (8, 3, 15, 6, 4, 2, 1, 4, 5, 6, 0, 3, 4, 5)
indices_2 = []
for i in range(len(numbers_2)):
    if numbers_2[i]%2 == 0:
        indices_2.append(i)
print(indices_2)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

from random import randint, seed

# seed(30)
numbers_3 = [randint(0, 100) for _ in range(10)]
print(numbers_3)

(numbers_min, numbers_max) = (numbers_3[0], numbers_3[0])
(i_min, i_max) = (0, 0)
for i in range(len(numbers_3)):
    if numbers_3[i] < numbers_min:
        numbers_min = numbers_3[i]
        i_min = i
    if numbers_3[i] > numbers_max:
        numbers_max = numbers_3[i]
        i_max = i
# или:
i_min = numbers_3.index(min(numbers_3))
i_max = numbers_3.index(max(numbers_3))

numbers_3[i_min], numbers_3[i_max] = numbers_3[i_max], numbers_3[i_min]
print(numbers_3)

# 4. Определить, какое число в массиве встречается чаще всего.

numbers_4 = [2, 0, 4, 1, 4, 5, 2, 5, 0, 0, 4, 2, 0]

elements = list(set(numbers_4))
counts = []
for e in elements:
    counts.append(numbers_4.count(e))

top_elements = []
for e, c in zip(elements, counts):
    if c == max(counts):
        top_elements.append(e)

print(top_elements)

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве.

from random import randint, seed

# seed(30)
numbers_5 = [randint(-100, 100) for _ in range(10)]
print(numbers_5)

negative_numbers_5, negative_indices_5 = [], []
for i in range(len(numbers_5)):
    if numbers_5[i] < 0:
        negative_numbers_5.append(numbers_5[i])
        negative_indices_5.append(i)

if not negative_numbers_5 == []:
    negative_max = negative_numbers_5[0]
    i_max = negative_indices_5[0]
    for n, i in zip(negative_numbers_5, negative_indices_5):
        if n > negative_max:
            negative_max = n
            i_max = i
    # или:
    negative_max = max(negative_numbers_5)
    i_max = numbers_5.index(negative_max)
    print('Макс. отриц. элемент {} по индексу {}'.format(negative_max, i_max))
else:
    print('Отрицательных элементов в массиве нет!')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.

numbers_6 = [63, -72, -94, -30, -38, -43, -65, 88, 89, -74]
print(numbers_6)

(numbers_min, numbers_max) = (numbers_6[0], numbers_6[0])
(i_min, i_max) = (0, 0)
for i in range(len(numbers_6)):
    if numbers_6[i] < numbers_min:
        numbers_min = numbers_6[i]
        i_min = i
    if numbers_6[i] > numbers_max:
        numbers_max = numbers_6[i]
        i_max = i
# или:
i_min = numbers_6.index(min(numbers_6))
i_max = numbers_6.index(max(numbers_6))

if i_max < i_min:
    i_1, i_2 = i_max, i_min
else:
    i_1, i_2 = i_min, i_max

print(numbers_6[i_1+1:i_2])
s = 0
for n in numbers_6[i_1+1:i_2]:
    s += n
print('Сумма:', s)

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они
# могут быть как равны между собой (оба являться минимальными), так и
# различаться.

numbers_7 = [66, 25, 333, 333, 5, 1234, 5]
print(numbers_7)

i = 0
res = [0, 0]
while i < 2:
    res[i] = min(numbers_7)
    numbers_7.remove(res[i])
    i += 1
print('Два наименьших элемента:', res)

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов
# строк. Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

l, d = 5, 5
rows = tuple(range(l))
cols = tuple(range(d))

m = [[0 for j in cols] for i in rows]
for i in rows:
    s = 0
    for j in cols[:-1]:
        m[i][j] = float(input('Введите M[{}, {}]'.format(i + 1, j + 1)))
        s += m[i][j]
    m[i][d - 1] = s

for i in rows:
    print(m[i])

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

m = [[1.14, -43.01, 5.03, 0.12], [64.76, 3.32, 66.89, -0.87]]
rows = tuple(range(len(m)))
cols = tuple(range(len(m[0])))

for i in rows:
    print(m[i])

min_j = m[0]
for i in rows:
    for j in cols:
        if m[i][j] < min_j[j]:
            min_j[j] = m[i][j]

max_min_j = min_j[0]
for j in cols:
    if min_j[j] > max_min_j:
        max_min_j = min_j[j]
print(max_min_j)