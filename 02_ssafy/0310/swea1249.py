# 최적경로
import sys

sys.stdin = open('input.txt', 'r')


def dfs(route):
    global ans

    if len(c_route) == n:
        dist = 0
        # 회사에서 첫번째 고객
        dist += abs(company[0] - c_route[0][0]) + abs(company[1] - c_route[0][1])
        # 이후 고객들의 집 방문
        for c in range(n - 1):
            dist += abs(c_route[c][0] - c_route[c + 1][0]) + abs(c_route[c][1] - c_route[c + 1][1])
        # 이후 마지막 고객집 -> 집 귀가
        dist += abs(home[0] - c_route[n - 1][0]) + abs(home[1] - c_route[n - 1][1])

        ans = min(ans, dist)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            c_route.append(customers[i])
            dfs(route)
            visited[i] = 0
            c_route.pop()

    # 회사에서 출발하여 N명의 고객을 모두 방문하고
    # 집으로 돌아오는 경로 중 가장 짧은 것을 찾으려 한다.

    return ans


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    route = list(map(int, input().split()))
    visited = [0] * n

    company = (route[0], route[1])
    home = (route[2], route[3])
    customers = []
    for i in range(4, 2 * n + 4, 2):
        customers.append((route[i], route[i + 1]))

    ans = 99999999
    c_route = []

    ans = dfs(route)
    print(f'#{tc} {ans}')
