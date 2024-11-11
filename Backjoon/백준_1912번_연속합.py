n = int(input())
a = list(map(int,input().split()))

d = [0] * n

for i in range(n):
    d[i] = a[i]

    # i == 0 이면 앞에 수가 존재하지 않음
    if i == 0: continue

    # 연속합의 최대를 찾는다
    d[i] = max(d[i] , d[i-1] + a[i])

# print(d)
print(max(d))