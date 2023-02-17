"""
1
7 4 2 0 0 6 0 7 0
"""
import sys

sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case + 1):

    n = int(input())  # 넓이
    arr_ = list(map(int, input().split()))
    ans = -9999

    for i in range(n):
        # 현재 위치에서 맨 꼭대기 상자가 오른쪽에 장애물이(상자) 없다고 했을때 최대 낙차
        height = n - (i + 1)
        box_cnt = 0

        # 또 반복문을 돌면서 오른쪽에 있는 장애물(상자) 의 수 구하기
        for j in range(i + 1, n):
            # 높이가 나와 같거나 큰 상자의 수
            if arr_[i] <= arr_[j]:
                box_cnt += 1

        # 최대 낙차 = 현재 위치에서 오른쪽에 상자가 없을 경우 최대 낙차 - 오른쪽 상자의 수
        result = height - box_cnt

        # 최대 낙차 중 최댓값을 갱신
        if ans < result:
            ans = result

    print(f"#{tc} {ans}")
# ctl + alt + l
