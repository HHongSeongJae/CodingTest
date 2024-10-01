# '''
# 총 인원 : N명 (짝수)
# 스타트 팀 : N / 2
# 링크 팀 : N / 2

# 스타트 팀과 링크 팀원의 능력치를 최소화
# '''
# import sys

# input = sys.stdin.readline

# N = int(input())

# people = []

# for i in range(N):
#     people.append(list(map(int,input().split())))

# # DFS를 위한 방문 기록
# visited = [0 for i in range(N)]
# # 최소 차이
# min_temp = int(1e9)

# #DFS
# def dfs(depth , idx): # 팀 분할을 완료했는지 안했는지를 확인하는 depth :: ex) N = 4이면 depth = 2가 되면 2팀으로 분류가 가능해진 상황
#     global min_temp

#     if depth == (N//2): # idx가 N의 절반이 되면 start와 link 팀 분배
#         # 이때 visited = 1 이면 start팀 , 0이면 link팀으로 편성하여서 최소 능력치 차이를 찾는다.
#         start = 0
#         link = 0

#         # N x N 으로 인원들의 능력치가 주어져있기 때문에 2중 for문을 이용한다.
#         for i in range(N): # 행
#             for j in range(N): # 열
#                 #start 팀 배정
#                 if visited[i] == 1 and visited[j] == 1:
#                     start += people[i][j]
#                 #link 팀 배정
#                 elif visited[i] == 0 and visited[j] == 0:
#                     link += people[i][j]
        
#         #최소값 갱신
#         min_temp = min(min_temp, abs(start-link))
    
#     #절반이 되기 전까지는 재귀적으로 방문을 진행한다.
#     for i in range(idx, N):
#         # 확인하지 않은 사람이 있다면 DFS
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(depth+ 1 , i+1)
#             visited[i] = 0
# dfs(0, 0)
# print(min_temp)

#### 재풀이
#### 백트래킹 : 브루트포스 + *종료조건
def go(idx, start, link):
    if idx == n:
        if len(start) != (n//2):
            return -1
        if len(link) != (n//2):
            return -1
        
        # start와 link팀의 능력치를 각각 더한다.
        t1 = 0
        t2 = 0

        # start와 link의 팀원이 각각 3명씩 나눠졌기 때문에 i,j는 n//2까지만 한다.
        for i in range(n//2):
            for j in range(n//2):
                if i == j: # i == j 인 경우는 0이다.
                    continue

                t1 += s[start[i]][start[j]] # Sij
                t2 += s[link[i]][link[j]]   # Sij
        diff = abs(t1-t2) # 두 팀의 능력치 차이를 구한다.

        return diff
    
    # 백트래킹 조건
    # 팀을 분배하는 상황에서 한팀에 n//2보다 인원이 많아지면 종료
    if len(start) > n//2:
        return -1
    if len(link) > n//2:
        return -1
    
    # 함수의 비정상 종료 조건이 -1이기 때문에 -1로 시작한다.
    result = -1

    # start팀에 인원을 배치하면서 확인
    t1 = go(idx + 1 , start + [idx] , link)
    if result == -1 or (t1 != -1 and result > t1):
        result = t1
    
    # start팀에 인원을 넣다가 n//2명이 이상되게 되면 위 go함수가 탈출되면서 link팀에 인원을 넣어본다.
    t2 = go(idx + 1 , start , link + [idx])
    if result == -1 or (t2 != -1 and result > t2):
        result = t2
    
    return result

n = int(input())

s = [list(map(int,input().split())) for _ in range(n)]

# start 팀과 link팀의 빈 리스트로 시작한다.
print(go(0,[],[]))