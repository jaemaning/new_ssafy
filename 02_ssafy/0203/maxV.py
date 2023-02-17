"""
3
5
55 7 78 12 42
6
55 7 78 12 42 1
7
55 7 78 12 42 2 1
"""

arr_ = [1, 99, 8, 20, 9, 11, 54, 74]

max_value = arr_[0]  # max_Value 값에 리스트의 첫번째 값을 넣어줌

# 리스트의 1번째 인덱스부터 for 돌며 값 비교
for arr_value in arr_[1:]:
    # 값 비교후 큰 값에 max_value 저장
    if arr_value > max_value:
        max_value = arr_value

print(max_value)