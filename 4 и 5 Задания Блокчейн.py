# Задание 4
a = 329
c = 571
d = 831

# Задание 5
one = 153 "00f3eecc8876dd74fd4556c76c979792305feee0c55113ac47d08db20cd2d88c" вставляем hash, который уже дан по заданию
two = 739  # пишим число, которое дано по заданию

# Ничего не тронгай ниже
import hashlib

x = 1
b = 1
print("Задание 4:")
o = str(hashlib.sha256(str(a).encode()).hexdigest())
print(o)
h = o + str(hashlib.sha256(str(c).encode()).hexdigest())
o = str(hashlib.sha256(str(h).encode()).hexdigest())
print(o)
j = o + str(hashlib.sha256(str(d).encode()).hexdigest())
o = str(hashlib.sha256(str(j).encode()).hexdigest())
print(o)
two1 = hashlib.sha256(str(two).encode()).hexdigest()
string = one + two1
while x != 1001:
    s = hashlib.sha256(str(b).encode()).hexdigest()
    gg = string
    gg += s
    gg = hashlib.sha256(str(gg).encode()).hexdigest()
    if gg[:2] == "00":
        i = gg
    x += 1
    b += 1
print()
print("Задание 5:")
print("В ответ пишешь: ", i)

