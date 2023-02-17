# boj 1003 피보나치 함수
import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())

    fibo_arr = [[1, 0], [0, 1]]


    def fibo(n):
        if len(fibo_arr) >= n+1:
            return fibo_arr[n]

        else:
            for i in range(2, n+1):
                fibo_arr.append([fibo(i-1)[0] + fibo(i-2)[0], fibo(i-1)[1] + fibo(i-2)[1]])
            return fibo(n)


    print(" ".join(map(str,fibo(n))))
