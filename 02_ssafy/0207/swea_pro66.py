# swea 전기버스
import sys
sys.stdin = open("sample_input.txt", "r")


def move(k, n):
    location = 0
    cnt = 0
    last_gas = 0

    while True:
        location += k
        if location >= n:
            return cnt

        else:
            while True:
                if (location in gas_stations) and (location != last_gas):
                    last_gas = location
                    cnt += 1
                    break
                elif location == last_gas:
                    return 0
                else:
                    location -= 1


T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    gas_stations = list(map(int, input().split()))

    print(f"#{tc} {move(K, N)}")
