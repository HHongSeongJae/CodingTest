# n,m = map(int,input().split())

# s = []
# idx = 1

# def back():
#     # 종료 조건
#     if len(s) == m:
#         print(*s)
#         return
    
#     #dfs , 백트래킹 수행
#     for i in range(1, n+1):
#         if i not in s: # 중복된 수열을 배제하기 위함
#             s.append(i)
#             back()
#             s.pop()

# back()

## 순열 : 순서를 고려 1 2 와 2 1은 다른 것
n , m = map(int,input().split())

visited = [0] * (n+1) # 중복을 허용하지 않기 때문에 필요
res = [0] * (m)

def dfs(start, cnt , n , m):
    if cnt == m:
        print(' '.join(map(str,res)))
        return

    for i in range(start, n+1): # 수열이 오름차순이어야 하기 때문에 start 부터 시작된다.
        if visited[i] == 0: # 중복을 방지하는 부분
            visited[i] = 1
            res[cnt] = i
            dfs(i , cnt + 1 , n , m)
            visited[i] = 0

dfs(1,0,n,m)

## 수를 선택하는지 안하는지를 기준으로 해결하는 방법
'''
0 : 선택 , x : 미선택

1 2 3 4 5
o o x x x : 1 2
o x o x x : 1 3
=> 해당 문제는 중복을 허용하지 않기 때문에 선택한 수에 대한 개수는 유지할 필요 없음
'''
# n , m = map(int,input().split())

# visited = [0] * m

# def dfs(number, select, n , m):
#     if select == m:
#         print(visited)
#         return
    
#     # m개를 선택(select)하지 못했지만 더 이상 선택할 경우가 없는 상황 -> 종료
#     if number > n:
#         return
    
#     # number+1를 선택하는 경우
#     visited[select] = number
#     dfs(number+1 , select + 1 , n , m) 
#     # number+1를 선택하지 않는 경우
#     visited[select] = 0
#     dfs(number+1 , select , n , m)

# dfs(1,0,n,m)