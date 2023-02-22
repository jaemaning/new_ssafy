import sys
sys.stdin = open('input.txt', 'r')

# 중위순회    l v r
def inorder(T):
    # 조건
    if T <= n:
        # left
        inorder(T*2)
        # visit
        print(n_list[T], end="")
        # right
        inorder(T*2+1)


for tc in range(1,11):

    n = int(input())
    n_list = [0]

    for _ in range(n):
        num, a, *c = input().split()
        n_list.append(a)
        # print(c)

    print(f"#{tc}", end=" ")
    inorder(1)
    print()

