N = int(input())
A = list(map(int, input().split()))

ans = 0
while True:
  for i in range(len(A)):
    if A[i] % 2 == 0:
      A[i] /= 2
    else:
      break
  else:
    ans += 1
    continue
  break

print(ans)