import sys
from collections import deque

sys.setrecursionlimit(200000)

n , k = map(int,input().split())

visited = [0] * (200001)
time = [-1] * (200001)
path = [-1] * (200001)

queue = deque()
queue.append(n)
visited[n] = 1
time[n] = 0

while queue:
    now = queue.popleft()

    for i in [now+1 , now-1 , now*2]:
        if 0 <= i <= 200000 and visited[i] == 0:
            visited[i] = 1
            time[i] = time[now] + 1
            queue.append(i)
            path[i] = now

print(time[k])

def go(n,k):
    if n != k:
        go(n , path[k])
    print(k , end=' ')

go(n,k)