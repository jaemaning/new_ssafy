numbers = [1, 2, 3, 4, 5]
n = len(numbers)
# selected[i] == 1 => 내가 i 번째 원소를 부분집합에 포함 o
# selected[i] == 0 => 내가 i 번째 원소를 부분집합에 포함 x
selected = [0] * n
# 합이 x보다 작은 부분집합만 구해야 한다면?
x = 6


# 재귀함수로 부분집합 구하기
# i 번째 우너소를 부분집합에 포함 할지 안할지 결정
def subset(i, subsum):
    # 0. 최적화 조건(백트래킹) 이 있는 경우
    if subsum >= x:
        return

    # 1. 종료 조건
    if i == n:
        # n개의 원소에 대해 선택을 끝냈다. (쓰던지 말던지)
        for j in range(n):
            if selected[j]:
                print(numbers[j], end=" ")
        print()
        return

    # 2. 재귀 호출
    # i 번째를 선택하고 다음 i+1 번째 원소를 선택하러 가거나
    selected[i] = 1
    subset(i + 1, subsum + numbers[i])
    # i 번째를 선택하지 않고 다음 i+1 번째 원소를 선택하러 가거나
    selected[i] = 0
    subset(i + 1, subsum)


subset(0, 0)
