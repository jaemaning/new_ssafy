import sys
three_arr = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
three_arr[0][0][0] = 1

input = sys.stdin.readline


def w(a, b, c):

    if three_arr[a][b][c] != 0:
        return three_arr[a][b][c]

    else:
        if a <= 0 or b <= 0 or c <= 0:
            return three_arr[0][0][0]

        if a < b and b < c:
            while three_arr[a][b][c] == 0:


while True:
    a, b, c = input().split()

    if a == b == c == -1:
        break
