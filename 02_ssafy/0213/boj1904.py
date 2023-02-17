# boj 1904   - 01타일

n = int(input())

cache = [0] * 1000001
cache[1] = 1
cache[2] = 2

if n >= 3:
    for i in range(3, n+1):
        cache[i] = (cache[i-1] + cache[i-2]) %15746

print(cache[n])