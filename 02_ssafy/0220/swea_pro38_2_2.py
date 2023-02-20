# 피자굽기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    ci = list(map(int, input().split())) + [21] * 210
    pizza = []
    cnt = 0
    for idx,i in enumerate(ci):
        pizza.append([i,idx])

    # print(pizza)
    front, rear = 0, n - 1
    qq = []

    while True:


        if pizza[front][0] == 21:
            front = (front+1) % n
            continue

        pizza[front][0] //= 2
        # print(pizza[front][0])

        if pizza[front][0] == 0:
            cnt += 1

            if cnt == m:
                print(f"#{tc} {pizza[front][1] + 1}")
                break

            rear += 1
            pizza[front], pizza[rear] = pizza[rear], pizza[front]

        front = (front + 1) % n



