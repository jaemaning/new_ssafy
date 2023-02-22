# 이진탐색

def inorder(t):
    global cnt
    # t 노드가 존재 한다면
    if t <= n:
        # print(t, n)
        # 왼쪽 방문
        inorder(t*2)
        # 데이터처리
        n_list[t] = cnt
        cnt += 1
        # 오른쪽 방문
        inorder(t*2+1)


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    n_list = [0] * (n+1)

    cnt = 1
    inorder(1)
    print(f"#{tc} {n_list[1]} {n_list[n // 2]}")
