N = int(input())
array = list(map(int, input().split()))
array.sort()

count = 0 
result = 0

for i in range(len(array)):
    X = array[i]
    count += 1
    if count == X:
        result += 1
        count = 0

print(result)