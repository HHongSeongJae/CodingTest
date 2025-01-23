n = int(input())
a = list(map(int,input().split()))
a_hash = dict()

m = int(input())
b = list(map(int,input().split()))

for tmp in a:
    a_hash[tmp] = 0

# 해시 탐색
for i in b:
    if i in a_hash:
        print('1')
    else:
        print('0')