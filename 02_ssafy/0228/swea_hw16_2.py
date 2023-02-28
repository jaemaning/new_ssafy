# 암호코드 스캔
import math
import sys

sys.stdin = open('input.txt', 'r')

my_dict = {"1123": 0,
           "1222": 1,
           "2212": 2,
           "1141": 3,
           "2311": 4,
           "1321": 5,
           "4111": 6,
           "2131": 7,
           "3121": 8,
           "2113": 9}



T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    spw = set()
    pw = ""

    for _ in range(n):
        a = input().strip()[:m]
        a = a.strip('0')
        cnt = 0
        e_cnt = 0

        for s in a:
            pw += s
            if s == "0":
                cnt += 1
            else:
                e_cnt += 1

            if cnt > e_cnt:
                ck_pw = pw.strip('0')
                if ck_pw:
                    spw.add(ck_pw)
                    cnt = 0
                    e_cnt = 0
        if pw:
            spw.add(pw)
            pw = ""
    print(tc)
    print(spw)
# b = math.gcd(*a)
#
# print(b)