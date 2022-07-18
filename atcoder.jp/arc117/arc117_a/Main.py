import math

A, B = map(int, input().split()) # Aが正の整数の数，Bが負の整数の数
Ea = []
Eb = []

is_big_a_b = True # trueならaがでかい
if A <= B:
    is_big_a_b = False

god_sum_half = 0
for i in range(A if is_big_a_b else B):
    god_sum_half += i + 1
    Ea.append(i + 1)
    Eb.append(i + 1)

temp = []
if is_big_a_b:
    temp = Eb
else:
    temp = Ea

for i in range(abs(A - B)):
    t = temp.pop()
    temp[-1] += t

if is_big_a_b:
    Eb = temp
else:
    Ea = temp

Eb = list(map(lambda x: -x, Eb))

print(*Ea, *Eb)
