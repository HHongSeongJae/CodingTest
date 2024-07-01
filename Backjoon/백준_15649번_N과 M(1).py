# 노드 N , 간선 M
def dfs():
     # 백트래킹 조건
     ## 한 줄에 표시할 최대 수(m)이 되면 더 이상 dfs 수행 x
    if len(s) == m:
        print(*s)
        return
    
    for i in range(1,n+1):
        if visited[i] == 1: # 방문노드는 무시
            continue

        visited[i] = 1 # 방문처리
        s.append(i) # s리스트에 현재 값 넣는다.
        dfs() # dfs 호출
        s.pop() # 가지치기를 위해서 리스트에서 값을 빼고 방문처리를 제거한다.
        print(s)
        print(visited)
        visited[i] = 0

n , m = map(int,input().split())
s = []
visited = [0] * (n+1)
dfs()


