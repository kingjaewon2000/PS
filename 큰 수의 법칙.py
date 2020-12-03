N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

ret = 0
max_index = 0

for i in range(1, M + 1):
    max_index = 0
    if(i % K == 0):
        max_index = 1
    ret += arr[max_index]

print(ret)
