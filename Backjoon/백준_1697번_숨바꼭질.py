'''
DFS
- -1 , 1 , 순간이동
- 가장 적은 DFS 호출 횟수 출력
'''
from collections import deque

n , k = map(int,input().split())

# 1 <= n,k <= 100000
# N = 52000 이고, K = 100000 이라면 52000 * 2 = 104000 이후 -1로 100000으로 가는 것이 더 빠르다.
# 이러한 경우를 대비하기 위해서 경계값을 200000정도로 지정하였다.
visited = [0] * 200001
res = [-1] * 200001

#BFS
q = deque()
q.append(n)

visited[n] = 1
res[n] = 0

while q:
    now = q.popleft()

    # 지금 방문할 위치에서 가능한 이동 3가지 경우 확인
    for move in [now+1 , now-1 , now * 2]:
        if 0 <= move <= 200000 and visited[move] == 0: # 이동이 가능한 좌표
            visited[move] = 1
            res[move] = res[now] + 1 # 한번 이동마다 1초 (가중치 : 1)
            q.append(move)

print(res[k])