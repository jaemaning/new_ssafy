# boj 16139
import sys

input = sys.stdin.readline

# 누적합 => target_alpha 가 정해져야 가능..? 26개 만들기?
name = input().strip()
name_arr = []
name_arr.extend(name)
name_arr = list(set(name_arr))
name_box = [[0] * len(name) for _ in range(26)]
tc = int(input())

# 누적합 만들기. (알파벳 소문자)
for i in range(len(name_arr)):
    for j in range(len(name)):
        # name_box 안에 n번째 박스안에 구간합 저장
        if name[j] == name_arr[i]:
            name_box[ord(name_arr[i]) - 97][j] += 1
        if j > 0:
            name_box[ord(name_arr[i]) - 97][j] += name_box[ord(name_arr[i]) - 97][j - 1]

for _ in range(tc):
    target_alpha, start, end = input().split()
    start, end = int(start), int(end)
    if start == 0:
        result = name_box[ord(target_alpha) - 97][end]
    elif start > 0:
        result = name_box[ord(target_alpha) - 97][end] - name_box[ord(target_alpha) - 97][start - 1]

    print(result)


