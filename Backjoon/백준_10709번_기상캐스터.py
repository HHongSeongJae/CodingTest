'''
가로 : H
세로 : W
H x W

북쪽으로 부터 i
서쪽으로 부터 j => (i,j) :: x,y 좌표축임

- 모든 구름은 1분이 지날 때마다 1킬로미터씩 동쪽(+1,0)으로 이동한다.
- 각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 구하여라.
- 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 예측하는 일을 맡았다.

처음부터 구역 (i, j) 에 구름이 떠 있었던 경우에는 0
몇 분이 지나도 구름이 뜨지 않을 경우에는 -1

입력
- H, W
- H번 반복 :: W의 문자열입력
(c : 구름 , . : 구름 x)
'''

H,W = map(int,input().split())

# 초기 구름이 있는 하늘 생성
cloud = []
for _ in range(H):
    cloud.append(list(input()))

# 한 행씩 순환하면서 구름이동량 계산
# c가 있다면 0으로 변수 초기화하고 +1 하면서 우측으로 이동
    # 만약 다시 c를 만나면 0으로 초기화
# .부터 나오는 상황에서는 -1로 채워 넣는다.
for idx_h, i in enumerate(cloud):
    count = -1
    for idx_w,j in enumerate(i):
        # print(idx_h, idx_w, j)
        if j == 'c': #구름 만나면 무조건 0으로 초기화
            count = 0
            cloud[idx_h][idx_w] = count
        elif count != -1 and j == '.': #구름을 한번 만난 후 구름이 없는 지역임
            count += 1
            cloud[idx_h][idx_w] = count
        elif count == -1 and j == '.': #처음부터 구름 없는 지역 만남
            cloud[idx_h][idx_w] = -1

for i in cloud:
    print(*i)