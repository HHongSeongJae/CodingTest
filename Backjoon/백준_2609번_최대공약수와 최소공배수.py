# 최대 공약수 구하기
def getGCD(a,b):
    if b == 0:
        return a
    else:    
        # 유클리드 호제법에 따른 재귀적 반복 구현
        return getGCD(b , a % b)
    
# 최소 공배수
def getLCM(a,b, gcd):
    return gcd * (a // gcd) * (b // gcd)

a,b = map(int,input().split())

gcd = getGCD(a,b)

print(gcd)
print(getLCM(a,b,gcd))