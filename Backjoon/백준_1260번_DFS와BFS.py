# import sys
# from collections import deque 

# N,M,V = map(int, input().split())

# def dfs(graph, start, visited = None):
#     if visited is None:
#         visited = set()
        
#     visited.add(start)
#     print(start, end=' ')
    
#     #keyerror문제 해결을 위한 코드
#     if(start not in graph):
#         return
    
#     #재귀를 이용한 DFS 구현
#     for n in graph[start]:
#         if n not in visited:
#             dfs(graph, n, visited)
    
# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     visited.add(start)
    
#    #queue를 이용한 BFS 구현
#     while queue:
#         n = queue.popleft()
#         print(n , end = ' ')
        
# 	#keyerror문제 해결을 위한 코드
#         if(n not in graph):  
#             return
        
#         for n in graph[n]:
#             if n not in visited:
#                 queue.append(n)
#                 visited.add(n)

# #그래프 생성
# graph = {}

# for i in range(M):
#     # a,b = map(int, input().split())
#     a,b = map(int, sys.stdin.readline().split())
    
#     if a not in graph:
#         graph[a] = [b]
#     else:
#         graph[a].append(b)
#         graph[a].sort()
        
#     if b not in graph:
#         graph[b] = [a]
#     else:
#         graph[b].append(a)
#         graph[b].sort()

# dfs(graph, V)
# print('\n', end='')
# bfs(graph, V)


##########################################################
# 2차 풀이
import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    # 양방향 그래프
    graph[a].append(b)
    graph[b].append(a)

# ★ 하나의 노드에서 여러 개의 경로가 있다면 작은 수의 노드부터 선택하게 하는 것이 문제의 조건
# ★ 그러므로 각 노드에서 인접한 노드를 오름차순으로 정렬하면 이를 구현 가능하다.
for j in range(1,N+1):
    graph[j].sort()

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1 # 방문 처리

    while queue:
        q = queue.popleft()
        print(q, end=" ") # 방문한 노드 표시

        # 인접 노드 확인
        for i in graph[q]:
            if visited[i] == 0: # 방문하지 않은 노드가 있다면
                visited[i] = 1 #방문처리
                queue.append(i)

def dfs(graph, start, visited):
    visited[start] = 1
    print(start , end=" ")

    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph , i , visited)

visited1 = [0 for _ in range(N+1)]
dfs(graph, V , visited1)

print()

visited2 = [0 for _ in range(N+1)]
bfs(graph, V , visited2)