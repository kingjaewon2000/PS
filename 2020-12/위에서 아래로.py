case = int(input())

array = [int(input()) for _ in range(case)]
array.sort(reverse=True)
for i in array:
    print(i, end = ' ')