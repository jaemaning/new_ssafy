prime = []
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)


T = int(input())
len_p = len(prime)

for tc in range(1, T+1):
    n = int(input())
    cnt = 0

    for i in range(len_p):
        for j in range(i, len_p):
            for k in range(j, len_p):
                if prime[i] + prime[j] + prime[k] == n:
                    cnt += 1

    print(f"#{tc} {cnt}")