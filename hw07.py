from random import randint, random, seed

# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100). Выведите на
# экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

seed(42)
orig_list = [randint(-100, 99) for _ in range(15)]
print('Массив 1:', orig_list)

def bubble_sort(orig_list):
    for i in range(len(orig_list), 0, -1):
        for j in range(i - 1):
            if orig_list[j] < orig_list[j + 1]:
                orig_list[j], orig_list[j + 1] = orig_list[j + 1], orig_list[j]
    return orig_list

print('Пузырьком по убыванию:', bubble_sort(orig_list))

def bubble_selection_sort(orig_list):
    for j in range(len(orig_list) - 1):
        f = False
        idx_max = j
        for i in range(j, len(orig_list) - j - 1):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                f = True
            if orig_list[i] > orig_list[idx_max]:
                idx_max = i
        if not f:
            continue
        if idx_max != j:
            orig_list[j], orig_list[idx_max] = orig_list[idx_max], orig_list[j]
    return orig_list

print('Пузырьком и выбором по убыванию:', bubble_selection_sort(orig_list))
print()

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
# и отсортированный массивы.

seed(21)
orig_list2 = [randint(0, 49) + round(random(), 3) for _ in range(15)]
print('Массив 2:', orig_list2)
print('Пузырьком и выбором по возрастанию:', bubble_selection_sort(orig_list2)[::-1])

def merge_sort(orig_list):
    if len(orig_list) <= 1:
        return orig_list
    middle = int(len(orig_list) / 2)
    left = merge_sort(orig_list[:middle])
    right = merge_sort(orig_list[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result.extend(left) # result += left
    else: #elif len(right) > 0:
        result.extend(right)
    return result

print('Слиянием по возрастанию:', merge_sort(orig_list2))
print()

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным
# образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий
# его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки
# исходного массива. Но если это слишком сложно, то используйте метод
# сортировки, который не рассматривался на уроках

seed(37)
m = 7
orig_list3 = [randint(-15, 49) + round(random(), 2) for _ in range(2 * m + 1)]
print('Массив 3:', orig_list3)

# В отсортированном массиве до медианы будет m элементов меньше/больше неё,
# а после - m элементов больше/меньше (всего 2m + 1). Для каждого элемента
# массива посчитаем количества больших и меньших его оставшихся элементов.
# Эти количества совпадут на медианном значении - при условии, что медиана в
# массиве одна или медианных элементов нечетное количество при общем нечетном
# количестве элементов массива (2m + 1).

for i in orig_list3:
    more, less = 0, 0
    for j in orig_list3:
        if i > j:
            more += 1
        elif i < j:
            less += 1
    if more == less:
        median = i
        break
print('Медиана:', median)

from numpy import median as np_median

print('Проверим по numpy:', np_median(orig_list3))

def gnome_sort(orig_list):
    i = 1
    while i < len(orig_list):
        if not i or orig_list[i - 1] <= orig_list[i]:
            i += 1
        else:
            orig_list[i], orig_list[i - 1] = orig_list[i - 1], orig_list[i]
            i -= 1
    return orig_list

print('Гномьей сортировкой по возрастанию:', gnome_sort(orig_list3))
print('m-й элемент:', gnome_sort(orig_list3)[m])