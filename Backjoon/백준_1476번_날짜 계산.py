## 방법 1
# E , S , M = map(int,input().split())
# e = 1
# s = 1
# m = 1
# year = 1

# while True:
#     if e == E and s == S and m == M:
#         print(year)
#         break

#     e += 1
#     s += 1
#     m += 1

#     if e > 15:
#         e = 1
    
#     if s > 28:
#         s = 1
    
#     if m > 19:
#         m = 1
    
#     year += 1

## 방법 2
E , S , M = map(int,input().split())

E -= 1
S -= 1
M -= 1

year = 0
while True:
    if year % 15 == E and year % 28 == S and  year % 19 == M:
        print(year+1)
        break

    year += 1