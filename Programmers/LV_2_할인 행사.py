#def solution(want, number, discount):
#     answer = 0
    
#     for i in range(len(discount) - 9):
#         print(i)
#         check = []
#         for j in want:
#             num = discount[i:i+10].count(j)
#             print(num)
#             check.append(num)
        
#         if(check == number):
#             answer = i + 1
#             break

#     return answer

def solution(want, number, discount):
    answer = 0
    
    new_list = []
    for i in range(len(want)):
        for j in range(number[i]):
            new_list.append(want[i])
    new_list.sort()
    
    for i in range(len(discount) - 9):
        check = discount[i:i+10]
        check.sort()
        if(check == new_list):
            answer += 1

    return answer