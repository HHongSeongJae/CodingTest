T = int(input())

def dfs():
    if len(s) == len(L):
        for i in s:
            print(L[i] , end="")
        print()
        return

    for i in range(len(L)):
        if visited[i] == 1: # 방문했던 것은 무시
            continue

        visited[i] = 1 #방문 처리
        s.append(i)
        dfs()
        s.pop()
        visited[i] = 0

count = 0
for _ in range(T):
    L = input()
    s = []
    visited = [0] * (len(L))
    
    count += 1
    print(f"Case # {count}:")

    dfs()