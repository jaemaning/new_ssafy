T = int(input())

for tc in range(1, T + 1):
    # n : 도화지의 크기, m : 도장을 찍은 횟수
    n, m = map(int, input().split())
    # 도화지 생성
    paper = [[0] * n for _ in range(n)]
    # 도장을 찍은 회수 만큼 도화지에 칠하는걸 반복
    # 겹쳐도 이미 칠해진곳은 1 다시 칠해도 1이므로 상관 x
    for _ in range(m):
        x, y, width, height = map(int, input().split())

        for i in range(width):
            for j in range(height):
                # 도화지의 높이가 height, 넓이가 width 라고 할때 x를 열들 y를 행들이라 하자.
                # 0으로 빈 종이에 도장을 찍으면 1로 칠해짐.
                paper[x+j][y+i] = 1

    # 이후 색칠된 곳의 넓이를 확인하여 result 에 저장.
    result = 0
    for i in range(n):
        result += sum(paper[i])

    print(f"#{tc} {result}")
