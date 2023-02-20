# 선형큐
front = -1
rear = -1

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    cheeze = list(map(int, input().split()))

    # 다음에 꺼내올 피자의 번호
    next_i = 0

    # 오븐
    oven = [0] * 1000
    ofront = orear = -1

    # 오븐에 차례대로 피자를 넣기
    for i in range(n):
        orear += 1
        oven[orear] = [cheeze[next_i], next_i]
        next_i += 1
        # 피자를 넣기(나중에 꺼낼때를 위해서 피자 번호도 같이 넣기)

    # 오븐에 남아있는 피자 개수
    remain = n
    # 마지막에 꺼낸 피자의 번호
    last_index = -1

    # 모든 피자의 치즈가 녹을때까지 반복
    while True:
        front += 1
        # 피자를 꺼내서
        pizza = oven[front][0]
        # 치즈를 녹이고 c // 2
        pizza //= 2
        # 치즈가 0이 되었다.
        if pizza == 0:
            # 피자를 오븐에서 뺸다.

        # 현재 오븐의 자리에 남은 피자 하나꺼내서 넣기
        # 넣을 피자가 없다.
        # 오븐에 남은 피자도 없는 상황이 온다.
        # 현재 피자의 번호가 답이된다.
        # 반복 종료
        # 치즈가 0이 안되었다 -> 다시 오븐에 넣기
        pass