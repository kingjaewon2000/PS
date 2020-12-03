import sys

N = int(input())
NArray = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
MArray = list(map(int, sys.stdin.readline().rstrip().split()))
NArray.sort()

def binary_search(array, target, start, end):
    if start > end:
        return "no"

    mid = (start + end) // 2

    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for target in MArray:
    print(binary_search(NArray, target, 0, N - 1), end = ' ')