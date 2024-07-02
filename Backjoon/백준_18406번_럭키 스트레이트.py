'''
숫자를 반으로 나눠 왼쪽과 오른쪽 각자릿수의 합이 같으면 조건 부합

'''

N = input()
L = len(N) // 2

a = N[:L]
b = N[L:]

sum_a = 0
sum_b = 0 

for i,j in zip(a,b):
    sum_a += int(i)
    sum_b += int(j)

if sum_a == sum_b:
    print("LUCKY")
else:
    print("READY")