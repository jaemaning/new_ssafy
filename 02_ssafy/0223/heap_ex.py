'''
완전이진트리
0번 index 사용 x
1번 index - last index 까지
'''

# 최대 100개의 key
# 최대 힙
heap = [0] * 101
# 아직까지 트리에 삽입이 0
last = 0

# 최대힙 삽입 구현
def enque(n):
    global last
    # 마지막 위치 인덱스 증가
    last += 1
    # 마지막 위치에 정점 추가
    heap[last] = n
    # 마지막 정점 삽입 후 부모랑 크기 비교
    c = last  # 현재 자식 인덱스
    p = c//2  # 자식의 부모 인덱스
    # 부모 자식 크기 비교후 자식이 더 크면 자리 바꾸기
    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 자리를 바꾸면 다시 부모랑 크기 비교를 위해 인덱스 최신화
        c = p
        p = c//2

    # 삽입 끝


# 최대힙 삭제 구현
def deque():
    global last
    # 마지막값 => last
    root = 1
    # root 와 마지막 값 변경
    # heap[root], heap[last] = heap[last], heap[root]
    tmp = heap[1]
    heap[1] = heap[last]
    heap[last] = 0
    # 바뀐 root 와 자식들을 비교하며 root 의 자리찾기
    while root < last and (heap[root] < heap[root+1] or heap[root] < heap[root+2]):
        # 왼쪽 자식보다 오른쪽 자식이 클때
        if heap[root+1] < heap[root+2]:
            heap[root+2], heap[root] = heap[root], heap[root+2]
            root += 2
        # 오른쪽 자식보다 왼쪽 자식이 클때
        else:
            heap[root+1], heap[root] = heap[root], heap[root+1]
            root += 1

    # 출력
    last -= 1
    return tmp


# 교수님 v
def deque2():
    global last
    tmp = heap[1]    # root 임시 저장
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p * 2 # 왼쪽 자식 기준

    while c <= last:    # 자식이 하나 이상 있으면
        # 오른쪽 자식도 있고, 오른쪽 자식의 키가 더 크면 비교 대상을 오른쪽 자식으로 변경
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1

        # 그래서 왼쪽이나 오른쪽 자식 중 큰놈 보다 부모가 더 작으면 자리 바꾸기
        if heap[c] > heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p * 2 # 왼쪽 자식 기준

        # 안 크면 안 바뀜

    return tmp



enque(3)
enque(19)
enque(10)
enque(6)
enque(4)
print(last)
print(heap)

print(deque())
print(deque())
print(deque())
print(deque())
print(deque())
print(heap)