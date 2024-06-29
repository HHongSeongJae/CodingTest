'''
N : 도시(노드)
M : 도로(간선) - 단방향
K : 최단 거리
X : 출발 노드
'''
### 다익스트라 풀이

# # N <= 300000 :: 비교적 큰수 -> 플루이드 워셜이 아닌 다익스트라를 통한 최단거리 사용
# import heapq
# import sys

# INF = int(1e9) #무한대 정의

# input = sys.stdin.readline

# #도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# n,m,k,x = map(int, input().split())

# # 그래프
# graph = [[] for _ in range(n+1)]
# # 최단거리 정보
# distance = [INF] * (n+1)

# # 간선 정보 입력받기
# for i in range(m):
#     a,b = map(int,input().split())

#     graph[a].append((b,1)) # a->b 경로 ,, 모든 거리는 1  # [노드 , 거리]

# # 다익스트라 알고리즒
# def dijkstra(start):
#     q = []

#     #자기 자신으로의 거리는 0
#     heapq.heappush(q, (0,start)) 
#     distance[start] = 0

#     while q:
#         dist , n_node = heapq.heappop(q)

#         # 힙에서 꺼낸 노드가 최단 거리면 아무것도 하지 않음
#         if distance[n_node] < dist:
#             continue

#         # 인접 노드 확인
#         for i in graph[n_node]:
#             # 거쳐가는 경로 비용
#             cost = dist + i[1] # graph => [노드,거리]

#             if cost < distance[i[0]]:
#                 # 최단거리 찾으면 갱신 후 힙에 넣는다.
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijkstra(x)

# if k not in distance:
#     print(-1)
#     exit()

# for idx , i in enumerate(distance):
#     if i == k:
#         print(idx)

import sys
### BFS 풀이
# 모든거리가 1이라는 조건이 있어서 BFS를 통해서 빠르게 해결 가능한 문제였다.
from collections import deque

INF = int(1e9) #무한대 정의

input = sys.stdin.readline

#도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n,m,k,x = map(int, input().split())

# 그래프
graph = [[] for _ in range(n+1)]
# 방문 노드 관리
visited = [0] * (n+1)

# 최단거리 유지
distance = [INF] * (n+1)
distance[x] = 0 # 출발도시의 거리값은 0

# 경로 입력 받음
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b) # a->b의 경로

# BFS
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = 1 # 방문 처리

    while q:
        # 큐에서 하나 꺼낸다.
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == 0: #방문하지 않은 노드라면 최단 거리 갱신
                distance[i] = distance[v] + 1
                q.append(i)

                # 방문처리
                visited[i] = 1

bfs(graph, x, visited)

if k not in distance:
    print(-1)
    exit()

for idx, i in enumerate(distance):
    if i == k:
        print(idx)