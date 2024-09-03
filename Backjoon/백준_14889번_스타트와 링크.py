'''
총 인원 : N명 (짝수)
스타트 팀 : N / 2
링크 팀 : N / 2

스타트 팀과 링크 팀원의 능력치를 최소화
'''
import sys

input = sys.stdin.readline

N = int(input())

people = []

for i in range(N):
    people.append(list(map(int,input().split())))

# DFS를 위한 방문 기록
visited = [0 for i in range(N)]
# 최소 차이
min_temp = int(1e9)

#DFS
def dfs(depth , idx): # 팀 분할을 완료했는지 안했는지를 확인하는 depth :: ex) N = 4이면 depth = 2가 되면 2팀으로 분류가 가능해진 상황
    global min_temp

    if depth == (N//2): # idx가 N의 절반이 되면 start와 link 팀 분배
        # 이때 visited = 1 이면 start팀 , 0이면 link팀으로 편성하여서 최소 능력치 차이를 찾는다.
        start = 0
        link = 0

        # N x N 으로 인원들의 능력치가 주어져있기 때문에 2중 for문을 이용한다.
        for i in range(N): # 행
            for j in range(N): # 열
                #start 팀 배정
                if visited[i] == 1 and visited[j] == 1:
                    start += people[i][j]
                #link 팀 배정
                elif visited[i] == 0 and visited[j] == 0:
                    link += people[i][j]
        
        #최소값 갱신
        min_temp = min(min_temp, abs(start-link))
    
    #절반이 되기 전까지는 재귀적으로 방문을 진행한다.
    for i in range(idx, N):
        # 확인하지 않은 사람이 있다면 DFS
        if visited[i] == 0:
            visited[i] = 1
            dfs(depth+ 1 , i+1)
            visited[i] = 0 # 백트래킹 ,, 방문 취소
dfs(0, 0)
print(min_temp)