def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):
        print(i)
        check = []
        for j in want:
            num = discount[i:i+10].count(j)
            print(num)
            check.append(num)
        
        if(check == number):
            answer = i + 1
            break

    return answer