def f(i, k, key):
    if i == k:
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]
        # print(s)
        if s == key:
            for j in range(k):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        bit[i] = 1
        f(i + 1, k, key)
        bit[i] = 0
        f(i + 1, k, key)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
bit = [0] * N
f(0, N, 10)
