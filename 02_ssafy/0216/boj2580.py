def solve_sudoku(sudoku, xx):
    global flag

    if flag:
        return

    if len(start) == xx:
        flag = 1
        return

    x, y = start[xx]
    possible_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        # 가로
        # 사용가능 리스트를 하나씩 지워나가라
        if possible_list.count(sudoku[x][i]):
            possible_list.pop(possible_list.index(sudoku[x][i]))
        # 세로
        if possible_list.count(sudoku[i][y]):
            possible_list.pop(possible_list.index(sudoku[i][y]))

    # 3 x 3
    for i in nemo_dict.get((x, y)):
        if possible_list.count(i):
            possible_list.pop(possible_list.index(i))

    # 추려진 possible_list 를 가지고 돌려보자
    for pre_num in possible_list:
        for _ in range(9):
            print(sudoku[_])
        print()
        sudoku[x][y] = pre_num
        solve_sudoku(sudoku, xx+1)
        sudoku[x][y] = 0



sudoku = [list(map(int, input().split())) for _ in range(9)]
# visited = [[False] * 9 for _ in range(9)]
# 시작 위치
start = []
nemo_dict = {}
flag = 0

# 3 x 3 박스를 딕셔너리에 미리 저장 해두자.
for i in (0, 3, 6):
    for j in (0, 3, 6):
        tmp = []
        for k in range(3):
            tmp += sudoku[i + k][j:j + 3]

        for p in range(3):
            for q in range(3):
                nemo_dict[(i + p, j + q)] = tmp

for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            start.append((i, j))


solve_sudoku(sudoku, 0)
for i in range(9):
    print(" ".join(map(str,sudoku[i])))
