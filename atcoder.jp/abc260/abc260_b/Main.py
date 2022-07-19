#!/usr/bin/env python3

from sys import stdin
input = stdin.readline

# N: 受験者数, X: 数学の点が高い方からX人
# Y: 英語の点が高い方からY人, Z: 数学と英語の合計点が高い方からZ人
N, X, Y, Z = map(int, input().split())

# A: 数学の点数, B: 英語の点数
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 数学と英語の合計点
C = list(map(lambda x, y: x + y, A, B))

# 合格者削除
def del_pass(max_index: int):
    A[max_index] = -1
    B[max_index] = -1
    C[max_index] = -1

# 合格者抽出
def search_pass(pass_number_of_people: int, score_list: list, ans_list: list):
    for i in range(pass_number_of_people):
        max_index = score_list.index(max(score_list))
        del_pass(max_index)
        ans_list.append(max_index + 1)

# 実行
ans_list = []
search_pass(X, A, ans_list)
search_pass(Y, B, ans_list)
search_pass(Z, C, ans_list)

# 昇順でソート
ans_list = sorted(ans_list)

# 出力
print(*ans_list, sep='\n')
