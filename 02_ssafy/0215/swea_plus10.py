# 추가문제10 자기 방으로 돌아가기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    corridor = [0] * 201

    for _ in range(n):
        now, home = map(int, input().split())
        now += 1
        home += 1
        if now > home:
            for i in range(home//2, now//2+1):
                corridor[i] += 1
        else:
            for i in range(now//2, home//2 +1):
                corridor[i] += 1

    print(f"#{tc} {max(corridor)}")
