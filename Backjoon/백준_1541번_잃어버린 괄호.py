'''
+ 연산은 괄호에 영향을 받지 않고 동일한 결과를 나타낸다.
- 연산이 괄호에 따라서 값이 바뀌게 된다.
'''

n = input().split('-')

result = []

# - 기준으로 분류된 것들은 모두 +로 이어진 것이다.
# 이들은 모두 더한다.
for i in n:
    sum = 0
    temp = i.split('+')
    
    for j in temp:
        sum += int(j)

    result.append(sum)

# 식의 첫 숫자 
start = result[0]

# 이후 숫자들은 모두 빼면 된다.
for j in range(1, len(result)):
    start -= result[j]

print(start)