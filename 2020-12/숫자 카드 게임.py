N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

min_arr = [min(arr[i]) for i in range(N)]
ret = max(min_arr)

print(ret)
