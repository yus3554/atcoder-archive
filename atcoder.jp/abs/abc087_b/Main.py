A = int(input()) # 500円の枚数
B = int(input()) # 100円の枚数
C = int(input()) # 50円の枚数
X = int(input()) # ちょうどX円にする

ans = 0
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            if X == i * 500 + j * 100 + k * 50:
                ans += 1

print(ans)
