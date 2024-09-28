# N = int(input())

# i = 2
# res = str(1)
# while i <= N+1:
#     if i-1 == N:
#         print(len(res))
#         break

#     res = res + str(i)
#     i += 1
#     print(res)

## => 시간 초과


### 자릿수 별로 구하기
N = int(input()) 

length = 1
start = 1
ans = 0
while start < N:
    end = start * 10 - 1 # end = 9

    if end > N:
        end = N

    ans += (end - start + 1) * length

    length += 1
    start *= 10

print(ans)