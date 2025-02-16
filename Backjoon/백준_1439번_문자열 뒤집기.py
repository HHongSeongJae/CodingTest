s = input()

one = []
zero = []

bidx = 0
tmp = s[0]

for idx , i in enumerate(s):
    if tmp == i:
        continue
    else:
        if tmp == '1':
            one.append(s[bidx:idx])
            bidx = idx
        else:
            zero.append(s[bidx:idx])
            bidx = idx
    
    tmp = i

# 리스트 슬라이싱의 범위로 인하여 마지막 부분이 포함되지 않는 것에 대한 처리
if i == '1':
    one.append(s[bidx:])
else:
    zero.append(s[bidx:])

print(zero)
print(one)

print(min(len(zero),len(one)))