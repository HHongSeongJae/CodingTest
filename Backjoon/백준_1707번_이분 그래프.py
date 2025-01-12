'''
# BFS 기준
1. 최초 탐색 시작할 정점의 색상을 빨간색(1)으로 칠한다.
2. 최초 정점의 인접 정점의 색상을 파란색(-1)으로 칠한다.
3. 해당 인접 정점들을 차례로 탐색을 시작하며 자신과 인접한 정점을 빨간색(1)으로 칠한다.
4. 이와 같은 방식의 탐색을 지속하며 반복하여 2개 이상의 색상으로 모두 칠한다.
5. 색상을 칠하다가 이웃 정점이 같은색으로 칠해져 있다면 이분 그래프가 될 수 없다.
'''
## BFS 풀이
import sys
from collections import deque

input = sys.stdin.readline

k = int(input())

def bfs(start, visited, graph, status):
    queue = deque()
    queue.append(start) # 정점 BFS 방문을 위해 큐에 넣는다.

    # 방문한 정점은 status 값으로 넣어준다.
    visited[start] = status

    while queue:
        now = queue.popleft()

        # now정점의 인접노드 방문
        for adj in graph[now]:
            if visited[adj] == 0: # 방문가능한 인접 노드
                visited[adj] = -1 * visited[now] # ★ now 정점 기준으로 인접 정점이기 때문에 now 정점과 상태 값이 반대로 설정되도록 한다.
                queue.append(adj)
            elif visited[adj] == visited[now]: # 현재 정점과 인접 정점의 상태(그룹)이 같다면 이분 그래프 성립 불가
                return False
    return True

for _ in range(k):
    v , e = map(int,input().split())
    
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a , b = map(int,input().split())

        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (v+1)
    ok = 1 # -1 : NO , 1 : YES

    for i in range(1,v+1):
        if visited[i] == 0:
            # bfs에서 이분 그래프가 성립되지 않는다면 False가 반환된다.
            if bfs(i, visited, graph , 1) == False:
                ok = -1
                break
    
    if ok == 1:
        print("YES")
    else:
        print("NO") 

## DFS 풀이
import sys

sys.setrecursionlimit(10**6) # 백준 저지를 위한 DFS 문제 기본 세팅 (파이썬의 재귀 깊이는 1000정도로 되어있기 때문이다)
input = sys.stdin.readline

k = int(input())

def dfs(start , visited, graph , status): # status는 현재 1을 기록해야하는 정점인지, -1을 기록해야하는 정점인지 구분
    visited[start] = status # 정점의 상태가 1 혹은 -1로 상황에 따라 다르게 기록

    # 인접정점 확인
    for adj in graph[start]:
        if visited[adj] == 0: # 인접정점의 상태가 0이라면 이분 그래프가 될 수 있고 이는 -1로 기록한다.
            if dfs(adj, visited , graph , status * -1) == False: # 1혹은 -1로 기록하기 위해 status * -1 로 한다.
                return False # DFS 경과 False로 리턴되면 이분 그래프가 될 수 없다.
        elif visited[start] == visited[adj]: # 방문 노드와 인접 노드가 상태가 같다면 이분 그래프가 될 수 없다.
            return False
    return True # 리턴되는 값 없이 인접노드 확인이 끝났다면 이분 그레프가 가능한 상황이므로 True 반환

for _ in range(k):
    v , e = map(int,input().split())
    
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a , b = map(int,input().split())

        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (v+1)
    ok = 1 # -1 : NO , 1 : YES

    # 시작 정점 순환
    for ss in range(1, v+1):
        if visited[ss] == 0: # 시작 정점이 0 상태면 방문할 수 있는 상태이고, 상태 값은 1로 표시한다.
            if dfs(ss, visited , graph , 1) == False: # DFS 경과 False로 리턴되면 이분 그래프가 될 수 없다.
                ok = -1
                break
    
    if ok == 1:
        print("YES")
    else:
        print("NO") 
