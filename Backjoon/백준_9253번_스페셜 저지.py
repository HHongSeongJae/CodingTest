## 시간 초과

# import sys

# input = sys.stdin.readline

# a = input().strip()
# b = input().strip()
# c = input().strip()

# max_cnt = 0
# for i in range(len(b)):
#     temp = b[i:]

#     if (temp in a) == True:
#         if temp == c:
#             print("YES")
#         exit()

# print("NO")

## 정말로 단순하게 문자열에 존재하는지만 비교하면 간단히 해결되는 문제
## 너무 복잡하게 생각을 했다.
## 사용자가 입력한 답인 C가 a와 b에 모두 존재한다면 그것이 정답인 것이기 때문에 if문으로 한번에 풀이가 될 수 있다.
a = input()
b = input()
c = input()

if c in a and c in b:
    print("YES")
else:
    print("NO")