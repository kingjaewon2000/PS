case = int(input())

array = []

for _ in range(case):
    data = input().split()

    array.append([data[0], data[1]])

array.sort(key = lambda data : data[1])

for i in array:
    print(i[0], end = ' ')