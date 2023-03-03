'''
2
0 1
1 0
'''
n = int(input())
n_list = [[0] * 2 * n]

for _ in range(n):
    input_list = [0] * (n//2)
    m_list = list(map(int,input().split()))
    output_list = [0] * (n//2)

    middle = input_list + m_list + output_list
    n_list.append(middle)

padding = [0] * 2 * n
n_list.append(padding)

print(n_list)