from collections import deque

n = int(input())
k = int(input())

# 빈칸 0 , 뱀 위치 1 , 사과 2
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    applex , appley = map(int,input().split())
    graph[applex][appley] = 2

l = int(input())

dir = deque()
for _ in range(l):
    dir.append(list((input().split())))

# 방향 벡터 : 동,남,서,북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

idx = 0 # 현재 방향
time = 0 # 게임 시간

# 뱀 시작 좌표
snailx , snaily = 1 , 1
graph[snailx][snaily] = 1

# 뱀이 꼬리 기록
route = deque()
route.append((1,1))

movetime , movedir = dir.popleft()

while True:
    # 뱀의 이동
    snailx += dx[idx]
    snaily += dy[idx]

    # 범위 밖이면 게임 종료
    if snailx <= 0 or snailx > n or snaily <= 0 or snaily > n or graph[snailx][snaily] == 1:
        print(time+1)
        break
    else: # 범위 안이면 이동
        # 위 두 조건이 아니면 이동가능
        # 사과가 있는지 여부 확인
        if graph[snailx][snaily] == 2: # 사과라면 몸 길이 증가
            graph[snailx][snaily] = 1
            route.append((snailx,snaily)) # 뱀의 새로운 경로 추가
        else: # 사과가 아니라면 머리 이동 후 꼬리 부분 삭제
            graph[snailx][snaily] = 1
            route.append((snailx , snaily))

            # print(route)
            delx , dely = route.popleft()
            graph[delx][dely] = 0

    time += 1
    
    # 뱀이 진행 방향을 바꾸는 타이밍
    if time == int(movetime):
        if movedir == 'L':
            idx = (idx - 1) % 4
        elif movedir == 'D':
            idx = (idx + 1) % 4

        # 다음 순번으로 최신화
        if len(dir) > 0:
            movetime , movedir = dir.popleft()
        else:
            movetime , movedir = -1 , -1 # 방향전환은 이제 없다.