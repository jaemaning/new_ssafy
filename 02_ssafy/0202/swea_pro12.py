# 실습 12 새로운 버스노선

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    end_max_v = 0
    information = []
    for _ in range(n):

        bus_type, start, end = map(int, input().split())

        information.append([bus_type, start, end])
        if end_max_v < end:
            end_max_v = end

    result = [0] * (end_max_v + 1)

    for bus_type, start, end in information:
        # 일반버스
        if bus_type == 1:
            for i in range(start, end + 1):
                result[i] += 1
        # 급행버스
        if bus_type == 2:
            if start % 2 == 0:
                for i in range(start, end + 1, 2):
                    result[i] += 1
            else:
                for i in range(start, end + 1, 2):
                    result[i] += 1
        # 광역 급행 버스
        if bus_type == 3:
            if start % 2 == 0:
                if start % 4 == 0:
                    for i in range(start, end + 1, 4):
                        result[i] += 1
                else:
                    for i in range(start + 2, end + 1, 4):
                        result[i] += 1
            else:
                for i in range(start, end + 1):
                    if (i % 3 == 0) and (i % 10 != 0):
                        result[i] += 1

    print(f"#{tc} {max(result)}")