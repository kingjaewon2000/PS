N = int(input())
array = list(map(int, input().split()))
array.sort()
result = 1

for x in array:
    if result < x:
        break
    result += x

print(result)    