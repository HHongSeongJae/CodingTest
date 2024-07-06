n,m = map(int,input().split())

s = []
idx = 1

def back():
    # 종료 조건
    if len(s) == m:
        print(*s)
        return
    
    #dfs , 백트래킹 수행
    for i in range(1, n+1):
        if i not in s: # 중복된 수열을 배제하기 위함
            s.append(i)
            back()
            s.pop()

back()

