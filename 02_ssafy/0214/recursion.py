# 재귀함수

def function1(num):
    print("now", num)

    #  1. 반드시 종료 조건을 정한다.
    if num == 0:
        return

    #  2. 종료 조건이 아닌 경우에 재귀 호출
    #  언젠가는 종료 조건을 만족하도록 변경 해줘야한다.
    else:
        function1(num - 1)

    print("back", num)


function1(5)


# 팩토리얼 함수
def fact(n):
    #  1. 종료조건
    if n == 1:
        return n
    #  2. 재귀 호출
    else:
        return n * fact(n - 1)


print(fact(5))


# 피보나치 수열 - 중복 호출이 많음
def fibo1(n):
    if n < 2:
        return n
    else:
        return fibo1(n - 1) + fibo1(n - 2)


# memoization - DP 의 핵심 기술
n = 20
cache = [0] * 50
cache[1] = 1


def fibo2(n):
    # n 번째 항을 계산한적이 없고, n이 2 이상이라면
    # n 번째 항을 계산해야한다.
    if n >= 2 and cache[n] == 0:
        cache[n] = fibo2(n - 1) + fibo2(n - 2)
    # 계산한적이 있으면 memo[n] 값을 그대로 사용

    return cache[n]


print(fibo2(40))
