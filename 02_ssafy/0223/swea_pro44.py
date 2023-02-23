import sys
sys.stdin = open('input.txt','r')

def enque(n):
    global last

    last += 1
    tree[last] = n
    c = last
    p = c // 2

    while p and tree[c] < tree[p]:
        tree[c], tree[p] = tree[p], tree[c]
        c = p
        p = c //2


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    tree = [0] * 501
    n_list = list(map(int, input().split()))
    last = 0
    ans = 0

    for i in n_list:
        enque(i)

    while last:
        last //= 2
        ans += tree[last]

    print(f"#{tc} {ans}")
