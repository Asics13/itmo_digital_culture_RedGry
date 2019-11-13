from sys import argv
from typing import Tuple, List


def get_input_numbers() -> Tuple[int, int, int, int]:
    args = argv[1:]
    args_len = len(args)
    p = q = c = 0
    k = 4
    if args_len < 1:
        p, q, c, k = get_inputs()
    else:
        if args_len == 4:
            p, q, c, k = map(int, args)
        elif args_len == 3:
            p, q, c = map(int, args)
            k = 4
        else:
            exit("args: 4 - p, q, c, k")
    return p, q, c, k


def get_inputs() -> List[int]:
    keys = 'pqck'
    d = {key: 0 for key in keys}
    for key in d.keys():
        enter_key = 'enter %s: ' % key
        input_temp = input(enter_key)
        input_int = int(input_temp)
        d[key] = input_int
    values = list(d.values())
    return values


p, q, c, k = get_input_numbers()
print(p, q, c, k)
# 31 199 2671 4

a = [207, 238, 236, 239, 232, 228, 243]

# 2 Упражнение
# Самостоятельно разбиваешь свое большое число по количеству знаков и убираешь лишние нули в начале числа
# Пример: 312223953446223521130234         По 4 знака - нули слева! : 3122 2395 3446 2235 2113 234
# Через запятую загоняешь в массив
name = [813, 4634, 8043, 9195, 9486, 5901, 9585, 8703]

# Числа из зыкрытого ключа
# 1 число:
g = 8329
# 2 число:
l = 9617

# Эту часть кода лучше не трогай)))
b = ''
op = ''
p1 = p - 1
q1 = q - 1
N = p * q
for gg in range(N + 1):
    if (c * gg % (p1 * q1)) == 1:
        d = gg
for i in a:
    if k == 5:
        if int(i) ** c % N // 1000 == 0:
            h = ('00' + str(int(i) ** int(c) % N))
            b += h
        elif int(i) ** c % N // 10000 == 0:
            h = ('0' + str(int(i) ** int(c) % N))
            b += h
        else:
            b += str(int(i) ** int(c) % N)
    else:
        if int(i) ** c % N // 100 == 0:
            h = ('00' + str(int(i) ** int(c) % N))
            b += h
        elif int(i) ** c % N // 1000 == 0:
            h = ('0' + str(int(i) ** int(c) % N))
            b += h
        else:
            b += str(int(i) ** int(c) % N)
print('1 Уппажнение')
print('d =', d)
print('N =', N)
print(b)
print()
print('2 Упражнение')
print('Просто вставь это слово:')
for i in name:
    temp_in = i ** g % l
    temp_out = chr(temp_in + 848)
    op += temp_out
print(op)
