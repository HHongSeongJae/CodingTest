# # 주사위 : [위 , 남, 동, 서, 북, 밑]
# # map[x][y] == 0 -> 주사위 바닥면에 있는 수가 map에 복제
# # map[x][y] != 0 -> map에 쓰인 수가 주사위 바닥에 복제되고, map은 0이 된다.
# # 동(1) , 서(2) , 북(3) , 남(4)

# # 주사위의 6면 선언 : 처음에는 모두 0이다.
# dice = [0] * 6

# # 주사위의 회전을 함수로 구현했다.
# # 이는 4방향 밖에 없기 때문에 배열을 조작하기 보다는 각 면이 어떻게 바뀌는지 확인하고 일대일로 변경해주는게 간편한다.
# # [위쪽, 남, 동, 서, 북, 아래]
# def rotate(direct):
#     if direct == 1:
#         dice[3] , dice[1] , dice[0] , dice[5] , dice[4] , dice[2] = dice[0] , dice[1] , dice[2], dice[3] , dice[4], dice[5]
#     elif direct == 2:
#         dice[2] , dice[1] , dice[5] , dice[0] , dice[4] , dice[3] = dice[0] , dice[1] , dice[2], dice[3] , dice[4], dice[5]
#     elif direct == 3:
#         dice[1] , dice[5] , dice[2] , dice[3] , dice[0] , dice[4] = dice[0] , dice[1] , dice[2], dice[3] , dice[4], dice[5]
#     elif direct == 4:
#         dice[4] , dice[0] , dice[2] , dice[3] , dice[5] , dice[1] = dice[0] , dice[1] , dice[2], dice[3] , dice[4], dice[5]

# # 방향 벡터
# # 동(1) , 서(2) , 북(3) , 남(4)
# dx = [0,0,-1,1] 
# dy = [1,-1,0,0]

# n , m , x , y , k = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]
# move = list(map(int,input().split()))

# for mm in move:
#     nx = x + dx[mm-1]
#     ny = y + dy[mm-1]

#     if 0 <= nx < n and 0 <= ny < m: # 범위 내에서만 동작이 유효
#         rotate(mm) # 주사위 회전

#         x , y = nx, ny # (x,y) 좌표 정보 업데이트

#         # (x,y)가 0이라면 주사위의 바닥면의 숫자가 복제된다.
#         if graph[x][y] == 0:
#             graph[x][y] = dice[5]
#         # (x,y)가 0이 아니라면 주사위에 (x,y)수가 복제되고 (x,y)값이 0으로 바뀐다.
#         else:
#             dice[5] = graph[x][y]
#             graph[x][y] = 0

#         # (x,y)에 위치할 때 주사위의 윗면을 출력시킨다.
#         print(dice[0])

### 재풀이
n , m , x , y , k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
move = list(map(int,input().split()))

dice = [0] * 6 # 주사위 선언

# 방향 벡터 (1 동 , 2 서 , 3 북 , 4 남)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 주사위 이동 구현
def rotate(direct_num):
    if direct_num == 1: # 동쪽 이동
        dice[0] , dice[1] , dice[2] , dice[3] , dice[4] , dice[5] = dice[2] , dice[1] , dice[5] , dice[0] , dice[4] , dice[3]
    elif direct_num == 2: # 서쪽 이동
        dice[0] , dice[1] , dice[2] , dice[3] , dice[4] , dice[5] = dice[3] , dice[1] , dice[0] , dice[5] , dice[4] , dice[2]
    elif direct_num == 3: # 북쪽 이동
        dice[0] , dice[1] , dice[2] , dice[3] , dice[4] , dice[5] = dice[1] , dice[5] , dice[2] , dice[3] , dice[0] , dice[4]
    elif direct_num == 4: # 남쪽 이동
        dice[0] , dice[1] , dice[2] , dice[3] , dice[4] , dice[5] = dice[4] , dice[0] , dice[2] , dice[3] , dice[5] , dice[1]

# 변수 겹치는 문제 주의 (변수 설정 잘하기..)
for mm in move:
    # 지도의 범위 내부인지 확인
    if 0 <= x + dx[mm-1] < n and 0 <= y + dy[mm-1] < m:
        # 내부이면 위치 이동
        x = x + dx[mm-1]
        y = y + dy[mm-1]

        # 주사위 굴리기
        rotate(mm)

        # 확인
        ## 지도가 0이면 주사위의 숫자가 복제
        if graph[x][y] == 0:
            graph[x][y] = dice[0]
        ## 지도가 0이 아니면 지도의 숫자가 주사위 맡다은 부분에 복제되고 지도가 0이 된다.
        else:
            dice[0] = graph[x][y]
            graph[x][y] = 0
        
        # 주사위의 윗면 출력
        print(dice[5])