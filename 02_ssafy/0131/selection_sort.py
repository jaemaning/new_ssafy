n_list = [64, 25, 10, 22, 11]
n = len(n_list)

for idx in range(n-1):
    max_idx = idx
    for i in range(idx, n):
        if n_list[max_idx] > n_list[i]:
            max_idx = i
    n_list[idx], n_list[max_idx] = n_list[max_idx], n_list[idx]

print(n_list)
