from sys import stdin
input = stdin.readline

N, M, X, T, D = map(int, input().split())


if X > M: # 0からMまでのを求める
    first_tall = T - (X * D)
    print(first_tall + (D * M))
else: # Tが答え
    print(T)

