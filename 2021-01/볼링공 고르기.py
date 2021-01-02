N, M = map(int, input().split())
K = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(N):
        if i >= j or K[i] == K[j]:
            continue
        result += 1

print(result)