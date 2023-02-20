def dequeue():
    global front

    if front < rear:
        front += 1
        return queue[front]
    else:
        return "index error"

def enqueue(data):
    global rear

    if rear < len(queue)-1:
        rear += 1
        queue[rear] = data
    else:
        print("size exceeded")
    return

front = rear = -1
queue = [0] * 10

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(10)
enqueue(20)
enqueue(30)
enqueue(10)
enqueue(20)
enqueue(30)
enqueue(10)
enqueue(20)
enqueue(30)

print(front, rear)
print(dequeue())
print(front, rear)
print(dequeue())
print(front, rear)
print(dequeue())
print(front, rear)
print(dequeue())
print(front, rear)
print(dequeue())
print(front, rear)
print(dequeue())

print(front, rear)
print(dequeue())
print(front, rear)
print(dequeue())
print(front, rear)
print(dequeue())

print(front, rear)
print(dequeue())
print(front, rear)
print(dequeue())
print(front, rear)
print(dequeue())



