import sys
input = sys.stdin.readline

n, m = map(int, input().split())
my_dict = {}

for _ in range(n):
    key, value = input().strip().split()
    my_dict[key] = value

for _ in range(m):
    site = input().strip()
    print(my_dict[site])