n = int(input())

d = [0] * (n+1)

for i in range(1,n+1):
    d[i] = i # 모두 1로 구성되었을 때 가지 수로 초기화
    
    for j in range(1,i+1):
        if j*j > i: # 1 <= i^2 <= n 조건 # 이때 1<=j<=i 이면 i가 n이 된다.
            break
        
        # D[i] : N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수
        d[i] = min(d[i], d[i-(j*j)] + 1) # 최소의 개수를 유지

print(d[n]) # n을 제곱수로 만들 수 있는 최소의 개수가 된다.