alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', \
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', \
            'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y','z')
alphabet_by_letter = dict(zip(alphabet, range(1, len(alphabet))))
alphabet_by_order = dict(enumerate(alphabet, start=1))

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
try:
    a = int(input('Введите любое трехзначное число: '))
except ValueError:
    print('Вы ввели не число!')
else:
    a_to_str = str(a)
    if len(str(a)) == 3:
        print('Сумма цифр:', int(a_to_str[0]) + int(a_to_str[1]) + int(a_to_str[2]))
        print('Произведение цифр:', int(a_to_str[0]) * int(a_to_str[1]) * int(a_to_str[2]))
    else:
        print('Вы ввели не трехзначное число!')

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

# В двоичной системе 5 - это 101, а 6 - это 110. Аналог операции И - это взятие минимума
# (если 0 и 0, результат 0; если 0 и 1, результат 0; если 1 и 1, результат 1),
# аналог ИЛИ - взятие максимума ((если 0 и 0, результат 0; если 0 и 1, результат 1;
# если 1 и 1, результат 1).

bin_5 = '101'
bin_6 = '110'

def in_dec(bin):
    res = 0
    for n, b in enumerate(bin[::-1]):
        res += int(b) * pow(2, n)
    return res

bin_and = ''
for b_5, b_6 in zip(bin_5, bin_6):
    bin_and += str(min(int(b_5), int(b_6)))

print('Результат побитовой операции (5 И 6) в 2-ной системе:', bin_and)
print('Результат побитовой операции (5 И 6) в 10-ной системе:', in_dec(bin_and)) #5&6

bin_or = ''
for b_5, b_6 in zip(bin_5, bin_6):
    bin_or += str(max(int(b_5), int(b_6)))

print('Результат побитовой операции (5 ИЛИ 6) в 2-ной системе:', bin_or)
print('Результат побитовой операции (5 ИЛИ 6) в 10-ной системе:', in_dec(bin_or)) #5|6

# При сдвиге к двоичному числу справа (если сдвиг влево) или слева (если сдвиг влево)
# дописывается то количество нулей, на сколько битов сдвигается число. Если сдвиг вправо,
# правая часть числа отрезается на количество бит сдвига. Поэтому при сдвиге вправо
# число уменьшается, влево - увеличивается.

shift_right = '00' + bin_5
shift_right = shift_right[:len(bin_5)]

print('Результат сдвига 5 на два бита вправо в 2-ной системе:', shift_right)
print('Результат сдвига 5 на два бита вправо в 10-ной системе:', in_dec(shift_right)) #5>>2

shift_left = bin_5 + '00'

print('Результат сдвига 5 на два бита влево в 2-ной системе:', shift_left)
print('Результат сдвига 5 на два бита влево в 10-ной системе:', in_dec(shift_left)) #5<<2

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y=kx+b, проходящей через эти точки.

# Уравнение прямой по двум точкам: (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)
# Из него:
# k = (y2 - y1) / (x2 - x1)
# b = - k * x1 + y1

try:
    x1 = float(input('Введите x1: '))
    y1 = float(input('Введите y1: '))
    x2 = float(input('Введите x2: '))
    y2 = float(input('Введите y2: '))
except ValueError:
    print('Вы ввели не число!')
else:
    if x1 == x2:
        print('Ошибка x1 = x2: прямая не имеет двух одинаковых абсцисс!')
    elif y1 == y2:
        print('Ошибка y1 = y2: прямая не имеет двух одинаковых ординат!')
    else:
        k = (y2 - y1) / (x2 - x1)
        b = - k * x1 + y1
        print('y = kx + b = {}*x + {}'.format(k, b))

# 4. Написать программу, которая генерирует в указанных пользователем границах:
# - случайное целое число;
# - случайное вещественное число;
# - случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти
# символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

try:
    l1 = int(input('Введите левую границу: '))
    l2 = int(input('Введите правую границу: '))
except ValueError:
    print('Вы ввели не число!')
