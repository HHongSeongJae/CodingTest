# 메모리 초과
# 집이 배치될 수 있는 x의 범위가 10억이다.
# 그러므로 집이 0위치와 10억번째 위치에 존재한다고할 때 DFS를 수행하면 재귀호출로 인한 메모리 초과 발생

# n , c = map(int,input().split())

# home = []

# for _ in range(n):
#     home.append(int(input()))

# home.sort()
# visited = [0] * (max(home) + 1)

# res = -int(1e9)
# def dfs(depth , cnt , visited , graph):
#     global res
#     # 공유기 위치 모두 선택 완료
#     if cnt == c:
#         tmp = int(1e9)
#         ok = 0

#         for idx , value in enumerate(visited):
#             if value == 1:
#                 if ok == 0:
#                     ok = 1
#                     before = idx
#                 else:
#                     tmp = min(tmp, abs(before - idx))
#                     before = idx
        
#         res = max(res, tmp)
#         return

#     for i in range(depth, n):
#         if visited[home[i]] == 0:
#             visited[home[i]] = 1
#             dfs(i , cnt+1 , visited , graph)
#             visited[home[i]] = 0

# dfs(0,0,visited,home)
# print((res))

###
# 이진 탐색으로 10억개라는 많은 수의 범위에서 탐색의 횟수를 줄여야한다.
# 또한 지금은 찾고자 하는 key값이 명확하지 않고, 이 key값을 찾아나가야 한다.
# 그래서 기준 값을 변경해가면서 가장 적절한 답을 찾아야 한다.

n , c = map(int,input().split())

home = []

for _ in range(n):
    home.append(int(input()))

home.sort() # 이진탐색의 조건 : 정렬된 리스트

# gap 설정
start = 1 # 최소로 가능한 gap :: 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
end = home[-1] - home[0] # 가장 큰 gap

while start <= end:
    mid = (start + end) // 2 # gap 설정
    key = home[0] # 가장 처음 집을 시작하여 공유기를 설치해본다.
    cnt = 1

    for i in range(1, n):
        if home[i] >= key + mid: # 현재 기준점 key에서 mid만큼의 gap이 가능한 구간에 대한 조건 => 공유기 설치 가능
            key = home[i] # 현재의 위치에서 공유기 설치가 가능하므로 이제 home[i] 위치에서 공유기를 다시 설치시작
            cnt += 1
    
    # 공유기가 c개 이상으로 설치가 된다는 것은 gap을 늘려도 된다.
    if cnt >= c:
        start = mid + 1 # start 기준을 mid+1로 하여 gap을 크게 한다.
        res = mid # 공유기 설치가 가능한 gap인 mid 값을 res에 저장
    # 공유기가 c개보다 작게 설치 된다는 것은 gap을 줄여야 한다.
    else:
        end = mid - 1

print(res)