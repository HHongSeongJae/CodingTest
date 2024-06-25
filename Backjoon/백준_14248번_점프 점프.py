# from collections import deque

# n = int(input())

# graph = [[] for _ in range(n+1)] # 0번 제외
# visited = [0] * (n+1)

# Ai = list(map(int,input().split()))

# for i in range(1,n+1):
#     graph[i].append(Ai[i-1])

# # print(graph)

# s = int(input())

# def bfs(graph, start, visited):
#     queue = deque([start]) #시작노드 큐에 넣음
#     visited[start] = 1 # 방문처리

#     count = 1

#     while queue:
#         v = queue.popleft()

#         for i in(graph[v]):
#             if 0 < (v - i) <= n:    
#                 if visited[v-i] == 0:
#                     queue.append(v-i)
#                     visited[v-i] = 1
#                     count += 1

#             if 0 < (v + i) <= n:
#                 if visited[v+i] == 0:
#                     queue.append(v+i)
#                     visited[v+i] = 1
#                     count += 1

#     # print(visited)
#     return count

# print(bfs(graph,s,visited))

## DFS -> stack
n = int(input())
Ai = list(map(int,input().split()))

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(1,n+1):
    graph[i].append(Ai[i-1])

s = int(input())

count = 1

def dfs(graph, start, visited):
    global count
    visited[start] = 1

    for i in graph[start]:
        if 0 < start - i <= n:
            if visited[start - i] == 0: # 방문 x
                count += 1
                dfs(graph, start - i , visited)
        
        if 0 < start + i <= n:
            if visited[start + i] == 0:
                count += 1
                dfs(graph, start + i, visited)

    return count

print(dfs(graph, s, visited))