import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, 1+T):
    s = input().strip()
    slen = len(s)
    line_15 = "..#" + "...#" * (slen-1) + ".."
    line_24 = ".#" * (slen*2) + "."
    middle_line = "#"
    for cr in s:
        middle_line += "."+cr+".#"

    print(line_15)
    print(line_24)
    print(middle_line)
    print(line_24)
    print(line_15)