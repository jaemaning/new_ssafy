def f(i,k,s,t):
    '''
    :param i: 원소
    :param k: 집합의 크기
    :param s: 부분집합의 합
    :param t: 목표 값
    :return:
    '''
    global cnt
    global fcnt
    fcnt += 1
    # if s > t:
    #     return
    # elif s == t:
    #     cnt += 1
    #     return
    # elif i == k:
    #     return

    if i == k:
        if s == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end=" ")
            print()
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t) if s+A[i] <= t else 0 # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t) if s <= t else 0 # A[i] 미포함



A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
bit = [0] * N
cnt = 0
fcnt = 0
f(0, N, 0, 1)
print(cnt)   # 합이 key 인 부분집합의 합 수
print(fcnt)  #