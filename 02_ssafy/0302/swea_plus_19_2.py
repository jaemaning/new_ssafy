# Magnetic
import sys
sys.stdin = open('input.txt', 'r')

'''
n극

1=n극 => 아래로
2=s극 => 위로

s극
'''

for tc in range(1,11):
    n = int(input())

    table = [list(map(int, input().split())) for _ in range(n)]
    t_table = list(zip(*table))
    cnt = 0

    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and 2 in t_table[j][i:]:
                cnt += 1
                for k in t_table[j][i+1:]:
                    if k == 1:
                        cnt -=1
                        break
                    elif k == 2:
                        break

    print(f'#{tc} {cnt}')
