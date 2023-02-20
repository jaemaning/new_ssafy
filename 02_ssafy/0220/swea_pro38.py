# 회전

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    front, rear = 0, n - 1

    for _ in range(m):
        front = (front + 1) % n
        rear = (rear + 1) % n
        if (rear + 1) % n == front:
            pass
            # 항상 꽉찬 상태로 돌아가기만 함
        elif rear == front:
            print("비어있음")

    print(f"#{tc} {n_list[front]}")
