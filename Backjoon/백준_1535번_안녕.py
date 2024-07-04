'''
세준이 인사 -> L[i] 만큼 체력을 잃고 , J[i] 만큼 기쁨을 얻는다. 
:: 주어진 체력내에 최대한 기쁨을 느끼는 것이 목표

체력이 0 혹은 음수가 되면 죽어서 기쁨을 못 느낌
세준이가 얻을 수 있는 최대 기쁨
'''
'''
입력1 : 잃는 체력 (처음 체력 100)
입력2 : 얻는 기쁨 
'''

N = int(input())
m_life = list(map(int,input().split())) # 인사할 때 감소하는 체력
happy = list(map(int,input().split()))  # 인사할 때 증가하는 기쁨

result = 0

def hello(i, cur_life , cur_happy):
    global result

    # 함수 종료 조건
    # 체력 소진
    if cur_life <= 0:
        prev = cur_happy - happy[i-1] # 죽은 단계의 기쁨은 추가하지 않는다. 
                                      # 죽기 직전의 기쁨이 결과 값이 된다.
        result = max(result, prev) # 최대 기쁨 값 유지
        return
    # 모든 사람 탐색 완료
    if i == N: 
        result = max(result, cur_happy) # 최대 기쁨 값을 유지
        return
    
    #인사 진행
    temp_happy = cur_happy + happy[i]
    temp_life = cur_life - m_life[i]

    #인사
    hello(i + 1 , temp_life , temp_happy)
    #인사안함
    hello(i + 1 , cur_life, cur_happy)

hello(0 , 100, 0)
print(result)