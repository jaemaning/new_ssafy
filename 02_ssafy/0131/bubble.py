"""
5
55 7 78 12 42
for i : N-1 -> 0   # 각 구간의 끝
    for j : 0 -> i-1   # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]
            arr[j] <-> arr[j+1]   # 큰 원소 오른쪽
"""


def bubble_sort_(arr_):
    cnt = 0
    for _ in arr_:
        cnt += 1

    for i in range(cnt - 1, 0, -1):  # 각 구간의 끝
        for j in range(0, i):  # 비교할 원소 구간
            if arr_[j] > arr_[j + 1]:  # 비교해서 왼쪽이 크면 자리 바꾸기
                arr_[j], arr_[j + 1] = arr_[j + 1], arr_[j]

    return arr_


arr1 = [55, 7, 78, 12, 42]
print(bubble_sort_(arr1))
