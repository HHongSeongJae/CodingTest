'''
- 극이 다르면 회전 x
'''

'''
N극 : 0 , S극 : 1

K : 회전횟수
회전시키는 톱니바퀴 번호 : 회전방향(시계(1), 반시계(-1))
'''

import sys
from collections import deque  # 회전을 사용하기 위한 deque 선언 :: rotate


# 우측 톱니바퀴 확인 함수
def checkRight(idx, direct):
    if idx > 3: # 우측에 톱니바퀴가 없음
        return # 회전 불가
    
    if wheel[idx-1][2] != wheel[idx][6]: # 오른쪽 인접 톱니바퀴와 극이 다르면 회전 가능
        # 오른쪽을 회전시키기 때문에 오른쪽 톱니바퀴 기준 또 오른쪽이 있을 수도 있기에 재귀 호출
        # 또한 현재의 톱니바퀴가 시계방향 회전이라면 오른쪽 톱니바퀴는 반시계방향으로 회전할 것이므로 -direct로 호출된다.
        checkRight(idx+1 , -direct)
        # 현재 톱니바퀴 회전
        wheel[idx].rotate(direct)

# 좌측 톱니바퀴 확인 함수
def checkLeft(idx, direct):
    if idx < 0: # 좌측에 톱니바퀴가 없음
        return # 회전 불가

    if wheel[idx+1][6] != wheel[idx][2]: # 왼쪽 인접 톱니바퀴와 극이 다르면 회전 가능
        # 왼쪽을 회전시키기 때문에 왼쪽 톱니바퀴 기준 또 왼쪽이 있을 수도 있기에 재귀 호출
        # 또한 현재의 톱니바퀴가 시계방향 회전이라면 왼쪽 톱니바퀴는 반시계방향으로 회전할 것이므로 -direct로 호출된다.
        checkLeft(idx-1, -direct)
        # 현재 톱니바퀴 회전
        wheel[idx].rotate(direct)

# 점수 계산
def sumSc():
    sc = 0
    temp = 1

    for i in wheel:
        # print(i)
        if i[0] == 1:
            sc = sc + temp
        temp *= 2

    return sc

input = sys.stdin.readline

wheel = []
result = 0
wheel = [deque(list(map(int, input().strip()))) for _ in range(4)]

T = int(input())

for i in range(T):
    K, D = map(int,input().split())
    K -= 1

    # 인접 톱니바퀴 회전 처리 (K번째 톱니바퀴 , D 방향)
    # 인접 톱니바퀴기 때문에 -D방향 회전으로 처리
    checkLeft(K - 1 , -D)
    checkRight(K + 1, -D)

    # 기준 톱니바퀴 회전
    wheel[K].rotate(D)

# 회전 후 점수 계산
print(sumSc())