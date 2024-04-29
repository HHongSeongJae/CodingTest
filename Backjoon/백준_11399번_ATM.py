'''
i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다


정렬 => 인출시간이 짧은 사람순으로 배치하고 인출시간 계산
'''

N = int(input())

people = list(map(int, input().split()))
people.sort()

total = 0
for i in range(1,N+1):
    total += sum(people[:i])

print(total)