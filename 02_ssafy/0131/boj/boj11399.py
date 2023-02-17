# boj 11399 ATM

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
sum_v = 0

for i in range(n):
    sum_v += sum(n_list[:i+1])

print(sum_v)