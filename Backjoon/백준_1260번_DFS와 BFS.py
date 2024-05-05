# a,b,c = map(int,input().split())

# graph = [[] for i in range(a+1)]

# for _ in range(b):
#     n, m = map(int,input().split())

#     #인접 리스트 그래프 생성
#     graph[n].append(m)
#     graph[m].append(n)

# #보편적으로 그래프에서는 낮은 순서대로 인접한 그래프를 유지한다.
# for i in graph:
#     i.sort()

# visited = [0] * (a+1)
# def dfs(graph, v, visited):
#     visited[v] = 1 # 현재 방문 노드
#     print(v, end =' ')

#     #현재 방문 노드에서 인접한 노드 순회
#     for i in graph[v]:
#         if visited[i] == 0: # 방문하지 않는 노드
#             dfs(graph, i, visited)

# from collections import deque

# dfs(graph, c, visited)

# print()

# visited = [0] * (a+1)
# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = 1 #현재노드 방문처리

#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')

#         for i in graph[v]:
#             if visited[i] == 0: # 방문하지 않는 노드
#                 queue.append(i) # 큐에 넣는다.
#                 visited[i] = 1 # 방문처리

# bfs(graph, c, visited)

## 2번째 풀이
n,m,v = map(int,input().split())

# 그래프 생성
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()
    
visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

# bfs :: 큐
from collections import deque


def bfs(graph, v, visited1):
    queue = deque([v])
    visited1[v] = 1 # 방문 처리
    
    while queue:
        temp = queue.popleft()
        print(temp , end=' ')
        
        for i in graph[temp]:
            if visited1[i] == 0:
                queue.append(i)
                visited1[i] = 1
    

# dfs :: 스택, 재귀

def dfs(graph,v,visited2):
    visited2[v] = 1  #현재노드 방문 처리
    print(v, end=' ')
    
    for i in graph[v]:
        if visited2[i] == 0:
            dfs(graph, i, visited2)

dfs(graph, v , visited2)
print()
bfs(graph, v, visited1)
