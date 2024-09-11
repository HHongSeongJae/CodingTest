# # BFS
# import sys
# from collections import deque

# input = sys.stdin.readline

# # N : 정점 , M : 간선
# N , M = map(int,input().split())

# # 연결 그래프 생성
# graph = [[] for _ in range(N + 1)] # 그래프 순회시 0번째를 표현하지 않기 위해 빈 배열 선언

# for i in range(M):
#     u,v = map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u) # ★ 무방향이므로 양쪽으로 해줘야한다.

# # 각 정점에 방문했는지 여부 확인
# visited = [0 for _ in range(N+1)]

# def bfs(graph, start):
#     queue = deque([start])
#     visited[start] = 1 # 노드 방문 처리

#     while queue:
#         q = queue.popleft()

#         for i in graph[q]: # 해당 정점에 연결된 노드 확인
#             if visited[i] == 0: # 방문 안했다면 방문
#                 visited[i] = 1  # 방문 처리
#                 queue.append(i)

# count = 0
# # 모든 정점 확인
# for i in range(1,N+1):
#     if visited[i] == 0: # 방문안한 노드였다면 bfs 진행
#         bfs(graph, i)
#         count+=1

# print(count)

## DFS (재귀)
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n , m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    visited[v] = 1 # 현재 노드 방문처리

    for i in graph[v]: #노드에 인접한 노드 확인
        if visited[i] == 0: #방문 안했다면 bfs
            dfs(graph, i , visited)

count = 0
for i in range(1,n+1):
    if visited[i] == 0:
        dfs(graph, i , visited)
        count += 1

print(count)