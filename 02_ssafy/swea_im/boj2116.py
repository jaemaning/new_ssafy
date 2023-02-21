# boj 2116 주사위 쌓기
from collections import deque


def set_dice(dice, num, bottom):
    global ans

    middle = []
    d = [i for i in range(6)]

    if bottom == 0:
        ceil = dice[num][5]
        d.pop(d.index(bottom))
        d.pop(d.index(5))
        for i in d:
            middle.append(dice[num][i])

    elif bottom == 1:
        ceil = dice[num][3]
        d.pop(d.index(bottom))
        d.pop(d.index(3))
        for i in d:
            middle.append(dice[num][i])

    elif bottom == 2:
        ceil = dice[num][4]
        d.pop(d.index(bottom))
        d.pop(d.index(4))
        for i in d:
            middle.append(dice[num][i])

    elif bottom == 3:
        ceil = dice[num][1]
        d.pop(d.index(bottom))
        d.pop(d.index(1))
        for i in d:
            middle.append(dice[num][i])

    elif bottom == 4:
        ceil = dice[num][2]
        d.pop(d.index(bottom))
        d.pop(d.index(2))
        for i in d:
            middle.append(dice[num][i])

    elif bottom == 5:
        ceil = dice[num][0]
        d.pop(d.index(bottom))
        d.pop(d.index(0))
        for i in d:
            middle.append(dice[num][i])

    ans += max(middle)

    if num + 1 < n :
        set_dice(dice, num + 1, dice[num+1].index(ceil))
    else:
        return


def set_dice2(s_num, s_bot):
    global ans

    q = deque()
    q.append((s_num, s_bot))

    while q:
        num, bottom = q.popleft()

        middle = []
        d = [i for i in range(6)]

        if bottom == 0:
            ceil = dice[num][5]
            d.pop(d.index(bottom))
            d.pop(d.index(5))
            for i in d:
                middle.append(dice[num][i])

        elif bottom == 1:
            ceil = dice[num][3]
            d.pop(d.index(bottom))
            d.pop(d.index(3))
            for i in d:
                middle.append(dice[num][i])

        elif bottom == 2:
            ceil = dice[num][4]
            d.pop(d.index(bottom))
            d.pop(d.index(4))
            for i in d:
                middle.append(dice[num][i])

        elif bottom == 3:
            ceil = dice[num][1]
            d.pop(d.index(bottom))
            d.pop(d.index(1))
            for i in d:
                middle.append(dice[num][i])

        elif bottom == 4:
            ceil = dice[num][2]
            d.pop(d.index(bottom))
            d.pop(d.index(2))
            for i in d:
                middle.append(dice[num][i])

        elif bottom == 5:
            ceil = dice[num][0]
            d.pop(d.index(bottom))
            d.pop(d.index(0))
            for i in d:
                middle.append(dice[num][i])

        ans += max(middle)

        if num + 1 < n:
            q.append((num + 1, dice[num+1].index(ceil)))
        else:
            return

    return


n = int(input())

dice = [list(map(int, input().split())) for _ in range(n)]

max_ans = -1
for i in range(6):
    ans = 0
    set_dice2(0, i)
    if ans > max_ans:
        max_ans = ans
        new = i

print(max_ans)
