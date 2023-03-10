def dfs(path, n):
    global answer

    if len(path) == n:

        nx = company[0]
        ny = company[1]

        result = 0

        for i in path:
            result += abs(i[0] - nx) + abs(i[1] - ny)
            nx, ny = i[0], i[1]

        result += abs(nx - home[0]) + abs(ny - home[1])

        answer = min(result, answer)

        return

    else:
        for i in range(n):
            if not checklist[i]:
                checklist[i] = True
                path.append(user[i])
                dfs(path, n)

                path.pop()
                checklist[i] = False


tc = int(input())

for test_case in range(tc):
    n = int(input())
    nlist = list(map(int, input().split()))
    checklist = [False] * n

    company = [nlist[0], nlist[1]]
    home = [nlist[2], nlist[3]]
    user = []

    for i in range(4, len(nlist), 2):
        user.append([nlist[i], nlist[i + 1]])
    answer = 9999999999999

    dfs([], n)
    print(f"#{test_case + 1} {answer}")