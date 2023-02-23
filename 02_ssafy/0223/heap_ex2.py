# 교수님 v2
import random

heap = [0] * 101
# 마지막에 넣은 원소 위치
last = 0


def enq(item):
    global last
    last += 1
    heap[last] = item

    # 추가하고 나서 최대힙 조건에 부합하게 개선
    c = last
    p = c // 2  # 부모의 위치 계산
    # 부모노드가 존재하고 자식이 부모보다 작을 때까지 위치를 바꿔준다.
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 자리를 바꿨으면 부모 자식 인덱스 갱신
        c = p
        p = c // 2


def deq():
    global last
    # 루트 노드 삭제
    tmp = heap[1]
    heap[1] = heap[last]
    heap[last] = 0
    last -= 1

    # 왼쪽 자식을 기준으로 검사
    p = 1
    c = p * 2

    # 자식이 있으면
    while c <= last:
        # 만약 오른쪽 자식이 있다면, 둘중에 큰 자식과 비교를 한다.
        if c + 1 <= last and heap[c] < heap[c + 1]:
            c += 1

        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        # 그 밑에는 작은 애들만 있으니까 갈 필요가 없음.
        else:
            break

    return tmp


for i in range(10):
    enq(random.randrange(1, 10001))

print(heap)

for _ in range(10):
    print(deq())
