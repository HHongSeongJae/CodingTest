'''
T : 붙일 색종이 수 (크기 10 10)
(왼쪽하단 좌표) (x,y)

구현
T * 100 - (겹치는 부분)
'''

T = int(input())

p = [[0]*100 for i in range(100)]

sum = 0
for i in range(T):
    x,y = map(int, input().split())

    for i in range(10):
        for j in range(10):
            if((x+i) <= 100 and (y+j) <= 100):
                p[x+i][y+j] = 1

for i in range(100):
    sum += p[i].count(1)

print(sum)