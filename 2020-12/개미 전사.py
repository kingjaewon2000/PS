N = int(input())
K = list(map(int, input().split()))
d = [0] * 101
d[1] = K[0]
d[2] = max(K[0], K[1])

for i in range(3, N + 1):
    d[i] = max(d[i - 1], d[i - 2] + K[i - 1])

print(d)
print(d[N])