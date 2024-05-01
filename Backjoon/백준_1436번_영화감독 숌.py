'''
어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수를 말한다.
제일 작은 종말의 수는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 이다
'''

## 시간 초과
## 다음과 같이 코드를 구성하게되면 666 케이스는 뛰어넘는 꼴이 되기 때문에 무한루프에 빠져서 시간초과가 발생한 것으로 보인다.
# n = int(input())
# num = 666
# cnt = 1
# while True:
#     num += 1    
#     if ('666' in str(num)):
#         cnt += 1

#         if cnt == n:
#             print(num)
#             break

## 통과
## 666 케이스도 바로 검사되도록 num+=1이 마지막으로 이동해야한다.
n = int(input())
num = 666
cnt = 0
while True:

    if ('666' in str(num)):
        cnt += 1

        if cnt == n:
            print(num)
            break
    num += 1    

## 이렇게 자릿수를 구해서 하는 방식은 연속적인 6이 나와야하는 것을 찾아야해서 매우 어려움이 존재
# def c(num):
#     #자릿수 확인
#     l = len(str(num))
#     di = pow(10,l-1)ㅇ
#     count = 0
#     while True:
#         if num // di == 6:
#             be = 1
#             count += 1
        
#         num = num % di
#         di = di // 10

#         if di < 1:
#             return count


# ## 각자리 숫자를 세어서 구하기
# n = int(input())
# num = 666

# count = 0
# while True:
#     cnt = c(num)
#     if(cnt >= 3):
#         count += 1
        
#         if count == n:
#             print(num)
#             break
#     num+=1
