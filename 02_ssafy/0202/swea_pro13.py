# 6019 기차사이의 파리

T = int(input())

for tc in range(1, T+1):
    dis, train_a, train_b, fly = map(int, input().split())
    time = dis / (train_a + train_b)
    result = fly * time

    print(f"#{tc} {result}")
