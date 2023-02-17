# 최대 공약수 GCD : Greatest Common Division

# 최소 공배수 LCM : Least Common Multiple

a, b = 20, 15


def gcd(a, b):
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def lcm(a, b):
    return a * b // gcd(a, b)


# 유클리드 호제법
def new_gcd(a, b):
    if b == 0:
        return a

    else:
        return new_gcd(b, a % b)


print(new_gcd(a, b))
print(lcm(a, b))
