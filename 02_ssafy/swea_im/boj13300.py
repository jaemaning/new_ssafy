# boj 13300 - 방 배정 ( IM 대비 문제 )
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

room = [[0] * 7 for _ in range(2)]
room_cnt = 0

for _ in range(n):
    s, y = map(int, input().split())
    room[s][y] += 1

for i in range(2):
    for j in range(7):
        room_cnt += room[i][j] // k
        if room[i][j] % k:
            room_cnt += 1

print(room_cnt)
