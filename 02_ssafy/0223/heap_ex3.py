import heapq

hq = []

# 기본
# for i in range(10):
#     heapq.heappush(hq, -i)
#
# for i in range(10):
#     print(-heapq.heappop(hq), end=" ")

# 응용
# heapq.heappush(hq, (4, "4등"))
# heapq.heappush(hq, (3, "3등"))
# heapq.heappush(hq, (1, "1등"))
# heapq.heappush(hq, (2, "2등"))
#
# print(heapq.heappop(hq))
# print(heapq.heappop(hq))
# print(heapq.heappop(hq))
# print(heapq.heappop(hq))

# 최대 힙
for i in range(10):
    heapq.heappush(hq, (-i, i))

for i in range(10):
    print(heapq.heappop(hq)[1])