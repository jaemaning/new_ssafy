# 믈놀이를 가자
import sys

sys.stdin = open('input.txt', 'r')


from collections import deque

def solve_greedy(wp, cnt):
    '''
    :param wp : 물 위치 저장 리스트
    :return: wp 로 리턴
    '''
    for _ in range(wp):
        x, y = wp.pop()

        for i in range(4):







T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    w_map = [list(input()) for _ in range(n)]
    ans = 0
    # 상하좌우
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    visited = [[0] * m for _ in range(n)]
    scores = [[0] * m for _ in range(n)]
    wp = set()
    mc = n*m

    for i in range(n):
        for j in range(m):
            # 물인 모든 칸 저장, 방문 처리
            if w_map[i][j] == 'W':
                visited[i][j] = 1
                wp.add((i,j))


    while mc != 0:
        wp = solve_greedy(wp, 1)

    print(f"#{tc} {ans}")
