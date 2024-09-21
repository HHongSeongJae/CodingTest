# # nan = []

# # for i in range(9):
# #     nan.append(int(input()))

# nan = [int(input()) for _ in range(9)]

# # 9명 난쟁이 전체 키의 합
# a = sum(nan)

# nan.sort()

# for i in range(9): # 제외할 첫번째 난쟁이 찾기
#     for j in range(i+1 , 9): # 제외할 두번째 난쟁이 찾기
#         if a - nan[i] - nan[j] == 100:
#             for z in range(9):
#                 if z == i or z == j:
#                     continue
#                 print(nan[z])
#             exit()
