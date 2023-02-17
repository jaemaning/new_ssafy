T = int(input())

for tc in range(1, T + 1):
    money = int(input())
    c = [0] * 8

    money_box = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(len(money_box)):
        if money >= money_box[i]:
            c[i] = money // money_box[i]
            money %= money_box[i]


    print(f"#{tc}", f"{' '.join(map(str,c))}", sep="\n")

