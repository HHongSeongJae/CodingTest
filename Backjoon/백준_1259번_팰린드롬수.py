## 팰린드롬 파이썬 뒤집기를 활용하지 않고 풀이

import sys

while True:
    n = sys.stdin.readline().strip()

    if n == "0":
        break
    
    check = 0
    for i in range(len(n) // 2):
        if n[i] != n[(len(n) - 1) - i]:
            check = 1
        
    if check == 1:
        print("no")
    else:
        print("yes")

# 파이썬 문자열 뒤집기를 활용한 간단한 풀이
# import sys

# while True:
#     n = sys.stdin.readline().strip()

#     if n == "0":
#         break

#     new_n = n[::-1]

#     if new_n == n:
#         print("yes")
#     else:
#         print("no")
    