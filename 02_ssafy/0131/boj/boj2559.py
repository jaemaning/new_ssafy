import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp_list = list(map(int, input().split()))
max_v = pre_v = sum(temp_list[0:k])

for i in range(n-k):
    value = pre_v - temp_list[i] + temp_list[i+k]
    if value > max_v:
        max_v = value
    pre_v = value

print(max_v)
