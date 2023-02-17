T = int(input())

for tc in range(1, T+1):

    n = int(input())
    a = [i for i in range(1, n**2+1)]
    box = [[0] * n for _ in range(n)]
    box[0][0] = a[0]

    def spin_move(x, y, n, start_idx):
        # 우하좌상
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        if n % 2:
            target_x = n//2
            target_y = n//2
        else:
            target_x = n//2
            target_y = n//2-1

        while box[target_x][target_y] == 0:

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and box[nx][ny] == 0:
                    box[nx][ny] = a[start_idx]
                    start_idx += 1
                    x = nx
                    y = ny
                    if i != 0:
                        dx = dx[1:] + dx[:1]
                        dy = dy[1:] + dy[:1]
                    break

        return


    spin_move(0, 0, n, 1)
    print(f"#{tc}")
    for i in range(n):
        print(" ".join(map(str, box[i])))
