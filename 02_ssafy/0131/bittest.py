arr = [3, -1, -2, -4, 5, 4]
arr.sort()
n = len(arr)
# result = []
#
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1 << j):
#             print(arr[j], end=", ")
#     print()
# print()

"""
부분집합에 포함이 되면 1로 표시 / 포함되지 않으면 0으로 체크 => 비트연산
부분 집합의 개수 => 2^n
 2^0 2^1 2^2 2^3 2^4 2^5
[ 3,  6,  7,  1,  5,  4]
[ 1,  0,  0,  1,  1,  0] => 0b011001 => 1 + 8 + 16 = 25 => 25번째 부분집합
총 부분집합의 개수 = 2^6 = 64개
[ 0,  0,  0,  0,  0,  0] => 0b000000 => 0 => 0번째 부분집합
[ 1,  0,  0,  0,  0,  0] => ob000001 => 1 => 1번째 부분집합
"""
ans = []
for i in range(1 << n):  # i번째 부분집합에 대해
    result = []
    for j in range(n):  # i번째 부분집합이 n개의 원소 중에 j 번째 원소를 포함하는지 검사
        if i & (1 << j):  # i를 이진수로 바꿨을때 j번째 원소가 1인경우 그 j번째 원소를 포함하는 부분집합
            result.append(arr[j])

    new_result = result[:]
    ans.append(new_result)
    if sum(new_result) == 0:
        print(f"합이 0 : {new_result}")

print(len(ans))
print(ans)