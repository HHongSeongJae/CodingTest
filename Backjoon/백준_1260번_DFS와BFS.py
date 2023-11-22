import sys
from collections import deque 

N,M,V = map(int, input().split())

def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
        
    visited.add(start)
    print(start, end=' ')
    
    #keyerror문제 해결을 위한 코드
    if(start not in graph):
        return
    
    #재귀를 이용한 DFS 구현
    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited)
    
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
   #queue를 이용한 BFS 구현
    while queue:
        n = queue.popleft()
        print(n , end = ' ')
        
	#keyerror문제 해결을 위한 코드
        if(n not in graph):  
            return
        
        for n in graph[n]:
            if n not in visited:
                queue.append(n)
                visited.add(n)

#그래프 생성
graph = {}

for i in range(M):
    # a,b = map(int, input().split())
    a,b = map(int, sys.stdin.readline().split())
    
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
        graph[a].sort()
        
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)
        graph[b].sort()

dfs(graph, V)
print('\n', end='')
bfs(graph, V)