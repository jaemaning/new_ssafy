size = 10+1 # 1칸 여유를 줘야함

cq = [0] * size
front = rear = 0

def isFull():
    return (rear + 1) % size == front

def isEmpty():
    return front == rear

def enqueue(item):
    global rear
    if isFull():
        print("꽉참")
        return
    rear = (rear+1) % size
    cq[rear] = item
    return


def dequeue():
    global front
    if isEmpty():
        return "empty"
    front = (front + 1) % size
    return cq[front]

print(cq)
print(isEmpty())

for _ in range(12):
    enqueue(_)

for _ in range(12):
    print(dequeue())