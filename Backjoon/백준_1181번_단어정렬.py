# N = int(input())

# word = []

# for i in range(N):
#     a = input()
#     if a not in word:
#         word.append(a)

# word.sort(key = lambda x : (len(x), x))

# for i in word:
#     print(i)

# import sys

# N = int(input())

# word = []

# for i in range(N):
#     a = sys.stdin.readline()
#     if a not in word:
#         word.append(a)

# word.sort(key = lambda x : (len(x), x))

# for i in word:
#     print(i)

import sys

N = int(sys.stdin.readline())

word = []

for i in range(N):
    a = sys.stdin.readline().strip()
    word.append(a)

#중복 제거를 위한 set
set_word = set(word)

#정렬을 위해 다시 리스트 변환
word = list(set_word)

word.sort(key = lambda x : (len(x), x))

for i in word:
    print(i)
