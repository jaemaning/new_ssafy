T = int(input())


def func1(num):
    prime_list = []
    check_list = [True] * (num + 1)
    for i in range(2, int(num ** 0.5) + 1):
        if check_list[i]:
            for j in range(2, (num // i) + 1):
                check_list[i * j] = False

    for idx, chk in enumerate(check_list):
        if chk:
            prime_list.append(idx)
    return prime_list


p_list = func1(int(10 **6) + 100)
p_list = p_list[2:]

for tc in range(1, T + 1):
    d, a, b = map(int, input().split())
    str_d = str(d)
    cnt = 0

    for idx, i in enumerate(p_list):
        if i == b:
            end = idx + 1
        if i > b:
            end = idx
            break

    for idx, i in enumerate(p_list):
        if i >= a:
            start = idx
            break

    for i in range(start, end):
        if str_d in str(p_list[i]):
            cnt += 1

    print(f"#{tc} {cnt}")
