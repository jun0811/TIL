# front, rear 이용
Q = [0] * 100
front, rear = -1, -1

def enQueue(item):
    global rear     # 값형 변수를 바꾸려고 하니까 global 사용
    if rear == len(Q) - 1:
        print("Queue Full")
    else:
        rear += 1
        Q[rear] = item

def deQueue():
    global front
    if front == rear:
        print("Queue Empty")
    else:
        front += 1
        return Q[front]

def Qpeek():
    if front == rear:
        print("Queue Empty")
    else:
        return Q[front+1]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
# 실제 값(Q)은 안지워지고 가리키는 곳이 달라지는 것임.
