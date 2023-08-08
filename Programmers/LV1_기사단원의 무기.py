def solution(number, limit, power):
    answer = 0
    a = []
    #약수 구하기
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**(1/2))+1): #i**(1/2) => 루트(i)
            if(i % j == 0):
                count += 1
                if (j**2 != i): #제곱이 되는 수를 count+1을 해주어 중복 방지 
                    count += 1
            if(count > limit):
                count = power
                break
        a.append(count)
    
    answer = sum(a)
    return answer