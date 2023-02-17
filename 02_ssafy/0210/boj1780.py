# 종이의 개수

n = int(input())
box = [list(map(int, input().split()) for _ in range(n))]
start = box[0][0]

for i in range(n):
    for j in range(n):
        if box[i][j] != start:
            break
    else:
        continue
    break
else:
    cnt = 0
    

# n 은 기존 n // 3 이 들어감.
def check_box(box, n):
