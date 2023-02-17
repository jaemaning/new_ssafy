# boj 9184 신나는 함수 실행
'''
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
'''

def w(a,b,c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif cache[a][b][c] != 0:
        return cache[a][b][c]

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    elif a < b and b < c:
        cache[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return cache[a][b][c]
    
    else: 
        cache[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return cache[a][b][c]

cache = [[[0] * 51 for _ in range(51)] for _ in range(51)]

while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")