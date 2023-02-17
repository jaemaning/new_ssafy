# input
T = int(input())
result = [0 for _ in range(T)]
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargeStation = list(map(int, input().split()))

    chargeStation.append(N)  # 연산을 쉽게 하기 위해 종점 정보를 충전 역 리스트에 추가

    # process
    k = K  # 충전량
    location = 0  # 현재 위치
    for location in range(1, N):
        k = k - 1
        if location in chargeStation:
            idx = chargeStation.index(location)
            if idx != M and k < chargeStation[idx + 1] - chargeStation[idx]:  # 충전량보다 충전기 거리가 먼 경우
                if K < chargeStation[idx + 1] - chargeStation[idx]:
                    result[test_case - 1] = 0
                    break
                else:
                    k = K
                    result[test_case - 1] = result[test_case - 1] + 1

    # output
    print(f"#{test_case} {result[test_case - 1]}")