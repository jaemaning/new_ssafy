# 암호코드 스캔
import sys
import math

sys.stdin = open('input.txt', 'r')

my_dict = {"112": 0,
           "122": 1,
           "221": 2,
           "114": 3,
           "231": 4,
           "132": 5,
           "411": 6,
           "213": 7,
           "312": 8,
           "211": 9}


def pw_solve(n):
    ans = ""
    for s in n:
        binary4 = ""
        # 10진수로 전환 후 2진수 전환 진행
        s = int(s, 16)

        for i in range(3, -1, -1):
            binary4 += "1" if s & (1 << i) else "0"

        ans += binary4

    # 뒤부터 검사해서 1이 등장하면 시작
    ans = ans[::-1].strip("0")
    pre = "1"
    cnt = 0
    check_list = []
    result = []
    flag = 1
    rlt = 0
    for s in ans:

        if flag:
            if s == pre:
                cnt += 1

            else:
                check_list.append(cnt)
                cnt = 1

            if len(check_list) == 3:
                gcd_num = math.gcd(*check_list)
                new_check = ""
                for i in range(3):
                    new_check += str(check_list[i] // gcd_num)

                result.append(my_dict.get(new_check, 0))
                check_list = []
                flag = 0

            pre = s
        else:
            if s == "1":
                flag = 1
                pre = s
                cnt = 1


        if len(result) == 8:
            check_sum = 0
            for i in range(7):
                if i % 2 == 0:
                    check_sum += result[i] * 3
                else:
                    check_sum += result[i]

            check_sum += result[7]

            if check_sum % 10 == 0:
                rlt += sum(result)
            else:
                pass

            result = []

    return rlt




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

        # print(s)
        #     if s == "0":
        #         spw.add(pw)
        #         pw = ""
        #     else:
        #         pw += s
        # else:
        #     if pw:
        #         spw.add(pw)
        #     pw = ""



    print(spw)
    rlt = pw_solve(spw)
    rlt = rlt[::-1]
    print(rlt)
    check_sum = 0

    if len(rlt) == 8:
        for i in range(7):
            if i % 2 == 0:
                check_sum += rlt[i] * 3
            else:
                check_sum += rlt[i]

        check_sum += rlt[7]
    else:
        check_sum = -1

    if check_sum % 10 == 0:
        print(f"#{tc} {sum(rlt)}")
    else:
        print(f"#{tc} 0")
