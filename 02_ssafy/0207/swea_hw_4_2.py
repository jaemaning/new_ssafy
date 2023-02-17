import sys

sys.stdin = open('input.txt', 'r')


def ladder_reverse(x, y):
    # 상, 좌, 우
    dx = [-1, 0, 0]
    dy = [0, -1, 1]

    # 위,아래 모드 변경 스위치 처음엔 위로 가겠지?
    switch = 0

    while True:
        # next_x , next_y 는 switch 방향으로 이동중
        nx = x + dx[switch]
        ny = y + dy[switch]

        # 스위치 on (즉 좌,우로 가고 있을때 : 위만 확인)
        if switch:

            # 끝에 도달(정답)
            if x-1 == -1:
                return y

            # 위에 값이 있다면? => 좌, 우로 다 갔구나,,
            if 0 <= x-1 < 100 and 0 <= y < 100 and ladder[x-1][y]:
                # 값 변경 및 스위치 끄기
                x -= 1
                switch = 0

            # 위에 값이 없었고, 좌 or 우 값이 있다면? => 그 방향으로 계속 가자,,
            # else 로도 처리가능할듯?
            else:
                x, y = nx, ny

        # 스위치가 off (즉 위로 가고있다 : 좌, 우를 확인하자)
        else:

            # 끝에 도달(정답)
            if nx == -1:
                return y

            # 왼쪽에 값이 있다면? => 옆길로 새자,,
            if 0 <= x < 100 and 0 <= y-1 < 100 and ladder[x][y-1]:
                # 값 변경 및 스위치 1번으로 변경
                y -= 1
                switch = 1

            # 오른쪽에 값이 있다면? => 옆길로 새자,,
            elif 0 <= x < 100 and 0 <= y+1 < 100 and ladder[x][y+1]:
                # 값 변경 및 스위치 2번으로 변경
                y += 1
                switch = 2

            # 좌, 우가 없다면? => 계속 위로 가자,,
            else:
                x, y = nx, ny


for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[-1][i] == 2:
            print(f"#{tc} {ladder_reverse(99, i)}")
