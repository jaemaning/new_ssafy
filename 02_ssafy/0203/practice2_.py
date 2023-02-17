def simple_strcmp(s1, s2):
    # s1 과 s2의 아스키 코드 값을 비교해서
    # 사전 순서 리턴
    return ord(s1) - ord(s2)

    i = 0

    while True:
        if s1[0] != s2[0]:
            if ord(s1) < ord(s2):
                return -1
            else:
                return 1
        else:
            i += 1


print(simple_strcmp("a", "b"))


def itoa(num):
    ret = ""
    # 숫자 하나씩 떼와서 (일의 자리부터) 문자열로 바꾸기
    while num > 0:
        i = num % 10
        ret += chr(ord('0') + i)    # ord('0') = 48
        num //= 10
    return ret[::-1]


s = itoa(123)
print(s)
print(type(s))
