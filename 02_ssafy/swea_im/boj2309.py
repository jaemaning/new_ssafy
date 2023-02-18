# boj 2309 - 일곱 난쟁이 ( IM 대비 문제 )

def comb(arr):

    start = arr.index(new_arr[-1]) if new_arr else 0

    if len(new_arr) == 7:
        if sum(new_arr) == 100:
            result.append(new_arr[:])
        return

    else:
        for i in range(start, 9):
            if visited[i] == False:
                visited[i] = True
                new_arr.append(arr[i])
                comb(arr)
                new_arr.pop()
                visited[i] = False

    return


n_list = []
new_arr = []
result = []
visited = [False] * 9

for _ in range(9):
    n = int(input())
    n_list.append(n)

comb(n_list)
result[0].sort()
for i in result[0]:
    print(i)
