# (M)198의 생성자는 (N)216

n = int(input())
res = []
for i in range(n):
    temp = i
    sum = temp
    while temp > 0:
        sum += (temp % 10)
        temp = temp // 10

    if sum == n:
        res.append(i)

if len(res) == 0:
    print("0")
else:
    print(min(res))