#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

K = int(input())

ans_m = 21 * 60 + K

h = str(ans_m // 60)
m = str(ans_m % 60) if ans_m % 60 >= 10 else ("0" + str(ans_m % 60))

print(h + ":" + m)
