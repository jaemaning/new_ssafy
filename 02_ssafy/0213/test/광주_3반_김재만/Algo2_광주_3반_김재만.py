T = int(input())

for tc in range(1, T + 1):
    # n : 두더지 출현횟수
    n = int(input())
    # (r, c) : 망치 위치
    r, c = map(int, input().split())
    cnt = 0
    for _ in range(n):
        # (a, b) : 두더지위치. k : 두더지 잡을 시간
        a, b, k = map(int, input().split())
        # 시간인 k가 0이 될떄까지 움직여라.
        while k:
            # 가로부터 이동하므로 a == r, 즉 망치와 두더지의 가로위치가 같을때까지 먼저 움직인다.
            if a != r:
                # 망치가 움직여야함.
                if a > r:
                    r += 1
                else:
                    r -= 1
            # 가로로 이동을 다 했다면?
            else:
                # 세로로 이동 시작
                if b > c:
                    c += 1
                elif b < c:
                    c -= 1
                # 세로로도 이동을 다한후 만약 두더지를 잡았으면 잡은 cnt 증가후 종료.
                if b == c:
                    cnt += 1
                    break
            # 시간 1초 감소.
            k -= 1

    print(f"#{tc} {cnt}")
