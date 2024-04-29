'''
우선순위가 가장 먼저 프린트(숫자 클수록 중요도up)
문서 개수, b번째로 인쇄될 문서의 인덱스
'''

'''
구현
1. 입력 받기
2. 우선순위 내림차순 정렬
3. 
'''
import sys

T = int(input())

for _ in range(T):
    a,b = map(int,sys.stdin.readline().split())
    # pri = list(map(int,input().split()))
    pri = list(map(int,sys.stdin.readline().split()))

    temp = [i for i in range(a)] # 우선순위 관리 (0~a-1)

    count = 0 # 인쇄 카운트

    while True:
        if pri[0] == max(pri): #현재의 문서가 최고 우선순위를 가지면 프린트
            count += 1
            
            #찾는 우선순위가 프린트될 횟수 출력
            if temp[0] == b:
                print(count)
                break
            else:
                #현재 문서가 최고 우선순위이지만 내가 찾고있는 문서의 출력횟수가 아닌 경우, 그냥 출력한다.
                del pri[0]
                del temp[0] #하나가 출력되었기 때문에 우선순위 하나 차감
        else: # 현재 문서보다 우선순위가 높은 문서가 있다면 현재 문서를 리스트의 가장 뒤에 위치시킨다.
            pri.append(pri[0])
            del pri[0]
            temp.append(temp[0])
            del temp[0]
