#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

# N: レベル N の赤い宝石を 1 個
# レベル n の赤い宝石 (n は 2 以上) を「レベル n−1 の赤い宝石 1 個と、レベル n の青い宝石 X 個」に変換する。
# レベル n の青い宝石 (n は 2 以上) を「レベル n−1 の赤い宝石 1 個と、レベル n−1 の青い宝石 Y 個」に変換する。
N, X, Y = map(int, input().split())

# 宝石のレベルと個数リスト
redstone_list = [0,0,0,0,0,0,0,0,0,0]
bluestone_list = [0,0,0,0,0,0,0,0,0,0]
redstone_list[N-1] = 1

# 変換
for i in range(N - 1, 0, -1):
    # 赤い宝石の変換
    redstone_list[i - 1] = redstone_list[i - 1] + redstone_list[i]
    bluestone_list[i] = bluestone_list[i] + redstone_list[i] * X

    # 青い宝石の変換
    redstone_list[i - 1] = redstone_list[i - 1] + bluestone_list[i]
    bluestone_list[i - 1] = bluestone_list[i - 1] + bluestone_list[i] * Y

# 出力
print(bluestone_list[0])

