# # set 자료형
# n = int(input())
# number = set(map(int,input().split()))

# m = int(input())
# check = list(map(int,input().split()))

# res = []
# for c in check:
#     if c in number:
#         res.append("1")
#     else:
#         res.append("0")

# print(*res)

# dict 자료형
n = int(input())
number = list(map(int,input().split()))

m = int(input())
check = list(map(int,input().split()))

n_dict = {}

for n in number:
    n_dict[n] = 0 # 초기화

for c in check:
    if c in n_dict:
        print("1" , end=' ')
    else:
        print("0" , end=' ')