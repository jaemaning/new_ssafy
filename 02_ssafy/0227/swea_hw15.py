# 단순 2진 암호코드
import sys
sys.stdin = open('input.txt', 'r')

my_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011':7, '0110111': 8, '0001011': 9}

def scanner(i, j):
    '''
    :param i: 시작 x 위치
    :param j: 끝나는 y 위치
    :return: 결과값값    '''
    check_sum = 0
    ans = 0
    for k in range(8):
        # 홀수 k : 0부터 시작하므로
        if k % 2 == 0:
            check_sum += (my_dict[pw[i][j-55+(k*7):j-55+7+(k*7)]])*3
            ans += my_dict[pw[i][j-55+(k*7):j-55+7+(k*7)]]
        else:
            check_sum += my_dict[pw[i][j-55+(k*7):j-55+7+(k*7)]]
            ans += my_dict[pw[i][j-55+(k*7):j-55+7+(k*7)]]

    if check_sum % 10 == 0:
        return ans
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    n, m = map(int,input().split())
    pw = [input() for _ in range(n)]

    # 시작이 무조건 0 끝이 무조건 1로 해독됨.
    for i in range(n):
        for j in range(m-1,-1,-1):
            if pw[i][j] == '1':
                result = scanner(i,j)
                break
        else:
            continue
        break

    print(f"#{tc} {result}")
