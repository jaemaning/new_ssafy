import sys

sys.stdin = open('input.txt', 'r')


def game_start(x, y, d, command):
    for c in command:
        # 슛을 하면 바라보고 있는 방향으로 포탄 발사
        if c == "S":
            # 초기 위치 저장 필요
            now = (x,y)
            nx = x + d[0]
            ny = y + d[1]

            while 0 <= nx < h and 0 <= ny < w and game_map[nx][ny] != "*" and game_map[nx][ny] != "#":
                # 갔으니까 위치 변경하고 계속 이동
                x, y = nx, ny
                nx = x + d[0]
                ny = y + d[1]

            # 다 돌고나서 멈춘 이유가 그냥 벽 때문이었다면 벽을 파괴 => 벽>평지 변경
            if 0 <= nx < h and 0 <= ny < w and game_map[nx][ny] == "*":
                game_map[nx][ny] = "."

            x, y = now

        elif c == "U":
            # 방향 변경 후
            d = (-1, 0)
            nx = x + d[0]
            ny = y + d[1]

            # 다음 이동이 맵 안에 있고 평지라면 이동
            if 0 <= nx < h and 0 <= ny < w and game_map[nx][ny] == ".":
                # 이동하며 내가 있던 원래 위치를 평지로 바꾸고 다음 위치로 이동
                game_map[x][y] = "."
                x, y = nx, ny
                game_map[x][y] = "^"
            # 못간다면 내 현재 위치에서 방향만 바꿈
            else:
                game_map[x][y] = "^"

        elif c == "D":
            # 방향 변경 후
            d = (1, 0)
            nx = x + d[0]
            ny = y + d[1]

            # 다음 이동이 맵 안에 있고 평지라면 이동
            if 0 <= nx < h and 0 <= ny < w and game_map[nx][ny] == ".":
                # 이동하며 내가 있던 원래 위치를 평지로 바꾸고 다음 위치로 이동
                game_map[x][y] = "."
                x, y = nx, ny
                game_map[x][y] = "v"
            # 못간다면 내 현재 위치에서 방향만 바꿈
            else:
                game_map[x][y] = "v"

        elif c == "L":
            # 방향 변경 후
            d = (0, -1)
            nx = x + d[0]
            ny = y + d[1]

            # 다음 이동이 맵 안에 있고 평지라면 이동
            if 0 <= nx < h and 0 <= ny < w and game_map[nx][ny] == ".":
                # 이동하며 내가 있던 원래 위치를 평지로 바꾸고 다음 위치로 이동
                game_map[x][y] = "."
                x, y = nx, ny
                game_map[x][y] = "<"
            # 못간다면 내 현재 위치에서 방향만 바꿈
            else:
                game_map[x][y] = "<"

        elif c == "R":
            # 방향 변경 후
            d = (0, 1)
            nx = x + d[0]
            ny = y + d[1]

            # 다음 이동이 맵 안에 있고 평지라면 이동
            if 0 <= nx < h and 0 <= ny < w and game_map[nx][ny] == ".":
                # 이동하며 내가 있던 원래 위치를 평지로 바꾸고 다음 위치로 이동
                game_map[x][y] = "."
                x, y = nx, ny
                game_map[x][y] = ">"
            # 못간다면 내 현재 위치에서 방향만 바꿈
            else:
                game_map[x][y] = ">"



'''
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)
'''

'''
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
'''

T = int(input())

for tc in range(1, T + 1):
    # h: 맵의 높이, w: 맵의 넓이
    h, w = map(int, input().split())
    # 맵 제작
    game_map = [list(input()) for _ in range(h)]
    # 커맨드 수
    n = int(input())
    # 커맨드 (게임 조작)
    command = list(input())

    # 시작 위치 찾기, 탱크 방향 찾기.
    for i in range(h):
        for j in range(w):
            if game_map[i][j] == "^":
                start_x, start_y, d = i, j, (-1, 0)
            elif game_map[i][j] == "v":
                start_x, start_y, d = i, j, (1, 0)
            elif game_map[i][j] == "<":
                start_x, start_y, d = i, j, (0, -1)
            elif game_map[i][j] == ">":
                start_x, start_y, d = i, j, (0, 1)

    game_start(start_x, start_y, d, command)

    print(f"#{tc}", end=" ")
    for _ in range(h):
        print(f"{''.join(game_map[_])}")
