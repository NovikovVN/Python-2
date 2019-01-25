# 1. Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.

from collections import defaultdict

companies_count = int(input('Введите количество компаний: '))

company_info = defaultdict(list)
n = 0
while n < companies_count:
    company_name = input('Введите название {}-й компании: '.format(n + 1))
    company_profit = [0] * 4
    i = 0
    while i < 4:
        company_profit[i] = float(input('Прибыль {} за {}-й квартал'.format( \
                                                         company_name, i + 1)))
        i += 1
    company_info[company_name] = company_profit
    n += 1

average_profit = 0.
for company_profit in company_info.values():
    s = 0.
    for i in company_profit:
        s += i
    average_profit += s/4
average_profit /= companies_count

profit_yes, profit_no = [], []
for company_name, company_profit in company_info.items():
    s = 0.
    for i in company_profit:
        s += i
    if average_profit >= s/4:
        profit_yes.append(company_name)
    else:
        profit_no.append(company_name)

print('Средняя прибыль за год для всех предприятий:', average_profit)
if profit_yes:
    print('Предприятия с прибылью выше средней:', profit_yes)
if profit_no:
    print('Предприятия с прибылью ниже средней:', profit_no)

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При
# этом каждое число представляется как массив, элементы которого это цифры
# числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из
# модуля collections

from collections import deque

hexes = deque([str(s) for s in range(10)])
hexes.extend(['A', 'B', 'C', 'D', 'E', 'F'])

h_a = deque(input('Введите первое число (х16): ').upper())
h_b = deque(input('Введите второе число (х16): ').upper())
print(h_a)
print(h_b)

def hex_sum(h_a, h_b):
    h_a, h_b = h_a.copy(), h_b.copy()

    if len(h_a) > len(h_b):
        h_b.extendleft('0'*(len(h_a) - len(h_b)))
    elif len(h_a) < len(h_b):
        h_a.extendleft('0'*(len(h_b) - len(h_a)))

    h_a.reverse()
    h_b.reverse()

    d = 0
    h_sum = deque([])
    for a, b in zip(h_a, h_b):
        s = hexes.index(a) + hexes.index(b) + d
        if s > 16:
            d = 1
            h_sum.append(hexes[s-16])
        else:
            d = 0
            h_sum.append(hexes[s])
    if d:
        h_sum.append('1')

    h_sum.reverse()

    return h_sum

def hex_mul(h_a, h_b):
    h_a, h_b = h_a.copy(), h_b.copy()

    if len(h_a) > len(h_b):
       h_a, h_b = h_b, h_a

    h_a.reverse()
    h_b.reverse()

    h_mul = deque('0')
    for b in h_b:
        d = 0
        s = deque('')
        for a in h_a:
            m = hexes.index(b) * hexes.index(a) + d
            s.extend(hexes[m%16])
            d = m//16
        if d:
            s.extend(str(d))
        s.reverse()
        s.extend('0'*h_b.index(b))

        h_mul = hex_sum(h_mul, s)

    return h_mul

print('Сумма: ', hex_sum(h_a, h_b))
print('Произведение: ', hex_mul(h_a, h_b))