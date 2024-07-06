'''
예제 1
1234 56789.... :: 최솟값 : 4
1 234 56789 10 1112131415161718 19 20 :: 최솟값 : 20
'''

n = input()

# 일치 숫자 확인
check = 0 # 현재 숫자의 숫자들과 일치 여부 확인
idx= 0  # 어느 숫자를 확인하고 있는지 유지

while True:
    check += 1

    for c in str(check):  # string타입 n과 숫자를 비교하기 위해 정수를 str로 변경
        if n[idx] == c: # 일치하면 idx를 하나 늘려 다음 수를 확인
            idx += 1

            if idx >= len(n): # idx의 범위가 입력받은 n보다 넘어가면 중단
                print(check)
                exit()