# 알고리즘 수업 - 점근적 표기1
# 솔직히 왜 시간복잡도 문제인지 잘 모르겠다..

a1, a0 = map(int,input().split())
c = int(input())
n = int(input())

if (a1*n) + a0 - (c*n) <= 0:
    print(1)
else:
    print(0)