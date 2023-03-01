# boj 1991 트리 순회

def preorder(x):

    if x == ".":
        return
    
    print(x, end="")
    preorder(cleft[tree.index(x)])
    preorder(cright[tree.index(x)])


def inorder(x):

    if x == ".":
        return
    
    inorder(cleft[tree.index(x)])
    print(x, end="")
    inorder(cright[tree.index(x)])


def postorder(x):

    if x == ".":
        return
    
    postorder(cleft[tree.index(x)])
    postorder(cright[tree.index(x)])
    print(x, end="")


n = int(input())
tree = [0] * (n+1)
cleft = [0] * (n+1)
cright = [0] * (n+1)

for i in range(1,n+1):
    p, c1, c2 = input().split()

    tree[i] = p
    cleft[i] = c1
    cright[i] = c2

preorder("A")
print()
inorder("A")
print()
postorder("A")
print()


