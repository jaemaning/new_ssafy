T = int(input())


def func1(num):
    prime_list = []
    check_list = [True] * (num + 1)
    for i in range(2, int(num ** 0.5) + 1):
        if check_list[i]:
            for j in range(2, num // i):
                check_list[i * j] = False

    for idx, chk in enumerate(check_list):
        if chk:
            prime_list.append(idx)
    return prime_list


def perm(arr, start, prime_list, n):
    # n개 만큼 뽑으면 종료
    if len(new_arr) == 3:
        if sum(new_arr) == n:
            ans = new_arr[:]
            result.append(ans)
        return

    for i in range(start, len(arr)):
        new_arr.append(arr[i])
        perm(arr, i, prime_list, n)
        new_arr.pop()


p_list = func1(999)
for tc in range(1, T + 1):
    n = n2 = int(input())
    new_arr = []
    result = []

    for idx, i in enumerate(p_list):
        if i > n2:
            n2 = i
            break

    end = p_list.index(n2) + 1
    perm(p_list[2:end], 0, p_list, n)

    print(f"#{tc} {len(result)}")
