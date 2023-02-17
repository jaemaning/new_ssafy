T = int(input())

for tc in range(1,T+1):
    n = int(input())
    bus_route = []
    result_list = [0] * (5001)
    for _ in range(n):
        start, end = map(int, input().split())
        for i in range(start, end+1):
            result_list[i] += 1

    p = int(input())
    ans = []
    for i in range(p):
        p_num = int(input())
        ans.append(result_list[p_num])

    print(f"#{tc} {' '.join(map(str, ans))}")