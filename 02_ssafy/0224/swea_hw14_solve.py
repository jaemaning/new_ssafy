# 교수님 풀이
def postorder(t):
    # t 노드가 숫자인 경우
    if node[t].isdigit():
        return int(node[t])
    # t 노드가 연산자인 경우
    else:
        l = postorder(cleft[t])
        r = postorder(cright[t])

        if node[t] == "+":
            node[t] = str(l + r)
        if node[t] == "-":
            node[t] = str(l - r)
        if node[t] == "*":
            node[t] = str(l * r)
        if node[t] == "/":
            node[t] = str(l // r)

        return int(node[t])


T = 10

for tc in range(1, T + 1):
    n = int(input())

    # 자식 정보
    cleft = [0] * (n + 1)
    cright = [0] * (n + 1)

    # 인덱스에 저장된 값 또는 연산자
    node = [0] * (n + 1)

    for i in range(n):
        info = input().split()

        idx = int(info[0])

        if info[1].isdigit():
            node[idx] = info[1]
        else:
            node[idx] = info[1]
            cleft[idx] = int(info[2])
            cright[idx] = int(info[3])

    print(postorder(1))