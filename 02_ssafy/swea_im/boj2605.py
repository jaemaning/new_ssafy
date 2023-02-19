# boj 2605 - 줄 세우기

n = int(input())
result = []
n_list = list(map(int, input().split()))

for idx, i in enumerate(n_list, start=1):
    result.insert(i,idx)

print(" ".join(map(str,result[::-1])))