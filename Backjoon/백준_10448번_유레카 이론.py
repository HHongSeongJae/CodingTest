## 반복문 처리를 투박하게 해결.. :: 476 ms
# T = int(input())

# init_tri = []

# # 삼각수 생성
# for i in range(1,46):
#     init_tri.append((i*(i+1) // 2))

# for _ in range(T):
#     K = int(input())
#     status = 0

#     for i in range(len(init_tri)):
#         for j in range(len(init_tri)):
#             for z in range(len(init_tri)):
#                 if (init_tri[i]+init_tri[j]+init_tri[z]) == K:
#                     print("1")
#                     status = 1
#                     break
#             if status == 1:
#                 break
#         if status == 1:
#                 break
#     if status != 1:
#         print("0")

## 다른 풀이 방법 :: 140ms
init_tri = []

# 삼각수 생성
for i in range(1,46):
    init_tri.append((i*(i+1) // 2))

# 삼각수 확인
res = [0] * 1001 # 3 <= K <= 1000

# 삼각수가 될 수 있는 범위 내 경우의 수를 기록한다.
for i in init_tri:
    for j in init_tri:
        for z in init_tri:
            temp = i+j+z
            if temp <= 1000:
                res[temp] = 1

T = int(input())

for _ in range(T):
    K = int(input())
    print(res[K])