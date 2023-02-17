"""
bubble sort 복습
input 값 =>
5
55 7 78 12 42

0 1
1 2
2 3
3 4
비교
0 1
1 2
2 3
"""

n = int(input())
nlist = list(map(int, input().split()))

for i in range(n, 1, -1):
    for j in range(i - 1):
        # 만약 nlist 값 비교중 앞에 값이 더 크다면 위치 바꾸기
        if nlist[j] > nlist[j + 1]:
            tmp = nlist[j]
            nlist[j] = nlist[j + 1]
            nlist[j + 1] = tmp

print(nlist)
