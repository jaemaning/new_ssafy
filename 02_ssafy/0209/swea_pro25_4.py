T = int(input())

for tc in range(1, 1+T):
    a, b = input().strip().split()
    target = list(b)
    length_b = len(b)
    stack = []
    cnt = 0
    for chr in a:
        stack.append(chr)
        if len(stack) >= len(b) and stack[-length_b:] == target:
            del stack[-length_b:]
            cnt += 1

    print(f"#{tc} {len(stack) + cnt}")
