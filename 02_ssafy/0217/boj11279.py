import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n):
    num = int(input())
    if num:
        heapq.heappush(heap, (-num, num))
    # num == 0 이고 heap 이 비어있지 않으면?
    elif num == 0 and heap:
        print(heapq.heappop(heap)[1])
    else:
        print(0)