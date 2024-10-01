# 그래프의 정의를 이용한 풀이
# n,m = map(int,input().split())

# # 간선 리스트
# edgeL = []
# # 인접 행렬
# aM = [[0]*n for _ in range(n)]
# # 인접리스트
# aL = [[] for _ in range(n)]

# for _ in range(m):
#     a,b= map(int,input().split())

#     #간선 리스트 생성
#     edgeL.append((a,b))
#     edgeL.append((b,a))

#     #인접 행렬 생성
#     aM[a][b] = aM[b][a] = 1

#     #인접 리스트 생성
#     aL[a].append(b)
#     aL[b].append(a)

# m = m*2 # 양방향이기 때문에 간선을 모두 확인하려면 2배가 된다.

# for i in range(m):
#     for j in range(m):
#         # 1. A->B , C->D 간선이 존재하는지 확인 :: 간선리스트 이용
#         A , B = edgeL[i]
#         C , D = edgeL[j]

#         if A==B or A==C or A==D or B==C or B==D or C==D: #중복되면 안된다.
#             continue

#         # 2. B->C 사이에 간선이 존재하는지 확인 :: 인접행렬 이용
#         if aM[B][C] == 0:
#             continue

#         # 3. D->E 경로가 존재하는지 확인 :: 인접리스트를 이용해 모든 E경로를 확인
#         for E in aL[D]:
#             if A==E or B==E or C==E or D==E:
#                 continue

#             # E로의 경로가 존재하는 경우
#             print(1)
#             exit()
# print(0)

## DFS 풀이
n,m = map(int,input().split())

graph = [[] for _ in range(n)] # 인접 리스트 생성
visited = [0] * (n+1) # 방문 정점을 유지할 리스트
res = 0

for _ in range(m):
    u,v = map(int,input().split())

    #양방향 인접리스트 생성
    graph[u].append(v)
    graph[v].append(u)

def dfs(depth, start):
    global res

    if depth == 4: # start가 A라고 하면 B C D E로 가는 경로가 존재하면 ABCDE 관계가 있는 것임
        res = 1
        return
    
    # 현재 정점 방문처리
    visited[start] = 1

    for i in graph[start]:
        if visited[i] == 0: # start 정점과 인접한 정점 중 방문이 가능한 정점이 있다면 이를 방문처리하고 방문한다.
            visited[i] = 1
            dfs(depth+1 , i)
            visited[i] = 0

for i in range(n):
    dfs(0,i)
    visited[i] = 0 # visited[i]에 대한 처리가 i에서 끝났기 때문에 이를 방문처리했던 것을 취소해준다.

    # A->B->C->D->E 경로를 찾은 경우
    if res == 1:
        print(1)
        exit()

print(0)

