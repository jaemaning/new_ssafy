# subtree
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    node_list = list(map(int, input().split()))
    cnt = 1

    # 2. 인덱스 번호가 => 자식노드의 번호
    parent = [0] * (E + 2)
    for i in range(E):
        p = node_list[i * 2]
        c = node_list[i * 2 + 1]

        parent[c] = p

    for i in range(E+2):
        while parent[i] != 0:
            if parent[i] == N:
                cnt += 1
            i = parent[i]

    print(f"#{tc} {cnt}")
