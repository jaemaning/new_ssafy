T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    max_cnt = -1

    for chr in str1:
        chr_cnt = str2.count(chr)
        if max_cnt < chr_cnt:
            max_cnt = chr_cnt

    print(f"#{tc} {max_cnt}")
