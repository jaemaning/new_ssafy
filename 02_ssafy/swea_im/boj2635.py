# boj 2635 - 수 이어가기

# dp 아님
# num = int(input())
#
# mid = num // 2
#
# mid2 = (mid + num) // 2
#
# mid3 = (mid + mid2) // 2
#
# dp = [num, mid3]
#
# while dp[-1] >= 0:
#     dp.append(dp[-2] - dp[-1])
#
# print(len(dp) - 1)
# print(" ".join(map(str,dp[:-1])))

num = int(input())

