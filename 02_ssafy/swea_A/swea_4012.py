# 요리사
import sys
sys.stdin = open('input.txt', 'r')

def comb(n):

    if len(dishes) == 4:
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
    n = int(input())
    dish_num = [i for i in range(0,n)]
    visited = [False] * (n+1)
    dishes = []
    dishes_comb = []

    dish_map = [list(map(int, input().split())) for _ in range(n)]

    comb(n)

    print(dishes_comb)

    min_v = 9999999
    for d in dishes_comb:
        # print(abs(dish_map[d[0]][d[2]] + dish_map[d[2]][d[0]] - dish_map[d[1]][d[3]] - dish_map[d[3]][d[1]]))
        if min_v > abs(dish_map[d[0]][d[1]] + dish_map[d[1]][d[0]] - dish_map[d[2]][d[3]] - dish_map[d[3]][d[2]]):
            min_v = abs(dish_map[d[0]][d[1]] + dish_map[d[1]][d[0]] - dish_map[d[2]][d[3]] - dish_map[d[3]][d[2]])
        if min_v > abs(dish_map[d[0]][d[2]] + dish_map[d[2]][d[0]] - dish_map[d[1]][d[3]] - dish_map[d[3]][d[1]]):
            min_v = abs(dish_map[d[0]][d[2]] + dish_map[d[2]][d[0]] - dish_map[d[1]][d[3]] - dish_map[d[3]][d[1]])
        if min_v > abs(dish_map[d[0]][d[3]] + dish_map[d[3]][d[0]] - dish_map[d[1]][d[2]] - dish_map[d[2]][d[1]]):
            min_v = abs(dish_map[d[0]][d[3]] + dish_map[d[3]][d[0]] - dish_map[d[1]][d[2]] - dish_map[d[2]][d[1]])

    print(min_v)
