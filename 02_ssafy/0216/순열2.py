numbers = [1, 2, 3, 4, 5]
n = len(numbers)


# i번째 원소의 자리를 바꿔가며 순열 생성
# 자리를 바꿀 수 있는 경우의 수
# 자리 바꾸기
def perm(i):
    # 1. 종료 조건
    if i == n:
        print(numbers)
        return

    # 2. 재귀 호출
    # 현재 위치 i에서 다른 위치 j에 있는 숫자와 한번식 다 바꿔보기
    # 이전에 i,j <=> j,i
    # 근데 위치를 바꾸지 않고 진행 할수도 있다.
    # i == j 이 경우는 위치를 바꾸지 않고 다음 원소의 자리를 바꾸러 이동하는것
    for j in range(i, n):
        # i 번째와 j 번째의 위치를 바꾸고 진행
        numbers[i], numbers[j] = numbers[j], numbers[i]
        # 다음 i+1 번째 원소의 자리를 바꾸러 간다.
        perm(i + 1)
        # i 번째와 j 번째 위치를 되돌려 놓고 다음 진행.
        numbers[i], numbers[j] = numbers[j], numbers[i]


perm(0)


# i번째 자리를 누구로 할것인가? 선택하는 방법
# i번째 자리가 누구인지 기억해야 하므로 배열 필요
def perm2(i, selected):
    global cnt2

    # 1. 종료 조건
    if i == n:
        cnt2 += 1
        print(selected)

    # 2. 재귀 호출
    # 현재 위치 i에 누구를 놓을것인가 선택
    for j in range(n):
        # j 번째 원소를 놓은적이 없다면 j 번째 원소를 i 위치에 놓기
        if numbers[j] not in selected:
            # i 위치는 j번째 원소가 선택되었다.
            selected[i] = numbers[j]
            # i위치의 주인을 정했으니 i+1 번째 위치의 주인을 정하러 갑니다.
            perm2(i+1, selected)
            selected[i] = 0

cnt2 = 0
perm2(0, [0] * n)
print(cnt2)