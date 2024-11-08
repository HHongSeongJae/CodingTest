n = int(input())

d =[[0] * 2 for _ in range(91)]

d[1][1] = 1
d[1][0] = 0

for i in range(2,n+1):
    d[i][1] = d[i-1][0]
    d[i][0] = d[i-1][0] + d[i-1][1]

print(sum(d[n]))