
'''
(N , K)
1 2 3 4 5 6 7    :: 3      2
1 2 4 5 6 7      :: 6      4
1 2 4 5 7        :: 2      6  -> 6-5 = 1
1 4 5 7          :: 7      3
1 4 5            :: 5      5  -> 5 - 3 = 2
1 4              :: 1      4  -> 4 - 2 = 2  -> 2 - 2 = 0
4                :: 4


K 번째부터 N번째 사람 제거
'''

N, K = map(int, input().split())

n = [i for i in range(1,N + 1)]
result = []

idx = 0

while True:
    if len(n) == 0:
        break

    idx += (K - 1)
    idx %= len(n)

    # result.append(str(n[idx]))
    # n.remove(n[idx])
    result.append(str(n.pop(idx)))



print('<', end="")
for i in range(len(result)):
    if i == len(result) - 1:
        print(str(result[i]) , end='')
    else:
        print(str(result[i]) , end=', ')
print('>', end="")

# print('<', ', '.join(result), '>' , sep="")

################################################################

N, K = map(int, input().split())

n = [i for i in range(1,N + 1)]

result = []
idx = 0
while True:
    if len(n) == 0:
        break

    idx = (idx + K - 1) % len(n)

    result.append(str(n.pop(idx)))
    # result.append(str(n[idx]))
    # n.remove(n[idx])


print('<', ', '.join(result), '>' , sep="")
