# 오등큰수

n = int(input())

n_map = list(map(int, input().split()))

max_v = max(n_map)

my_lst = [0] * (max_v + 1)

stack = []
result = [-1] * n

for i in n_map:
    my_lst[i] += 1

for i in range(len(n_map) - 1):
    if my_lst[n_map[i]] < my_lst[n_map[i + 1]]:
        result[i] = n_map[i + 1]
        while stack:
            val, idx = stack.pop()
            if my_lst[n_map[i + 1]] > val:
                result[idx] = n_map[i + 1]
            else:
                stack.append((val, idx))
                break
    else:
        stack.append((my_lst[n_map[i]], i))

print(' '.join(map(str, result)))