else:
    if l1 == l2:
        print('Ошибка: границы совпадают!')
    else:
        if l1 > l2:
            l1, l2 = l2, l1
            print('Границы перепутаны! Значения поменяны местами')

        random_int = random.randint(l1, l2)
        print('Случайное целое число из [{}, {}]: {}'.format(l1, l2, random_int))

try:
    l1 = float(input('Введите левую границу: '))
    l2 = float(input('Введите правую границу: '))
except ValueError:
    print('Вы ввели не число!')
else:
    if l1 == l2:
        print('Ошибка: границы совпадают!')
    else:
        if l1 > l2:
            l1, l2 = l2, l1
            print('Границы перепутаны! Значения поменяны местами')

        ok = False
        while not ok:
            random_float = random.randint(l1, l2) + random.random()
            if l1 <= random_float <= l2:
                ok = True
        print('Случайное вещественное число из [{}, {}]: {}'.format(l1, l2, random_float))

l1 = input('Введите первую букву (LAT): ').lower()
l2 = input('Введите вторую букву (LAT): ').lower()
if not l1 in alphabet_by_letter or not l2 in alphabet_by_letter:
    print('Введена не буква латинского алфавита!')
else:
    if l1 == l2:
        print('Ошибка: границы совпадают!')
    else:
        l1_position = alphabet_by_letter[l1]
        l2_position = alphabet_by_letter[l2]

        if l1_position > l2_position:
            l1, l2 = l2, l1
            l1_position, l2_position = l2_position, l1_position

        random_position = random.randint(l1_position, l2_position)

        print('Случайная буква от {} до {}: {}'.format(l1, l2, alphabet_by_order[random_position]))

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита
# они стоят и сколько между ними находится букв.

l1 = input('Введите первую букву (LAT): ').lower()
l2 = input('Введите вторую букву (LAT): ').lower()
if not l1 in alphabet_by_letter or not l2 in alphabet_by_letter:
    print('Введена не буква латинского алфавита!')
else:
    l1_position = alphabet_by_letter[l1]
    l2_position = alphabet_by_letter[l2]
    print('Буква "{}" на {} месте'.format(l1, l1_position))
    print('Буква "{}" на {} месте'.format(l2, l2_position))
    print('Между ними {} букв'.format(abs(l1_position - l2_position) - 1))

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

try:
    l_position = int(input('Введите номер буквы: '))
except ValueError:
    print('Вы ввели не число!')
else:
    if not 0 < l_position <= len(alphabet):
        print('Буквы с номером {} в алфавите нет!'.format(l_position))
    else:
        print('Буква "{}" на {} месте'.format(alphabet_by_order[l_position], l_position))

# 7. По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой
# треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

# Треугольник всегда можно построить из трех ненулевых отрезков любой идлины.

try:
    ab = float(input('Введите AB: '))
    bc = float(input('Введите BC: '))
    ac = float(input('Введите AC: '))
except ValueError:
    print('Вы ввели не число!')
else:
    if ab <= 0 or bc <= 0 or ac <= 0:
        print('Длина сторон треугольника должна быть больше 0!')
    else:
        if ab == bc and bc == ac:
            print('Треугольник равнобедренный, равносторонний')
        elif ab == bc or bc == ac or ab == ac:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')

# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные;
# остальные годы, номер которых кратен 4, — високосные.

try:
    year = int(input('Введите год: '))
except ValueError:
    print('Вы ввели не число!')
else:
    if year%400 == 0:
        print('{}-й год високосный'.format(year))
    elif year%100 == 0:
        print('{}-й год не високосный'.format(year))
    elif year%4 == 0:
        print('{}-й год високосный'.format(year))
    else:
        print('{}-й год не високосный'.format(year))

# 9. Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

try:
    a = float(input('Введите A: '))
    b = float(input('Введите B: '))
    c = float(input('Введите C: '))
except ValueError:
    print('Вы ввели не число!')
else:
    if a == b or b == c or a == c:
        print('Два числа равны, поэтому среднего нет!')
    else:
        if b < a < c or c < a < b:
            print('Среднее A'.format(a))
        elif a < b < c or c < b < a:
            print('Среднее B'.format(b))
        else:
            print('Среднее C'.format(c))