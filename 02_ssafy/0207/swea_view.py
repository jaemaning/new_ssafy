

for tc in range(1,11):
    n = int(input())
    n_list = list(map(int, input().split()))
    result = 0

    for i in range(2, n - 2):

        near_list = []
        max_height = -1
        for j in range(1, 3):
            # max 금지
            if n_list[i-j] > max_height:
                max_height = n_list[i-j]
            if n_list[i+j] > max_height:
                max_height = n_list[i+j]

        if max_height < n_list[i]:
            result += n_list[i] - max_height

    print(f"#{tc} {result}")

