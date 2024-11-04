'''
1. 전체 부분 수열을 구한다.
2. 각각의 부분 수열에 대한 합을 구한다.
3. S와 같은 경우의 수의 개수를 세아린다.
'''
tmp = []
res = 0

def dfs(idx, cnt, visited , n , s , length):
    global res 

    if cnt == length:
        if sum(tmp) == s:
            res += 1
        return
    
    for i in range(idx, n):
        if visited[i] == 0:
            visited[i] = 1
            tmp.append(num[i])
            dfs(i , cnt + 1 , visited, n , s , length)
            visited[i] = 0
            tmp.pop()

n , s = map(int,input().split())
num = list(map(int,input().split()))
visited = [0] * n

# 모든 부분 수열 구하기
for i in range(1,n+1):
    dfs(0,0,visited,n,s,i)

print(res)