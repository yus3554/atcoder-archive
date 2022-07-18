#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

S = input()

flg = True

for i in range(3):
    if S.count(S[i]) == 1:
        print(S[i])
        flg = False
        break

if flg:
    print("-1")
