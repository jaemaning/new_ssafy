# 요리사
import sys
sys.stdin = open('input.txt', 'r')

# 조합
def comb(n):

    if len(dishes) == n//2:
        dishes_comb.append(dishes[:])
        return

    start = dish_num.index(dishes[-1]) if dishes else 0
    for i in range(start, n):
        if visited[i] == False:
            dishes.append(dish_num[i])
            visited[i] = True
            comb(n)
            visited[i] = False
            dishes.pop()


T = int(input())

for tc in range(1, T+1):
    # 초기값 설정
    n = int(input())
    dish_num = [i for i in range(0,n)]
    visited = [False] * (n+1)
    dishes = []
    dishes_comb = []
    t_dishes_comb = [i for i in range(n)]

    dish_map = [list(map(int, input().split())) for _ in range(n)]

    comb(n)

    # 최솟값 구하기
    min_v = 9999999
    for d in dishes_comb:
        c_d = list(set(t_dishes_comb) - set(d))
        ans = 0
        c_ans = 0

        # 어차피 0,0 같이, 같은 요리 재료 2개로 만든 값은 0이므로 모두 더해줘도 상관없음.
        for i in d:
            for j in d:
                ans += dish_map[i][j]

        for i in c_d:
            for j in c_d:
                c_ans += dish_map[i][j]

        # 두 값의 차가 현재 알고 있는 최저값보다 작다면 ? 최소값 갱신
        min_v = min(min_v, abs(c_ans-ans))

    print(f"#{tc} {min_v}")
