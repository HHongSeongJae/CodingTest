'''
X : 땅 , '.' : 바다

50년이 지나면, 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다는 사실을 알았다.

(+) 범위를 벗어나는 구간은 모두 바다이다.
'''

### x,y 이동되는 좌표 순서 헷깔리지 않기!

import copy

R,C = map(int,input().split())

#상하좌우  ==> 구현관련 알고리즘에서 자주사용된다 ★★★
dx = [0,0,-1,1]
dy = [-1,1,0,0]

map = []
for _ in range(R):
    map.append(list((input())))

map2 = []

# map은 육지가 잠기는 것으로 변경시킬 지도
# map2는 육지 주변의 바다의 개수를 세기 위한 지도
## 따라서 map2는 map이 변할 때 함께 변하면 안되기 때문에 깊은 복사를 통해서 별도의 객체를 생성한다.
map2 = copy.deepcopy(map)
land_cnt = 0

for i in range(R): # x
    for j in range(C): # y
        count = 0
        if map2[i][j] == 'X':
            land_cnt += 1 
            for z in range(4):
                nx = i + dx[z]
                ny = j + dy[z]

                # 범위 벗어나면 바다임
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    count += 1
                # 상하좌우중 바다 확인
                elif map2[nx][ny] == '.':
                    count += 1
                
            if count == 3 or count == 4:
                map[i][j] = '.'
                land_cnt -= 1 


if land_cnt == 0:
    print('X') # 육지가 하나밖에 없는 경우
else:
    #시작과 마무리 Row를 찾는 것은 단순히 X가 위치한 Row만 확인하면 되기 때문에 range(R)을 순회하면서 확인 가능
    sR = 0   # x1  
    lR = 0   # x2

    #시작과 마무리 column은 row마다 순회하면서 min, max 값을 찾아야 한다.
    # 따라서 start column은 max값인 C-1을 , last Column은 min값인 0으로 초기값을 주었다.
    sC = C-1   # y1
    lC = 0   # y2

    #행 범위 찾기
    for i in range(R):
        if 'X' in map[i]:
            sR = i
            break
    
    for i in range(R-1 , -1 , -1):
        if 'X' in map[i]:
            lR = i
            break
    
    # 열 범위
    for i in range(sR,lR+1):
        for j in range(C):
            if map[i][j] == 'X':
                sC = min(sC, j)
                lC = max(lC, j)

for i in range(sR, lR + 1):
    for j in range(sC, lC+1):
        print(map[i][j], end='')
    print()
