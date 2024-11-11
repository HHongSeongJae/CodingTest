## 오답

# n = int(input())
# a = list(map(int,input().split()))
# res = []
# d = [0] * 1001

# for i in range(n):
#     d[i] = 1
#     s = ''
#     for j in range(i):
#         if a[i] > a[j]:
#             if d[j] + 1 > d[i]:
#                 d[i] = d[j] + 1
#                 s += (str(a[j]) + ' ')
#     s += str(a[i]) # 본인 추가
#     res.append(s)

# ans1 = max(d)
# ans2_idx = d.index(ans1)
# ans2 = res[ans2_idx]

# print(ans1)
# print(ans2)


## 재귀를 통한 역추적
# n = int(input())
# a = list(map(int,input().split()))

# d = [0] * n
# v = [-1] * n # 이전 위치 인덱스의 위치를 저장하는 것이므로 0으로 초기화하면 안된다.

# for i in range(n):
#     d[i] = 1
#     for j in range(i):
#         if a[i] > a[j]:
#             if d[j] + 1 > d[i]:
#                 d[i] = d[j] + 1
#                 v[i] = j

# res = max(d)

# print(res)

# tmp = d.index(res) # 최대 길이 수열의 인덱스 위치를 찾는다.

# # 재귀 방식을 이용하여 가장 긴 부분 수열을 역추적한다.
# def go(n):
#     if n == -1:
#         return

#     go(v[n])
#     print(a[n], end=' ')

# go(tmp)

## 반복문을 통한 역추적
n = int(input())
a = list(map(int,input().split()))

d = [0] * n
v = [-1] * n # 이전 위치 인덱스의 위치를 저장하는 것이므로 0으로 초기화하면 안된다.

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[i] > a[j]:
            if d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                v[i] = j

res = max(d)

print(res)

tmp = d.index(res) # 최대 길이 수열의 인덱스 위치를 찾는다.

# 재귀 방식을 이용하여 가장 긴 부분 수열을 역추적한다.
ans = []
while tmp != -1: # 이전 인덱스가 -1이면 더이상 이전 수열이 없는 것
    ans.append(a[tmp])
    tmp = v[tmp] # 이전 인덱스를 찾는다.

# 현재 만들어진 수열은 역순이므로 뒤집기
ans.reverse()

print(' '.join(map(str,ans)))