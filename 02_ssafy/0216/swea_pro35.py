# 토너먼트 카드게임
import sys
sys.stdin = open('input.txt', 'r')


def winner(left, right):
    # 1: 가위 , 2: 바위, 3: 보
    # 1>3 , 3>2, 2>1
    if n_list[left] == 1:
        if n_list[right] == 2:
            return right

    elif n_list[left] == 2:
        if n_list[right] == 3:
            return right

    else:
        if n_list[right] == 1:
            return right

    return left



def game(x, y):


    # 1. 종료 조건
    if x == y:
        # 승자 리턴
        return x

    # 2. 재귀 호출
    mid = (x+y)//2
    left = game(x,mid)
    right = game(mid+1,y)

    return winner(left, right)


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))
    length = len(n_list)

    print(f"#{tc} {game(0, length - 1) + 1}")
