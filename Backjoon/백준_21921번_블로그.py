'''
N : 블로그 시작하고 난 일수
X : X일간 가장 많이 들어온 방문자수

가장 많은 방문자 출력
가장 많은 방문자가 0이면 SAD
'''

## 시간초과
## 원인 : 반복문안에 sum이 있다. sum은 O(n)이라는 시간복잡도를 가지므로, for문이 돌때마다 시간을 잡아먹는다.
##        따라서 sum은 한번만 쓰고 슬라이딩 윈도우 방식을 고려해야함
# import sys

# input = sys.stdin.readline

# n , x=map(int,input().split())

# hit = list(map(int,input().split()))
# max_num = 0
# cnt = 1

# for i in range(len(hit)):
#     if (i+x) > len(hit):
#         break
#     else:
#         temp = sum(hit[i:i+x])
        
#         if temp > max_num:
#             max_num = temp
#             cnt = 1
#         elif temp == max_num:
#             cnt += 1

# if max_num == 0:
#     print("SAD")
# else:
#     print(max_num)
#     print(cnt)

## 슬라이딩 윈도우 방식
import sys

input = sys.stdin.readline

n , x=map(int,input().split())
hit = list(map(int,input().split()))

max_num = sum(hit[:x])
temp = max_num
cnt = 1

for i in range(x, len(hit)):
    # x의 크기를 가진 window를 한칸씩 슬라이딩
    temp -= hit[i-x]
    temp += hit[i]

    if temp > max_num:
        max_num = temp
        cnt = 1
    elif temp == max_num:
        cnt += 1

if max_num == 0:
    print("SAD")
else:
    print(max_num)
    print(cnt)