'''
- 도시i 에서 도시j로 갈 수 있는 최소비용을 구하는 것 => 최단 경로 알고리즘
- 출력에서 모든 도시로부터 각각의 최단 거리를 원한다.
'''

# # 다익스트라 알고리즘 활용 (시작점을 바꾸어가면서 distance를 각각 출력하면 된다.)
# import heapq  # 우선순위 큐 사용을 위한 힙 선언

# INF = int(1e9)

# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     a , b , c = map(int,input().split())
#     graph[a].append((b,c)) # (도착지 , 비용)

# # 다익스트라
# def dijkstra(start):
#     q = []

#     # 다익스트라에 사용되는 우선순위 큐는 거리가 우선순위다. (거리, 노드)
#     heapq.heappush(q, (0 , start)) # 시작점의 거리는 0
#     distance[start] = 0

#     while q:
#         dist , now = heapq.heappop(q) # 우선순위 큐의 값을 하나씩 방문

#         # 기존의 정보가 더 최단 거리면 무시
#         if distance[now] < dist:
#             continue

#         # 현재 방문한 노드의 인접 노드 확인
#         for g in graph[now]:
#             cost = dist + g[1] # graph는 (도착지 , 비용) 으로 데이터가 들어감

#             # 최단 경로가 나오면 최신화
#             if cost < distance[g[0]]:
#                 distance[g[0]] = cost
#                 heapq.heappush(q , (cost, g[0]))

# # 모든 도시(노드)별로 각각의 갈 수 있는 최소 비용을 출력해야한다.
# # 플로이드 워셜 알고리즘을 사용할 수도 있지만 다익스트라의 출발점을 각각 바꾸어가면서 출력해도 된다.
# for i in range(1,n+1):
#     distance = [INF] * (n+1) # 각 시작점별로 최단 경로가 달라지므로 distance를 매번 초기화
#     dijkstra(i) # 다익스트라 수행
    
#     for res in range(1,n+1):
#         if distance[res] == INF: # (문제 조건) 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다. 
#             print("0", end=' ')
#         else:
#             print(distance[res], end=' ')
#     print()

####################
# 2 <= n <= 100 이기 때문에 O(n^3)인 플로이드 워셜 알고리즘을 사용해도 충분하다.
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)] # 모든 경로의 최단거리 그래프 초기화

# 자기 자신의 거리 정보는 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    
    # 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 플로이드 워셜
# d[a][b] = min(d[a][b] , d[a][k] + d[k][b])
for k in range(1,n+1): # a -> k -> b ,, 즉, k는 거쳐가는 지점이 된다.
    for a in range(1,n+1): # 출발지
        for b in range(1,n+1): # 목적지
		        # 플로이드 워셜 점화식
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print("0", end=' ')
        else:
            print(graph[i][j] , end=' ')
    print()