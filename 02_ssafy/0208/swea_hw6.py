for tc in range(1, 11):
    n = int(input())
    box = [list(input().strip()) for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8 - n + 1):
            ans1 = ""
            ans2 = ""
            for k in range(n):
                ans1 += box[i][j + k]
                ans2 += box[j + k][i]

            if ans1 == ans1[::-1]:
                cnt += 1
            if ans2 == ans2[::-1]:
                cnt += 1

    print(f"#{tc} {cnt}")
