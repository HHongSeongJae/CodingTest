# 브루트포스 방식 풀이
# 시간 초과 => 1칸 갈지 2칸 갈지 매번 선택
        #  => O(2^n) = 2^300 :: 불가능

# n = int(input())

# stairs = [0] * (n*2)
# res = -int(1e9)

# for i in range(1,n+1):
#     stairs[i] = int(input())

# def dfs(s , cnt , idx):
#     global res

# 		# idx 초과되면 백트래킹
# 		# cnt == 2인 것은 계단을 3개 연속 밟은 경우
#     if idx > n or cnt == 2:
#         return

# 		# 꼭대기에 도착한 경우 :: 결과값을 저장
#     if idx == n:
#         res = max(res , s)
#         return
		
# 		# 계단 1칸 올라간다 :: 1칸 올라가면 연속으로 올라가는 상황이므로 cnt+1
#     dfs(s+stairs[idx+1] , cnt+1 , idx+1)
#     # 계단 2칸 올라간다 :: 2칸은 연속으로 올라가는 것이 중단되는 것이므로 cnt = 0이 된다.
#     dfs(s+stairs[idx+2] , 0 , idx+2)

# # 각각 다른 위치에서 시작하는 함수 호출
# if n <= 2:
#     print(sum(stairs))
# else:
#     dfs(stairs[1], 0 , 1) # +1 로 시작
#     dfs(stairs[2], 0 , 2) # +2 로 시작

#     print(res)

## DP
## 해당 계단을 선택할 것인지 아닌지
n = int(input())

dp = [0] * (n+1)
stairs = [0] * (n+1)

for i in range(1 , n+1):
    stairs[i] = int(input())

if n <= 2:
    print(sum(stairs)) # 2이하는 1칸씩 올라가는 방법뿐
else:
    # dp 초기값
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, n+1):
        # n번째 계단에 올라올 수 있는 경우의 수 2가지
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i] , dp[i-2] + stairs[i]) # 점화식

    print(dp[n])
