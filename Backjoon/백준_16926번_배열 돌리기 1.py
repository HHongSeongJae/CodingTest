n,m,r = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]

# 1차원 배열을 저장할 빈 리스트
groups = []

# 문제조건 : min(N, M) mod 2 = 0
# groupn이 끝에서 부터 k번 떨어진 k의 범위가 된다.
groupn = min(n,m) // 2 

# 그룹 만들기
# 마지막 범위의 자릿수는 겹치지 않도록 범위를 설정한다.
for k in range(groupn):
    group = []

    # 1
    for j in range(k,m-k):
        group.append(A[k][j])
    
    # 2
    for i in range(k+1 , n-1-k):
        group.append(A[i][m-1-k])

    # 3
    for j in range(m-k-1 , k , -1): # k+1 <= j <= m-k-1
        group.append(A[n-1-k][j])
    
    # 4
    for i in range(n-1-k , k , -1): # k+1 <= i <= n-k-1
        group.append(A[i][k])

    groups.append(group)

print(f'debug : {groups}')

# index를 이용하여 회전시킨 후 다시 넣기
for k in range(groupn):
    group = groups[k]
    l = len(group)

    idx = r % l # 배열의 길이를 초과하는 회전 횟수면 % 연산자를 통해서 범위 초과 방지

# idx에 대해서 그룹을 변화시키고 그룹을 넣을 때에는 그룹을 만들었던 범위 그대로 넣어주어야한다.
    # 1
    for j in range(k,m-k):
        A[k][j] = group[idx]
        idx = (idx+1) % l
    
    # 2
    for i in range(k+1 , n-1-k):
        A[i][m-1-k] = group[idx]
        idx = (idx+1) % l

    # 3
    for j in range(m-k-1 , k , -1):
        A[n-1-k][j] = group[idx]
        idx = (idx+1) % l
    
    # 4
    for i in range(n-1-k , k , -1):
        A[i][k] = group[idx]
        idx = (idx+1) % l

for res in A:
    print(*res)