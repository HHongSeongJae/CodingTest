## 오답 -> 해당 코드는 누적합 방식으로 구현되었고, 해당 문제는 누적합 방식으로 구해지는 것이 아니다
# n = int(input())

# card = []

# for _ in range(n):
#     card.append(int(input()))

# res = 0
# card.sort()

# if n > 2:
#     tmp = card[0] + card[1]
#     res += tmp

#     for i in range(2, n):
#         tmp = tmp + card[i]
#         res += tmp
#     print(res)
# else:
#     # n = 1,2 인 경우
#     if n == 1:
#         print("0")
#     else:
#         print(card[0] + card[1])

## 

## heap.push / heap.pop
import heapq

n = int(input())

# 힙 선언
card = []
res = 0

for _ in range(n):
    heapq.heappush(card, int(input()))

# heap에서 2개씩 요소를 빼서 합을 구한다.
# 더해진 값은 다시 heap에 넣음으로써 새롭게 정렬된다. (min heap 방식)
while True:
    if len(card) <= 1:
        print(res)
        break

    tmp = (heapq.heappop(card) + heapq.heappop(card))
    res += tmp
    heapq.heappush(card, tmp)