# res = []

# def dfs(idx, cnt , visited , k , s):
#     global res

#     if cnt == 6:
#         print(' '.join(map(str,res)))
#         return
    
#     for i in range(idx, k):
#         if visited[i] == 0:
#             visited[i] = 1
#             res.append(s[i])
#             dfs(i , cnt + 1 , visited , k , s)
#             visited[i] = 0
#             res.pop()

# while True:
#     n = list(map(int,input().split()))

#     if n[0] == 0:
#         break

#     k = n[0]
#     s = n[1:]

#     visited = [0] * k
#     dfs(0,0,visited,k,s)
#     print()

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

while True:
    n = list(map(int,input().split()))

    if n[0] == 0:
        break

    k = n[0]
    s = n[1:]
    
    # k개의 숫자 중 6개의 숫자를 선택하기 위한 시작 순열
    d = [0] * (k-6) + [1] * 6  # 0 : 선택 x , 1 : 선택 o
    res = []
    
    while True:
        cur_permutation = [s[i] for i in range(k) if d[i] == 1] # 0111111 , 1011111 .. 와 같이 생성되는 순열에서 1로 표시된 위치에 s리스트의 숫자를 선택한다.
        res.append(cur_permutation)
        
        # 다음 순열 구하기
        # 혹시나 마지막이면 반복 종료
        if next_permutation(d) == False:
            break
    
    # 사전순 출력이므로 정렬
    res.sort()
        
    for i in res:
        print(' '.join(map(str,i)))
    print()