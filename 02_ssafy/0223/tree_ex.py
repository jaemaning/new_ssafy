'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 11 13
'''



def preorder(i):
    print(i, end=" ")

    if child[i]:
        preorder(child[i][0])

    if len(child[i]) == 2:
        # print("오른쪽", end=" ")
        preorder(child[i][1])

    return


V = int(input())
tree = list(map(int, input().split()))
E = V-1
child = [[] for _ in range(V+1)]

for i in range(E//2):
    p, c = tree[i*2], tree[i*2+1]
    child[p].append(c)

print(child)
preorder(1)
