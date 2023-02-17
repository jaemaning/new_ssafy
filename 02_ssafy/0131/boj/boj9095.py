import math
n = int(input())
cnt = 1 # 11111

# 2의 최대 개수 1과 2로 만들 수 있는 수
two_v = n // 2
two_p = n % 2

for i in range(two_v):
    cnt += math.factorial(two_v+two_p + i) // (math.factorial(two_p + i*2)*math.factorial((two_v+two_p + i) - (two_p + i*2)))

# 3의 최대 개수 1과 3으로 만들 수 있는 수
three_v = n // 3
three_p = n % 3
for i in range(three_v):
    cnt += math.factorial(three_v+three_p + i*2) // (math.factorial(three_p + i*3)*math.factorial((three_v+three_p + i*2) - (three_p + i*3)))

# 1, 2, 3 으로 만들 수 있는 수


# 2, 3으로 만들 수 있는 수


print(cnt)