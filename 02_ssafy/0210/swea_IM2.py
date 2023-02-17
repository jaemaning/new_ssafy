# 의석이의 세로로 말해요
# 다시 풀기.
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    box = [list(input().strip()) for _ in range(5)]
    max_len = -1
    for i in range(5):
        if max_len < len(box[i]):
            max_len = len(box[i])

    t_box = list(map(list, zip(*box)))
    s = ""
    for x in range(max_len):
        for y in range(5):
            try:
                s += box[y][x]
            except:
                pass

    print(f"#{tc} {s}")
