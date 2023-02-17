# 스택 직접 구현하기
# 스택 초기화
stack = [0] * 10
size = 10
top = -1


def my_push(item):
    # push 를 하고 나면 top 변수가 변하기떄문
    global top

    if top == size - 1:
        print("가득참(오버플로우)")
        return
    else:
        top += 1
        stack[top] = item


def my_pop():
    global top
    if top == -1:
        print('언더플로우')
        return
    else:
        top -= 1
        return stack[top+1]


for i in range(10):
    my_push(i)

print(stack)

for i in range(10):
    print(my_pop(), end=" ")
print()