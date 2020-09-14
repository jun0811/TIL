# front, rear 이용
SIZE = 4
Q = [0] * SIZE
front, rear = 0, 0

def enQueue(item):
    global rear
    if (rear + 1) % SIZE == front:  # full
        print("Queue Full")
    else:
        rear = (rear + 1) % SIZE     #rear += 1
        Q[rear] = item

def deQueue():
    global front
    if front == rear:
        print("Queue Empty")
    else:
        front = (front + 1) % SIZE
        return Q[front]

def Qpeek():
    if front == rear:
        print('queue empty')
    else:
        return Q[(front + 1) % SIZE]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(4)
enQueue(5)
enQueue(6)
enQueue(6)
print(deQueue())
print(Q)

# 선형큐의 단점을 극복하기 위해서 원형큐 사용
