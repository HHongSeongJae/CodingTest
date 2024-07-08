'''
1. N : 센서 개수
2. K : 집중국 개수
3. n개 센서들의 좌표
'''

'''
구현
1. 센서를 좌표 순서대로 정렬
2. 인접 센서간 거리 리스트 생성
  2-1. 인접 센서간 거리가 가장 큰 것부터 자르게 되면 센서의 수신 가능영역을 최소화 할 수 있다.
  2-2. 집중국을 k개 배치할 수 있기 때문에 가장 큰 거리를 k개 제외 시킨 후 나머지 거리를 더하면 최소의 거리가 된다. 
'''

n = int(input())
k = int(input())
point = list(map(int,input().split()))

point.sort()
dist = []

# 런타임 에러 방지
## 집중국이 센서보다 많으면 최소 수신가능거리는 0이 된다.
if k >= n:
    print(0)
    exit()

# 인접 센서간 거리 구하기
for i in range(1,n):
    dist.append(point[i]-point[i-1])

dist.sort(reverse=True)

# 집중국 배치
# 2개의 집중국을 배치하려면 센서를 특정 위치에서 한 번만 쪼개면 2개의 범위로 나눠진다. 
# 그래서 range(k-1)이 된다.
for i in range(k-1):
    dist.pop(0)
print(sum(dist))
