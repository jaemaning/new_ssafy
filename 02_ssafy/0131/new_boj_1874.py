# boj 1874 스택 수열
import sys
input = sys.stdin.readline

n = int(input())
out_list = [i for i in range(n, 0, -1)]
in_list = []
print_list = []

for _ in range(n):
    target_number = int(input())

    if not ((target_number in in_list) or (target_number in out_list)):
        print("NO")
        break

    if target_number in out_list:
        popnum = out_list.pop()
        in_list.append(popnum)
        print_list.append("+")

        while target_number != popnum:
            popnum = out_list.pop()
            in_list.append(popnum)
            print_list.append("+")

    if target_number in in_list:
        popnum = in_list.pop()
        print_list.append("-")

        while target_number != popnum:
            popnum = in_list.pop()
            print_list.append("-")

else:
    for _ in print_list:
        print(_)
