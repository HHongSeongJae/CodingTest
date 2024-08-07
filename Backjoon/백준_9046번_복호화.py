# 오답 코드
# n = int(input())

# for _ in range(n):
#     s = input()
#     check = [0 for _ in range(256)]

#     for i in s:
#         check[ord(i)] += 1

#     # 최빈 단어가 여러 개 있는지 확인
#     if check.count(max(check)) > 1:
#         print("?")
#     else:
#         temp = check.index(max(check))
#         print(chr(temp))

# (수정 후) 정답 코드
## 오답의 원인
## 입력되는 문자열이 asvdge ef ofmdofn와 같이 공백이 포함되어있다.
## 하지만 오답 코드와 같이 코드를 진행하게 되면 공백도 함께 처리를 하게 된다.
## 그래서 공백에 대해서는 continue를 통해서 카운트를 하지 않도록 처리하였더니 정답이 되었다.
n = int(input())

for _ in range(n):
    s = input()
    check = [0 for _ in range(256)]

    for i in s:
        if i == ' ':
            continue
        check[ord(i)] += 1

    # 최빈 단어가 여러 개 있는지 확인
    if check.count(max(check)) > 1:
        print("?")
    else:
        temp = check.index(max(check))
        print(chr(temp))