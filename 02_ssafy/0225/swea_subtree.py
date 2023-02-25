# 8일차 서브트리 연습문제 다시 풀어보기

T = int(input())

for tc in range(1,T+1):
    e, n = map(int,input().split())
    e_list = list(map(int,input().split()))
    tree = [[] for _ in range(e+2)]

    # 부모 노드번호를 인덱스로 자식 번호 값들을 저장
    for i in range(e):
        tree[e_list[i*2]].append(e_list[i*2+1])

    cnt = 1
    stack = tree[n]
    
    while stack:
        cnt += 1
        node = stack.pop()
        for i in tree[node]:
            stack.append(i)

    print(f"#{tc} {cnt}")