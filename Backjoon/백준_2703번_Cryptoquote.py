import sys

T = int(input())

for _ in range(T):
    n = sys.stdin.readline().strip()
    m = sys.stdin.readline().strip()

    alpha = [0 for i in range(26)]

    # print(alpha)
    start = ord('A')
    idx = 0
    for i in m:
        alpha[idx] = ord(i) - start
        idx+=1
    
    for i in n:
        if i == ' ':
            print(' ',end='')
        else:
            print(chr((alpha[ord(i) - start]) + start),end='')
    print()