import sys

sys.stdin = open('input.txt', 'r')


def check_box(n):
    # 100개부터 확인해서 걸리면 바로 리턴
    for i in range(100 - n + 1):
        for j in range(100):
            sbox = box[j][i:n + i]
            t_sbox = t_box[j][i:n + i]
            if sbox == sbox[::-1] or t_sbox == t_sbox[::-1]:
                return n
    else:
        return check_box(n - 1)


for _ in range(10):
    tc = int(input())
    n = 100
    box = [list(input()) for _ in range(n)]
    t_box = list(map(list, zip(*box)))
    print(f"#{tc} {check_box(n)}")
