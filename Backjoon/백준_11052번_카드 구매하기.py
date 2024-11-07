n = int(input())

card = list(map(int,input().split()))

d = [0] * 1001

d[0] = 0 # 카드를 구매하지 않는 경우를 1가지로 한다.
d[1] = card[0] # 카드 1개 고르는 경우는 1개가 포함된 카드팩을 구하는 것

for i in range(1,n+1):
    for j in range(1,i+1): # 1 <= j <= i
        d[i] = max(d[i],card[j-1] + d[i-j]) # card의 리스트는 0부터 시작하므로 j-1 해줘야함
        # 점화식 : d[i] = max(d[i-j] + card[j]) # 1<=j<=i 

print(d[n])