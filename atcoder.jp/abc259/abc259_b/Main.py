from sys import stdin
input = stdin.readline

import math

a, b, d = map(int, input().split())

a_dash = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
b_dash = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))
print(a_dash, b_dash)

