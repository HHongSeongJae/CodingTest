# '''
# N : day
# T : 상담을 완료하는데 걸리는 시간
# P : 상담을 했을 때 받을 수 있는 금액

# N일 동안 상담을 해서 최대한 많은 이익을 얻는 방법
# '''

# '''

# # 조건
# - 현재 일 수 + T 일 > N 이면 상담 불가

# # 조건

# # 알고리즘
# def dfs(시작점):

#     # 현재 일수가 N보다 큰 상황 -> 뒤 돌아간다.(백트래킹)
#     if 현재일수 > N:
#         return

#     result = max(result , 현재까지의 전체 cost 합)

#     ## dfs는 T를 기준으로 방문한 T가 N을 넘지 않으면 계속 방문
#     ## T를 방문하면 i + T[i] 가 되어야한다.
    
#     for i in range(시작점,n+1):       
#             s.append(P[i]) # 현재 cost 추가
#             dfs(i+T[i])
#             s.pop()
    
#     return 방문 노드의 cost 합

# result = 0
# for i in range(N):
#     c = [] # 모든 cost 값 저장
#     dfs(i)

# print(result)
# '''

def dfs(start):
    global result
    if start > n:
        return
    
    result = max(result, sum(c))

    for i in range(start , n):
        c.append(p[i])
        dfs(i + t[i])
        c.pop()

t = []
p = []

n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)

result = 0
for i in range(n):
    c = []
    dfs(i)

print(result)