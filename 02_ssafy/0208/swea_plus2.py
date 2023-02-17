import sys

sys.stdin = open('input.txt', 'r')


def rot_box(box1, box2):

    # 90도 회전은 1 행 => n 열로 간다.    2 행 => n-1 열
    # 이름을 box, box90 => box90 box180 => box180 box270으로 바꾸면서 작업
    for i in range(n - 1, -1, -1):
        for idx, j in enumerate(box1[i]):
            box2[idx].append(j)

    return


T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    box = []
    box90 = [[] for _ in range(n)]
    box180 = [[] for _ in range(n)]
    box270 = [[] for _ in range(n)]

    for _ in range(n):
        box.append(list(map(int, input().split())))

    rot_box(box, box90)
    rot_box(box90, box180)
    rot_box(box180, box270)

    print(f"#{tc}")
    for i in range(n):
        print(f"{''.join(map(str,box90[i]))} {''.join(map(str,box180[i]))} {''.join(map(str,box270[i]))}")


