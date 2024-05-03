import sys
from collections import deque


def bfs(graph, start, visited):
    #bfs구현을 위한 큐 선언
    queue = deque([start]) #start부터 큐를 선언하면서 넣고 시작

    #현재 노드 방문 처리
    visited[start] = 1

    #큐에 값이 없을 때까지 반복
    while queue:
        temp = queue.popleft()

        for i in graph[temp]:
            if visited[i] == 0: # 해당 노드와 인접 노드가 방문한 적이 없을때
                queue.append(i) # 큐에 삽입
                visited[i] = 1 # 방문처리

n = int(input()) # PC 수
m = int(input()) # PC가 연결된 쌍 수

graph = [[] for i in range(n+1)] # 컴퓨터 개수만큼 그래프 초기화 , 0번부터시작하는 리스트 고려
visited = [0] * (n+1)

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

print(graph)

bfs(graph,1,visited)

# visited에서 1인 개수를 출력
# print(visited)
print(visited.count(1) - 1) # 자기 자신 제외