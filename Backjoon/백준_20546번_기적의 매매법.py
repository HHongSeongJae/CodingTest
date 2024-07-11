'''
# 준현(BNF)
- 한번산 주식을 절대 팔지 않는다.
- 주식을 살 수 있다면 최대한 많이산다. 그리고 이후에 주식을 살 수 있다면 즉시 매수한다.

# 성민 (TIMMING)
- 모든 거래는 전량 매수와 전량 매도  :: 현금 < 주가 -> 주식 살 수 없다. / 현금 > 주가 -> 최대의 수로 산다.
- 3일 연속 가격이 전일 대비 상승하는 주식은 다음날 무조건 가격이 하락  :: 주식 전량 매도
- 3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가격이 상승  :: 주식 전량 매수

준현이(BNP)와 성민이(TIMING) 중 더 높은 수익률을 내는지 예측
'''

# BNF (현금, 주가)
def BNP(money, price):
    result = 0 # 투자 후 얻은 자산
    temp = 0
    for i in price:
        # 살 수 있으면 최대한 산다.
        if money >= i:
            # 최대한 살 수 있는 주식 수
            temp = money // i
            money = money - (temp * i)
    result = temp * i + money
    return result

# TIMMING
def TIMING(money, price):
    buy = []

    before_pri = 0
    up_check = -1 # 3일 연속 상승 확인
    down_check = -1 # 3일 연속 하락 확인
    for i in price:
        if i > before_pri: # 상승
            up_check += 1
        elif i < before_pri: # 하락
            down_check += 1
        else: # 가격이 유지되면 연속 카운트
            up_check = 0
            down_check = 0

        # rule1 : 3일 연속 상승하면 전량 매도 (동일 주가 제외)
        if up_check == 3:
            # 전량 매도
            for j in buy:
                money += (i * j) # 현재주가의 주식 개수만큼 가격을 더하면 전량 매도

            buy = [] # 싹다 비워서 초기화
            up_check = 0
            down_check = 0

        # rule2 : 3일 연속 하락하면 전량 매수 (동일 주가 제외)
        if down_check == 3:
            # 전량 매수 + 현재 돈 상황 확인
            if money > i: # 주식을 살 돈이 있음
                #전량 매수
                temp = money // i # 살 수 있는 주식 개수
                money = money - (temp * i) # 남은돈
                
                buy.append(temp) # 구매한 주식 개수 유지

            up_check = 0
            down_check = 0

        before_pri = i 

    # 14일 자산
    result = sum(buy) * i + money
    return result

n = int(input())
#주가
price = list(map(int,input().split()))

# 결과 확인
result_1 = BNP(n,price)
result_2 = TIMING(n,price)

if result_1 > result_2:
    print("BNP")
elif result_1 < result_2:
    print("TIMING")
else:
    print("SAMESAME")