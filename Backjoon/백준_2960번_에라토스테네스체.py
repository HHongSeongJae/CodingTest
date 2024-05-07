'''
2 3 4 5 6 7
'''

# N , K = map(int,input().split())

# temp = [i for i in range(2,N+1)]
# count = 0
# result = 0

# while True:
#     P = min(temp)

#     for idx, i in enumerate(temp):
#         if i == 1001: continue
#         if i % P == 0:
#             temp[idx] = 1001
#             count += 1

#             if count == K:
#                 result = i
#                 break
    
#     if result != 0:
#         print(result)
#         break

#     if temp.count(1001) == (N-2+1): # 모든 수 삭제
#         break


## 다른 풀이
## True False를 통해서 삭제값 확인

N,K = map(int,input().split())

count = 0
check = [True] * (N+1)

for i in range(2, N+1):
    for j in range(i, N+1, i): #배수만큼증가하며 리스트 삭제
        if check[j] == True: #아직삭제가 안되었으면 False로 설정
            check[j] = False
            count += 1

            if count == K:
                print(j)
                break

# 조금 더 간결하게 해결할 수 있다
# 에로토스테네스체는 소수를 찾는 좋은 알고리즘이니 잘 기억해두자