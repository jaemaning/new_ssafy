# 스위치 켜고 끄기

n = int(input())

switches = list(map(int,input().split()))

m = int(input())

for _ in range(m):
    s, num = map(int, input().split())
    new_num = num

    # 남학생 이면?
    if s == 1:
        switches[num-1] = 0 if switches[num-1] else 1
        while new_num + num < n:
            new_num += num
            switches[new_num-1] = 0 if switches[new_num-1] else 1
    # 여학생 이면 ?
    else:
        nnum = num - 1
        bnum = num + 1
        switches[num-1] = 0 if switches[num-1] else 1
        while 0 < nnum <= n and 0 < bnum <= n and switches[nnum-1] == switches[bnum-1]:
            switches[nnum-1] = 0 if switches[nnum-1] else 1
            switches[bnum-1] = 0 if switches[bnum-1] else 1
            nnum -= 1
            bnum += 1

cnt = 0
for i in switches:
    print(i, end=" ")
    cnt += 1
    if cnt % 20 == 0:
        print()

