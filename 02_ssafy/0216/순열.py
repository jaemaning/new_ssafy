def ff(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i + 1, k)
            p[i], p[j] = p[j], p[i]


# 왜이렇게 어렵게 풀지 ? 이걸
# 제가 푸는 방법은 좀더 직관적이에요 이건 이해가 안되잖아요
# 메모리

def f(i, k):
    start = p.index(q[-1]) if q else 0

    if len(q) == k:
        print(q)
        return

    else:
        for i in range(start, len(p)):
            if visited[i] == False:
                # visited[i] = True
                q.append(p[i])
                f(i,k)
                q.pop()
                # visited[i] = False



p = [1, 2, 3]
q = []
visited = [False] * len(p)
k = 3
f(0,2)
# 이게 더 쉬워요
