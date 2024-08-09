import sys

input = sys.stdin.readline

n = int(input())

res = []
for _ in range(n):
    res.append(int(input()))

res.sort()

for i in res:
    print(i)