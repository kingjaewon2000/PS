from collections import deque
import copy

N = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
timetable = [0] * (N + 1) 

def topology_sort(N):
    indegree_copy = copy.deepcopy(indegree)
    q = deque()
    min_time = 0
    min_value = int(1e9)

    for i in range(1, N + 1):
        if indegree_copy[i] == 0:
            min_value = min(min_value, timetable[i])
            q.append(i)
            
    min_time += min_value

    while q:
        min_value = int(1e9)
        now = q.popleft()

        for i in graph[now]:
            indegree_copy[i] -= 1
            
            if indegree_copy[i] == 0:
                min_value = min(min_value, timetable[i])
                q.append(i)
        
        if min_value < int(1e9):
            min_time += min_value

    print(min_time)

for i in range(1, N + 1):
    data = list(map(int, input().split()))

    for j in range(1, len(data)):
        if data[j] == -1:
            break

        graph[data[j]].append(i)
        indegree[i] += 1

    timetable[i] = data[0]

    topology_sort(i)