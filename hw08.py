from numpy import unique as np_unique
from pandas import DataFrame as pd_DataFrame
from random import choice, seed

# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

s = input('Введите любую строку из из маленьких латинских букв: ').lower()

sub_strings = set()
for sub_len in range(1, len(s)):
    for i in range(len(s) - sub_len + 1):
        sub = s[i : i + sub_len]
        sub_strings.add(sub)

# наивный поиск
naive_results = 0
for sub in sub_strings:
    sub_counts = 0
    sub_len = len(sub)
    for i in range(len(s)):
        if s[i : i + sub_len] == sub:
            sub_counts += 1
    naive_results += sub_counts

# Поиск подстроки в строке с использованием хеширования. Алгоритм Рабина-Карпа
hash_results = 0
for sub in sub_strings:
    sub_counts = 0
    sub_len = len(sub)
    h_sub = hash(sub)
    h_s = hash(s[0:sub_len])
    for i in range(len(s) - sub_len + 1):
        if h_sub == h_s:
            if s[i : i + sub_len] == sub:
                sub_counts += 1
        h_s = hash(s[i + 1: i + 1 + sub_len])
    hash_results += sub_counts

print(s)
print('Substrings count by naive search: {}'.format(naive_results))
print('Substrings count by Rabin-Karp with hash(): {}'.format(hash_results))


# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

seed(42)

message = input('Введите любую строку: ')
message_list = list(message)

message_symb, message_freq = np_unique(message_list, return_counts=True)

df = pd_DataFrame({'s': message_symb, 'f': message_freq})
message_dict = dict(zip(message_symb, ['' for _ in range(len(message_symb))]))

while df.shape[0] >= 2:
    df.sort_values(by=['f'], inplace=True) #by=['f', 's'], ascending=True
    i0, i1 = choice([[1, 0], [0, 1]])
    for s in message_dict:
        if s in df.iloc[i0].s:
            message_dict[s] = '0' + message_dict[s]
        if s in df.iloc[i1].s:
            message_dict[s] = '1' + message_dict[s]
    df = df.append(df.iloc[0:2].sum(), ignore_index=True)
    df = df.iloc[2:]

coded_message = message
for s in message_dict:
    coded_message = coded_message.replace(s, message_dict[s])

print(message)
print('Huffman table: {}'.format(message_dict))
print('Coded message: {}'.format(coded_message))