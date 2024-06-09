import sys

N = int(input())

n = []
for _ in range(N):
    # n.append(list(map(int,input().split())))
    n.append(list(map(int,sys.stdin.readline().split()))) # 약 10배의 시간차이

new_n = sorted(n , key = lambda x : (x[0] , x[1])) # x좌표 기준 정렬인데, x좌표가 동일하면 y좌표 기준 오름차순

for i in new_n:
    print(*i)