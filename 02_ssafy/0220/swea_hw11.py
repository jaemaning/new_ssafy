# 암호 생성기
import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    _ = int(input())

    pws = list(map(int, input().split()))

    front = 0

    while 1:

        for i in range(1,6):
            pws[front] -= i

            if pws[front] <= 0:
                pws[front] = 0
                break

            front = (front + 1) % 8
        else:
            continue
        break

    print(f"#{tc} {' '.join(map(str,pws[front + 1:] + pws[:front + 1]))}")