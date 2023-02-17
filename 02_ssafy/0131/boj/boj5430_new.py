from collections import deque
import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):

    prompts_ = input().strip()
    n = int(input().strip())
    a = input().strip()[1:-1].split(",")
    r_cnt = 0
    d_right_cnt = 0
    d_left_cnt = 0
    que = deque(list(map(int, [-1] if a == [''] else a)))

    for prompt_ in prompts_:
        if prompt_ == "R":
            r_cnt += 1

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
                    if que[-d_right_cnt-1] != -1:
                        d_right_cnt += 1
                        que[-d_right_cnt] = -1
                    else:
                        print("error")
                        break

            else:
                print("error")
                break

    else:
        que = list(filter(lambda x: x != -1, que))
        if r_cnt % 2 == 1:
            que.reverse()

        str_ = [str(x) for x in que]
        print("[", end="")
        print(",".join(str_), end="")
        print("]")