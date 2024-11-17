# 1 : 시계 방향 , -1 : 반시계 방향
def rotate(idx, direct):
    # 시계 방향
    if direct == 1:
        tmp = wheel[idx][-1]

        for i in range(7,0,-1):
            wheel[idx][i] = wheel[idx][i-1]
        
        wheel[idx][0] = tmp
    elif direct == -1:
        tmp = wheel[idx][0]

        for i in range(7):
            wheel[idx][i] = wheel[idx][i+1]

        wheel[idx][-1] = tmp

# 오른쪽 톱니바퀴에 의한 왼쪽 톱니 바퀴 회전 여부 확인
def checkleft(idx, direct):
    if idx < 0:
        return
    
    if wheel[idx][2] != wheel[idx+1][6]:
        checkleft(idx - 1 , -direct)
        rotate(idx , direct)

# 왼쪽 톱니바퀴에 의한 오른쪽 톱니 바퀴 회전 여부 확인
def checkright(idx, direct):
    if idx > (n-1):
        return
    
    if wheel[idx][6] != wheel[idx-1][2]:
        checkright(idx + 1 , -direct)
        rotate(idx, direct)

n = int(input())
wheel = [list(map(int,input())) for _ in range(n)]
k = int(input())

for i in range(k):
    number , direct = map(int,input().split())
    # 주어진 톱니의 번호는 1,2,3,4로 주어진다.
    # 이를 리스트의 인덱스에 맞도록 하기 위해서 number -= 1을 해준다.
    number -= 1

    # 현재 number가 회전하기 때문에 이로인해서 좌측, 우측 톱니바퀴 회전여부 확인
    checkleft(number - 1 , -direct)
    checkright(number + 1 , -direct)

    rotate(number , direct)

res = 0
for w in wheel:
    if w[0] == 1:
        res += 1

print(res)