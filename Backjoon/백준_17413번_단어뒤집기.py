# S = input()
# S += " " #맨마지막 공백추가
# stack = []
# result = ""
# check = 1
# for i in S:
#     if i == "<":
#         check *= -1
        
#         for j in range(len(stack)):
#             result += stack.pop() #FILO인 스택의 성질이용하면 문자열이 뒤집어진다.
    
#     stack.append(i)

#     if i == ">":
#         check *= -1
        
#         for j in range(len(stack)):
#             result += stack.pop(0) #괄호안은 뒤집지 않음

#     if (i == " ") and check == 1:
#         #뒤집어지면서 공백이 앞으로가는 것을 위해 공백제거
#         stack.pop()
#         for j in range(len(stack)):
#             result += stack.pop() #문자 뒤집에서 저장
#         result += " " #아까 제거했던 공백 추가

# print(result)

s = input()

temp = []
result = []

check = 1

for i in s:
    if i == "<":
        check *= -1 # 괄호 확인

        temp.reverse()
        result.append(''.join(temp))
        temp = [i]

    elif i == ">": #괄호 끝
        check *= -1
        temp.append(">")
        #괄호는 뒤집지 않음
        result.append(''.join(temp))
        temp = []
    elif i == " " and check == 1:
        temp.reverse()
        result.append(''.join(temp))
        result.append(' ')
        temp = []
    else:
        temp.append(''.join(i))

if temp:
    temp.reverse()
    result.append(''.join(temp))

print(''.join(result))
