N, K = map(int, input().split())

A, B = list(map(int, input().split())), list(map(int, input().split()))
A.sort()
B.sort(reverse = True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))