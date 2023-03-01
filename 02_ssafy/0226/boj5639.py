# 이진 검색 트리
import sys
sys.setrecursionlimit(10**9)

'''
50
30
24
5
28
45
98
52
60
'''

def postorder(idx):

    if tree[idx] == 0:
        return

    postorder(idx*2)
    postorder(idx*2+1)
    print(tree[idx])


pre = -1
cnt = 1
i = 1
tree = [0] * 99999
tree[0] = 9999999
while True:
    try:
        n = int(sys.stdin.readline())
        cnt += 1
        if pre == -1:
            tree[i] = n
        elif n < pre:
            i *= 2
            tree[i] = n
        elif n > pre:
            while i != 0:
                i //= 2
                if tree[i] > n:
                    break
            
            if i == 0:
                i = 3
            else:
                i = (i*2)*2 + 1
            # print(i)
            tree[i] = n
        
        pre = n

    except:
        break

if pre != -1:
    postorder(1)