# boj 1463  - 1로 만들기

n = int(input())

cache = [0] * 1000001
cache[2] = 1
cache[3] = 1

for i in range(4, n+1):
    cache[i] = cache[i-1] + 1

    if i % 2 == 0:
        cache[i] = min(cache[i], cache[i // 2] + 1)
    
    if i % 3 == 0:
        cache[i] = min(cache[i], cache[i // 3] + 1)

print(cache[n])