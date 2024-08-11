import copy
import sys

input = sys.stdin.readline

# 빙고판 선언
ori_binggo = []

for i in range(5):
    ori_binggo.append(list(map(int,input().split())))

binggo = copy.deepcopy(ori_binggo)

#가로 체크
def check_row():
    cnt = 0
    for i in range(5):
        if binggo[i].count(0) == 5:
            cnt += 1
    return cnt

# 세로 체크
def check_col():
    cnt = 0
    for i in range(5):
        temp = 0
        for j in range(5):
            if binggo[j][i] == 0:
                temp += 1

                if temp == 5:
                    cnt += 1
    return cnt

# 대각선 체크
def check_dia():
    temp1 = 0
    temp2 = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                if binggo[i][j] == 0:
                    temp1 += 1
            
                if binggo[i][4-j] == 0:
                    temp2 += 1
    
    if temp1 == 5 and temp2 == 5:
        return 2
    elif (temp1 == 5 and temp2 != 5) or (temp2 == 5 and temp1 != 5):
        return 1
    else:
        return 0
    
n = []
for i in range(5):
    n .append(list(map(int,input().split())))

count = 0
for n1 in n:
    for temp in n1:
        count += 1
        for i in range(5):
            for j in range(5):
                if binggo[i][j] == temp:
                    binggo[i][j] = 0

                    a = check_row()
                    b =check_col()
                    c = check_dia()

                    if a+b+c >= 3:
                        print(count)
                        exit()