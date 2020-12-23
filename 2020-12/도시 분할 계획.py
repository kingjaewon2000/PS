def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (N + 1)

result = 0
edges = []

for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    A, B, C = map(int, input().split())

    edges.append((C, A, B))

edges.sort()
last = 0

for edge in edges:
    C, A, B = edge

    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += C
        last = C

print(result - last)
