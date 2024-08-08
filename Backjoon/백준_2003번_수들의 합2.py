n , m = map(int,input().split())

num = list(map(int,input().split()))

interval = 0 # start와 end 사이의 합을 유지하는 변수
count = 0 # interval == m인 개수
end = 0

for start in range(n):

    # 부분합이 m보다 커지기 전까지 end point만 이동
    while (interval < m) and (end < n):
        interval += num[end] # start와 end 사이의 부분합 계산
        end += 1
    
    # 부분합이 m과 같은 경우 count
    if interval == m:
        count += 1
    
    # start가 end 위치로 이동하는 동안 interval합을 뺀다.
    interval -= num[start]

print(count)
    