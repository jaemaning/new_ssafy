# 파도반 수열

T = int(input())
cache = [0] * 101
cache[1] = 1
cache[2] = 1
cache[3] = 1

for _ in range(T):
    n = int(input())

    for i in range(4, n+1):
        cache[i] = cache[i-2] + cache[i-3]

    print(cache[n])
