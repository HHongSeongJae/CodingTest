'''
A B 의 크기
A배열
B배열
'''
a,b = map(int,input().split())

a_num = list(map(int,input().split()))
b_num = list(map(int,input().split()))

new = (a_num + b_num)

new.sort()

print(*new)

## 문자열로 입력받고 join을 통해서 이를 합치는 방법을 사용했는데 런타임에러
# input()
# a = input().split()
# b = input().split()

# print(*(sorted("".join(a+b), key=int)))
