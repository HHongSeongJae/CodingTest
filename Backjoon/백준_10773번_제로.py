'''
0 -> 최근에 쓴 수 지운다.
stack
모든 수의 합
'''
K = int(input())

stack = []
for _ in range(K):
    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))

# a = [1,2,3]

# a.pop()

# print(a)