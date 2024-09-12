'''
- N의 진짜 약수의 개수
- N의 진짜 약수 (1과 자기 자신은 제외)

=> N을 찾기
'''

a = int(input()) # 진짜 약수의 개수

num = list(map(int,input().split())) # 진짜 약수

# 1과 N을 제외한 모든 약수가 num으로 주어짐
# 주어진 약수에서 가장 작은 값과 가장 큰 값을 곱해주면 된다.

num.sort()

print(num[0] * num[-1])