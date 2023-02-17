# boj 5430 AC

from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    prompts_ = input().strip()
    n = int(input())
    a = input().strip()[1:-1].split(",")
    r_cnt = 0
    d_right_cnt = 0
    d_left_cnt = 0
    que = deque(list(map(int, [-1] if a == [''] else a)))

    for prompt_ in prompts_:
        if prompt_ == "R":
            r_cnt += 1
            d_right_cnt, d_left_cnt = d_left_cnt, d_right_cnt
        else:
            if len(que) > d_right_cnt + d_left_cnt:
                if r_cnt % 2 == 0:
                    if que[d_left_cnt] != -1:
                        que[d_left_cnt] = -1
                        d_left_cnt += 1
                    else:
                        print("error")
                        break
                else:
                    if que[d_right_cnt] != -1:
                        d_right_cnt += 1
                        que[(-1)*d_right_cnt] = -1
                    else:
                        print("error")
                        break

            else:
                print("error")
                break

    else:
        if r_cnt % 2 == 1:
            que.reverse()

        str_ = ""
        print("[", end="")
        for i in range(len(que)):
            if que[i] != -1:
                str_ += str(que[i])
        print(",".join(str_), end="")
        print("]")

        # print(",".join(map(str, que)), end="")
