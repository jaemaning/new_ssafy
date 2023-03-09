# 일타 싸피 연습

import math
# board : 가로 100 세로 30

start = (0, 0)
end = (2, 2)

# 거리
dist = math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

print(dist)

# 각도
theta = math.asin