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

result = []

for i in range(num//2, num+1):
    cnt = 0
    tmp = [num, i]
    while 1:
        tmp.append(tmp[-2] - tmp[-1])
        if tmp[-1] < 0:
            tmp.pop()
            break
    
    if len(tmp) > len(result):
        result = tmp[:]

print(len(result))
print(f"{' '.join(map(str,result))}")
