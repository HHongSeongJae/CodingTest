## 비트마스크
'''
1. NM자리의 비트 마스크 생성
2. 이를 일차원 배열로 변경 , A[i][j] = i x M + j  (비트마스크는 일차원 배열)
3. 수의 합
    - 각각의 행에서 얼마나 수가 연속되는지 (가로)
        ex) 기존의 수가 32에 5가 다시 연속된다. 그러면 325가 되어야 한다.
            이는 32 * 10 + 5를 통해서 325를 숫자로 만들 수 있다... 세로에서도 동일하게 적용
            연속적인 숫자는 세로의 방향을 만나게 되면 연속성이 끝나게 된다.
    - 각각의 열에서 얼마나 수가 연속되는지 (세로)
'''
# n , m = map(int,input().split())
# graph = [list(map(int,input())) for _ in range(n)]

# res = 0

# for s in range(1<<n*m):
#     sum = 0

#     # 가로 방향 확인
#     for i in range(n):
#         cur = 0

#         for j in range(m):
#             k = i * m + j

#             if (s & (1 << k)) == 0:
#                 cur = cur * 10 + graph[i][j]
#             else:
#                 sum += cur
#                 cur = 0
#         sum += cur

#     # 세로 방향 확인
#     for j in range(m):
#         cur = 0

#         for i in range(n):
#             k = i * m + j

#             if (s & (1 << k)) != 0:
#                 cur = cur * 10 + graph[i][j]
#             else:
#                 sum += cur
#                 cur = 0
#         sum += cur
    
#     res = max(res , sum)
# print(res)

## DFS
n, m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

res = 0

def dfs(s):
    global res
    sum = 0

    # 생성된 리스트의 길이가 n*m이 되면 모두 생성 완료
    if len(s) == n*m:
        tmp = []
        # 1차원으로 된 s 리스트를 2차원 리스트로 변경한다.
        for i in range(n):
            tmp.append(s[i*m:i*m+m])
        
        # 가로 확인
        for i in range(n):
            cur = 0

            for j in range(m):
                if tmp[i][j] == 0:
                    cur = cur * 10 + graph[i][j]
                else:
                    sum += cur
                    cur = 0
            sum += cur
        
        # 세로 확인
        for j in range(m):
            cur = 0
            for i in range(n):
                if tmp[i][j] == 1:
                    cur = cur * 10 + graph[i][j]
                else:
                    sum += cur
                    cur = 0
            sum += cur

        res = max(res,sum)
        return
    else:
        dfs(s+[0]) # 해당칸을 가로방향으로 지정
        dfs(s+[1]) # 해당칸을 세로방향으로 지정

dfs([])
print(res)