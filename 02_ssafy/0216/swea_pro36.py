import sys
sys.stdin = open('input.txt', 'r')

def bt(n, arr, row, s):
    global min_v

    # 1. 탈출 조건
    # 다 골랐으면 탈출 => 탈출하면서 min_v 값 갱신
    if n == len(rlt):
        if s < min_v:
            min_v = s
        return

    # 2. 재귀 호출
    if s < min_v:
        for i in range(n):
            if checker[row][i] == False:
                s += arr[row][i]
                checker[row][i] = True
                rlt.append(arr[row][i])

                j = 1
                while row+j < n:
                    checker[row+j][i] = True
                    j += 1

                bt(n,arr,row+1, s)

                rlt.pop()

                j = 0
                while row+j < n:
                    checker[row+j][i] = False
                    j += 1
                s -= arr[row][i]



T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = []
    rlt = []
    checker = [[False] * n for _ in range(n)]
    min_v = 99999

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    bt(n, arr, 0, 0)
    print(f"#{tc} {min_v}")

    # print(arr)
