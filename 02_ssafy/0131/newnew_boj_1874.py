import sys
input = sys.stdin.readline

n = int(input())
prt_list = []
result_list = []
cnt = 1

for _ in range(n):

    target_number = int(input())

    while cnt <= target_number:
        prt_list.append("+")
        result_list.append(cnt)
        cnt += 1

    if result_list[-1] == target_number:
        prt_list.append("-")
        result_list.pop()

    else:
        print("NO")
        break
else:
    for star in prt_list:
        print(star)